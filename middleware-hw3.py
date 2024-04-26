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

    if airport is not None:
        if len(airport) > 3:
            return jsonify({})
        
        info = requests.get(f"https://www.airport-data.com/api/ap_info.json?iata={airport}")

        data = info.json()
        longitude = data["longitude"]
        latitude = data["latitude"]

        temperature = requests.get(f"http://api.weatherapi.com/v1/current.json?q={latitude},{longitude}&key={weather_api_key}")
        temp_data = temperature.json()

        return str(temp_data['current']['temp_c'])

    elif stock_name is not None:
        stock = yf.Ticker(stock_name)
        price = stock.info["currentPrice"]

        return str(price)

    elif values is not None:
        result = eval(values)

        return str(result)
    else:
        return jsonify({})