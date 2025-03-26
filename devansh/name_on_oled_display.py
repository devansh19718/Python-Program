import requests
import json

url = "https://wizklub.com/api/secured/wiziot-poll-request/"
payload = json.dumps({"mode": "WRITE", "device_id": "sc13502", "source": "API", "api": "oled", "type": "text", "msg_to_write": "Devasnsh sain", "x_axis": "0", "y_axis": "0"})

headers = {"Api-Access-Key": "MzZyRHh6VVVjM1ZpTU5vdkxrYWU=", "Api-Secret-Key": "MU5WWmxhb1JraTJFNVpQRTd0SWg5QVFLak9RaDJ0RlJtUQ==", "Content-Type": "application/json"}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)