from abc import abstractmethod, ABC
from prometheus_client import start_http_server

class DataPipelineBase(ABC):

    def __init__(self, app_name, spark, prom_endpoint):
        self.app_name = app_name
        self.spark = spark
        start_http_server(prom_endpoint)
    
    @abstractmethod
    def get_metrics(self) -> dict:
        pass

    @abstractmethod
    def run(self):
        pass