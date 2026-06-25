# Databricks notebook source

# All Available Utilities
dbutils.help()

# COMMAND ----------

# File System Utilities
dbutils.fs.help()

# COMMAND ----------

display(dbutils.fs.ls("/Volumes/dev/bronze/ext_vol/files/"))

# COMMAND ----------

display(dbutils.fs.head("dbfs:/Volumes/dev/bronze/ext_vol/files/emp.csv"))

# COMMAND ----------

dbutils.fs.mkdirs("dbfs:/Volumes/dev/bronze/ext_vol/files/input/csv")

# COMMAND ----------

dbutils.fs.cp("dbfs:/Volumes/dev/bronze/ext_vol/files/emp.csv","dbfs:/Volumes/dev/bronze/ext_vol/files/input/csv")

# COMMAND ----------

# Widgets
dbutils.widgets.help()

# COMMAND ----------

dbutils.widgets.text("input_cust_id","10000","customer_id")

# COMMAND ----------

dbutils.widgets.get("input_cust_id")

# COMMAND ----------

# Secrets
dbutils.secrets.help()

# COMMAND ----------

# Notebook Utilities
dbutils.notebook.help()

# COMMAND ----------

