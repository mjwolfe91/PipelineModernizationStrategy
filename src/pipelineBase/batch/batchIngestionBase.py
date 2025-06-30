from pipelineBase.dataPipelineBase import DataPipelineBase
from prometheus_client import Counter
from abc import abstractmethod
from pyspark.sql import dataframe

class BatchIngestionBase(DataPipelineBase):
    def __init__(self, app_name, spark, prom_endpoint, conn_details, table_details, write_options):
        super().__init__(app_name, spark, prom_endpoint)
        self.app_name = app_name
        self.spark = spark
        self.prom_endpoint = prom_endpoint
        self.conn_details = conn_details
        self.table_details = table_details
        self.write_options = write_options
        self._metrics = {
            f'{self.app_name}_rows': Counter(
                f'{self.app_name}_rows_total',
                f'Total number of rows processed by ingestion app {self.app_name}'
            )
        }

    def get_metrics(self):
        return self._metrics
    
    @abstractmethod
    def get_dataframe(self) -> dataframe:
        pass

    def run(self):
        df = self.get_dataframe
        
        row_count = df.count()
        metrics = self.get_metrics
        metrics['processed_rows'].inc(row_count)

        df.write
        