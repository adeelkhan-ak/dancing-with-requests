import requests
url = 'https://jsonplaceholder.typicode.com/todos/1' 
response = requests.get(url)        # To execute get request 
print(response.status_code)     # To print http response code  
print(response.text)            # To print formatted JSON response 
r_json = response.json()

print(r_json['title'])
data = {'title':'Pyton Requests','body':'Requests are qwesome','userId':1} 
response = requests.post('https://jsonplaceholder.typicode.com/posts', data, stream = True) 
print(response.raw.read(30))  
 