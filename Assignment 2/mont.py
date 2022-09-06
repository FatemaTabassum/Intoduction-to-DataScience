#!/usr/bin/env python
# coding: utf-8

# In[13]:





# In[24]:





# In[ ]:


input_features=['Age', 'Gender', 'Chest Pain', 'Blood Pr', 'Cholesterol', 'Blood Sugar',
       'ElectroCardio', 'Max Heart Rate', 'Exercise Induced Angina',
       'ST depression ind. By exercise', 'Slope of the peak exercise ',
       '# of vessels', 'defect', 'Result']
y=[]


# In[28]:


import csv
with open("IDS_Assignment_2_testdata4.csv","r") as f_input:
    csv_input = csv.DictReader(f_input)
    age =[]
    gender =[]
    chestPain =[]
    cholestrolVal =[]
    defect =[]
    y_true =[]
    for row in csv_input:
        age.append(int(float(row['Age'])))
        gender.append(int(float(row['Gender'])))
        chestPain.append(int(float(row['Chest Pain'])))
        cholestrolVal.append(int(float(row['Cholesterol'])))
        defect.append(int(float(row['defect'])))
        y_true.append(row['Result'])


# In[36]:


y_pred=[]
for i in range(len(y_true)):
    if(chestPain[i]==4):
        if(age[i]>=60):
            if(gender[i]==1):
                if(cholestrolVal[i]>=210):
                    y_pred.append('yes')
                
                else:
                    y_pred.append('no')
            elif(gender[i]==0):
                if(cholestrolVal[i]>=220):
                    y_pred.append('yes')
                else:
                    y_pred.append('no')
        elif(age[i]<=59):
            if(defect[i]>5):
                y_pred.append('yes')
            else:
                y_pred.append('no')
    elif(chestPain[i]==3):
        if(age[i]>=50):
            if(defect[i]>5):
                y_pred.append('yes')
            else:
                y_pred.append('no')
        else:
            y_pred.append('no')
    else:
        y_pred.append('no')

    


# In[35]:


y_pred,y_true


# In[37]:


import numpy as np
count=0
#y_true=[0,1,0,0,1,1,0,0,1,1,1,0,1,0,0,0,1,0,0,0,0]
#y_pred=[0,1,0,0,1,0,1,0,1,1,1,0,1,0,0,0,1,0,0,1,1]
for i in range(len(y_true)):
    if(y_true[i]!=y_pred[i]):
        count+=1
print(count)
accuracy=((len(y_true)-count)/len(y_true))
print(accuracy)
print("The accuracy of the model is {:.2%}".format(accuracy))


# In[19]:



''''
age=int(input("Enter a value of age:"))
gender=int(input("Enter Gender Value"))
chestPain=int(input("Enter a value of ChestPain:"))
defect=int(input("Enter a value of defect:"))
cholestrolVal=int(input("Enter a value of cholestrol:"))
''''
if(chestPain==4):
    if(age>=60):
        if(gender==1):
            if(cholestrolVal>=210):
                Result='Yes'
            else:
                Result='No'
        elif(gender==0):
            if(cholestrol>=220):
                Result='Yes'
            else:
                Result='No'
    elif(age<=59):
        if(defect>5):
            Result='Yes'
        else:
            Result='No'
elif(chestPain==3):
    if(age>=50):
        if(defect>5):
            Result='Yes'
        else:
            Result='No'
    else:
        Result='No'
else:
    Result='No'
if(Result=='Yes'):
    print("Heart Disease")
else:
    print('No heart disease')
        
        


# In[24]:


defect


# In[17]:


import pandas as pd
df = pd.read_csv("IDS_Assignment_2_testdata6.csv")
df
type(df.Gender)


# In[4]:


my_u = u'my ünicôdé strįng'
type(my_u)


# In[18]:


import pandas as pd
 
# read DataFrame
data = pd.read_csv("IDS_Assignment_2_traindata.csv",chunksize=22)
 
for i, chuck in enumerate(data): 
    chuck.to_csv('IDS_Assignment_2_testdata{}.csv'.format(i),index=False) # i is for chunk number of each iteration 


# In[ ]:




