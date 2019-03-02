# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 21:46:27 2019

@author: PRATYUSH
"""


from flask import Flask,render_template
import numpy as np
import pandas as pd
from datetime import datetime
#import matplotlib.pyplot as plt

app = Flask(__name__)

commodity_dict = {
            "arhar":"static/Arhar.csv",
            "bajra":"static/Bajra.csv",
            "barley":"static/Barley.csv",
            "copra":"static/Copra.csv",
            "cotton":"static/Cotton.csv",
            "sesamum":"static/Sesamum.csv",
            "gram":"static/Gram.csv",
            "groundnut":"static/Groundnut.csv",
            "jowar":"static/Jowar.csv",
            "maize":"static/Maize.csv",
            "masoor":"static/Masoor.csv",
            "moong":"static/Moong.csv",
            "niger":"static/Niger.csv",
            "paddy":"static/Paddy.csv",
            "ragi":"static/Ragi.csv",
            "rape":"static/Rape.csv",
            "jute":"static/Jute.csv",
            "safflower":"static/Safflower.csv",
            "soyabean":"static/Soyabean.csv",
            "sugarcane":"static/Sugarcane.csv",
            "sunflower":"static/Sunflower.csv",
            "urad":"static/Urad.csv",
            "wheat":"static/Wheat.csv"
             }

annual_rainfall = [19, 22.9, 27.5, 37.7, 62.6, 167, 289, 256.7, 172.2, 76.5, 29.8, 14.9]
base = {
    "Paddy": 1245.5,
    "Arhar": 3200,
    "Bajra": 1175,
    "Barley": 980,
    "Copra": 5100,
    "Cotton": 3600,
    "Sesamum": 4200,
    "Gram": 2800,
    "Groundnut": 3700,
    "Jowar": 1520,
    "Maize": 1175,
    "Masoor": 2800,
    "Moong": 3500,
    "Niger": 3500,
    "Ragi": 1500,
    "Rape": 2500,
    "Jute": 1675,
    "Safflower": 2500,
    "Soyabean": 2200,
    "Sugarcane": 2250,
    "Sunflower": 3700,
    "Urad": 4300,
    "Wheat": 1350

}
commodity_list=[]

class Commodity:
        
        def __init__(self,csv_name):
            self.name = csv_name
            dataset = pd.read_csv(csv_name)
            X=dataset.iloc[:,:-1].values
            Y=dataset.iloc[:,3].values
           
            from sklearn.model_selection import train_test_split
            X_train,X_test,Y_train,Y_test = train_test_split(X,Y, test_size=0.1, random_state=0)
            
            
            #Fitting decision tree regression to dataset
            from sklearn.tree import DecisionTreeRegressor
            self.regressor = DecisionTreeRegressor(max_depth=10,random_state = 0)
            self.regressor.fit(X,Y)
            y_pred_tree = self.regressor.predict(X_test)
            #fsa=np.array([float(1),2019,45]).reshape(1,3)
            #fask=regressor_tree.predict(fsa)
            
        def getPredictedValue(self,value):
            fsa=np.array(value).reshape(1,3)
            return self.regressor.predict(fsa)

        def getCropName(self):
            a = self.name.split('.')
            return a[0]
        
@app.route('/')
def index():
    context = {
        "top5": TopFiveWinners(),
        "bottom5": TopFiveLosers()
    }
    return render_template('index.html',context = context)

@app.route('/commodity/<name>')
def crop_profile(name):
    max_crop, min_crop, forecast_crop_values = TwelveMonthsForecast(name)
    prev_crop_values = TwelveMonthPrevious(name)
    print(max_crop)
    print(min_crop)
    print(forecast_crop_values)
    print(prev_crop_values)
    print()
    context = {
        "max_crop": max_crop,
        "min_crop": min_crop,
        "forecast_values": forecast_crop_values,
        "previous_values": prev_crop_values
    }
    return render_template('commodity.html',context = context)

def TopFiveWinners():
    current_month = datetime.now().month
    current_year = datetime.now().year
    current_rainfall = annual_rainfall[current_month-1]
    prev_month = current_month-1
    prev_rainfall = annual_rainfall[prev_month-1]
    current_month_prediction = []
    prev_month_prediction = []
    change = []

    for i in commodity_list:
        current_predict = i.getPredictedValue([float(current_month),current_year,current_rainfall])
        current_month_prediction.append(current_predict)
        prev_predict = i.getPredictedValue([float(prev_month),current_year,prev_rainfall])
        prev_month_prediction.append(prev_predict)
        change.append((((current_predict-prev_predict)*100/prev_predict),commodity_list.index(i)))
    sorted_change = change
    sorted_change.sort(reverse=True)
    #print(sorted_change)
    to_send= []
    for j in range(0, 5):
        perc, i = sorted_change[j]
        name = commodity_list[i].getCropName().split('/')[1]
        to_send.append([name, round((current_month_prediction[i][0]*base[name])/100,2), round(perc[0],2)])
    print(to_send)
    return to_send

def TopFiveLosers():
    current_month = datetime.now().month
    current_year = datetime.now().year
    current_rainfall = annual_rainfall[current_month-1]
    prev_month = current_month-1
    prev_rainfall = annual_rainfall[prev_month-1]
    current_month_prediction = []
    prev_month_prediction = []
    change = []

    for i in commodity_list:
        current_predict = i.getPredictedValue([float(current_month),current_year,current_rainfall])
        current_month_prediction.append(current_predict)
        prev_predict = i.getPredictedValue([float(prev_month),current_year,prev_rainfall])
        prev_month_prediction.append(prev_predict)
        change.append((((current_predict - prev_predict) * 100 / prev_predict), commodity_list.index(i)))
    sorted_change = change
    sorted_change.sort()
    to_send= []
    for j in range(0, 5):
        perc, i = sorted_change[j]
        name = commodity_list[i].getCropName().split('/')[1]
        to_send.append([name, round((current_month_prediction[i][0]*base[name])/100,2), round(perc[0],2)])
    print(to_send)
    return to_send
"""
def SixMonthsPrediction():
    current_month = datetime.now().month
    current_year = datetime.now().year
    current_rainfall = annual_rainfall[current_month - 1]
    months=[]
    rainfalls=[]
    for i in range(0,6):
        months.append(current_month+i)
        rainfalls.append(current_month+i)
    six_month_prediction = []
    prev_month_prediction = []
    change = []

    for i in commodity_list:
        current_predict = i.getPredictedValue([float(current_month), current_year, current_rainfall])
        current_month_prediction.append(current_predict)
        prev_predict = i.getPredictedValue([float(prev_month), current_year, prev_rainfall])
        prev_month_prediction.append(prev_predict)
        change.append((((current_predict - prev_predict) * 100 / prev_predict), commodity_list.index(i)))
    sorted_change = change
    sorted_change.sort(reverse=True)
    # print(sorted_change)
    to_send = []
    for j in range(0, 5):
        perc, i = sorted_change[j]
        name = commodity_list[i].getCropName().split('/')[1]
        to_send.append([name, round((current_month_prediction[i][0] * base[name]) / 100, 2), round(perc[0], 2)])
    print(to_send)
"""

def TwelveMonthsForecast(name):
    current_month = datetime.now().month
    current_year = datetime.now().year
    current_rainfall = annual_rainfall[current_month - 1]
    name = name.lower()
    commodity=commodity_list[0]
    for i in commodity_list:
        if name == str(i):
            commodity = i
            break
    month_with_year = []
    for i in range(1,13):
        if current_month+i <=12:
            month_with_year.append((current_month+i,current_year, annual_rainfall[current_month+i-1]))
        else:
            month_with_year.append((current_month+i-12,current_year+1,annual_rainfall[current_month+i-13]))
    max_index = 0
    min_index = 0
    max_value = 0
    min_value = 9999
    wpis = []
    current_wpi = commodity.getPredictedValue([float(current_month),current_year, current_rainfall])
    change = []

    for m, y, r in month_with_year:
        current_predict = commodity.getPredictedValue([float(m), y, r])
        if current_predict > max_value:
            max_value = current_predict
            max_index = month_with_year.index((m,y,r))
        if current_predict < min_value:
            min_value = current_predict
            min_index = month_with_year.index((m,y,r))
        wpis.append(current_predict)
        change.append(((current_predict - current_wpi) * 100) / current_wpi)

    max_month, max_year, r1 = month_with_year[max_index]
    min_month, min_year, r2 = month_with_year[min_index]
    min_value = min_value*base[name.capitalize()]/100
    max_value = max_value*base[name.capitalize()]/100
    crop_price = []
    for i in range(0,len(wpis)):
        m,y,r = month_with_year[i]
        crop_price.append([m,y,round((wpis[i]*base[name.capitalize()]/100)[0],2),round(change[i],2)])
    max_crop = [max_month, max_year, round(max_value,2) ]
    min_crop = [min_month, min_year, round(min_value,2) ]

    return max_crop, min_crop, crop_price






def TwelveMonthPrevious(name):
    name = name.lower()
    current_month = datetime.now().month
    current_year = datetime.now().year
    current_rainfall = annual_rainfall[current_month-1]
    commodity = commodity_list[0]
    wpis = []
    crop_price = []
    for i in commodity_list:
        if name == str(i):
            commodity = i
            break
    month_with_year = []
    for i in range(1,13):
        if current_month - i >=1:
            month_with_year.append((current_month-i, current_year,annual_rainfall[current_month-i-1]))
        else:
            month_with_year.append((current_month-i+12, current_year-1,annual_rainfall[current_month-i+11]))

    for m, y, r in month_with_year:
        current_predict = commodity.getPredictedValue([float(m), y,r])
        wpis.append(current_predict)

    for i in range(0,len(wpis)):
        m,y,r = month_with_year[i]
        crop_price.append([m,y,round((wpis[i]*base[name.capitalize()]/100)[0],2)])

    return crop_price




if __name__ == "__main__":
    arhar = Commodity(commodity_dict["arhar"])
    commodity_list.append(arhar)
    bajra = Commodity(commodity_dict["bajra"])
    commodity_list.append(bajra)
    barley = Commodity(commodity_dict["barley"])
    commodity_list.append(barley)
    copra = Commodity(commodity_dict["copra"])
    commodity_list.append(copra)
    cotton = Commodity(commodity_dict["cotton"])
    commodity_list.append(cotton)
    sesamum = Commodity(commodity_dict["sesamum"])
    commodity_list.append(sesamum)
    gram = Commodity(commodity_dict["gram"])
    commodity_list.append(gram)
    groundnut = Commodity(commodity_dict["groundnut"])
    commodity_list.append(groundnut)
    jowar = Commodity(commodity_dict["jowar"])
    commodity_list.append(jowar)
    maize = Commodity(commodity_dict["maize"])
    commodity_list.append(maize)
    masoor = Commodity(commodity_dict["masoor"])
    commodity_list.append(masoor)
    moong = Commodity(commodity_dict["moong"])
    commodity_list.append(moong)
    niger = Commodity(commodity_dict["niger"])
    commodity_list.append(niger)
    paddy = Commodity(commodity_dict["paddy"])
    commodity_list.append(paddy)
    ragi = Commodity(commodity_dict["ragi"])
    commodity_list.append(ragi)
    rape = Commodity(commodity_dict["rape"])
    commodity_list.append(rape)
    jute = Commodity(commodity_dict["jute"])
    commodity_list.append(jute)
    safflower = Commodity(commodity_dict["safflower"])
    commodity_list.append(safflower)
    soyabean = Commodity(commodity_dict["soyabean"])
    commodity_list.append(soyabean)
    sugarcane = Commodity(commodity_dict["sugarcane"])
    commodity_list.append(sugarcane)
    sunflower = Commodity(commodity_dict["sunflower"])
    commodity_list.append(sunflower)
    urad = Commodity(commodity_dict["urad"])
    commodity_list.append(urad)
    wheat = Commodity(commodity_dict["wheat"])
    commodity_list.append(wheat)
    print(TopFiveWinners())
    print(TopFiveLosers())
    print(arhar.getPredictedValue([4,2019,100]))
    print(bajra.getPredictedValue([4,2019,100]))
    print(barley.getPredictedValue([4,2019,100]))
    print(copra.getPredictedValue([4,2019,100]))
    app.run()
    
    
    
    
    
    