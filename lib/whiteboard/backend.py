import json

from flask import request, session

from whiteboard import app


@app.before_request
def setup_session():
    if not 'memorycache' in session:
        session['memorycache'] = dict()

@app.route('/api/v.0.1/update/<session_id>', methods=['POST'])
def update(session_id):
    if not session_id in session['memorycache']:
        session['memorycache'][session_id] = extract_json(request.get_data())

    return json.dumps({'status': 'ok'}), 200

@app.route('/api/v.0.1/retrieve/<session_id>', methods=['GET'])
def retrieve(session_id):
    data = {}
    if session_id in session['memorycache']:
        data = json.dump(session['memorycache'])
    return json.dumps(data), 200

###
def extract_json(data):
    content = None
    try:
        content = json.loads(data)
    except:
        app.logger.warning("Received malformed data: %s" % data)
    return content
