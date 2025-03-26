import requests
import json

url = "https://wizklub.com/api/secured/wiziot-poll-request/"

payload = json.dumps({"mode": "WRITE", "device_id": "sc13502", "source": "API", "api": "oled", "type": "circle", "x_axis": "60", "y_axis": "30", "radius": "30", "fill_type": "0"})
headers = {"Api-Access-Key": "MzZyRHh6VVVjM1ZpTU5vdkxrYWU=", "Api-Secret-Key": "MU5WWmxhb1JraTJFNVpQRTd0SWg5QVFLak9RaDJ0RlJtUQ==", "Content-Type": "application/json"}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)