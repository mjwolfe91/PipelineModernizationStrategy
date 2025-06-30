from pipelineBase.dataPipelineBase import DataPipelineBase
from abc import abstractmethod
from pyspark.sql import dataframe
from pyspark.sql.functions import col, current_timestamp
from prometheus_client import Counter, Histogram, Gauge

class StreamingIngestionBase(DataPipelineBase):

    def __init__(self, app_name, spark, prom_endpoint, conn_details, table_details, write_options):
        super().__init__(app_name, spark, prom_endpoint)
        self.app_name = app_name
        self.conn_details = conn_details
        self.table_details = table_details
        self.write_options = write_options
        self._metrics = {
            f'{self.app_name}_rows': Counter(
                f'{self.app_name}_rows_total',
                f'Total number of rows processed by ingestion app {self.app_name}'
            ),
            f'{self.app_name}_event_latency_seconds': Histogram(
                'event_latency_seconds',
                'Latency between Kafka event timestamp and processing time'
            ),
            f'{self.app_name}_latest_event_latency': Gauge(
                'latest_event_latency_seconds',
                'Most recent event latency in seconds'
            )
        }

    def get_metrics(self):
        return self._metrics

    def batch_handler(self, batch_df, batch_id):
        row_count = batch_df.count()
        metrics = self.get_metrics
        metrics['processed_rows'].inc(row_count)

        if row_count > 0:
            latencies = batch_df.selectExpr(
                "CAST((unix_timestamp(ingest_time) - unix_timestamp(event_time)) AS DOUBLE) AS latency"
            ).rdd.map(lambda row: row['latency']).collect()

            for latency in latencies:
                metrics['event_latency_seconds'].observe(latency)
            metrics['latest_event_latency'].set(latencies[-1])

        batch_df.writeTo(self.table_details['table_name']).options(**self.write_options).append()

    @abstractmethod
    def get_data_stream(self) -> dataframe:
        pass
        
    def run(self):
        df = self.get_data_stream \
                .load() \
                .withColumn("event_time", col("timestamp")) \
                .withColumn("ingest_time", current_timestamp())
        
        stream = df.writeStream \
            .option("checkpointLocation", self.table_details["checkpoint_location"]) \
            .foreachBatch(self.batch_handler) \
            .start()

        stream.awaitTermination()

        