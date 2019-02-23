# Python_flask

Serve static files with Python flask for Daa visualization

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

**Note!** Static HTML files must be served from the 'templates' directory. 
