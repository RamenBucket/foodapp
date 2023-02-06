from flask import Flask, render_template, request
import random

restaurants = open("restaurants.txt").read().splitlines()
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('pick') == 'pick a restaurant':
            restaurant = random.choice(restaurants)
        elif request.form.get('choose') == 'choose from 5':
            sample = random.sample(restaurants, 5)
            restaurant = ""
            for s in sample:
                restaurant += f'{s}\n'

    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template('index.html', restaurant = restaurant)