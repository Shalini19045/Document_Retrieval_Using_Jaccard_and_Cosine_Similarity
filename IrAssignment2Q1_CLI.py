#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Ques1 Ass2

import glob

folders = [i for i in glob.glob('C:/Users/Shalini Bhardwaj/Downloads/stories/stories/*')]
print(len(folders))
Num_docs=len(folders)


# In[2]:


from num2words import num2words
doc_inv_index={}
all_files = [i for i in glob.glob('C:/Users/Shalini Bhardwaj/Downloads/stories/stories/*')]
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
idf={}
idf_final={}

def preprocessing():
   
    
    
   
    for h in all_files:
      
            
            templist=[]
            file=open(h,encoding="latin1")
            
            X=file.read()
           
            
            X =X.lower()
            
           
            
            
           
            X=X.translate(str.maketrans("","",string.punctuation))
          
            stop_words = set(stopwords.words('english'))
            tokens = word_tokenize(X)
            
            tokens=list(tokens)


            
            result = [i for i in tokens if not i in stop_words]
   
            

            lemmatizer=WordNetLemmatizer()
        
            for word in result:
                if word.isdecimal()==True:
                    word=num2words(word)
                
                lem_word=lemmatizer.lemmatize(word) 
                
                    
                templist.append(lem_word)
                
            templist1=set(templist)
            
            for lem_word in templist1:  
                
                if lem_word in idf.keys():
                    idf[lem_word] =idf[lem_word]+1

                else:
                    idf[lem_word]=1
                      
            
                    
           
        
           
            doc_inv_index[h[52:]]=templist
            



                    


preprocessing() 
print("pre processing completed")


# In[3]:


def Jaccard_coeff(k):
    from heapq import nlargest
    
    
    
   
    query=set(querylist)
    J_score={}
    for doc in doc_inv_index.keys():
        token_set=set(doc_inv_index[doc])
        intersection=len(query.intersection(token_set))
        union=len(query.union(token_set))
        score=intersection/union
        
        J_score[doc]=score
        #print("score",J_score[doc]) 
        
    kHighest = nlargest(k, J_score, key = J_score.get) 
  
     
    

    for val in kHighest: 
        print(val, ":", J_score.get(val))


# In[4]:


import math
tf_idf_dict={}
def tf_idf(k):
    from heapq import nlargest
    
    print("Choose Variation of tf: enter 1/2/3")
    #var1=int(input("enter choice"))
    var1=int(input())
    for t in doc_inv_index.keys():
        total=0
        for x in querylist:
            if x not in idf_final.keys():
                idf_final[x]=0
        
        for p in querylist:
            count1=doc_inv_index[t].count(p)
   
            if var1==1:
                 tf=count1/len(doc_inv_index[t])
            elif var1==2:
                 tf=count1
            else:
                y=count1
                tf=math.log(1+y,10)
                

            tf_idf=tf*idf_final[p]
            total=total+tf_idf
        tf_idf_dict[t]=total


    kHighest = nlargest(k,tf_idf_dict,key = tf_idf_dict.get)
    
    
    for val in kHighest: 
        print(val, ":",  tf_idf_dict.get(val))
    
    

    
    


# In[5]:


def choose_idf():
    import math
    print("Choose Variation of Idf:enter 1/2/3")
    #print("1.")
    var=int(input())
    if var==1:
        
        for lem_word in idf.keys():
                      idf_final[lem_word]=Num_docs/idf[lem_word]
    elif var==2:
        
        for lem_word in idf.keys():
                      y=Num_docs/(idf[lem_word]+1)
                      idf_final[lem_word]=math.log(y,10)
    else:
        
        for lem_word in idf.keys():
                      y=Num_docs/(idf[lem_word])
                      idf_final[lem_word]=math.log(y,10)
                  
                    


# In[6]:


from nltk.tokenize import word_tokenize
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
 
index_file=open("C:/Users/Shalini Bhardwaj/Downloads/stories/stories/index1.txt","r")
title_dict={}
String_title=index_file.readlines()
print(len(String_title))
r=0
while r < (len(String_title)-1):
    titleTokensHead=String_title[r].lower().split("\t")
    
    titleTokens=word_tokenize(String_title[r+1].lower())
    #titleTokens=titleTokens.translate(str.maketrans("","",string.punctuation))
   
    stop_words = set(stopwords.words('english'))
    result=[r for r in titleTokens if not r in stop_words ]
    title_list=[]
    lemmatizer=WordNetLemmatizer()
    for word in result:
        title_list.append(lemmatizer.lemmatize(word))
    title_dict[titleTokensHead[0]]=title_list 
    r=r+2
    
title_dict["index1.txt"]=[]
print("length.......",len(title_dict))
print(title_dict)
                      


# In[ ]:


# print((idf_final["flower"]))
# print(doc_inv_index["vgilante.txt"])


# In[7]:


import math
tf_idf_dict={}
def tf_idf_with_title(k):
    from heapq import nlargest
    
    print("Choose Variation of tf: enter 1/2/3")
    #var1=int(input("enter choice"))
    var1=int(input())
    for t in doc_inv_index.keys():
        total=0
        for x in querylist:
            if x not in idf_final.keys():
                idf_final[x]=0
        
        for p in querylist:
            count1=doc_inv_index[t].count(p)
   
            if var1==1:
                 tf=count1/len(doc_inv_index[t])
            elif var1==2:
                 tf=count1
            else:
                y=count1
                tf=1+math.log(1+y,10)
                
            if p in title_dict[t]:
                tf_idf=tf*idf_final[p]
            else:
                tf_idf=0.7*tf*idf_final[p]
            total=total+tf_idf
        tf_idf_dict[t]=total

#         for p in querylist:
#             count1=doc_inv_index[t].count(p)
#             #print(count1)
            
#             tf=count1/len(doc_inv_index[t])
#             if p in title_dict[t]:
#                 tf_idf=tf*idf_final[p]+0.5(tf*idf_final[p])
#             else:
#                 tf_idf=tf*idf_final[p]
#             total=total+tf_idf
#         tf_idf_dict[t]=total
    
    
    
    kHighest = nlargest(k,tf_idf_dict,key = tf_idf_dict.get)
    
    
    for val in kHighest: 
        print(val, ":",  tf_idf_dict.get(val))
    
    

    
    
    


# In[8]:


import math
cos_query={}
cos_doc={}
cos_score={}
cos_query1={}
from heapq import nlargest
def cosine_similarity(k):
    cos_query={}
    cos_doc={}
    cos_score={}
    cos_query1={}
    print(querylist)
#     for q in querylist:
#         count=querylist.count(q)
#         y=Num_docs/(idf[q]+1)       #Num_docs/(idf[lem_word]+1) :idf formula used
#         cos_idf=math.log(y,10)
#         cos_query[q]=count*cos_idf
        
    
    cos_query1=cos_query
    for d in doc_inv_index.keys():
        cos_doc={}
        cos_query={}
        for x in querylist:
            if x not in idf.keys():
                idf[x]=0
        #cos_query=cos_query1
        for q in querylist:
            count=querylist.count(q)
            y=Num_docs/(idf[q]+1)       #Num_docs/(idf[lem_word]+1) :idf formula used
            cos_idf=math.log(y,10)
            cos_query[q]=count*cos_idf
#             if q in title_dict[d]:
#                 cos_query[q]=cos_query[q]+(cos_query[q])

#         for q in querylist:
#             if q in title_dict[d]:
#                 cos_query[q]=cos_query[q]+0.5*(cos_query[q])   

        for p in querylist:
            count1=doc_inv_index[d].count(p)
            z=count1
            tf=1+math.log(1+z,10)
            y=Num_docs/(idf[q]+1)       #Num_docs/(idf[lem_word]+1) :idf formula used
            cos_idf=math.log(y,10)
            cos_doc[p]=tf*cos_idf
        Num=0
        Q_Denom=0
        D_Denom=0
        for  p in querylist: 
            #print(p," ",cos_query[p]," ",cos_doc[p])
            Num +=cos_query[p]*cos_doc[p]
            Q_Denom +=cos_query[p]*cos_query[p]
            D_Denom +=cos_doc[p]*cos_doc[p]
#             print(Q_Denom)
#             print(D_Denom)
            
        Q_Denom=math.sqrt(Q_Denom)
        D_Denom=math.sqrt(D_Denom)
        N = Num/(1+(Q_Denom*D_Denom))
        
        cos_score[d]=N
    
        
    
    kHighest = nlargest(k,cos_score,key = cos_score.get)
    
    
    for val in kHighest: 
        print(val, ":", cos_score.get(val))
 


# In[9]:


import math
cos_query={}
cos_doc={}
cos_score={}
cos_query1={}
from heapq import nlargest
def cosine_similarity_with_title(k):
    cos_query={}
    cos_doc={}
    cos_score={}
    cos_query1={}
    print(querylist)
#     for q in querylist:
#         count=querylist.count(q)
#         y=Num_docs/(idf[q]+1)       #Num_docs/(idf[lem_word]+1) :idf formula used
#         cos_idf=math.log(y,10)
#         cos_query[q]=count*cos_idf
        
    
    cos_query1=cos_query
    for d in doc_inv_index.keys():
        cos_doc={}
        cos_query={}
        for x in querylist:
            if x not in idf.keys():
                idf[x]=0
        #cos_query=cos_query1
        for q in querylist:
            count=querylist.count(q)
            y=Num_docs/(idf[q]+1)       #Num_docs/(idf[lem_word]+1) :idf formula used
            cos_idf=1+math.log(y,10)
            cos_query[q]=count*cos_idf
            if q in title_dict[d]:
                cos_query[q]=cos_query[q]+(cos_query[q])
            else:
                cos_query[q]=0.7*count*cos_idf


        for p in querylist:
            count1=doc_inv_index[d].count(p)
            z=count1
            tf=math.log(1+z,10)
            y=Num_docs/(idf[q]+1)       #Num_docs/(idf[lem_word]+1) :idf formula used
            cos_idf=math.log(y,10)
            cos_doc[p]=tf*cos_idf
        Num=0
        Q_Denom=0
        D_Denom=0
        for  p in querylist: 
            #print(p," ",cos_query[p]," ",cos_doc[p])
            Num +=cos_query[p]*cos_doc[p]
            Q_Denom +=cos_query[p]*cos_query[p]
            D_Denom +=cos_doc[p]*cos_doc[p]
#             print(Q_Denom)
#             print(D_Denom)
            
        Q_Denom=math.sqrt(Q_Denom)
        D_Denom=math.sqrt(D_Denom)
        N = Num/(1+(Q_Denom*D_Denom))
        
        cos_score[d]=N
    
        
    
    kHighest = nlargest(k,cos_score,key = cos_score.get)
    
    
    for val in kHighest: 
        print(val, ":", cos_score.get(val))
    
               
    
   


# In[10]:



query=input()
query_list=[]

#query_list ="The three little pigs started to feel they need a real home"
  
query=query.lower()
#translator=query.maketrans(string.punctuation,'                                ')
query=query.translate(str.maketrans("","",string.punctuation))
#query=query.translate(translator)
stop_words = set(stopwords.words('english'))
query = word_tokenize(query)
query=list(query)
result = [i for i in query if not i in stop_words]
querylist=[]
lemmatizer=WordNetLemmatizer()
for word in result:
    if word.isdecimal()==True:
        word=num2words(word)
    querylist.append(lemmatizer.lemmatize(word))
print(querylist)


# In[ ]:


print("Choose the  metric to retrieve document:")
print("1.Jaccard  2.Tf-idf   3.tf_idf with title 4.Cosine Similarity 5.Cosine Similarity with title 6.Exit")
choice=int(input())
#choice=0
while(choice !=6):
    
    print("Number of documents to retrive")
    k=int(input())
    if choice ==1 :
        Jaccard_coeff(k)
    elif choice ==2 :
        choose_idf()
        #choose_tf()
        tf_idf(k)
    elif choice ==3 :
        choose_idf()
        tf_idf_with_title(k)

    elif choice ==4 :
        cosine_similarity(k)
        
    elif choice ==5 :
        cosine_similarity_with_title(k)
    else :
        exit
        
    print("Choose the  metric to retrieve document:")
    print("1.Jaccard  2.Tf-idf   3.tf_idf with title 4.Cosine Similarity 5.Cosine Similarity with title 6.Exit")
    choice=int(input())

