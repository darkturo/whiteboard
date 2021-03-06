from flask import render_template, redirect
from flask_bootstrap import Bootstrap

from whiteboard import app

import whiteboard.navbar
import whiteboard.session


Bootstrap(app)

WebAppName = "Collaborative Whiteboard"


@app.route('/', methods=['GET'])
def view():
    return render_template('main.html')


@app.route('/whiteboard', methods=['GET'])
def get_new_session():
    url = "/whiteboard/{session_id}".format(session_id=whiteboard.session.gen_session())
    return redirect(url)


@app.route('/whiteboard/<session_id>', methods=['GET'])
def working_space(session_id):
    return render_template('working-space.html', session_id=session_id)


@app.route('/showsessions', methods=['GET'])
def showsessions():
    return render_template('search-session.html')


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


whiteboard.navbar.register(app, WebAppName, 
                           {'Start': 'view', 
                            'About': 'about'})   
