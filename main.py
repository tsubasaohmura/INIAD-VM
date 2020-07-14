from flask import Flask, render_template, request
from urllib import parse
import apis
import products
import newsapi
import foursquare

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  #product.py
  items = products.all()
  itemsupper = products.upper()
  itemslower = products.lower()

  #apis.py
  city = '東京都品川区平塚'
  if request.method == 'POST':
    city = request.form['keyword']
  lat,lng = apis.address_to_latlng(city)
  forecast = apis.get_weather(lat, lng)

  #nwesapi.py
  newsdict = newsapi.get_news("jp")
  topnews = newsapi.get_headline("jp")

  #foursquare.py
  spot = foursquare.get_name()


  return render_template('index.html', city=city, lat=lat, lng=lng, forecast=forecast, items=items, itemsupper=itemsupper, itemslower=itemslower,  topnews=topnews, newsdict=newsdict, spot=spot )





if __name__ == '__main__':
  app.run(host='0.0.0.0')




