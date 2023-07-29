from flask import Flask, render_template, jsonify

app = Flask(__name__)  # created a flask app

JOBS = [
  {
    'id':1,
    'title':'Data Analyst',
    'location':'London, England',
    'salary':'£30,000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Manchester, England',
    'salary':'£30,000'
  },
  {
    'id':3,
    'title':'Frontend Engineer',
    'location':'Remote',
    'salary':'£30,000'
  },
  {
    'id':4,
    'title':'Backend Engineer',
    'location':'San Francisco, USA',
    'salary':'$40,000'
  },
]

@app.route("/")  # registered a route to the app 
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Khan')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":  # checked if we are runnning the app.py file
  app.run(host='0.0.0.0', debug=True)  # start the app using app.run
  