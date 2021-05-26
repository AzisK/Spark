# Spark
 
## Build images

`bash build.sh`

## Bring up the containers

`docker compose up`

## Read Parquet

The script the convert CSV to Parquet can be found in `csv2parquet.parquet.ipynb`

For Avro format: https://spark.apache.org/docs/latest/sql-data-sources-avro.html

## Create a Kafka topic

**That is now automatically done by Docker**

docker-compose exec broker kafka-topics --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic topic-demo

## Submit a Spark application

Connect to `docker exec -it spark-master bash`

and submit

```bash
cd /usr/bin/spark-3.1.1-bin-hadoop3.2/bin
bash spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1 /opt/notebooks/spark2kafka.py
```
