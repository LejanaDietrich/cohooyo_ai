#imports for nlp
import requests
import json

latest_clusering = None

#users[x][0] - description
#users[x][0] - liked profiles
#users[x][0] - description
users = [
    [[0], ['Ausbildung', 'Elektrotechnik', 'Volt'], ['5f3b78a4809ba900124873fa', '5f3b770d809ba900124873ee'], ['5f914b8a759f730012afba96'],[]],
    [[1], ['Brot backen'], ['5f914b8a759f730012afba96'], [], [[{'latitude': 49.4874592, 'longitude': 8.466039499999999}]] ],
    [[2], ['Holzverarbeitung'], ['5f3b7a10809ba9001248740c'], ['5f3b78a4809ba900124873fa'], [[]]],
    [[3], [],[],[], []],
    [[4], ['Informatik'],[],[], []],
]

#e.g. userid, jobid, rating-score (e.g. 0-5) 
evaluations = [
    [0,'5f914b8a759f730012afba96', 1],
    [0,'5f914a19759f730012afba91', 5],
    [0,'5f8eb46de4d7f00012ea81b7', 0],
    [0,'5f46cb7c0b4ceb0012577524', 2],
    [0,'5f46c88b0b4ceb001257751e', 0],
    [0,'5f46c4020b4ceb0012577514', 2],
    [0,'5f3ba0d0809ba90012487452', 5],
    [0,'5f3ba0ae809ba9001248744e', 4],
    [0,'5f3b9ee1809ba90012487449', 2],
    [0,'5f3b9d1b809ba9001248743e', 4],
    [0,'5f3b7a10809ba9001248740c', 5],
    [0,'5f3b78a4809ba900124873fa', 5],
    [0,'5f3b770d809ba900124873ee', 5],
    [0,'5f2fdf6c15633f0012d6dbed', 5],
    [0,'5f2fddac15633f0012d6dbe8', 0],
    [0,'5f2eb49615633f0012d6dbc7', 0],
    [1,'5f914b8a759f730012afba96', 5],
    [1,'5f914a19759f730012afba91', 4],
    [1,'5f8eb46de4d7f00012ea81b7', 0],
    [1,'5f46cb7c0b4ceb0012577524', 4],
    [1,'5f46c88b0b4ceb001257751e', 4],
    [1,'5f46c4020b4ceb0012577514', 0],
    [1,'5f3ba0d0809ba90012487452', 3],
    [1,'5f3ba0ae809ba9001248744e', 1],
    [1,'5f3b9ee1809ba90012487449', 4],
    [1,'5f3b9d1b809ba9001248743e', 2],
    [1,'5f3b7a10809ba9001248740c', 0],
    [1,'5f3b78a4809ba900124873fa', 4],
    [1,'5f3b770d809ba900124873ee', 4],
    [1,'5f2fdf6c15633f0012d6dbed', 1],
    [1,'5f2fddac15633f0012d6dbe8', 5],
    [1,'5f2eb49615633f0012d6dbc7', 3],
    [2,'5f914b8a759f730012afba96', 5],
    [2,'5f914a19759f730012afba91', 5],
    [2,'5f8eb46de4d7f00012ea81b7', 2],
    [2,'5f46cb7c0b4ceb0012577524', 5],
    [2,'5f46c88b0b4ceb001257751e', 1],
    [2,'5f46c4020b4ceb0012577514', 3],
    [2,'5f3ba0d0809ba90012487452', 4],
    [2,'5f3ba0ae809ba9001248744e', 2],
    [2,'5f3b9ee1809ba90012487449', 1],
    [2,'5f3b9d1b809ba9001248743e', 0],
    [2,'5f3b7a10809ba9001248740c', 4],
    [2,'5f3b78a4809ba900124873fa', 1],
    [2,'5f3b770d809ba900124873ee', 1],
    [2,'5f2fdf6c15633f0012d6dbed', 1],
    [2,'5f2fddac15633f0012d6dbe8', 3],
    [2,'5f2eb49615633f0012d6dbc7', 5],
    [3,'5f914b8a759f730012afba96', 1],
    [3,'5f914a19759f730012afba91', 1],
    [3,'5f8eb46de4d7f00012ea81b7', 4],
    [3,'5f46cb7c0b4ceb0012577524', 0],
    [3,'5f46c88b0b4ceb001257751e', 2],
    [3,'5f46c4020b4ceb0012577514', 5],
    [3,'5f3ba0d0809ba90012487452', 4],
    [3,'5f3ba0ae809ba9001248744e', 5],
    [3,'5f3b9ee1809ba90012487449', 4],
    [3,'5f3b9d1b809ba9001248743e', 1],
    [3,'5f3b7a10809ba9001248740c', 3],
    [3,'5f3b78a4809ba900124873fa', 1],
    [3,'5f3b770d809ba900124873ee', 2],
    [3,'5f2fdf6c15633f0012d6dbed', 2],
    [3,'5f2fddac15633f0012d6dbe8', 1],
    [3,'5f2eb49615633f0012d6dbc7', 5],
    [4,'5f914b8a759f730012afba96', 4],
    [4,'5f914a19759f730012afba91', 3],
    [4,'5f8eb46de4d7f00012ea81b7', 0],
    [4,'5f46cb7c0b4ceb0012577524', 4],
    [4,'5f46c88b0b4ceb001257751e', 1],
    [4,'5f46c4020b4ceb0012577514', 2],
    [4,'5f3ba0d0809ba90012487452', 2],
    [4,'5f3ba0ae809ba9001248744e', 5],
    [4,'5f3b9ee1809ba90012487449', 1],
    [4,'5f3b9d1b809ba9001248743e', 0],
    [4,'5f3b7a10809ba9001248740c', 0],
    [4,'5f3b78a4809ba900124873fa', 5],
    [4,'5f3b770d809ba900124873ee', 1],
    [4,'5f2fdf6c15633f0012d6dbed', 1],
    [4,'5f2fddac15633f0012d6dbe8', 1],
    [4,'5f2eb49615633f0012d6dbc7', 0]
]

#access API
r = requests.get('https://api.cohooyo.com/jobs')
jobs = json.loads(r.text)

