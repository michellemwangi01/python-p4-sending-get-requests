import requests
import json

url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/locations.json"

response = requests.get(url)

json_content = json.loads(response.text)

print(json.dumps(json_content, indent=4))

# USING GET METHOD WITH PYTHON
# 1. `import requests`
# 2. `url = "https://learn-co-curriculum.github.io/json-site-example/"` The URL to get data from
# 3. `response = requests.get(url)`
# 4. `response.text`

# CONVERTING TO JSON
# 1. `import json`
# 2. `json.loads(response.content)`
# 3. Organize the data if need be:
    # print(json.dumps(json.loads(response.content), indent=4, sort_keys=True))



