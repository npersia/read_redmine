import requests
from flask import Flask




__headers__ = {"X-Redmine-API-Key": "1e8a0e5eff9a6c4311daac0f0f69b20fd00f765b"}

__url_base__ = "https://redmine.semperti.com"


def getRedMine(url,headers=__headers__):
    return requests.get(url,headers=headers).json()


def getAllIssues():
    url = __url_base__ + "/issues.json"
    return getRedMine(url)


def getIssuesUpdate():
    r = getAllIssues()
    issues = {}
    for x in r["issues"]:
        issues[x["id"]] = x["updated_on"]
    return issues


def getIssueRedMine(issue):
    url = __url_base__ + "/issues/" + issue + ".json?include=journals"
    return getRedMine(url)



app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/issue/<issue_id>')
def getIssueid(issue_id):
    return str(getIssueRedMine(issue_id))

