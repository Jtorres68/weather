# -*- coding: utf-8 -*-

"""routes are the diff URLs that the application implements
handlers for the app routes are written as Python funct called view funct
View functions are mapped to one or more route URLs so that Flask knows what 
logic to execute when a client requests a given URL"""

from app import app
from weather import Weather, Unit
from flask import render_template, request

#@app.route are decorators which modifies the funct that follows it
#app route maps are for URLs like http://localhost:5000/index
@app.route('/')
@app.route('/index')
def index():
    """view function returns html template"""
    
    return render_template('index.html')

@app.route('/weather', methods=['POST', 'GET'])
def index_post():
    """returns weather based on location given by user"""
    
    if request.method == 'POST':
        loc = request.form['location']
        if request.form['temp'] == 'CELSIUS':
            CorF = 'C'
            weather = Weather(unit=Unit.CELSIUS)
            
        if request.form['temp'] == 'FAHRENHEIT':
            CorF = 'F'
            weather = Weather(unit=Unit.FAHRENHEIT)
            
        location = weather.lookup_by_location(loc)
        condition = location.condition
    
        return render_template('weather.html', condition = condition, loc = loc, CorF = CorF)
        #return "{}C \n{}".format(condition.temp, condition.text)

if __name__ == '__main__':
    app.run(debug = True)