import requests

url = 'http://localhost:9696/predict'

client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}

response = requests.post(url,json=client).json()
print(response)

if response['card probability'] >= 0.5:
    print('Client will get a credit card')
else:
    print('Client will not get a credit card')