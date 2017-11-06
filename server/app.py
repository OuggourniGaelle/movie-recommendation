from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/my-movies')
def list_user_movies():
    return render_template('my-movies.html', page_title='My Movies')

my_movies_rated = pd.read_csv('./data/my-ratings.csv', sep=',', header=0)


{% for index, movie in my_movies_rated.iterrows() %}