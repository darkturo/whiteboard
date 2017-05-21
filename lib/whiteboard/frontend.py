from flask import render_template
from flask_bootstrap import Bootstrap

from whiteboard import app

import whiteboard.navbar

Bootstrap(app)

WebAppName = "Collaborative Whiteboard"

@app.route('/', methods=['GET'])
def view():
    return render_template('main.html')


@app.route('/about', methods=['GET'])
def about():
    return "Not implemented", 200


whiteboard.navbar.register(app, WebAppName, 
                           {'Start': 'view', 
                            'About': 'about'})   

        
