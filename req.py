import requests
url = 'https://jsonplaceholder.typicode.com/todos/1' 
#response = requests.get(url)        # To execute get request 
#print(response.status_code)     # To print http response code  
#print(response.text)            # To print formatted JSON response 
#r_json = response.json()

#print(r_json['title'])
#data = {'title':'Pyton Requests','body':'Requests are qwesome','userId':1} 
#response = requests.post('https://jsonplaceholder.typicode.com/posts', data, stream = True) 
#print(response.raw.read(30))  
try: 
    response = requests.get(url,timeout=0.1) 
    response.raise_for_status()                 # Raise error in case of failure 
except requests.exceptions.HTTPError as httpErr: 
    print ("Http Error:",httpErr) 
except requests.exceptions.ConnectionError as connErr: 
    print ("Error Connecting:",connErr) 
except requests.exceptions.Timeout as timeOutErr: 
    print ("Timeout Error:",timeOutErr) 
except requests.exceptions.RequestException as reqErr: 
    print ("Something Else:",reqErr) 