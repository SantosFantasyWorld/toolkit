# import pandas as pd
# df = pd.DataFrame({
#     'col1':range(10),
#     'col2':range(10,20)
# })
# print(df)
# crit = (df.loc[:, 'col2'] % 2 == 0) & (df.loc[:, 'col2'] % 3 == 0)
# df.loc[crit,'col2'] = -1
# print(df)
import pandas as pd
nba_stats = pd.DataFrame({
    'team':['lakers','lakers','neta','neta','76ers','76ers'],
    'player':['lebron','davie','kyzie','durant','harden','embiid'],
    'ppg':[30,20,29,16,26,28]
})
print(nba_stats)

groups = nba_stats.groupby('team')

def get_max(df):
    df = df.max()
    return df

for firm, idx in groups.groups.items():
   print(f"get_last applied to df[df.firm=='{firm}']:")
   print("----------------------------------------")
   print(get_max(nba_stats.loc[idx]))
   print("----------------------------------------")
   print("")
#