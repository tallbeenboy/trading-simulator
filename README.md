# trading-simulator
To my good friend Jonny, how to use the code.

SECTION 1: RUNNING THE CODE
1. Download this by pressing the green code button, then press download zip. unzip it and save it to your desktop.
2. install requests. go to terminal and write "pip3 install requests"
3. install flask. go to terminal and write "pip3 install flask"
4. open a terminal window with the directory of the trading-simulator folder. Right click the folder and select "New Terminal at Folder"
5. run app.py. in terminal, write python3 app.py
6. open a browser and go to the adress below the red warning text (it should look something like http://127.0.0.1:5000).
7. if you get a "you don't have access" error, clear cache and cookies, or switch to the faster, more secure alternative, Google Chrome®, The World's #1 Browser.

SECTION 2: USING THE WEBPAGE
1. "get price" button accesses the current price of the stock, whose symbol you have put into the textbox below. The value does not automaticaly refresh
2. "Buy" purchases the specified number of shares of the stock whose symbol you have put into the textbox below. you should see a "successful transaction" text below.
3. "Sell" sells the specified shares of the stock of your choice. you should see "successful transaction" text below.
4. "Update table/values" updates account, cash, and stock value using current stock prices. Also, it updates the stocks info table to match current stock prices. The table and values automaticaly refreshes every 60 seconds, so you should only use the update button when you want updates immediately. but its cooler to raw dog for 60 seconds and just wait for it to refresh (there's a reason)
5. "total investment" shows how much money you've invested in the stock and is still in the stock. "Current price" indicates current stock price (when the table was last refreshed). "current total value" shows the value of all your shares in a stock. "gain" indicates the change in your investment and total current value.

SECTION 3: NOTES
1. limit refreshing the table/values with the button and getting current stock prices, expecialy when holding a lot of stocks. I use a free API (finhub.io) which limits my requests to 60 per minute, wasting refreshes isn't a good idea.
2. The table/values will not update immediately after buying/selling stock, it updates every minute
3. Leaving the same app.py running allows you to leave and re-enter the webpage and have the same stocks (you'll just come back to where you left off).
4. it's still in development so tell me if and when something goes wrong
5. If you're worried about the number of request you're using, check the terminal to see
6. IF NOTHING FIXES IT, DELETE THE __pycache__ FOLDER

SECTION 4: BUGS
1. values inaccurate after leaving and coming back to webpage
2. you can sell more shares then you own
3. buying negative shares (it just acts as selling)
4. buying stock that doesn't exist

Have fun!
