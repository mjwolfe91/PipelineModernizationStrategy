from pipelineBase.dataPipelineBase import DataPipelineBase
from prometheus_client import Counter

class DataRefinementBase(DataPipelineBase):

    def __init__(self, app_name, spark, prom_endpoint, table_details, write_options):
        super().__init__(app_name, spark, prom_endpoint)
        self.app_name = app_name
        self.table_details = table_details
        self.write_options = write_options
        self._metrics = {
            f'{self.app_name}_rows': Counter(
                f'{self.app_name}_rows_total',
                f'Total number of rows processed by ingestion app {self.app_name}'
            ),
        }