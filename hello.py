from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
import scrapper
import os, pickle, json

def pickle_read(filename):
    with open(filename,'rb') as file:
        return pickle.load(file)


@app.route('/')
def index():

    scrapper.starter()

    units = pickle_read("units.txt")
    navs = pickle_read("scrapped.pickle")

    nav_dates = list(map(lambda nav: nav['date'], navs))
    nav_prices = list(map(lambda nav: nav['nav'], navs)) 
    nav_dates.reverse()
    nav_prices.reverse()

    return render_template(
        'jinja.html',
        navs=navs, 
        units=units,
        nav_dates=json.dumps(nav_dates),
        nav_prices=json.dumps(nav_prices)
    )



@app.route('/change/<nav>')
def change_nav_view(nav):
    scrapper.starter()

    units = pickle_read("units.txt")
    navs = pickle.load(open("scrapped.pickle", "rb"))

    return render_template('jinja.html',navs=navs, units=float(nav))

@app.route('/change/', methods=['POST', 'GET'])
def change_nav():

    if request.method == 'POST':
        with open("units.txt", "wb") as units_file:
            pickle.dump( float(request.form['newUnit']), units_file )
        return redirect ('/')
        # return 'success fully changed'

    if request.method == 'GET':
        return redirect('/')
