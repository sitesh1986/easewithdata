# Databricks notebook source
# MAGIC %sql
# MAGIC create table if not exists dev.bronze.SALE_EXTERNAL(
# MAGIC     invoice_id string,
# MAGIC     cust_id string,
# MAGIC     product_code string,
# MAGIC     QTY int,
# MAGIC     PRICE double
# MAGIC )
# MAGIC location 'abfss://data@easewithdata01adb.dfs.core.windows.net/adb/ext_tables/sales_external'
# MAGIC ;
# MAGIC
# MAGIC insert into dev.bronze.sale_EXTERNAL values('INV1001', 'CUST1001', 'PCODE1001', 10, 100);

# COMMAND ----------

# MAGIC %sql
# MAGIC describe extended   dev.bronze.sale_MANAGED;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC describe extended  dev.bronze.SALE_EXTERNAL;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DROP TABLE dev.bronze.SALE_MANAGED;

# COMMAND ----------

# MAGIC %sql
# MAGIC USE CATALOG dev;
# MAGIC
# MAGIC SHOW TABLES DROPPED IN bronze;

# COMMAND ----------

# MAGIC %sql
# MAGIC UNDROP TABLE DEV.BRONZE.SALE_MANAGED

# COMMAND ----------

