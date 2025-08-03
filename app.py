from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    with open('data/dummy_data.json') as f:
        all_data = json.load(f)  # now a list of interns

    # Get from query string
    name = request.args.get('name')
    referral = request.args.get('referral')

    # Default to first intern if no match
    selected_user = all_data[0]

    # Try to find the matching user
    for user in all_data:
        if name and user["name"].lower() == name.lower():
            selected_user = user
            break
        elif referral and user["referral_code"].lower() == referral.lower():
            selected_user = user
            break

    return render_template("dashboard.html", data=selected_user)


@app.route("/api/user")
def user_data():
    with open('data/dummy_data.json') as f:
        return jsonify(json.load(f))
    
@app.route("/api/users")
def all_users():
    with open('data/dummy_data.json') as f:
        return jsonify(json.load(f))


@app.route("/leaderboard")
def leaderboard():
    return render_template("leaderboard.html")

@app.route("/logout")
def logout():
    return render_template("logout.html")


if __name__ == "__main__":
    app.run(debug=True)
