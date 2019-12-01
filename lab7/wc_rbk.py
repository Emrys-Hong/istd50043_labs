import pyspark
import time
import re
import sys
'''
[headnode] [hdfs path]
Note that HDFS port is 9000
'''
sc = pyspark.SparkContext("spark://{}:7077".format(sys.argv[1]), "test")
data = sc.textFile(sys.argv[2])

start = time.time()
words = data.flatMap(lambda x: re.split('\W+', x)).map(lambda x: (x,1)).reduceByKey(lambda x,y: x+y)

words.saveAsTextFile("hdfs://{}:9000/output".format(sys.argv[1]))
end = time.time()
print("\nTime: ", (end-start))
