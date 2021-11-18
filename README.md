## SHIPMENT PRICE PREDICTION


The market for supply chain analytics is expected to develop at a CAGR of 17.3% from 2019 to 2024,more than doubling in size

The main goal is to predict the supply chain shipment pricing 

## Screenshots

![Alt text](https://github.com/xx-CRAZINESS-xx/shipment-price-prediction/blob/main/static/image/Screenshot.png?raw=true)

  
##  Dataset

https://www.kaggle.com/divyeshardeshana/supply-chain-shipment-pricing-data
## Installation

 * Create a new environment

 * Copy the downloaded files or clone the files from github to your environment 

 * pip3 install -r requirements.txt

 * python app.py   
## Data Preprocessing and Feature Engineering

* Some values of column Weight and Freight price were mapped to a specific Id in the dataset like 
  See DN-4307 (ID#:83920) so using some custom function retrived the values from the column

* The null value was filled by using median value 

* Outliers were removed by using IQR 

* Created a new feature distance ie., distance from the manufacturing country to destination country,
  for that used Geopy to get the latitude and longitude of different countries to get the distance

* Few features were dropped using correlation



## Model Creation and Model Selection

* The categorical values were encoded using Category Encoders library

* Used Linear Regression as a base model score

* For advanced model selection and hyperparameter tuning I used FLAML AutoML and chose
  ExtraTreesRegressor as the best model with a R2 score of 85.01% and RMSE of 3391.33 on the test dataset



## Deployment

Deployed in Heroku 

https://shipment-price-prediction.herokuapp.com/
