from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

def load_state():
    try:
        with open("state.json", "r") as f:
            return json.load(f)
    except:
        return {}

@app.route("/")
def dashboard():
    state = load_state()
    return render_template("dashboard.html", state=state)

@app.route("/api/state")
def api_state():
    return jsonify(load_state())

if __name__ == "__main__":
    app.run(debug=True)
