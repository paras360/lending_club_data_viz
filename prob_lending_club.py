import matplotlib.pyplot as plt 
import pandas as pd 
import scipy.stats as stats 

#this will load the loan data from a csv to the dataframe 

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv') 

#this will remove the empty rows so we have clean data 

loansData.dropna(inplace=True)

#this will generate a boxplot of the Amount.Requested column 

loansData.boxplot(column='Amount.Requested')
plt.title('Lending Club Amount Requested Box Plot')
plt.savefig('boxplot_lending_club_data.png')

#this will generate a histogram of the Amount.Requested column which will allow us to determine whether or not the data is normally distributed 

loansData.hist(column='Amount.Requested')
plt.title('Lending Club Amount Requested Histogram')
plt.savefig('histogram_lending_club_data.png')

#this will generate a qq plot 

plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.title('Lending Club QQ Plot')
plt.savefig('qq_plot_lending_club_data.png')