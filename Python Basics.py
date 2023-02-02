#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Hello world

print("Hello world")


# In[ ]:


name="umair"
age=22
print(name,age)


# In[ ]:


is_adult= False 
print(name,age)


# In[ ]:


#Catentation

name=input("what is your name ?")
print ("hello"+ name)


# In[ ]:


#Tpye Conversion(int,float,str,bool)

age=input("input your age")
new=int(age) + 2
print(new)


# In[ ]:


first=input("enter first number")
second=input("enter second number")
result=int(first)+int(second)
print(result)


# In[ ]:


#Strings

name="umair"
print(name.upper())
print(name.find('i'))
print(name.replace("umair",("jam")))


# In[ ]:


#IN keyword

name="umair"
print ("umair" in name)
print("jam"in name)


# In[ ]:


#Arthimatic operation

print(5+2)
print(5-2)
print(5*2)
print(5/2)
print(5**2)
print(5//2) #to remove decimal


# In[ ]:


#operator precedence

result=2+3*5/4-2
print(result)

print(2>1 or 2==2)
# In[ ]:


#If-Else

age=18
if(age>=19):
    print("your an adult")
    print("you can vote")
elif(age<18 and age>3):
    print("your in school")
else:
    print("your a kid")
    
print("Thank you")    

#indent matters first 2 print function have same indent last print has
#different means last is out of block it will run every time.


# In[ ]:


# Calculator Task

a=input("Please enter first number ")
b=input("Please enter second number ")
opr=input("enter operator")
a=int(a)
b=int(b)
if(opr=='+'):
    print(a+b)
elif(opr=='-'):
    print(a-b)
elif(opr=='*'):
    print(a*b)
elif(opr=='/'):
    print(a/b)
elif(opr=='%'):
    print(a%b)
else:
    print('invaid')


# In[ ]:


#Range

#range(5)=0,1,2,3,4
numbers=range(5)
print (numbers)


# In[ ]:


# While loops

i=1
while i <=5:
    print(i)
    i=i+1


# In[ ]:


#For loops

for item in range(5):
    print(item)
print('----------------------')
for item in range(5):
    print(item+1)


# In[20]:


#List
marks=[95,98,97,95]
print(marks)
print(marks[-1])#count from last
print(marks[-2])
print(marks[0:2])# index 2 is not included
print(marks[1:4])
#-----------------------------------------------

#for loop in lists

for iteams in marks:
    print(marks)
#-----------------------------------------------
#operations in lists

marks.append(100) #add in the end
print (marks)
marks.insert(0, 94) #insert in the start with an index.
print (marks)
print(99 in marks)#to check or search value(will return bool value).
print(len(marks))# calculate lenght of list.


# In[42]:


#Break and continue keywords

students= ["umair", "ali","ahmad" ,"hamza"]
for i in students:
    if i =="ahmad":
        break;
    print(i)
print("------------------------------------")
#-------------------------------------------

# the loop will not work for ahmad in continue mode

students= ["umair", "ali","ahmad" ,"hamza"]
for i in students:
    if i =="ahmad":
        continue;
    print(i)
    
        
    

    


# In[39]:


# Tuple.
   
# will work unlikely lists.
# cant modify after created like append, insert, delete.
# can perfomr ony 2 operaions.

marks=(95,98,97,97)
print(marks.count(97))
print(marks.index(95))

   



# In[41]:


# Sets
#cant perfom indexing...print(number[0])
marks={95,98,97,97}
print(marks) #can print only unique values and it is unordered data
for i in marks:
    print(i)



# In[48]:


#Dictionary 
#like sets
#key-value pair
marks={"english":95 ,"maths":96 ,"computer":97 ,"science":98}
print(marks)
print(marks["english"])
marks["english"]=99
print(marks)






# In[51]:


#Function
def add (first, second):
    print(first+second)
    
add(1,2)
    



# In[ ]:


#()=tuples
#[]=lists
#{}=Dictionary and sets

