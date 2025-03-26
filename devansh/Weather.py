import requests
import json

url = "https://wizklub.com/api/secured/wiziot-poll-request/"
headers = {"Api-Access-Key": "MzZyRHh6VVVjM1ZpTU5vdkxrYWU=", "Api-Secret-Key": "MU5WWmxhb1JraTJFNVpQRTd0SWg5QVFLak9RaDJ0RlJtUQ==", "Content-Type": "application/json"}
payload = json.dumps({"mode": "WRITE", "device_id": "sc13505", "source": "API", "api": "sensor", "sensor": "weather", "state": "start"})

response = requests.request("POST", url, headers=headers, data=payload)

payload1 = json.dumps({"mode": "READ", "device_id": "sc13505", "source": "API", "api": "sensor", "sensor": "weather"})
s
response1 = requests.request("POST", url, headers=headers, data=payload1)

print(response1.text)
