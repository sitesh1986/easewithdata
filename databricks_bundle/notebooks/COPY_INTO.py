# Databricks notebook source
# MAGIC %sql
# MAGIC -- Create new volume loading under dev > bronze
# MAGIC CREATE VOLUME dev.bronze.landing
# MAGIC COMMENT "This is Landing Managed Volume"
# MAGIC ;

# COMMAND ----------


dbutils.fs.mkdirs("dbfs:/Volumes/dev/bronze/landing/input")

# COMMAND ----------

dbutils.fs.cp("/databricks-datasets/definitive-guide/data/retail-data/by-day/2010-12-03.csv", "dbfs:/Volumes/dev/bronze/landing/input")

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Create placeholder table dev.bronze.invoice_cp
# MAGIC Create table if not exists dev.bronze.invoice_cp
# MAGIC ;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- use copy into to load data into place holder table
# MAGIC COPY INTO dev.bronze.invoice_cp
# MAGIC FROM "/Volumes/dev/bronze/landing/input"
# MAGIC FILEFORMAT = CSV
# MAGIC PATTERN = '*.csv'
# MAGIC FORMAT_OPTIONS (
# MAGIC     'header' = 'true',
# MAGIC     'mergeSchema' = 'true'
# MAGIC     )
# MAGIC     copy_options (
# MAGIC     'mergeSchema' = 'true'
# MAGIC     )
# MAGIC ;

# COMMAND ----------

# MAGIC %sql
# MAGIC Select * from dev.bronze.invoice_cp
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC describe extended dev.bronze.invoice_cp

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Create new table with only 3 column invoice_cp_alt and custom column _insert_date
# MAGIC
# MAGIC alter table dev.bronze.invoice_cp_alt
# MAGIC (
# MAGIC     InvoiceNo string,
# MAGIC     StockCode string,
# MAGIC     _insert_date timestamp
# MAGIC );
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Load data using copy into in the new table invoice_cp_alt
# MAGIC COPY INTO dev.bronze.invoice_cp_alt
# MAGIC FROM (
# MAGIC     Select InvoiceNo,StockCode,current_timestamp() _insert_date, cast(Quantity as double) Quantity
# MAGIC     FROM
# MAGIC     "/Volumes/dev/bronze/landing/input"
# MAGIC     )
# MAGIC FILEFORMAT = CSV
# MAGIC PATTERN = '*.csv'
# MAGIC FORMAT_OPTIONS (
# MAGIC     'header' = 'true',
# MAGIC     'mergeSchema' = 'true'
# MAGIC     )
# MAGIC    

# COMMAND ----------

# MAGIC %sql
# MAGIC Select count(1) from dev.bronze.invoice_cp_alt