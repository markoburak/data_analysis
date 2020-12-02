#%%

from itertools import islice
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split

#%%

data = pd.read_csv('../datasets/covid19_by_settlement_dynamics.csv', delimiter=',')


#%%

data.head()

#%%

data.drop(columns=['registration_region', 'registration_settlement', 'new_susp', 'new_confirm', 'new_death' ,'new_recover'], inplace=True)

#%%

data = data.groupby(['zvit_date', 'registration_area']).sum()

#%%

data.reset_index(inplace=True)

#%%

data.set_index('zvit_date', inplace=True)

#%%

data.head()

#%%

new_df = pd.DataFrame()

#%%

for area in data.registration_area.unique():
    new_df[area] = data.loc[data.registration_area == area].active_confirm

#%%

new_df = new_df.fillna(0)

#%%

new_df.head()



#%%

new_df.corr()

#%%

def lag_corr(series1: pd.Series, series2: pd.Series, lag: int):
    if lag == 0 :
        return series1.corr(series2)
    shifted = series1.shift(lag)
    shifted.dropna()
    return shifted.iloc[abs(lag):-abs(lag)].corr(series2.iloc[abs(lag):-abs(lag)])


#%%

def best_lag(series1: pd.Series, series2: pd.Series, max_lag: int):
    best_corr = lag_corr(series1, series2, 0)
    best_lag = 0
    for lag in range(-max_lag, max_lag + 1):
        corr = lag_corr(series1, series2, lag)
        if corr > best_corr:
            best_сorr, best_lag = corr, lag
    return best_corr, best_lag

#%%

corr_best = new_df.corr(method=lambda x, y: best_lag(pd.Series(x), pd.Series(y), max_lag=30)[0])
corr_best

#%%

corr_lag = new_df.corr(method=lambda x, y: best_lag(pd.Series(x), pd.Series(y), max_lag=30)[1])
corr_lag

#%%

f, ax = plt.subplots(figsize=(11, 9))
mask = np.triu(np.ones_like(corr_best, dtype=bool))
sns.heatmap(corr_best, mask=mask)

#%%


f, ax = plt.subplots(figsize=(20, 20))
sns.heatmap(corr_lag, annot=True, center = 0, cmap='coolwarm')

#%%

lead = new_df.columns[new_df.iloc[-1].argmax()]
lead

#%%

top_lag_area = corr_lag.columns[corr_lag[lead].argmax()]
print(f"{top_lag_area} відстає від {lead} на {corr_lag[lead].max()} днів")

#%%


leader = corr_lag > 0
all_count = leader.sum(axis=1)

#print(all_count.sort_values())
leader1 = all_count.index[all_count.argmax()]
leader2 = 'Тернопільська'
leader3 = 'Миколаївська'
print(leader3, all_count.max())
print(all_count)

#%%

def prediction(data, values_for_x, values_for_y, days):


    reg_lag = corr_lag[values_for_x][values_for_y]
    df = pd.DataFrame({'x': data[values_for_x].shift(int(reg_lag)), 'y':data[values_for_y]})
    df = df.dropna()
    x1 = np.array(df.x).reshape(-1, 1)


    x_train = x1[:-days]
    x_test = x1[-days:]
    y_train = df.y[:-days]
    y_test = df.y[-days:]
    regr = LinearRegression()
    regr.fit(x_train, y_train)
    y_pred = regr.predict(x_test)

    print(f'r2: {r2_score(y_test, y_pred)}')
    print(f'rmse - {mean_squared_error(y_test, y_pred)}')
    return y_pred

#%%



#%%

col = corr_best.columns.tolist()
pred = pd.DataFrame()

days = 60
for i in col:
    print(i)
    pred[leader1] = new_df[leader1][-days:]
    pred[i] = prediction(new_df, leader1, i, days)
print(pred)


#%%

figure = plt.figure(figsize=(10, 10))
figure.autofmt_xdate()
for i in col:
    plt.plot(pred.index, pred[i], color = 'red', label='predicted' )
    plt.plot(pred.index, new_df[(pred.index[0]):(pred.index[-1])][i], label='original',  color = 'black')

    plt.xticks(rotation=45, fontsize=5)
    plt.legend()
    plt.title(i)
    plt.show()
    #plt.savefig('foo.png')

#%%


col = corr_best.columns.tolist()
pred = pd.DataFrame()

days = 60
for i in col:
    pred[leader2] = new_df[leader2][-days:]
    pred[i] = prediction(new_df, leader2, i, days)
pred


#%%

figure = plt.figure(figsize=(10, 10))
figure.autofmt_xdate()
for i in col:
    plt.plot(pred.index, pred[i], color = 'red', label='predicted' )
    plt.plot(pred.index, new_df[(pred.index[0]):(pred.index[-1])][i], label='original',  color = 'black')
    plt.xticks(rotation=45, fontsize=5)
    plt.legend()
    plt.title(i)
    plt.show()
    #plt.savefig('foo.png'

#%%


