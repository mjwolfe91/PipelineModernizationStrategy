from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType

spark = SparkSession.builder \
    .appName("LocalRefinement") \
    .master("local[*]") \
    .getOrCreate()

traffic_df = spark.read.format('csv').schema(StructType() \
    .add("customer_id", StringType(), True) \
    .add("activity", StringType(), True) \
    .add("timestamp", StringType(), True)) \
    .load('src/demo/data/web_traffic.csv')

customer_df = spark.read.option('header', True).csv('src/demo/data/customers.csv')

refined_df = traffic_df.join(customer_df, 'customer_id').select('customer_name', 'activity', 'timestamp')
refined_df.show()
