import requests
import json
r = requests.get('https://api.cohooyo.com/jobs')
jobs = json.loads(r.text)
print(len(jobs))
print(jobs[12])