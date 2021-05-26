import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

store_data= pd.read_csv('dataset.csv' , header= None)
# print(store_data.shape)
# print(store_data)
records = []

for i in range(0,50):
	records.append([str(store_data.values[i,j]) for j in range(0,6)])

# print(records)
association_rules = apriori(records, min_support=0.0045, min_confidence=0.4, min_lift=1.9, min_length=2)
association_results = list(association_rules)
print(len(association_results))
print("=====================================")
print(association_results)
print("=====================================")

for item in association_results:

    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])
    print("Support: " + str(item[1]))
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")