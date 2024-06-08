from pyspark.sql import SparkSession

 # Start SparkSession
spark = SparkSession.builder \
    .appName("Word Counter") \
    .getOrCreate()

 # Read text file
text_file = spark.read.text("/opt/spark-app/data/text.txt")  # Path inside container (./ = /opt/spark-app/)
 # Count Words
word_counts = text_file.selectExpr("explode(split(value, ' ')) as word") \
    .groupBy("word") \
    .count() \
    .sort("count", ascending=False)

 # Show Results
word_counts.show()

 # Stop Spark Session
spark.stop()
