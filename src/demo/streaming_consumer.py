from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, TimestampType

spark = SparkSession.builder \
    .appName("KafkaLocalStreaming") \
    .master("local[*]") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.13:3.3.0") \
    .getOrCreate()

schema = StructType() \
    .add("customer_id", StringType()) \
    .add("activity", StringType()) \
    .add("timestamp", TimestampType())

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "web_traffic") \
    .option("startingOffsets", "earliest") \
    .load()

json_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

query = json_df.writeStream \
    .outputMode("append") \
    .format("csv") \
    .option("path", "src/demo/data/web_traffic.csv") \
    .option("checkpointLocation", "src/demo/data/checkpoints") \
    .start()

query.awaitTermination()
