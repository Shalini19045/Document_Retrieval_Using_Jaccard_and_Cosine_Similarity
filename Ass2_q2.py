#!/usr/bin/env python
# coding: utf-8

# In[2]:


dictionary=open("C:/Users/Shalini Bhardwaj/Downloads/english2/english2.txt","r")
dictionaryWords=dictionary.read().split("\n")
print(dictionaryWords[9])


# In[5]:


from nltk.tokenize import word_tokenize
import string
import re
print("Enter Query :")
query=input()
wrong_list=[]
  
query=query.lower()
#translator=query.maketrans(string.punctuation,'                                ')
query=query.translate(str.maketrans("","",string.punctuation))

query=re.sub(r"\d+","",query)
query = word_tokenize(query)

for p in query:
    if p not in dictionaryWords:
        wrong_list.append(p)
print(wrong_list)
print("number of dictionary words to be retrieved:")
k=int(input())


# In[6]:


from heapq import nsmallest 
def editDistDP(str1, str2, m, n): 
    
    ed = [[0 for y in range(n + 1)] for y in range(m + 1)] 
    
    p=m+1
    q=n+1
     
    for i in range(0,p): 
        for j in range(0,q): 
  
           
            if i == 0: 
                ed[i][j] = j*2    
  
            
            elif j == 0: 
                ed[i][j] = i   
  
           
            elif str1[i-1] == str2[j-1]: 
                ed[i][j] = ed[i-1][j-1] 
  
          
            else: 
                ed[i][j] = min(2+ed[i][j-1],         
                                   1+ed[i-1][j],        
                                   3+ed[i-1][j-1])    
  
    return ed[m][n] 

for i in wrong_list:
    dis_list={}
    for j in dictionaryWords:
        dis_list[j] =editDistDP(i,j, len(i), len(j))
    kSmallest = nsmallest(k,dis_list,key = dis_list.get)
    
    for val in kSmallest: 
        print(i,val, ":",dis_list.get(val))


# In[ ]:




