from flask import Flask
#flask = library, Flask = Class 
app = Flask(__name__)

@app.route("/") #part of the URL (path)
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug=True) #run locally