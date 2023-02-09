import pandas as pd
from matplotlib import pyplot as plt

x = []
y = []
z = []

df = pd.read_csv('Book1.1.csv')
df.plot(x='Name', figsize=(10, 5), grid=True)
# plt.show()
df = df.sort_values('Months of Treatment', ascending=False)
plt.show()
