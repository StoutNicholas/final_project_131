import pandas as pd, numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def image3():
    df =pd.read_csv('weatherAUS.csv', index_col=0)
    df = pd.DataFrame(df, columns = ['Date', 'Location', 'WindGustSpeed', 'MaxTemp'])
    df.set_index('Date') #use date column as the index
    df.dropna()
    #creates dataframes with selected columns from Sydney, Adelaide, and Melbourne
    syd_humid = df.loc[df['Location'] == 'Sydney']
    ade_humid = df.loc[df['Location'] == 'Adelaide']
    mel_humid = df.loc[df['Location'] == 'Melbourne']
    #scatterplot with regression line - Sydney
    syd_humid.plot.scatter(x ='WindGustSpeed', y ='MaxTemp', s = .05)
    sns.set_style('white')
    sns.set_style('ticks')
    sns.regplot(x ='WindGustSpeed', y ='MaxTemp', data = syd_humid, line_kws = {'color': 'orange'})
    plt.suptitle("Sydney Wind Speed (Km) & Max Temperatures (C)")
    plt.show()
    #scatterplot with regression line - Adelaide
    ade_humid.plot.scatter(x ='WindGustSpeed', y ='MaxTemp', s = .05)
    sns.set_style('white')
    sns.set_style('ticks')
    sns.regplot(x ='WindGustSpeed', y ='MaxTemp', data = ade_humid, line_kws = {'color': 'orange'})
    plt.suptitle("Adelaide Wind Speed (Km) & Max Temperatures (C)")
    plt.show()
    #scatterplot with regression line - Melbourne
    mel_humid.plot.scatter(x ='WindGustSpeed', y ='MaxTemp', s = .05)
    sns.set_style('white')
    sns.set_style('ticks')
    sns.regplot(x ='WindGustSpeed', y ='MaxTemp', data = mel_humid, line_kws = {'color': 'orange'})
    plt.suptitle("Melbourne")
    plt.show()

def main():
    image3()

if __name__=="__main__":
    main()