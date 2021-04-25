import pandas as pd, numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def image2():
    df = pd.read_csv('weatherAUS.csv', index_col=0)
    #select columns within dataframe
    df = pd.DataFrame(df, columns = ['Date', 'Location', 'Rainfall', 'MaxTemp'])
    #creates dataframes with selected columns from Sydney, Adelaide, and Melbourne
    syd_rain = df.loc[df['Location'] == 'Sydney']
    ade_rain = df.loc[df['Location'] == 'Adelaide']
    mel_rain = df.loc[df['Location'] == 'Melbourne']
    #bar plot - Sydney
    plt.bar(syd_rain.Rainfall/5, syd_rain.MaxTemp/2)
    plt.xlabel('Rainfall' + " (in meters)")
    plt.ylabel('Max Temp' + " (in Celsius)")
    plt.suptitle('Sydney Rainfall & Max Temp')
    plt.show()
    #bar plot - Adelaide
    plt.bar(ade_rain.Rainfall/5, ade_rain.MaxTemp/2)
    plt.xlabel('Rainfall' + " (in meters)")
    plt.ylabel('Max Temp' + " (in Celsius)")
    plt.suptitle('Adelaide Rainfall & Max Temp')
    plt.show()
    #bar plot - Melbourne
    plt.bar(mel_rain.Rainfall/5, mel_rain.MaxTemp/2)
    plt.xlabel('Rainfall' + " (in meters)")
    plt.ylabel('Max Temp' + " (in Celsius)")
    plt.suptitle('Melbourne Rainfall & Max Temp')
    plt.show()

def main():
    image2()

if __name__=="__main__":
    main()