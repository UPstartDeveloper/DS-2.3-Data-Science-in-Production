from pyspark.sql import SparkSession
from pyspark import SparkContext
sc = SparkContext()

spark = SparkSession \
    .builder \
    .appName("Python Spark regression example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
