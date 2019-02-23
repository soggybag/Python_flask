import csv
import requests


URL = "http://www.nasdaq.com/quotes/nasdaq-100-stocks.aspx?render=download"


def get_data():
    r = requests.get(URL)
    data = r.text
    RESULTS = {'children': []}
    for line in csv.DictReader(data.splitlines(), skipinitialspace=True):
        if float(line['Nasdaq100_points']) > .01:
            RESULTS['children'].append({
                'name': line['Name'],
                'symbol': line['Symbol'],
                'symbol': line['Symbol'],
                'price': line['lastsale'],
                'net_change': line['netchange'],
                'percent_change': line['pctchange'],
                'volume': line['share_volume'],
                'value': line['Nasdaq100_points']
            })
    return RESULTS


# for i, j in get_data().items():
#     print(len(j))

from flask import Flask, render_template, jsonify
from livereload import Server, shell

app = Flask(__name__, static_url_path='')

# visit: http://127.0.0.1:5000/data
@app.route("/data")
def data():
    return jsonify(get_data())

# define a route to serve a static HTML page
# index.html is located in the template directory
# visit: http://127.0.0.1:5000/
@app.route("/")
def home():
    return render_template('index.html')

# visit: http://127.0.0.1:5000/bars
@app.route("/bars")
def bars():
    return render_template('chart-bars.html')

# visit: http://127.0.0.1:5000/d3
@app.route("/d3")
def d3():
    return render_template('d3-example.html')

if __name__ == '__main__':
    # import os
    # port = int(os.environ.get('PORT', 5000))
    # app.run(host='0.0.0.0', port=port)
    app.debug = True
    app.run()
    # server = Server()
    # server.serve()
    print('hello')