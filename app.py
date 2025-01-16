from flask import Flask;

app = Flask(__name__);

@app.route("/info")
def test():
    return "Hello, Welcome to ...";

app.run(host='0.0.0.0');
