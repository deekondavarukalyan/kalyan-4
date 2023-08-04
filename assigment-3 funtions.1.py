#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Write a python program to reverse the string


# In[1]:


def revers_string(word):
    for i in range(len(word)-1,-1,-1):
        print(word[i],end="")
word1=input("Enter the word that need to revers: ")
revers_string(word1)


# In[ ]:


# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.


# In[2]:


def upper_lower_number(word):
    upper_count=0
    lower_count=0
    for char in word:
        if char.isupper():
            upper_count+=1
        elif char.isspace():
            continue
        else:
            lower_count+=1
    print("The number of upper case letters are",upper_count)
    print("The number of lower case letters are",lower_count)

word=input("Enter the sentence: ")
upper_lower_number(word)


# In[ ]:




