import pandas as pd
from datetime import datetime
import requests
from graph import graphs
import matplotlib.pyplot as plt

# max rows and columns
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# convert time to 24 format
def convert24(time_now):
    if time_now[-2:] == "AM" and time_now[:2] == "12":
        return "00" + time_now[2:-2]

    elif time_now[-2:] == "AM":
        return time_now[:-2]

    elif time_now[-2:] == "PM" and time_now[:2] == "12":
        return time_now[:-2]

    else:
        try:
            return str(int(time_now[:2]) + 12) + time_now[2:-2]
        except:
            return str(int(time_now[:1]) + 12) + ':' + time_now[2:-2]


# convert temperature to C
def convert_temp(temp):
    return round((temp - 32) / 1.8, 2)


# main function
def convert_humid(humid):
    return float(int(humid[:2]) / 100)


def convert_wind(windSpeed):
    return int(windSpeed[:2])


def convert_pressure(press):
    return float(press.replace(',', '.'))


def parser():
    df = pd.read_csv('database.csv', sep=';')

    # duplicate K temp
    df['Temperature(K)'] = df['Temperature']
    # assign C temp as a float
    df['Temperature'] = df['Temperature'].astype(float)
    # df['Pressure'] = df['Pressure'].astype(float)
    # main loop
    for i in range(len(df)):
        # date assignment
        df.at[i, 'day/month'] = datetime.strptime(df.at[i, 'day/month'] + ".2019", '%d.%b.%Y').date()
        # time and temperature assignment

        df.at[i, 'Time'] = datetime.strptime(convert24(df.at[i, 'Time'])[:-1] + ':00', '%H:%M:%S').time()
        df.at[i, 'Temperature'] = (convert_temp((df.at[i, 'Temperature'])))
        df.at[i, 'Humidity'] = convert_humid((df.at[i, 'Humidity']))
        df.at[i, 'Wind Speed'] = convert_wind((df.at[i, 'Wind Speed']))
        df.at[i, 'Wind Gust'] = convert_wind((df.at[i, 'Wind Gust']))
        df.at[i, 'Pressure'] = convert_pressure((df.at[i, 'Pressure']))

    # indexing
    df.set_index('day/month', inplace=True)
    return df


df2 = parser()
print(df2)
graphs(plt, df2, pd)




# bonus task!!!
r = requests.get(
    'https://api.weather.com/v1/location/LGAV:9:GR/observations/historical.json?apiKey'
    '=6532d6454b8aa370768e63d6ba5a832e&units=e&startDate=20201001&endDate=20201031')
x = r.json()
weather = pd.DataFrame(x['observations'])


# func to clear starting json
def clear_observation(observation):
    res = {}
    res["Time"] = [datetime.fromtimestamp(time).strftime('%d/%m/%Y') for time in observation["valid_time_gmt"]]
    res["Temperature"] = observation["temp"]
    res["Dew Point"] = observation["dewPt"]
    res["Pressure"] = observation["pressure"]
    res["Wind Speed"] = observation["wspd"]
    res["Precipitation"] = observation["precip_hrly"]
    res["Humidity"] = observation["rh"]

    return res


weather = pd.DataFrame(clear_observation(weather))

# new final dataframe
final_weather = weather.groupby('Time').agg({'Temperature': 'mean'})
final_weather['maxTemp'] = weather.groupby('Time').agg({'Temperature': 'max'})
final_weather['minTemp'] = weather.groupby('Time').agg({'Temperature': 'min'})
final_weather['Dew Point'] = weather.groupby('Time').agg({'Dew Point': 'mean'})
final_weather['maxDew'] = weather.groupby('Time').agg({'Dew Point': 'max'})
final_weather['minDew'] = weather.groupby('Time').agg({'Dew Point': 'min'})
final_weather['Humidity'] = weather.groupby('Time').agg({'Humidity': 'mean'})
final_weather['maxHum'] = weather.groupby('Time').agg({'Humidity': 'max'})
final_weather['minHum'] = weather.groupby('Time').agg({'Humidity': 'min'})
final_weather['Wind Speed'] = weather.groupby('Time').agg({'Wind Speed': 'mean'})
final_weather['maxWind'] = weather.groupby('Time').agg({'Wind Speed': 'max'})
final_weather['minWind'] = weather.groupby('Time').agg({'Wind Speed': 'min'})
final_weather['Pressure'] = weather.groupby('Time').agg({'Pressure': 'mean'})
final_weather['maxPressure'] = weather.groupby('Time').agg({'Pressure': 'max'})
final_weather['minPressure'] = weather.groupby('Time').agg({'Pressure': 'min'})
final_weather['Precipitation'] = weather.groupby('Time').agg({'Precipitation': 'min'})

print(final_weather)
