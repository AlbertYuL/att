import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.loc[data['whoAmI'] == 'human', 'human'] = 1
data.loc[data['whoAmI'] == 'robot', 'human'] = 0
data.loc[data['whoAmI'] == 'human', 'robot'] = 0
data.loc[data['whoAmI'] == 'robot', 'robot'] = 1
data['human'] = data['human'].astype(int)
data['robot'] = data['robot'].astype(int)
data = data.drop(columns='whoAmI')

#print(pd.get_dummies(data['whoAmI']))
print(data.head(10))