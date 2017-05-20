
# coding: utf-8

# In[2]:

import pandas as pd
from pandas import Series,DataFrame


# In[3]:

titanicdf = pd.read_csv('train.csv')


# In[3]:

titanicdf.head()


# In[4]:

titanicdf.info()


# In[6]:

#questions:
#    1)who are the passangers?
#    2)what deck where they and the relationship between that and their class?
#    3)their origins?
#    4)who was alone and who was with family?
#    5) factors of surviving?


# In[11]:

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
get_ipython().magic('matplotlib inline')


# In[29]:

sb.factorplot('Sex',data=titanicdf,kind='count')


# In[32]:

sb.factorplot('Sex',data=titanicdf,kind='count',hue='Pclass')


# In[35]:

sb.factorplot('Pclass',data=titanicdf,kind='count',hue='Sex')


# In[53]:

def male_fem_chiled(passenger):
       age,sex = passenger
       
       
       if age < 16:
           return 'child'
       else:
           return sex


# In[54]:

titanicdf['person'] = titanicdf[['Age','Sex']].apply(male_fem_chiled, axis=1)


# In[39]:

titanicdf[0:10]


# In[40]:

sb.factorplot('Pclass',data=titanicdf,kind='count',hue='person')


# In[45]:

titanicdf['Age'].hist(bins=80)


# In[46]:

titanicdf['Age'].mean()


# In[47]:

titanicdf['person'].value_counts()


# In[48]:

fig = sb.FacetGrid(titanicdf,hue='Sex',aspect=4)
fig.map(sb.kdeplot,'Age',shade=True)


oldest = titanicdf['Age'].max()


fig.set(xlim=(0,oldest))
fig.add_legend()


# In[49]:

fig = sb.FacetGrid(titanicdf,hue='person',aspect=4)
fig.map(sb.kdeplot,'Age',shade=True)


oldest = titanicdf['Age'].max()


fig.set(xlim=(0,oldest))
fig.add_legend()


# In[50]:

fig = sb.FacetGrid(titanicdf,hue='Pclass',aspect=4)
fig.map(sb.kdeplot,'Age',shade=True)


oldest = titanicdf['Age'].max()


fig.set(xlim=(0,oldest))
fig.add_legend()


# In[5]:

titanicdf.head()


# In[8]:

deck = titanicdf['Cabin'].dropna()


# In[10]:

deck.head()


# In[28]:

levls = []


for lev in deck:
    levls.append(lev[0])
    
    
cabdf = DataFrame(levls)
cabdf.columns = ['Cabin']
sb.factorplot('Cabin',data=cabdf,kind='count',palette='winter_d',size=10)


# In[29]:

sb.factorplot('Embarked',data=titanicdf,kind='count',hue='Pclass',size=10)


# In[30]:

#who was alone and who was not alone


# In[31]:

titanicdf['Alone'] = titanicdf.SibSp + titanicdf.Parch


# In[33]:

titanicdf['Alone'].head()


# In[34]:

titanicdf['Alone'].loc[titanicdf['Alone']>0] = 'with family'
titanicdf['Alone'].loc[titanicdf['Alone']==0] = 'alone'


# In[35]:

titanicdf.head()


# In[37]:

sb.factorplot('Alone',data=titanicdf,kind='count',palette='Blues')


# In[43]:

titanicdf['Survivor'] = titanicdf.Survived.map({0:'no',1:'yes'})
sb.factorplot('Survivor',data=titanicdf,kind='count')


# In[48]:

sb.factorplot(x='Pclass',y='Survived',data=titanicdf)


# In[55]:

sb.factorplot(x='Pclass',y='Survived',data=titanicdf,hue='person')


# In[56]:

sb.lmplot('Age','Survived',data=titanicdf)


# In[57]:

sb.lmplot('Age','Survived',hue='Pclass',data=titanicdf)


# In[58]:

gen = [10,20,40,60,80]
sb.lmplot('Age','Survived',hue='Pclass',data=titanicdf,x_bins=gen)


# In[59]:

sb.lmplot('Age','Survived',hue='Sex',data=titanicdf,x_bins=gen)


# In[65]:

titanicdf.head()


# In[70]:

sb.factorplot('Deck', data=titanicdf,kind='count', hue='Survived',order=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'T','n'])


# In[71]:

sb.factorplot('Deck', data=titanicdf,kind='count', hue='Survived',order=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'T'])


# In[72]:

#people with no deck had a better chance  to survive.....yeah poor people got lucky


# In[73]:

#having a family member increase the odds of surviving the crash?


# In[75]:

sb.factorplot('Survived', data=titanicdf, hue='Alone',kind='count')


# In[76]:

#children and women 1st .....


# In[77]:

titanicdf['Alone'].value_counts()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



