import pandas as pd
from helpers import getNames
import seaborn as sns
import matplotlib.pyplot as plt

pressure = "Атмосферное давление на уровне станции"
hubimidy = 'Относительная влажность воздуха'
temperature = 'Температура воздуха по сухому терм-ру'


def getTemperaturesPlot(fileNumber, year, month = -1):
    df = pd.read_csv('files/{}.csv'.format(fileNumber))
    df['date'] = pd.to_datetime(df['date'])
    filtered_df = df[df['date'].dt.year == year]
    if month != -1:
        filtered_df = df[df['date'].dt.month == month]
    sns.lineplot(data=filtered_df, x=filtered_df['date'], y = filtered_df[temperature])
    plt.show()


def getHubimidy(fileNumber):
    f = pd.read_csv('files/{}.csv'.format(fileNumber))
    return f[hubimidy]

def getPressure(fileNumber):
    f = pd.read_csv('files/{}.csv'.format(fileNumber))
    return f[pressure]



getTemperaturesPlot(24763, 2005)