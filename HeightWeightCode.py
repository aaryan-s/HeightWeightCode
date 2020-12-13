import pandas as pd
import plotly.express as px

dataframe = pd.read_csv("SOCR-HeightWeight.csv")

height = list(dataframe["Height(Inches)"])
#print(height)
weight = list(dataframe["Weight(Pounds)"])
'''
#Height mean:
i = 0
x=0
while i<len(height):
    x = x+height[i]
    i+=1
print(x/len(height))
'''
'''
#Height median:
height.sort()
if len(height)%2==0:
    i = int(len(height)/2)
    print((height[i-1]+height[i])/2)
else:
    i = int(len(height)/2)
    print(height[i])
'''
'''
# Height Mode:
dictnum = Counter(height)

max = 0
for k in dictnum:
    if max<dictnum[k]:
        max = dictnum[k]
#print(max)

for k in dictnum:
    if height == dictnum[k]:  
        print(k)
'''
'''
#Weight mean:
i = 0
x=0
while i<len(weight):
    x = x+weight[i]
    i+=1
print(x/len(weight))
'''
'''
#Weight median:
weight.sort()
if len(weight)%2==0:
    i = int(len(weight)/2)
    print((height[i-1]+weight[i])/2)
else:
    i = int(len(weight)/2)
    print(weight[i])
'''
'''
# Weight Mode:
dictnum = Counter(weight)

max = 0
for k in dictnum:
    if max<dictnum[k]:
        max = dictnum[k]
#print(max)

for k in dictnum:
    if weight == dictnum[k]:  
        print(k)
'''

