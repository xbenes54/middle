from flask import Flask, request
import yfinance as yf
import requests

weather_api_key = "c880d86a7b7f406f91b173324242504"


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> Hello World </p>"

@app.route("/queryAirportTemp")
def airport_temperature():
    airport = request.args.get('expr')
    info = requests.get(f"https://www.airport-data.com/api/ap_info.json?iata={airport}")

    data = info.json()
    longitude = data["longitude"]
    latitude = data["latitude"]

    temperature = requests.get(f"http://api.weatherapi.com/v1/current.json?q={longitude},{latitude}&key={weather_api_key}")
    temp_data = temperature.json()
    print(info)
    return {
        "temp" : temp_data["current"]["temp_c"]
    }

@app.route("/queryStockPrice")
def query_stock_price():
    stock_name = request.args.get("expr")
    stock = yf.Ticker(stock_name)
    price = stock.info["currentPrice"]
    return {
        "price" : price
    }

@app.route("/queryEval")
def query_eval():
    values = request.args.get('expr')
    result = eval(values)
    return {
        "result" : result
    }


