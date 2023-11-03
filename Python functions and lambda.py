# Databricks notebook source
# MAGIC %md
# MAGIC ### functions

# COMMAND ----------

lab = lambda a,b : (a+b,a*b)
lab(5,10)

# COMMAND ----------

def fun_name (a,b,c):
   print( 'sum of values is: ',a+b,b+c,a+c)
fun_name(1,2,3)

# COMMAND ----------

def fun_na(name,age):
    print('my name is :',name)
    print('my name is :',age)
fun_na('siva',35)

# COMMAND ----------

def new_comp(name="alephys",count=10,loc='hyderabad'):
    print("my company name is :",name)
    print("my company members are :",count)
    print("my company located at :",loc)
#new_comp("alephys",10)
  



# COMMAND ----------

new_comp("alephys",10,"chennai")

# COMMAND ----------

def check_list(num_list):
    even = []
    for number in num_list:
        if number % 2 == 0:
            even.append(number)
        else:
            pass
    return even
check_list([1,2,3,4,5,7,6,8,9,10])

# COMMAND ----------

def check_list(num_list):
    even = []
    for number in num_list:
        if number % 2 == 1:
            even.append(number)
        else:
            pass
    return even
check_list([1,2,3,4,5,7,6,8,9,10])

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

def even_no(numbers):
    even=[]
    odd=[]
    for i in numbers:
        if i %2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even ,odd


# COMMAND ----------

even_no([1,2,3,4,5,6,7,8,9,10])

# COMMAND ----------


