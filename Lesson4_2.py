import requests
# resp = requests.get('http://wikipedia.org')
#
# print(resp.headers['Content-Type'])
# print(resp.url)
# print(resp.history)


url = 'http://httpbin.org/get'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)

print(r.text)


payload = {'key1': 'value1'}
r = requests.get(url, params=payload)

print(r.url)

print(r.text)