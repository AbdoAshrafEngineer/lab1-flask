from flask import Flask, render_template

app = Flask(__name__)

jobs = [
    {
        "id": 1,
        "title": "Software Engineer",
        "location": "Cairo",
        "company": "Tech Company",
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "location": "Alexandria",
        "company": "Data Corp",
    },
    {
        "id": 3,
        "title": "Web Developer",
        "location": "Zagazig",
        "company": "Web Solutions",
    },
    {
        "id": 4,
        "title": "Mobile Developer",
        "location": "Cairo",
        "company": "App Innovations",
    },
    {
        "id": 5,
        "title": "DevOps Engineer",
        "location": "Giza",
        "company": "Cloud Services",
    },
]

companies = [
    {
        "id": 1,
        "name": "Tech Company",
        "location": "Cairo",
        "industry": "Software",
        "employees": 120
    },
    {
        "id": 2,
        "name": "Data Corp",
        "location": "Alexandria",
        "industry": "Data Analytics",
        "employees": 75
    },
    {
        "id": 3,
        "name": "Cloud Services",
        "location": "Giza",
        "industry": "Cloud Computing",
        "employees": 200
    }
]


@app.route('/jobs/list')
def list_jobs():
    return render_template("jobs_list.html", jobs=jobs)

# Lab:

# - create end points for:


#     - single job by id
@app.route('/job/<int:id>')
def get_job(id):
    for j in jobs:
        if j["id"] == id:
            return render_template("job_id.html", job=j)
    return "job not found", 404


#     - create list endpoint for companies (id, name, location, industry, employees count)
@app.route('/companies')
def list_companies():
    return render_template("list_companies.html", cs=companies)


#     - single company by id
@app.route('/company/<int:id>')
def get_company(id):
    for comp in companies:
        if id == comp["id"]:
            return render_template("company_id.html", c=comp)
    return "company not found", 404



