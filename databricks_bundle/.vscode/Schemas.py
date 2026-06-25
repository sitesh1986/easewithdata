-- Databricks notebook source
-- Create Schema Without external location in Dev Catalog

Create schema if not exists dev.bronze
comment 'This is schema in Dev catalog without external location';

-- COMMAND ----------

-- Create Schema Without Extenral Location in Dev_Ext Catalog

Create schema if not exists dev_ext.bronze
comment 'This is schema in Dev_ext catalog without external location';

-- COMMAND ----------

-- Create External Location for Schema

create external location `ext_schema`
url 'abfss://data@easewithdata01adb.dfs.core.windows.net/adb/schema/'
with (storage credential `uc_catalog_storage`)

-- COMMAND ----------

-- Create Schema With External Location In Dev_Ext Catalog
Create schema if not exists dev_ext.bronze_ext
managed location 'abfss://data@easewithdata01adb.dfs.core.windows.net/adb/schema/bronze_ext'
comment 'This is schema in Dev_ext catalog with external location'

-- COMMAND ----------

Create table if not exists dev_ext.bronze_ext.RAW_SALE(
    invoice_id string,
    cust_id string,
    product_code string,
    QTY double,
    PRICE double
);

insert into dev_ext.bronze_ext.RAW_SALE values('INV1001', 'CUST1001', 'PCODE1001', 10, 100)

-- COMMAND ----------

-- Describe the table
describe extended dev.bronze.raw_sale;

-- COMMAND ----------

describe extended dev_ext.bronze.raw_sale;

-- COMMAND ----------

describe extended dev_ext.bronze_ext.RAW_SALE;

-- COMMAND ----------

