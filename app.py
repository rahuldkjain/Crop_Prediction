# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 21:46:27 2019

@author: PRATYUSH
"""


from flask import Flask,render_template
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

commodity_dict = {
            "arhar":"static/Arhar.csv",
            "bajra":"static/Bajra.csv",
            "barley":"static/Barley.csv",
            "copra":"static/Copra(Coconut).csv",
            "cotton":"static/Cotton Seed.csv",
            "sesamum":"static/Gingelly Seed(Sesamum).csv",
            "gram":"static/Gram.csv",
            "groundnut":"static/Groundnut seed.csv",
            "jowar":"static/Jowar.csv",
            "maize":"static/Maize.csv",
            "masoor":"static/masoor.csv",
            "moong":"static/Moong.csv",
            "niger":"static/Niger Seed.csv",
            "paddy":"static/Paddy.csv",
            "ragi":"static/Ragi.csv",
            "rape":"static/Rape and Mustard Seed.csv",
            "jute":"static/Raw Jute.csv",
            "safflower":"static/Safflower(Kardi Seed).csv",
            "soyabean":"static/Soyabean.csv",
            "sugarcane":"static/Sugarcane.csv",
            "sunflower":"static/Sunflower.csv",
            "urad":"static/Urad.csv",
            "wheat":"static/Wheat.csv"
             }

annual_rainfall = [19, 22.9, 27.5, 37.7, 62.6, 167, 289, 256.7, 172.2, 76.5, 29.8, 14.9]
base = {
    "paddy": 1245.5,

}

class Commodity:
        
        def __init__(self,csv_name):
        
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
        
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    arhar = Commodity(commodity_dict["arhar"])
    bajra = Commodity(commodity_dict["bajra"])
    barley = Commodity(commodity_dict["barley"])
    copra = Commodity(commodity_dict["copra"])
    cotton = Commodity(commodity_dict["cotton"])
    sesamum = Commodity(commodity_dict["sesamum"])
    gram = Commodity(commodity_dict["gram"])
    groundnut = Commodity(commodity_dict["groundnut"])
    jowar = Commodity(commodity_dict["jowar"])
    maize = Commodity(commodity_dict["maize"])
    masoor = Commodity(commodity_dict["masoor"])
    moong = Commodity(commodity_dict["moong"])
    niger = Commodity(commodity_dict["niger"])
    paddy = Commodity(commodity_dict["paddy"])
    ragi = Commodity(commodity_dict["ragi"])
    rape = Commodity(commodity_dict["rape"])
    jute = Commodity(commodity_dict["jute"])
    safflower = Commodity(commodity_dict["safflower"])
    soyabean = Commodity(commodity_dict["soyabean"])
    sugarcane = Commodity(commodity_dict["sugarcane"])
    sunflower = Commodity(commodity_dict["sunflower"])
    urad = Commodity(commodity_dict["urad"])
    wheat = Commodity(commodity_dict["wheat"])
    
    print(arhar.getPredictedValue([4,2019,100]))
    print(bajra.getPredictedValue([4,2019,100]))
    print(barley.getPredictedValue([4,2019,100]))
    print(copra.getPredictedValue([4,2019,100]))
    app.run()
    
    
    
    
    
    