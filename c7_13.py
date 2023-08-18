import requests
response = requests.get('https://kamasanchi.hatenablog.com/entry/color-4096')
text = response.text
print(text)
