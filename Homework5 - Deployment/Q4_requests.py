import requests

url = 'http://127.0.0.1:9696/predict'

customer = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}

response = requests.post(url,json=customer).json()
print(response)

if response['card probability'] >= 0.5:
    print('Client will get a credit card')
else:
    print('Client will not get a credit card')