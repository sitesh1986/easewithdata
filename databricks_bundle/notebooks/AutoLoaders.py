# Databricks notebook source
#Create autoloader_input folder in Volume
dbutils.fs.mkdirs("/Volumes/dev/bronze/landing/autoloader_input/2010/12/01")
dbutils.fs.mkdirs("/Volumes/dev/bronze/landing/autoloader_input/2010/12/02")
dbutils.fs.mkdirs("/Volumes/dev/bronze/landing/autoloader_input/2010/12/03")
dbutils.fs.mkdirs("/Volumes/dev/bronze/landing/autoloader_input/2010/12/04")
dbutils.fs.mkdirs("/Volumes/dev/bronze/landing/autoloader_input/2010/12/05")
dbutils.fs.mkdirs("/Volumes/dev/bronze/landing/autoloader_input/2010/12/06")
dbutils.fs.mkdirs("/Volumes/dev/bronze/landing/autoloader_input/2010/12/07")

# COMMAND ----------

#Create checkpoints location in volumes
dbutils.fs.mkdirs("/Volumes/dev/bronze/landing/checkpoint/autoloader")

# COMMAND ----------

#Copy files to nested location
dbutils.fs.cp("/databricks-datasets/definitive-guide/data/retail-data/by-day/2010-12-01.csv", "/Volumes/dev/bronze/landing/autoloader_input/2010/12/01")
dbutils.fs.cp("/databricks-datasets/definitive-guide/data/retail-data/by-day/2010-12-02.csv", "/Volumes/dev/bronze/landing/autoloader_input/2010/12/02")
dbutils.fs.cp("/databricks-datasets/definitive-guide/data/retail-data/by-day/2010-12-03.csv", "/Volumes/dev/bronze/landing/autoloader_input/2010/12/03")


# COMMAND ----------

dbutils.fs.cp("/databricks-datasets/definitive-guide/data/retail-data/by-day/2010-12-05.csv", "/Volumes/dev/bronze/landing/autoloader_input/2010/12/05")

# COMMAND ----------

# Read Files Using Autoloader with checkpoint
# and schema location /volumes/dev/bronze/landing/checkpoint/autoloader
# Files Detection Mode
#   - Directory Listing (Uses Api calls to detect the new files)
#   - File notification (uses Notification and Queue services - requires elevated cloud permissions for setup)

df =(
    spark
    .readStream
    .format("cloudfiles")
    .option("cloudfiles.format", "csv")
    .option("pathGlobFilter", "*.csv")
    .option("header", "true")
    .option("cloudFiles.schemaHints", "Quantity int, UnitPrice double")
    .option("cloudfiles.schemaLocation", "/Volumes/dev/bronze/landing/checkpoint/autoloader/1/")
    .option("cloudFiles.schemaEvolutionMode", "addNewColumns") # it has 3 option addNewColumns, rescue, none
    .load("/Volumes/dev/bronze/landing/autoloader_input/*/")
)

# COMMAND ----------

# Write data 
from pyspark.sql.functions import col
(
    df
    .withColumn("__file", col("_metadata.file_name"))
    .writeStream
    .format("delta")
    .option("checkpointLocation", "/Volumes/dev/bronze/landing/checkpoint/autoloader/1/")
    .outputMode("append")
    .trigger(availableNow=True)
    .toTable("dev.bronze.invoice_al_1") 
)


# COMMAND ----------

# MAGIC %sql
# MAGIC Select 
# MAGIC     __file,
# MAGIC     count(1)
# MAGIC  from 
# MAGIC     dev.bronze.invoice_al_1
# MAGIC group by __file

# COMMAND ----------

