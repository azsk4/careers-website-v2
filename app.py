from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)  # created a flask app

@app.route("/")  # registered a route to the app 
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs, company_name='Khan')

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

if __name__ == "__main__":  # checked if we are runnning the app.py file
  app.run(host='0.0.0.0', port = 4444, debug=True)  # start the app using app.run
  