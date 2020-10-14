import random
import matplotlib.colors as mcolors
import numpy as np
import datetime
import matplotlib.patches as mpatches
import matplotlib.dates as mdates
import seaborn as sns


def graphs(plt, df2, pd):
    while (True):
        print('For what value you want to graph a chart?\n'
              'max dots\n'
              'linear\n'
              'pie\n'
              'hist\n'
              'box\n')
        answ = input()

        if answ == 'max dots':
            while (True):
                print('"pressure" or "temperature" or "dew point" or "humidity" or "wind speed" or "wind gust" or '
                      '"precip"?')
                answ2 = input()
                if answ2 == 'pressure':
                    plt.title('Dot Graph')

                    p_max = df2.groupby('day/month').agg({'Pressure': 'max'})

                    plt.plot(p_max, 'o')
                    patch = mpatches.Patch(color='blue', label='max per day')
                    plt.legend(handles=[patch])
                    plt.xticks(rotation=45)
                    plt.xlabel('day/month/year')
                    plt.ylabel('max pressure')
                    plt.show()
                elif answ2 == 'temperature':
                    plt.title('Dot Graph')
                    t_max = df2.groupby('day/month').agg({'Temperature': 'max'})

                    plt.plot(t_max, 'o')
                    patch = mpatches.Patch(color='blue', label='max per day')
                    plt.legend(handles=[patch])
                    plt.xticks(rotation=45)
                    plt.xlabel('day/month/year')
                    plt.ylabel('max temperature(C)')
                    plt.show()
                elif answ2 == 'time':
                    new_time = [datetime.datetime.combine(datetime.date.today(), t) for t in df2['Time']]
                    df2['Time'] = new_time
                elif answ2 == 'dew point':
                    plt.title('Dot Graph')
                    t_max = df2.groupby('day/month').agg({'Dew Point': 'max'})

                    plt.plot(t_max, 'o')
                    plt.xticks(rotation=45)
                    patch = mpatches.Patch(color='blue', label='max per day')
                    plt.legend(handles=[patch])
                    plt.xlabel('day/month/year')
                    plt.ylabel('Dew Point')
                    plt.show()
                elif answ2 == 'humidity':
                    plt.title('Dot Graph')
                    t_max = df2.groupby('day/month').agg({'Humidity': 'max'})

                    plt.plot(t_max, 'o')
                    patch = mpatches.Patch(color='blue', label='max per day')
                    plt.legend(handles=[patch])
                    plt.xticks(rotation=45)
                    plt.xlabel('day/month/year')
                    plt.ylabel('Humidity')
                    plt.show()
                elif answ2 == 'wind speed':
                    plt.title('Dot Graph')
                    t_max = df2.groupby('day/month').agg({'Wind Speed': 'max'})

                    plt.plot(t_max, 'o')
                    patch = mpatches.Patch(color='blue', label='max per day')
                    plt.legend(handles=[patch])
                    plt.xticks(rotation=45)
                    plt.xlabel('day/month/year')
                    plt.ylabel('Wind Speed')
                    plt.show()
                elif answ2 == 'wind gust':
                    plt.title('Dot Graph')
                    t_max = df2.groupby('day/month').agg({'Humidity': 'max'})

                    plt.plot(t_max, 'o')
                    patch = mpatches.Patch(color='blue', label='max per day')
                    plt.legend(handles=[patch])
                    plt.xticks(rotation=45)
                    plt.xlabel('day/month/year')
                    plt.ylabel('Wind gust')
                    plt.show()
                elif answ2 == 'precip':
                    plt.title('Dot Graph')
                    t_max = df2.groupby('day/month').agg({'Precip.': 'max'})

                    plt.plot(t_max, 'o')
                    patch = mpatches.Patch(color='blue', label='max per day')
                    plt.legend(handles=[patch])
                    plt.xticks(rotation=45)
                    plt.xlabel('day/month/year')
                    plt.ylabel('Precip.')
                    plt.show()
                elif answ2 == 'exit':
                    break
                else:
                    print('wrong command')
        elif answ == "linear":
            while (True):
                print('"pressure" or "temperature" or "dew point" or "humidity" or "wind speed" or "wind gust" or '
                      '"precip"?')
                answ2 = input()
                if answ2 == 'humidity':
                    plt.title('Linear Graph')
                    pd.options.mode.chained_assignment = None
                    t_max = df2.groupby('day/month').agg({'Humidity': 'max'})
                    t_max1 = t_max.iloc[:int(len(t_max) / 2)]
                    t_max2 = t_max.iloc[int(len(t_max) / 2 + 1):]

                    index_list = list(range(1, len(t_max1) + 1))
                    t_max1['count'] = index_list
                    t_max2['count'] = index_list

                    ax = plt.gca()
                    t_max1.plot(kind='line', x='count', y='Humidity', ax=ax)
                    t_max2.plot(kind='line', x='count', y='Humidity', ax=ax)
                    ax.legend(["First half", "Second half"])
                    ax.grid('on', which='minor', axis='y')
                    ax.grid('off', which='major', axis='y')
                    plt.xticks(rotation=45)
                    plt.xlabel('day/month/year')
                    plt.ylabel('max Humidity %')
                    plt.show()
                elif answ2 == 'temperature':

                    pd.options.mode.chained_assignment = None
                    t_max = df2.groupby('day/month').agg({'Temperature': 'max'})
                    t_max1 = t_max.iloc[:int(len(t_max) / 2)]
                    t_max2 = t_max.iloc[int(len(t_max) / 2 + 1):]

                    index_list = list(range(1, len(t_max1) + 1))
                    t_max1['count'] = index_list
                    t_max2['count'] = index_list

                    ax = plt.gca()
                    t_max1.plot(kind='line', x='count', y='Temperature', ax=ax)
                    t_max2.plot(kind='line', x='count', y='Temperature', ax=ax)
                    ax.legend(["First half", "Second half"])
                    ax.grid('on', which='minor', axis='y')
                    ax.grid('off', which='major', axis='y')
                    plt.title('Linear Graph')
                    plt.xticks(rotation=45)
                    plt.xlabel('day/month/year')
                    plt.ylabel('max Temperature')
                    plt.show()
                elif answ2 == 'pressure':
                    pd.options.mode.chained_assignment = None
                    t_max = df2.groupby('day/month').agg({'Pressure': 'max'})
                    t_max1 = t_max.iloc[:int(len(t_max) / 2)]
                    t_max2 = t_max.iloc[int(len(t_max) / 2 + 1):]

                    index_list = list(range(1, len(t_max1) + 1))
                    t_max1['count'] = index_list
                    t_max2['count'] = index_list

                    ax = plt.gca()
                    t_max1.plot(kind='line', x='count', y='Pressure', ax=ax)
                    t_max2.plot(kind='line', x='count', y='Pressure', ax=ax)
                    ax.legend(["First half", "Second half"])
                    ax.grid('on', which='minor', axis='y')
                    ax.grid('off', which='major', axis='y')
                    plt.title('Linear Graph')
                    plt.xticks(rotation=45)
                    plt.xlabel('day/month/year')
                    plt.ylabel('max Pressure')
                    plt.show()
                elif answ2 == 'dew point':
                    pd.options.mode.chained_assignment = None
                    t_max = df2.groupby('day/month').agg({'Dew Point': 'max'})
                    t_max1 = t_max.iloc[:int(len(t_max) / 2)]
                    t_max2 = t_max.iloc[int(len(t_max) / 2 + 1):]

                    index_list = list(range(1, len(t_max1) + 1))
                    t_max1['count'] = index_list
                    t_max2['count'] = index_list

                    ax = plt.gca()
                    t_max1.plot(kind='line', x='count', y='Dew Point', ax=ax)
                    t_max2.plot(kind='line', x='count', y='Dew Point', ax=ax)
                    ax.legend(["First half", "Second half"])
                    ax.grid('on', which='minor', axis='y')
                    ax.grid('off', which='major', axis='y')
                    plt.title('Linear Graph')
                    plt.xticks(rotation=45)
                    plt.xlabel('day/month/year')
                    plt.ylabel('max Dew Point')
                    plt.show()
                elif answ2 == 'wind speed':
                    pd.options.mode.chained_assignment = None
                    t_max = df2.groupby('day/month').agg({'Wind Speed': 'max'})
                    t_max1 = t_max.iloc[:int(len(t_max) / 2)]
                    t_max2 = t_max.iloc[int(len(t_max) / 2 + 1):]

                    index_list = list(range(1, len(t_max1) + 1))
                    t_max1['count'] = index_list
                    t_max2['count'] = index_list

                    ax = plt.gca()
                    t_max1.plot(kind='line', x='count', y='Wind Speed', ax=ax)
                    t_max2.plot(kind='line', x='count', y='Wind Speed', ax=ax)
                    ax.legend(["First half", "Second half"])
                    ax.grid('on', which='minor', axis='y')
                    ax.grid('off', which='major', axis='y')
                    plt.title('Linear Graph')
                    plt.xticks(rotation=45)
                    plt.xlabel('day/month/year')
                    plt.ylabel('max Wind Speed')
                    plt.show()
                elif answ2 == 'wind gust':
                    pd.options.mode.chained_assignment = None
                    t_max = df2.groupby('day/month').agg({'Wind Gust': 'max'})
                    t_max1 = t_max.iloc[:int(len(t_max) / 2)]
                    t_max2 = t_max.iloc[int(len(t_max) / 2 + 1):]

                    index_list = list(range(1, len(t_max1) + 1))
                    t_max1['count'] = index_list
                    t_max2['count'] = index_list

                    ax = plt.gca()
                    t_max1.plot(kind='line', x='count', y='Wind Gust', ax=ax)
                    t_max2.plot(kind='line', x='count', y='Wind Gust', ax=ax)
                    ax.legend(["First half", "Second half"])
                    ax.grid('on', which='minor', axis='y')
                    ax.grid('off', which='major', axis='y')
                    plt.title('Linear Graph')
                    plt.xticks(rotation=45)
                    plt.xlabel('day/month/year')
                    plt.ylabel('max Wind Gust')
                    plt.show()
                elif answ2 == 'precip':
                    pd.options.mode.chained_assignment = None
                    t_max = df2.groupby('day/month').agg({'Precip.': 'max'})
                    t_max1 = t_max.iloc[:int(len(t_max) / 2)]
                    t_max2 = t_max.iloc[int(len(t_max) / 2 + 1):]

                    index_list = list(range(1, len(t_max1) + 1))
                    t_max1['count'] = index_list
                    t_max2['count'] = index_list

                    ax = plt.gca()
                    t_max1.plot(kind='line', x='count', y='Precip.', ax=ax)
                    t_max2.plot(kind='line', x='count', y='Precip.', ax=ax)
                    ax.legend(["First half", "Second half"])
                    ax.grid('on', which='minor', axis='y')
                    ax.grid('off', which='major', axis='y')
                    plt.title('Linear Graph')
                    plt.xticks(rotation=45)
                    plt.xlabel('day/month/year')
                    plt.ylabel('max Precip. ')
                    plt.show()
                elif answ2 == 'exit':
                    break
                else:
                    print('wrong command')
        elif answ == "pie":
            print('wind or condition?')
            answ2 = input()
            colors = random.choices(list(mcolors.CSS4_COLORS.values()), k=40)
            if answ2 == "wind":
                sums_wind = df2.groupby('Wind').size().reset_index(name='Wind_value')
                sums_wind.set_index('Wind', inplace=True)
                sums_wind.plot.pie(y='Wind_value', figsize=(9, 9), labels=None, colors=colors)
                plt.title('Pie Chart')
                plt.show()
            if answ2 == "cond":
                sums_cond = df2.groupby('Condition').size().reset_index(name='Condition_value')
                sums_cond.set_index('Condition', inplace=True)
                sums_cond.plot.pie(y='Condition_value', figsize=(9, 9), labels=None, colors=colors)
                plt.title('Pie Chart')
                plt.show()
        elif answ == "hist":
            while (True):
                print('"pressure" or "temperature" or "dew point" or "humidity" or "wind speed" or "wind gust" or '
                      '"precip"?')
                answ2 = input()
                if answ2 == "wind speed":
                    sums_wind_speed = df2.groupby('Wind Speed').size().reset_index(name='Wind speed frequency')
                    sums_wind_speed.set_index('Wind Speed', inplace=True)
                    sums_wind_speed.hist()
                    plt.xlabel('Velocity', fontsize=15)
                    plt.ylabel('Frequency per day', fontsize=15)
                    plt.title('Histogram')
                    plt.xticks(fontsize=15)
                    plt.yticks(fontsize=15)
                    patch = mpatches.Patch(color='blue', label='amount per day')
                    plt.legend(handles=[patch])
                    x_new = [x for x in range(0, 140, 10)]
                    plt.xticks(x_new)
                    plt.show()
                elif answ2 == "wind gust":
                    frame = df2['Wind Gust']
                    frame.hist()
                    plt.xlabel('Wind Gust', fontsize=15)
                    plt.ylabel('Frequency', fontsize=15)
                    patch = mpatches.Patch(color='blue', label='amount')
                    plt.legend(handles=[patch])
                    plt.title('Histogram')
                    plt.show()
                elif answ2 == "pressure":
                    frame = df2['Pressure']
                    frame.hist()
                    plt.xlabel('Pressure', fontsize=15)
                    plt.ylabel('Frequency', fontsize=15)
                    patch = mpatches.Patch(color='blue', label='amount')
                    plt.legend(handles=[patch])
                    plt.title('Histogram')
                    plt.show()
                elif answ2 == "temperature":
                    frame = df2['Temperature']
                    frame.hist()
                    plt.xlabel('Temperature', fontsize=15)
                    plt.ylabel('Frequency', fontsize=15)
                    patch = mpatches.Patch(color='blue', label='amount')
                    plt.legend(handles=[patch])
                    plt.title('Histogram')
                    plt.show()
                elif answ2 == "dew point":
                    frame = df2['Dew Point']
                    frame.hist()
                    plt.xlabel('Dew Point', fontsize=15)
                    plt.ylabel('Frequency', fontsize=15)
                    patch = mpatches.Patch(color='blue', label='amount')
                    plt.legend(handles=[patch])
                    plt.title('Histogram')
                    plt.show()
                elif answ2 == "humidity":
                    frame = df2['Humidity']
                    frame.hist()
                    plt.xlabel('Humidity', fontsize=15)
                    plt.ylabel('Frequency', fontsize=15)
                    patch = mpatches.Patch(color='blue', label='amount')
                    plt.legend(handles=[patch])
                    plt.title('Histogram')
                    plt.show()
                elif answ2 == "precip":
                    frame = df2['Precip.']
                    frame.hist()
                    plt.xlabel('Precip', fontsize=15)
                    plt.ylabel('Frequency', fontsize=15)
                    patch = mpatches.Patch(color='blue', label='amount')
                    plt.legend(handles=[patch])
                    plt.title('Histogram')
                    plt.show()
                elif answ2 == 'exit':
                    break
                else:
                    print('wrong command')
        elif answ == "box":
            while (True):
                print('"pressure" or "temperature" or "dew point" or "humidity" or "wind speed" or "wind gust" or '
                      '"precip"?')
                answ2 = input()
                if answ2 == "temperature":
                    plt.figure(figsize=(15, 15))
                    df2 = df2.reset_index()
                    box = sns.boxplot(x='Temperature', y='day/month', orient='h', data=df2, linewidth=2)
                    plt.title('Box plot')
                    plt.show()
                elif answ2 == "pressure":
                    plt.figure(figsize=(15, 15))
                    df2 = df2.reset_index()
                    box = sns.boxplot(x='Pressure', y='day/month', orient='h', data=df2, linewidth=2)
                    plt.title('Box plot')
                    plt.show()
                elif answ2 == "dew point":
                    plt.figure(figsize=(15, 15))
                    df2 = df2.reset_index()
                    box = sns.boxplot(x='Dew Point', y='day/month', orient='h', data=df2, linewidth=2)
                    plt.title('Box plot')
                    plt.show()
                elif answ2 == "humidity":
                    plt.figure(figsize=(15, 15))
                    df2 = df2.reset_index()
                    box = sns.boxplot(x='Humidity', y='day/month', orient='h', data=df2, linewidth=2)
                    plt.title('Box plot')
                    plt.show()
                elif answ2 == "wind speed":
                    plt.figure(figsize=(15, 15))
                    df2 = df2.reset_index()
                    box = sns.boxplot(x='Wind Speed', y='day/month', orient='h', data=df2, linewidth=2)
                    plt.title('Box plot')
                    plt.show()
                elif answ2 == "wind gust":
                    plt.figure(figsize=(15, 15))
                    df2 = df2.reset_index()
                    box = sns.boxplot(x='Wind Gust', y='day/month', orient='h', data=df2, linewidth=2)
                    plt.title('Box plot')
                    plt.show()
                elif answ2 == "precip":
                    plt.figure(figsize=(15, 15))
                    df2 = df2.reset_index()
                    box = sns.boxplot(x='Precip.', y='day/month', orient='h', data=df2, linewidth=2)
                    plt.title('Box plot')
                    plt.show()
                elif answ2 == 'exit':
                    break
                else:
                    print('wrong command')
        elif answ == 'exit':
            break
