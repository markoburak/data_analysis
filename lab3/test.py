import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt


def lag_corr(x, y, lag):
    mxl, mxc = 0, x.corr(y)
    for cur_lag in range(1, lag + 1):
        cur_corr = x.corr(y.shift(cur_lag))
        if cur_corr > mxc:
            mxl = cur_lag
            mxc = cur_corr
    return mxl, mxc


# data = pd.read_csv('covid19_by_area_type_hosp_dynamics.csv', delimiter=',')
url = 'https://raw.githubusercontent.com/VasiaPiven/covid19_ua/master/covid19_by_area_type_hosp_dynamics.csv'
data = pd.read_csv(url, error_bad_lines=False)

pd.options.display.max_rows = 1000
pd.options.display.max_columns = 1000
active_confirm_by_area = pd.DataFrame()
for a in data['registration_area'].unique():
    active_confirm_by_area = pd.concat([active_confirm_by_area, data.loc[data['registration_area'] == a].groupby(
        'zvit_date').sum()['active_confirm'].to_frame(name=a)], axis=1)

active_confirm_by_area = active_confirm_by_area.sort_index().fillna(method='ffill').fillna(0.0)


print(active_confirm_by_area)

active_confirm_by_area_correlation = active_confirm_by_area.corr()

areas = active_confirm_by_area.columns
lag_table = pd.DataFrame(0, columns=areas, index=areas)
lag_corr_table = pd.DataFrame(0.0, columns=areas, index=areas)
for row in areas:
    for column in areas:
        lag, corr = lag_corr(active_confirm_by_area[row], active_confirm_by_area[column], 250)
        lag_table.at[row, column] = lag
        lag_corr_table.at[row, column] = corr


# lag_table.to_csv('lag_table.csv')
# lag_corr_table.to_csv('lag_corr_table.csv')
# lag_table = pd.read_csv('lag_table.csv', delimiter=',', header=0, index_col=0)
# lag_corr_table = pd.read_csv('lag_corr_table.csv', delimiter=',', header=0, index_col=0)
# print(lag_table)
# print(lag_corr_table)

sn.heatmap(lag_table, cmap='magma')
plt.show()
sn.heatmap(lag_corr_table, cmap='magma')
plt.show()

# leader = active_confirm_by_area.iloc[-1:].idxmax(axis=1)[0]
# test_lag = lag_table.at[leader, 'Львівська']
# shifter = active_confirm_by_area['Львівська'].shift(test_lag).fillna(0)
