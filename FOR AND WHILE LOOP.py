# Databricks notebook source
i=0
while  i<10 :
    print(i)
    i+=1
    

# COMMAND ----------

i=0
while  i<3 :
    print (i)
    i+=1
    
    

# COMMAND ----------

v_range = range(7)
name = "NAGARJUNA"
for a in range(8) :
    print(a)

# COMMAND ----------

a = "alephys practie lab "
for i in range(1,10,4):
    print('this is ',a)

# COMMAND ----------

val = [1,2,3,4]
for i in ['nag']:
    print('this is numberof  :',i)

# COMMAND ----------

for x in "apple":
    print('characters are :',x)


# COMMAND ----------

fruits= ["app","ban","cher","ora","mang"]
for i in fruits :
    if i == "cher":
        continue
    print(i)

# COMMAND ----------


for i in range(10) :
    if i in (4,4,7):
        continue
    print(i)

# COMMAND ----------

i=0
while i<10:  
    i += 1
    if i in (4,7):
        continue
    print(i)  


# COMMAND ----------

num=0
target_value=10
for i  in range(target_value+1):
    num = num + i
print('sum of 10 :',num)
print('sum of 10 numbers')
    

# COMMAND ----------

#num=0

for i in range(15):
    if i%2==1:
        pass
        print("odd number: ",i)
    

# COMMAND ----------

v_even=0
v_evenlist =[]
for i in range (11):
    if i%2==1:
        v_evenlist.append(i)
        v_even+=i
print('sum of even numbers is :',v_even)
print('sum of even numbers is :',sum(v_evenlist))

# COMMAND ----------

        
