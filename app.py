from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)  # created a flask app

@app.route("/")  # registered a route to the app 
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found", 404
    
  return render_template('jobpage.html', 
                         job=job)

if __name__ == "__main__":  # checked if we are runnning the app.py file
  app.run(host='0.0.0.0', port = 8080, debug=True)  # start the app using app.run
  