# Databricks notebook source
print("Hello World of Databrics!")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "Hello world of Databricks from SQL!"

# COMMAND ----------

# MAGIC %md
# MAGIC # Title 1
# MAGIC ## Title 2
# MAGIC ### Title 3
# MAGIC
# MAGIC Order list:
# MAGIC 1. One
# MAGIC 1. Two
# MAGIC 1. Three
# MAGIC
# MAGIC Unordered list:
# MAGIC * apples
# MAGIC * bananans
# MAGIC * mango
# MAGIC
# MAGIC Table: 
# MAGIC | user_id | user_name |
# MAGIC |---------|-----------|
# MAGIC |    2    |   Marko   |
# MAGIC |    1    |   Dragana |
# MAGIC |    3    |   Dunja   |
# MAGIC

# COMMAND ----------

# MAGIC %run ../includes/Setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

dbutils.fs.ls('/databricks-datasets/')

# COMMAND ----------

dispay(files)
