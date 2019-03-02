# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 20:29:04 2019

@author: PRATYUSH
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Hello World"

class Commodity:
    
    def __init__(self,csv_name):
    
        dataset = pd.read_csv(csv_name)
        X=dataset.iloc[:,:-1].values
        Y=dataset.iloc[:,3].values
       
        from sklearn.cross_validation import train_test_split
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
    

commodity_dict = {
        "arhar":"Arhar.csv",
        "bajra":"Bajra.csv",
        "barley":"Barley.csv",
        "copra":"Copra(Coconut).csv",
        "cotton":"Cotton Seed.csv",
        "sesamum":"Gingelly Seed(Sesamum).csv",
        "gram":"Gram.csv",
        "groundnut":"Groundnut seed.csv",
        "jowar":"Jowar.csv",
        "maize":"Maize.csv",
        "masoor":"masoor.csv",
        "moong":"Moong.csv",
        "niger":"Niger Seed.csv",
        "paddy":"Paddy.csv",
        "ragi":"Ragi.csv",
        "rape":"Rape and Mustard Seed.csv",
        "jute":"Raw Jute.csv",
        "safflower":"Safflower(Kardi Seed).csv",
        "soyabean":"Soyabean.csv",
        "sugarcane":"Sugarcane.csv",
        "sunflower":"Sunflower.csv",
        "urad":"Urad.csv",
        "wheat":"Wheat.csv"
         }


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