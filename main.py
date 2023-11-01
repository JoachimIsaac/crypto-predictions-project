import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt, dates as mdates
from matplotlib.backends.backend_pdf import PdfPages
import warnings
import datetime


#Suppresses unecessary warnings.
warnings.filterwarnings('ignore')

def plot_points1(plt_obj,x_data,y_data,label_name):
  plt_obj.plot(x_data, y_data, label=label_name,color="blue",marker='D',markersize=6)

def plot_points2(plt_obj,x_data,y_data,label_name):
  plt_obj.plot(x_data, y_data, label=label_name,color="red",marker='^')

def Appendtext(fname,input_text):
	with open(fname,'a+') as f:
		f.write(input_text)
	f.close()

def list_all_xvalues_on_xaxis():
  ax = plt.gca()
  locator = mdates.DayLocator()
  ax.xaxis.set_major_locator(locator)

def get_date(data,index):
  current_date = data.loc[0, "Date"]
  current_date = datetime.datetime.strptime(current_date, '%Y-%m-%d')
  current_year = current_date.year
  return current_year


def get_yearly_all_time_highs(data):
  # print(data['Date'])
  #create a loop that loops for all the data per year.
  #let's work by averaging the high's by year.
  yearly_high_total = 0
  yearly_low_total = 0
  count = 0

  max_year_price = float("-inf")

  
  current_year = get_date(data,0)
  X_years = [current_year]


  # previous_year = 2015
  # current_year = 0
  Y_price_values = []

  
  for index in range(len(data)) :

   
    #get current date's year
    current_date = data.loc[index, "Date"]
    current_date = datetime.datetime.strptime(current_date, '%Y-%m-%d')
    current_year = current_date.year

    # print(current_year,"year")
    #get next date's year
    if index + 1 < len(data):
      next_date = data.loc[index+1, "Date"]
      next_date = datetime.datetime.strptime(next_date, '%Y-%m-%d')
      next_year = next_date.year

    current_high_price = float(data.loc[index,"High"])

    max_year_price = max(max_year_price,current_high_price)

    yearly_high_total += current_high_price

    




    if current_year != next_year:
    
      X_years.append(next_year)
      Y_price_values.append(max_year_price)
      max_year_price = float("-inf")

      #reset everything needed
      # previous_year = current_year = current_date.year
    

    elif(index == len(data)-1):
      Y_price_values.append(max_year_price)


  

  return X_years,Y_price_values

#need to make a fucntion that grabs all the years and returns them in an array, that's our x values. I can modify the exsisting fucntion


files = ["DFI-USD.csv","CRO-USD.csv","CEL-USD.csv"]
ticker_symbols = ["DFI","CRO","CEL"]
result_file_names = ["DFI-results.txt","CRO-results.txt","CEL-results.txt"]



file_index = 0

pdf_file = PdfPages("prediction-plots.pdf") 

for file in files:

  current_crypto_data = pd.read_csv(file)

  values = get_yearly_all_time_highs(current_crypto_data)

  Y_values = np.array(values[1])
  X_values = np.array(values[0])


  X_values = X_values.reshape(-1, 1)
  Y_values = Y_values.reshape(-1, 1)
  lr = LinearRegression()
  lr.fit(X_values, Y_values)

  starting_year = int(X_values[0])
  ending_year = int(X_values[0])+12

  future_year_template = [year for year in range(starting_year,ending_year)]
  future_years = np.array(future_year_template).reshape(-1,1)

  prediction_10_years = lr.predict(future_years)

  result = ""

  for index,price in enumerate(prediction_10_years):
    year = future_years[index]
    prediction_of_year = f"{ticker_symbols [file_index]}: Predicted yearly ATH price: year:{year} and price{price}\n"
    result += prediction_of_year

  Appendtext(result_file_names[file_index],result)

  
  
  origin1 = f"Yearly ATH {ticker_symbols[file_index]} price"
  origin2 = f"Predicted Yearly ATH {ticker_symbols[file_index]} price"
  
  fig, ax = plt.subplots()
  plot_points1(ax,X_values,Y_values,origin1)
  plot_points2(ax,future_years,prediction_10_years,origin2)

  ax.legend()

  pdf_file.savefig(fig)
  file_index += 1

pdf_file.close()


  