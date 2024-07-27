import pandas as pd 
data = {"Ename": ["Roshan", "Amar", "Ashwini", "Lohith", "Mohan", "Pramod"],
      "Type": ["Regular", "Adhoc", "Regular", "Adhoc", "Contract", "Regular"],
      "Department": ["CS", "CS", "EC", "EC", "CS", "EC"],
      "Experience": [10, 20, 5, 14, 9, 8],
      "Salary": [50000, 15000, 30000, 15000, 10000, 40000]}
df = pd.DataFrame(data)
pivot_a = pd.pivot_table(df, values="Salary", index="Type", columns="Department", aggfunc="mean")
print(pivot_a)
pivot_b = pd.pivot_table(df, values="Salary", index="Type", aggfunc=["sum", "mean", "count"])
print(pivot_b)
pivot_c = pd.pivot_table(df, values="Salary", index="Type", aggfunc="std")
print(pivot_c)