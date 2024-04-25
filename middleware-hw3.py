from flask import Flask, request, jsonify
import yfinance as yf
import requests

weather_api_key = "c880d86a7b7f406f91b173324242504"


app = Flask(__name__)


@app.route("/")
def control():
    airport = request.args.get('queryAirportTemp')
    stock_name = request.args.get("queryStockPrice")
    values = request.args.get('queryEval')


    if airport != None:
        info = requests.get(f"https://www.airport-data.com/api/ap_info.json?iata={airport}")

        data = info.json()
        longitude = data["longitude"]
        latitude = data["latitude"]

        temperature = requests.get(f"http://api.weatherapi.com/v1/current.json?q={latitude},{longitude}&key={weather_api_key}")
        temp_data = temperature.json()
        print(info)
        return {
            "airport_temp" : temp_data["current"]["temp_c"]
        }

    elif stock_name != None:
        stock = yf.Ticker(stock_name)
        price = stock.info["currentPrice"]
        return {
            "stock" : price
        }

    elif values != None:
        result = eval(values)
        return {
            "value" : result
        }
    else:
        return {}