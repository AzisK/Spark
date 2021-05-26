PARQUET = "/opt/data/target/waterbase.parquet"

from pyspark.sql import SparkSession

spark = SparkSession.\
        builder.\
        appName("spark2kafka_producer").\
        master("spark://spark-master:7077").\
        config("spark.executor.memory", "512m").\
        getOrCreate()    

df = spark.read.parquet(PARQUET)

schema = df.schema

stream_df = spark.readStream.schema(schema).parquet(PARQUET)

print(stream_df.isStreaming)

query = stream_df \
  .selectExpr("CAST(UID AS STRING) AS key", "to_json(struct(*)) AS value") \
  .writeStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "localhost:9092") \
  .option("topic", "topic-demo") \
  .option("checkpointLocation", "/opt/data/checkpoint/") \
  .start() \
  .awaitTermination()
