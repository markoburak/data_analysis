import pandas as pd
import matplotlib.pyplot as plt
import webbrowser
import matplotlib.patches as mpatches

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 1000)

url = 'https://raw.githubusercontent.com/VasiaPiven/covid19_ua/master/covid19_by_area_type_hosp_dynamics.csv'
df = pd.read_csv(url, error_bad_lines=False)


# 1)
def state(df, name):
    # select one state
    area = df.loc[df['registration_area'] == name]
    return area

def state_group(df):
    state = df.groupby('zvit_date').sum()
    return state
temp = pd.dataframe
def plot_analysis(state1, state2, column):
    raw1 = state(df, state1)
    raw2 = state(df, state2)
    start1 = state_group(raw1)
    start2 = state_group(raw2)

    state1_df = pd.concat(
            [start1[['new_susp', 'new_confirm', 'new_death', 'new_recover']].cumsum(),
             start1['active_confirm'], raw1.loc[raw1['is_required_hospitalization'] == 'Так'].
                 groupby(['zvit_date']).sum().cumsum().rename(columns={'new_susp': 'hospitalized'})[
                 'hospitalized']],
            axis=1)
    state1_df['test'] = state1

    print(state1_df)
    state2_df = pd.concat(
        [start2[['new_susp', 'new_confirm', 'new_death', 'new_recover']].cumsum(),
         start2['active_confirm'], raw2.loc[raw2['is_required_hospitalization'] == 'Так'].
             groupby(['zvit_date']).sum().cumsum().rename(columns={'new_susp': 'hospitalized'})[
             'hospitalized']],
        axis=1)

    ax = plt.gca()

    plot_line(state1_df, column, column)
    plot_line(state2_df, column, column)

    ax.legend([state1,state2])
    # ax.grid('on', which='minor', axis='y')
    # ax.grid('off', which='major', axis='y')
    # plt.xticks(rotation=45)
    # plt.xlabel('day/month/year')
    # plt.ylabel('max Humidity %')
    show()

# 3)
def plot_variaty(df_grouped, df_raw):

    variaty = pd.concat(
        [df_grouped[['new_susp', 'new_confirm', 'new_death', 'new_recover']].cumsum(),
         df_grouped['active_confirm'], df_raw.loc[df_raw['is_required_hospitalization'] == 'Так'].
             groupby(['zvit_date']).sum().cumsum().rename(columns={'new_susp': 'hospitalized'})[
             'hospitalized']],
        axis=1)

    plot_line(variaty, 'new_confirm', 'Confirmed cases line')
    show()
    plot_line(variaty, 'new_susp', 'Suspected cases line')
    show()
    plot_line(variaty, 'new_recover', 'Recovered cases line')
    show()
    plot_line(variaty, 'new_death', 'Lethal cases line')
    show()
    plot_line(variaty, 'hospitalized', 'Hospitalized cases line')
    show()
    plot_line(variaty, 'active_confirm', 'Active cases line')
    show()

def plot_line(df, column, name):
    df[column].plot(kind='line', title=name)
def show():
    plt.show()


print('1)')

print('Вінницька\t',
      'Волинська\t',
      'Дніпропетровська\t',
      'Донецька\t',
      'Житомирська\t',
      'Закарпатська\t',
      'Запорізька\t',
      'Івано-Франківська\t',
      'Київська\t',
      'Кіровоградська\t',
      'Луганська\t',
      'Львівська\t',
      'Миколаївська\t',
      'м. Київ\t',
      'Одеська\t',
      'Полтавська\t',
      'Рівненська\t',
      'Сумська\t',
      'Тернопільська\t',
      'Харківська\t',
      'Херсонська\t',
      'Хмельницька\t',
      'Черкаська\t',
      'Чернівецька\t',
      'Чернігівська\t',
      )

# df for state
name_state = input()
df_state = state(df, name_state)
print(df_state)

# 2)
# df for every day
print('2)')
fake = input()
df_date = df.groupby('zvit_date').agg(
    {'new_susp': 'sum', 'active_confirm': 'sum', 'new_death': 'sum', 'new_recover': 'sum', 'new_confirm': 'sum'})
print(df_date)

# 3)
print('3)')

while True:
    choice = input('plot for all or for state\nall\nstate\n')
    if choice == 'all':
        plot_variaty(df_date, df)
    elif choice == 'state':
        stateGrouped = state_group(df_state)
        plot_variaty(stateGrouped, df_state)
    else:
        break

print('4)')
fake = input()
webbrowser.open(
    "https://www.google.com/maps/d/u/0/viewer?mid=1OejaE3qulsxbCS4N56G9mToVRv018nPg&ll=49.05356893509722%2C30"
    ".797848999999978&z=6",
    new=1)

print('5)')
while True:

    print('Вінницька\t',
          'Волинська\t',
          'Дніпропетровська\t',
          'Донецька\t',
          'Житомирська\t',
          'Закарпатська\t',
          'Запорізька\t',
          'Івано-Франківська\t',
          'Київська\t',
          'Кіровоградська\t',
          'Луганська\t',
          'Львівська\t',
          'Миколаївська\t',
          'м. Київ\t',
          'Одеська\t',
          'Полтавська\t',
          'Рівненська\t',
          'Сумська\t',
          'Тернопільська\t',
          'Харківська\t',
          'Херсонська\t',
          'Хмельницька\t',
          'Черкаська\t',
          'Чернівецька\t',
          'Чернігівська\t',
          )
    print('choose 2 states')
    state1 = input('state1 = ')
    state2 = input('state2 = ')
    print('new_confirm\t',
          'new_susp\t',
          'new_recover\t',
          'new_death\t',
          'hospitalized\t',
          'active_confirm\t')

    option = input('type option = ')

    plot_analysis(state1, state2,option)
    exit = input()
    if exit == "exit":
        break

df.groupby('registration_area')['new_confirm'].sum().sort_values(ascending=False).plot(kind='bar')
plt.show()

df_date.to_excel('date_excel.xlsx')
df_state.to_excel('state_excel.xlsx')
df.to_excel('start.xlsx')
states = df.groupby('registration_area').agg(
    {'new_susp': 'sum', 'active_confirm': 'sum', 'new_death': 'sum', 'new_recover': 'sum', 'new_confirm': 'sum'})
states.to_csv('states.csv')
states.to_excel('states.xlsx')
