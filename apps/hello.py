from pyspark.sql import SparkSession
from pyspark.conf import SparkConf

conf = SparkConf()
conf.set("spark.eventLog.enabled", True)
conf.set("spark.eventLog.dir", "/opt/spark/spark-events")
conf.set("spark.history.fs.logDirectory", "/opt/spark/spark-events")
conf.set("spark.executor.memory", "512m")

spark = SparkSession.\
        builder.\
        appName("pyspark-notebook").\
        config(conf=conf).\
        getOrCreate()

spark.sparkContext.getConf().get('spark.eventLog.dir')
conf.getAll()

from datetime import datetime, date
from pyspark.sql import Row

df = spark.createDataFrame([
    Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
    Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
    Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
])
df.show()