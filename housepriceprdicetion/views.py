from django.http import HttpResponse
from django.shortcuts import render
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import  metrics

def home(request):
    return render(request,'home.html')
def myData(request):
    var1 = request.GET.get('value1')
    var2 = request.GET.get('value2')
    var3 = request.GET.get('value3')
    var4 = request.GET.get('value4')
    var5 = request.GET.get('value5')
    data = pd.read_csv(r"C:\Users\nayan\OneDrive\Desktop\study\django\House_price_prediction\housepriceprdicetion\USA_Housing.csv")
    data = data.drop(['Address'], axis=1)
    X = data.drop('Price', axis=1)
    Y = data['Price']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size= 0.30)
    model = LinearRegression()
    model.fit(X_train, Y_train)
    pred = model.predict(np.array([float(var1), float(var2), float(var3), float(var4), float(var5)]).reshape(1, -1))


    pred = round(pred[0])
    

    
    # Do something with the values
    return render(request, 'result.html',{"result":str(pred)})
