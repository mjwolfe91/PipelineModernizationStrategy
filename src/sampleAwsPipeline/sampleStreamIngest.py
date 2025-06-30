from pipelineBase.streaming.streamingIngestionBase import StreamingIngestionBase
from pyspark.sql import SparkSession

class ExampleStreamIngest(StreamingIngestionBase):
    def __init__(self, app_name, spark, prom_endpoint, conn_details, table_details, write_options):
        super().__init__(app_name, spark, prom_endpoint, conn_details, table_details, write_options)
        self.app_name = 'AwsSampleStreaming'
        self.spark = SparkSession.builder.appName(f'{self.app_name}_streaming').getOrCreate()
        self.prom_endpoint = '8000'
        self.conn_details = {
            "kafka_server": "localhost:9092",
            "kafka_topic": "customer_traffic_data"
        }
        self.table_details = {
            "table_name": "customer_traffic_raw",
            "checkpoint_location": "s3://web_traffic_data/customer_traffic_raw/checkpoints"
        }
        self.write_options = {
            "spark.sql.catalog.catalog-name.type": "glue",
            "write.format.default": "avro",
            "write.merge.mode": "merge-on-read",
            "write.update.mode": "merge-on-read",   
            "write.delete.mode": "merge-on-read"
        }
    
    def get_data_stream(self):
        df = self.spark.readStream \
            .format('kafka') \
            .option('kafka.boostrap.servers', self.conn_details['kafka_server']) \
            .option('subscribe', self.conn_details['kafka_topic']) \
            .load()
        
        return df
    