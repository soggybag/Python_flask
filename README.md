# Python_flask

Serve static files with Python flask for Data visualization.

Data is pulled from:

http://www.nasdaq.com/quotes/nasdaq-100-stocks.aspx?render=download

## Why?

This is a quick test to serve static HTML via Flask that visualizes stock data processed with Python via Chart.js. 

## Getting started

Install Flask

`pip install flask`

Run the Python server

`python companies_renevue_flk.py`

The example serves data from three routes: 

Display JSON stocks data: 

[http://127.0.0.1:5000/data](http://127.0.0.1:5000/data)

Displays index.html

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

Displays chart-bars.html

[http://127.0.0.1:5000/bars](http://127.0.0.1:5000/bars)

Displays d3-example.html (This D3 example use D3 v5)

[http://127.0.0.1:5000/d3](http://127.0.0.1:5000/d3)

**Note!** Static HTML files must be served from the 'templates' directory. 

## TODO

- Move Code to static directory
  - break code into files for easier use
- Ivestigate color bug 
  - colors show gray in some browsers Chart.js examples 
  - HSLA hue could be the problem
- Flask Server auto reload watch 
