import pandas as pd
import matplotlib.pyplot as plt
data = {
        'Name':['John', 'Vihan', 'Numbo', 'Krishna', 'Arithi'],
        'Social':[15, 50, 75, 96, 37],
        'English':[95, 95, None, 65, 60],
        'Hindi':[60, 85, 64, 56, 67],
        'Math':[50, 13, None, 6, 90],
        'Science':[59, None, None, None, None]}
df = pd.DataFrame(data)
print('Original DataFrame')
print(df)
pivot_table = df.melt(id_vars=['Name'],var_name = 'Subject', value_name = 'Scores')
pivot_table = pivot_table.pivot_table(index = 'Name', columns = 'Subject', values = 'Scores', aggfunc='mean')
print("\n pivot_table:")
print(pivot_table)
df['Total'] = df[['Social', 'English', 'Hindi', 'Math', 'Science']].sum(axis=1)
print("\nDataFrame with total scores:")
print(df)
sorted_df = df[df['English'] > 80].sort_values(by='English', ascending=False)
print("\nsorted DataFrame('English > 80'):")
df.plot(kind='bar', x='Name', y=['Social', 'English', 'Hindi', 'Math', 'Science'],stacked=True)
plt.xlabel('Name')
plt.ylabel('Scores')
plt.title('Student total scores')
plt.show()
