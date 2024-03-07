from flask import Flask, request, session, jsonify, make_response

app = Flask(__name__)
# # Disable compact JSON representation in the response
app.json.compact = False

# # Set a secret key for the Flask application
app.secret_key = b'?w\x85Z\x08Q\xbdO\xb8\xa9\xb65Kj\xa9_'

@app.route('/sessions/<string:key>', methods=['GET'])
def show_session(key):

    # Set default values for session variables if not already set
    session["hello"] = session.get("hello") or "World"
    session["goodnight"] = session.get("goodnight") or "Moon"

    # Create a response containing session information and cookies
    response = make_response(jsonify({
        'session': {
            'session_key': key,
            'session_value': session[key],
            'session_accessed': session.accessed,
        },
        'cookies': [{cookie: request.cookies[cookie]}
            for cookie in request.cookies],
    }), 200)

    # Set a new cookie named 'mouse' with the value 'Cookie'
    response.set_cookie('mouse', 'Cookie')

    return response

if __name__ == '__main__':
    app.run(port=5555)
    