from flask import render_template
from flask_bootstrap import Bootstrap
                                                                                 
from whiteboard import app       

Bootstrap(app)

@app.route('/', methods=['GET'])
def view():
    return render_template('main.html')

