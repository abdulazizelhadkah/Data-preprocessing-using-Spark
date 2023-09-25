# Databricks notebook source
# MAGIC %sql
# MAGIC select * from default.wa_fn_usec__hr_employee_attrition_csv

# COMMAND ----------

# DBTITLE 1,Total Employee count
# MAGIC %sql
# MAGIC Select sum(EmployeeCount) from default.wa_fn_usec__hr_employee_attrition_csv

# COMMAND ----------

# DBTITLE 1,Find out attrition division
# MAGIC %sql
# MAGIC select sum(EmployeeCount), Attrition from default.wa_fn_usec__hr_employee_attrition_csv group by Attrition

# COMMAND ----------

# DBTITLE 1,Age Analysis
# MAGIC %sql
# MAGIC select sum(EmployeeCount), 
# MAGIC case when Age between 18 and 24 then "18-24" 
# MAGIC   when Age between 25 and 31 then "25-31"
# MAGIC   when Age between 32 and 38 then "32-38"
# MAGIC   when Age between 39 and 45 then "39-45"
# MAGIC   when Age between 46 and 52 then "46-52"
# MAGIC   else "53+"
# MAGIC END AS AgeRange
# MAGIC from default.wa_fn_usec__hr_employee_attrition_csv where Attrition="Yes" 
# MAGIC group by AgeRange

# COMMAND ----------

# DBTITLE 1,Attrition by Department
# MAGIC %sql
# MAGIC select sum(EmployeeCount), Department from default.wa_fn_usec__hr_employee_attrition_csv where Attrition ="Yes"  group by Department

# COMMAND ----------

# DBTITLE 1,Attrition by education (1- bellow college, 2- college, 3- Bachelor, 4- master, 5-Doctor)
# MAGIC %sql
# MAGIC select sum(EmployeeCount),
# MAGIC case when Education = 1 then "Bellow college"
# MAGIC   when Education = 2 then "College"
# MAGIC   when Education = 3 then "Bachelor"
# MAGIC   when Education = 4 then "master"
# MAGIC   else "Doctor"
# MAGIC end as Education_Degree
# MAGIC from default.wa_fn_usec__hr_employee_attrition_csv where Attrition = "Yes" 
# MAGIC group by Education_Degree

# COMMAND ----------

# DBTITLE 1,Attrition by job satisfaction (1-Low ,2-Medium ,3-High ,4-Highly satisfied )
# MAGIC %sql
# MAGIC select sum(EmployeeCount) As No_Employees,
# MAGIC case when EnvironmentSatisfaction = 1 then "Low"
# MAGIC   when EnvironmentSatisfaction = 2 then "Medium"
# MAGIC   when EnvironmentSatisfaction = 3 then "High"
# MAGIC   when EnvironmentSatisfaction = 4 then "Highly satisfied"
# MAGIC   else "Doctor"
# MAGIC end as Employees_satisfaction
# MAGIC from default.wa_fn_usec__hr_employee_attrition_csv where Attrition = "Yes" 
# MAGIC group by Employees_satisfaction

# COMMAND ----------

# DBTITLE 1,Attrition by Business Travel
# MAGIC %sql
# MAGIC Select sum(EmployeeCount) ,BusinessTravel 
# MAGIC from default.wa_fn_usec__hr_employee_attrition_csv where Attrition = "Yes"
# MAGIC group by BusinessTravel
