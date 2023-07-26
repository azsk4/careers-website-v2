from flask import Flask, render_template

app = Flask(__name__)  # created a flask app

@app.route("/")  # registered a route to the app 
def hello_world():
  return render_template('home.html')

if __name__ == "__main__":  # checked if we are runnning the app.py file
  app.run(host='0.0.0.0', debug=True)  # start the app using app.run
  