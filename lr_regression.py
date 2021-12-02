import sys
import numpy as np
import pandas as pd
from pyspark.sql import functions as F
from pyspark.sql.functions import lit
from functools import reduce
from pyspark.sql import SparkSession

# Matrix multiplication for two matrices
def matrix_mult(df, col1, col2):
    colDFs = []
    for c2 in col1:
        colDFs.append( df.select( [ F.sum(df[c1]*df[c2]).alias("op_{0}".format(i)) for i,c1 in enumerate(col2) ] ) )
    mtxDF = reduce(lambda a,b: a.select(a.columns).union(b.select(a.columns)), colDFs )
    return np.array(mtxDF.rdd.collect())

if __name__ == "__main__":
    if len(sys.argv) !=2:
        print("Usage: spark-submit lr_regression.py <input-file-from-hadoop>", file=sys.stderr)
        sys.exit(-1)
  
spark = (SparkSession
        .builder
        .appName("Linear Regression using Spark")
        .getOrCreate())

sc = spark.sparkContext
sc.setLogLevel('WARN')  # see what happens when this line is commented out

# input file path
input_csv = sys.argv[1]

df = spark.read.format("csv").load(input_csv)

# Typecast all columns to double
for col in df.columns:
    df = df.withColumn(col, df[col].cast("double"))

# Add additional column of 1s
df_one = df.select(lit(1).alias("one_col"), "*")
#df_X = df_one[df_one.columns[:-1]]

# Identify independent and dependent variable(s)
indep = df_one.columns[:-1]
dep = [df_one.columns[-1]]

# Below for X.T * X
xtx = matrix_mult(df_one,indep,indep)

# Below for X.T * Y
xty = matrix_mult(df_one,indep,dep)

beta_mat = np.matmul(np.linalg.inv(xtx),xty)
np.set_printoptions(suppress=True)
print("beta : ")
print(beta_mat)		# The output is in a matrix form. To access each value individually, you may need to get each value by its index.

