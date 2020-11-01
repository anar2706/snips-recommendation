# snips-recommendation
1.install requirements


2.execute 'python -m snips_nlu download en'


3.run app with 'python run.py'


4.send request to /nlu endpoint


example:

  import requests

  url = "http://localhost:5000/nlu"

  payload = {"sentence":"How is weather in Singapur"}
  headers = {
  'Content-Type': 'application/json'
  }

  response = requests.post(url, headers=headers, json = payload)

  print(response.content)
