#
# import pandas as pd
# from matplotlib import pyplot as plt
#
# x = []
# y = []
# z = []
# # with open('Book1.1.csv', 'r') as csvfile:
#
# # plots = csv.reader(csvfile, delimiter=',')
# df = pd.read_csv('Book1.csv')
# state_code = df.loc[df['Name'] == 'Cornette', 'Name'].iloc[0]
# state_code.rename(columns={'Name': "Cornette"}, inplace=True)
# print(df)
# state_code.plot(x='Name', figsize=(10, 5), grid=True)
# # plt.show()
# # df = df.sort_values('Months of Treatment', ascending=False)
# plt.show()
import calendar

import pandas as pd
import matplotlib.pyplot as plt

# Read the csv file into a pandas dataframe
df = pd.read_csv("Book1.csv")

# # # Filter the data based on some condition
df_data = df[df['Name'] == 'dannz']

month = ['Jan', 'Feb', 'Mar', 'Apr', 'Jun', 'July']
eating_behaviour = []
harm_behaviour = []
mood_behaviour = []
social_interactions = []


for i in range(1, 7):

    eating_behaviour.append(df_data[calendar.month_abbr[i]+"-Eating-Behaviour"])
    harm_behaviour.append(df_data[calendar.month_abbr[i]+"-Self-Harm"])
    mood_behaviour.append(df_data[calendar.month_abbr[i]+"-Mood"])
    social_interactions.append(df_data[calendar.month_abbr[i]+"-Social-Interactions"])
#
#
print(eating_behaviour)
print(harm_behaviour)
#
plt.plot(month, eating_behaviour, label='Eating')
plt.plot(month, harm_behaviour, label='Harm')
plt.plot(month, mood_behaviour, label='mood')
plt.plot(month, social_interactions, label='social')

plt.xlabel('month')
plt.ylabel('Behaviour')
plt.title('patient History')
plt.legend()
plt.show()


# print(df_data)

# for i in range(1, 8):
#     df = pd.DataFrame(df_data, columns=["Name", calendar.month_abbr[i] + "-Eating-Behaviour",
#                                         calendar.month_abbr[i] + "-Self-Harm",
#                                         calendar.month_abbr[i] + "-Social-Interactions"])

# df[["month"]] = df.apply([df['month'] for i in calendar.month_abbr[i]], axis=1, result_type="expand")
# df.plot(x="Name", figsize=(10, 5), grid=True )
# df.plot(x="Eating-Behaviour", figsize=(10, 5), grid=True )
# df.plot(x="Name", figsize=(10, 5), grid=True )
# df.plot(x="Name", figsize=(10, 5), grid=True )
# df.plot(x="Name", figsize=(10, 5), grid=True )
# df.plot(x="Name", figsize=(10, 5), grid=True )
# plt.plot(x, y, label = "line 1")
# plt.plot(y, x, label = "line 2")

# print(df)
# for i in range(1, 7):
#     df.plot(x="Name", y=[[calendar.month_abbr[i]+"-Eating-Behaviour",
#                          calendar.month_abbr[i]+"-Self-Harm",
#                          calendar.month_abbr[i]+"-Social-Interactions"]],
#             figsize=(9, 8))

# for i in range(1, 13):
#     #     plt.plot(monthly_data.loc[i, 'column_name'], label=calendar.month_abbr[i])
#     # plot the dataframe
#     df.plot(x="Name", y=[calendar.month_abbr[i]+"-Eating Behaviour", calendar.month_abbr[i]+"-Self-Harm",
#                          calendar.month_abbr[i]+"-Social Interactions"], kind='bar',
#             figsize=(9, 8))

plt.show()

# print(df_data['Jan-Self-Harm'])
# plt.plot(df_data['Jan-Eating Behaviour'], df_data['Feb-Eating Behaviour'], label='Eating Behavior')
# plt.plot(df_data['Jan-Self-Harm'], df_data['Feb-Self-Harm'], label='Harm Behavior')

# Change the number of columns here
# plt.legend(ncol=3)
#
# plt.show()

# print(df)
# # Plot the graph using Matplotlib
# plt.plot(df['Name'])


#
# plt.xlabel('Month')
# plt.ylabel('Average Value')
# plt.title('Monthly Average Plot')
# plt.legend()
# plt.show()
# plt.xlabel('Name')
# plt.ylabel('Jun-Social Interactions')
# plt.title('Graph Title')
# plt.show()


# df['date'] = pd.to_datetime(df['date'])
#
# # Set the date column as the index
# df.set_index('date', inplace=True)
#
# # Group the data by month
# monthly_data = df.groupby(df.index.month).mean()
#
# # Plot the graph for each month
# for i in range(1, 13):
#     plt.plot(monthly_data.loc[i, 'column_name'], label=calendar.month_abbr[i])
#
# plt.xlabel('Month')
# plt.ylabel('Average Value')
# plt.title('Monthly Average Plot')
# plt.legend()
# plt.show()
