Appendix: Python codes: -
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv('data.csv', encoding="ISO-8859-1")
data = data.dropna()
data.info()
data['Country'].unique()
data.describe()
data.describe(exclude='number')
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
print("""This Dataset start from {}
 to {}""".format(data['InvoiceDate'].describe()['first'],
 data['InvoiceDate'].describe()['last']))
data_plus = data[data['Quantity']>=0]
data_plus.info()
data_plus.describe()
top_10 = data_plus.groupby('Country').nunique().sort_values('Invoice',
ascending=False).head(10)
top_10
top_10_transaction =
pd.DataFrame(data_plus.groupby('Country').nunique().sort_values('Invoice',

ascending=False).head(10)['Invoice'])
top_10_transaction
#Import plotly.express libraries for visualization
import plotly.express as px
# total bookings per market segment (incl. canceled)
segments=top_10_transaction
# pie plot
fig = px.pie(segments,
 values=top_10_transaction['Invoice'],
 names=top_10_transaction.index,
 title="Country Performance by Number of Invoice",
 template="seaborn")
fig.update_traces(rotation=-90, textinfo="percent+label")
fig.show()
basket_plus = (data_plus[data_plus['Country'] =="United Kingdom"].groupby(['Invoice',
'Description'])['Quantity']
 .sum().unstack().reset_index().fillna(0).set_index('Invoice'))
basket_plus
basket_plus.tail()
def encode_units(x):
 if x <= 0:
 return 0
 if x >= 1:
 return 1

basket_encode_plus = basket_plus.applymap(encode_units)
basket_encode_plus
basket_encode_plus.tail()
basket_filter_plus = basket_encode_plus[(basket_encode_plus > 0).sum(axis=1) >= 2]
basket_filter_plus
from mlxtend.frequent_patterns import apriori
frequent_itemsets_plus = apriori(basket_filter_plus, min_support=0.03,
 use_colnames=True).sort_values('support',
ascending=False).reset_index(drop=True)
frequent_itemsets_plus['length'] = frequent_itemsets_plus['itemsets'].apply(lambda x:
len(x))
frequent_itemsets_plus
frequent_itemsets_plus[ (frequent_itemsets_plus['length'] == 2) &
 (frequent_itemsets_plus['support'] >= 0.03) ]
from mlxtend.frequent_patterns import association_rules
association_rules(frequent_itemsets_plus, metric='lift',
 min_threshold=1).sort_values('lift',
ascending=False).reset_index(drop=True)