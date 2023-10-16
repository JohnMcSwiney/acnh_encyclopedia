from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
# CORS(app, resources={r"/members/*": {"origins": "*"}})

CORS(app, resources={r"/members/*": {"origins": "http://localhost:3000", "allow_headers": ["Content-Type"], "supports_credentials": True}})

# ... your routes and application code ...


#members API route
@app.route("/members")
def members():
    return{"members": ["member1","member2","member3"]}

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=8000)
#used these videos:
#https://www.youtube.com/watch?v=7LNl2JlZKHA