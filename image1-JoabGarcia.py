import pandas as pd, numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def image1():
    #import csv data and turn into a dataframe, then dropping NA values
    df = pd.read_csv('weatherAUS.csv')
    df = pd.DataFrame(df, columns = ['Date', 'Location', 'MinTemp', 'MaxTemp'])
    df.dropna()
    #creates dataframes with temperatures from Sydney, Adelaide, and Melbourne
    syd_temps = df.loc[df['Location'] == 'Sydney']
    ade_temps = df.loc[df['Location'] == 'Adelaide']
    mel_temps = df.loc[df['Location'] == 'Melbourne']
    #histogram 1 - Sydney
    hist1 = syd_temps.hist(bins=365)
    plt.suptitle("Sydney Temperatures (in Celsius)")
    plt.show()
    #histogram 2 - Adelaide
    hist2 = ade_temps.hist(bins=365)
    plt.suptitle("Adelaide Temperatures (in Celsius)")
    plt.show()
    #histogram 3 - Melbourne
    hist3 = mel_temps.hist(bins=365)
    plt.suptitle("Melbourne Temperatures (in Celsius)")
    plt.show()

def main():
    image1()

if __name__=="__main__":
    main()