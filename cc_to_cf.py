import time
start_time=time.time()
print('Importing libraries.....')
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings 
warnings.filterwarnings('ignore')

print('Imported libraries successfully.....program starting.......')
url='https://drive.google.com/file/d/1VfCaU5vFVWsSYrvKQF2x9iS6I7KoWEVH/view?usp=share_link'
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
df = pd.read_csv(url)
print('Loaded data successfully')

# To see shape of dataframe
print("Originally the shape of dataframe is :",df.shape)
df_1=df.dropna()
print("Removing nan values, the dataframe shape is :",df_1.shape)

yt=df_1['cf_rating']
xt=df_1['cc_rating']
#LMPlot

print('Regression plot')
#Regression plot
f1=plt.figure(1)
sns.regplot(xt,yt)
plt.title("Regression plot between CodeChef and Codeforces Rating")
# plt.show()


  
def estimate_coef(x, y):
    print('Estimating parameters......')
    # number of observations/points
    n = np.size(x)
  
    # mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)
  
    # Cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x
  
    # Regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
    print('Calculated parameters.....')
    return (b_0, b_1)
  
def plot_regression_line(x, y, b):
    plt.scatter(x, y, color = "m",marker = "o", s = 30)
  
    # Plotting regression line with predicted response vector
    y_pred = b[0] + b[1]*x
    plt.xlabel('Codechef Rating')
    plt.ylabel('Codeforces Rating')
    plt.plot(x, y_pred, color = "g")
    plt.title('Linear Estimator graph')
    # function to show plot

b = estimate_coef(xt, yt)

print("Estimated coefficients:")
print('Formula would be (codechef_rating*slope) +constant ')
print('Formula with values :')
print('codeforces_rating=codechef_rating*',b[1],'+',b[0])
print("Constant (c) =",b[0])
print("Slope of line (m) =",b[1])
end_time=time.time()
print('Time for program to run :',end_time-start_time)
# plotting regression line
f2=plt.figure(2)
plot_regression_line(xt, yt, b)
plt.show()