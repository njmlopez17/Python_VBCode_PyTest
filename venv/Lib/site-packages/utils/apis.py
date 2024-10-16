import requests

class APIs:
    BASE_URL= "https://jsonplaceholder.typicode.com"

    def __init__(self):
        self.header = {
            "Content-Type":"application/json"
        }

#  **GET method**
    def get(self,endpoint):
        url=f'{self.BASE_URL}/{endpoint}'
        getResponse = requests.get(url, headers=self.header)
        return getResponse

#  **POST method**
    def post(self,endpoint, data):
        url=f'{self.BASE_URL}/{endpoint}'
        postResponse = requests.post(url, headers=self.header, json=data)
        return postResponse
    
#  **PUT method**
    def put(self,endpoint, data):
        url=f'{self.BASE_URL}/{endpoint}'
        putResponse = requests.put(url, headers=self.header, json=data)
        return putResponse
    
#  **DELETE method**
    def delete(self,endpoint):
        url=f'{self.BASE_URL}/{endpoint}'
        deleteResponse = requests.put(url, headers=self.header)
        return deleteResponse
    