from flask import Flask, render_template, json

app = Flask(__name__)
with open('static/contributors.json', 'r') as contrib_file:
    contributors = contrib_file.read()


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html", data=json.loads(contributors))


if __name__ == "__main__":
    app.run()
