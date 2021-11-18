from flask import Flask, request, render_template
from lats_long import get_manufaturing_country_lat,get_manufaturing_country_long
from lats_long import get_country_lat,get_country_long,cal_distance
from category_encoders import *
import numpy as np
import pickle
import pandas as pd



app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))
encode=pickle.load(open('encoder.pkl','rb'))

@app.route("/")

def home():
    return render_template("home.html")

@app.route("/predict", methods = ["POST"])

def predict():
    if request.method == "POST":

        manufacturing_country=request.form['manufacturing']
        # print(manufacturing_country)

        manufacturing_country_lat=get_manufaturing_country_lat(manufacturing_country)
        manufacturing_country_long=get_manufaturing_country_long(manufacturing_country)
        # print(manufacturing_country_lat,manufacturing_country_long)

        date=request.form['date']
        month = int(pd.to_datetime(date, format="%Y-%m-%dT").month)
        year = int(pd.to_datetime(date,format="%Y-%m-%dT").year)
        # print(month,year)

        country = request.form['Country']
        # print(country)

        country_lat=get_country_lat(country)
        country_long = get_country_long(country)
        # print(country_lat,country_long)

        fulfill = request.form['Fulfill']
        # print(fulfill)

        shipment = request.form['Shipment']
        # print(shipment)

        classification = request.form['classification']
        # print(classification)

        qty = int(request.form['qty'])
        # print(qty)

        weight = int(request.form['weight'])
        # print(weight)

        distance=cal_distance(manufacturing_country_lat,manufacturing_country_long,country_lat,country_long)
        print('distance',distance)

        cols={'Country':country,'Fulfill Via':fulfill,'Shipment Mode':shipment,'Sub Classification':classification,
              'Line Item Quantity':qty,'Weight (Kilograms)':weight,'Manufacturing_Country':manufacturing_country,
              'Delivery_Month':month,'Delivery_Year':year,'distance':distance}

        data=pd.DataFrame(cols,index=[0])
        data_encoded=encode.transform(data)

        prediction = model.predict(data_encoded)
        output=np.round(prediction[0])
        print(output)
        return render_template('home.html',prediction_text="YOUR SHIPMENT PRICE IS {} $".format(output))

    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)