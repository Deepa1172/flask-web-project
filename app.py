from flask import Flask, render_template, jsonify
#flask = library, Flask = Class
app = Flask(__name__)
CATS = [{
  "name": "Cash",
  "rank": 1,
  "breed": "British Shorthair",
  "Instagram": "@meow_cash"
}, {
  "name": "Kitty",
  "rank": 2,
  "breed": "Bengal Cat",
  "Instagram": "@bengalkittycat"
}, {
  "name": "Meatball",
  "rank": 3,
  "breed": "Tuxedo",
  "Instagram": "@meevin_official"
}]


@app.route("/")  #part of the URL (path)
def hello_world():
  return render_template('home.html',
                         cats=CATS)  #figure out how to add icon in flask
@app.route("/api/cats")
def jsonif():
  return jsonify(CATS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)  #run locally
