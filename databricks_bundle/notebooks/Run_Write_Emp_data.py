# Databricks notebook source
# Run the child notebook with Parameter - sales or production or office
_count = dbutils.notebook.run(
    "Write_Emp_Data", # location of child notebook
    600, # Timout seconds
    {"dept" : "office"} # parameter what we are passing
)

# COMMAND ----------

print(f"child notebook count {_count}")