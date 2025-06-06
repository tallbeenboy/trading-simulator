import requests
import yfinance as yf
import json
import copy
from flask import Flask, render_template, request, redirect,jsonify

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

owned=[]
cash=10000
stockV=0
API_KEY = "60JHFYETUTJ9ERZL"
@app.route("/")
def index():
    return render_template("index.html")

def get_price(symbol):

    """ticker = yf.Ticker(symbol)
        
    todays_data = ticker.history(period='1d', interval='1m')
    if not todays_data.empty:
        return todays_data['Close'].iloc[-1]"""
    
    API_KEY = 'd0v5lc9r01qmg3ukcs60d0v5lc9r01qmg3ukcs6g'

    url = f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={API_KEY}'

    response = requests.get(url)
    data = response.json()
    #print(data)
    price = data['c']

    return price


    '''API_KEY = '1eGPdeW5sAOHMnWgmYaFghH27vkpiZK4'
    BASE_URL = 'https://api.polygon.io/v2/aggs/ticker/'
    ticker_symbol = symbol
    url = f'{BASE_URL}{ticker_symbol}/prev?apiKey={API_KEY}'
    response = requests.get(url)
    
    data = response.json()

    if data['results']:
        price = data['results'][0]['c'] 

    return price'''
def gen_rows(owned):
    rows=[]
    for stock in owned:
        current_price=get_price(stock["symbol"])
        existing=False
        for row in rows:
            if stock["shares"]==0:
                break

            if stock["symbol"] in row.values():
                existing=True
                row["shares"]+=stock["shares"]
                row["totalinvestment"]+=round(stock["buyprice"]*stock["shares"],2)
                row["currentprice"]+=current_price
                row["currentvalue"]+=round(current_price*stock["shares"],2)
                row["gain"]+=round((current_price*stock["shares"])-(stock["buyprice"]*stock["shares"]),2)
                break

        if stock["shares"]!=0:
            if not existing:
                rows.append({"symbol":stock["symbol"],"shares":stock["shares"],"totalinvestment":stock["shares"]*stock["buyprice"],"currentprice":current_price,"currentvalue":round(float(current_price*float(stock["shares"])),2),"gain":round((current_price*stock["shares"])-(stock["buyprice"]*stock["shares"]),2)})

    return rows

def stockvalue():
    r=gen_rows(owned)
    value=0
    for stock in r:
        value+=round(stock["currentvalue"],2)

    return value

@app.route("/price" , methods=["POST"])
def price():
    
    data = request.get_json()
    symbol = data.get("symbol", "").upper().strip()
    
    price=get_price(symbol)
    print(f"Latest price: {price}")
    
        

    return jsonify(str(price))

@app.route("/buy",methods=["POST"])
def buy():
    global cash
    data=request.get_json()
    symbol=data.get("symbol","").upper().strip()
    shares=int(data.get("shares","").upper().strip())

    price=get_price(symbol)

    if shares<1:
        return jsonify("failed transaction: invalid shares")

    if price-0==0:  
        return jsonify("failed transaction: symbol doesn't exist")

    if price*float(shares)<=cash:
        #print(symbol,price)
        owned.append({"symbol":symbol,"buyprice":round(float(price),2),"shares":round(float(shares),2)})
        #print(owned)
        cash-=float(price)*float(shares)
        return jsonify(f"successful transaction (${round(float(price)*float(shares),2)})")
    else:
        return jsonify(f"failed transaction: not enough cash")

@app.route("/allinvestments",methods=["POST"])
def get_rows():
    rows=gen_rows(owned)
    return jsonify(rows)


@app.route("/sell",methods=["POST"])
def sell():
    global owned,stockV,cash
    data=request.get_json()
    symbol=data.get("symbol","").upper().strip()
    shares=int(data.get("shares","").upper().strip())
    old_owned=copy.deepcopy(owned)
    
    if shares<1:
        return jsonify("failed transaction: invalid shares")

    subtracted=0
    for stock in owned:
        if stock["symbol"]==symbol:
            if stock["shares"]<shares:
                subtracted+=stock["shares"]
                stock["shares"]=0
            else:
                subtracted=shares
                stock["shares"]=stock["shares"]-shares

        if subtracted==shares:
            break

    if subtracted<shares:
        owned=old_owned
        return jsonify("transaction failed: you don't own enough shares")

    
    diff=shares*get_price(symbol)
    
    stockV-=diff
    cash+=diff
    diff=round(diff,2)
    stockV=round(stockV,2)
    cash=round(cash,2)
    return jsonify(f"successful transaction ({diff})")




@app.route("/updatevalues",methods=["POST"])
def update_values():
    global cash
    cash=round(cash,2)
    stockV=round(stockvalue(),2)
    accValue=round(stockV+cash,2)
    data={"stockValue":stockV,"accValue":accValue,"cash":cash}

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
