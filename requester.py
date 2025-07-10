import requests

class Requester():
    def __init__(self):
        self.url = ""
        self.method = ""

    def __str__(self):
        response = requests.request("GET", "http://127.0.0.1:8000/")
        return response.text
    
    def Get(self, method, url, headers, payload):
        response = requests.request(method, url, headers=headers, data= payload)

    def Put(self, method, url, headers, payload):
        response = requests.request(method, url, headers=headers, data= payload)

if __name__ == "__main__":
    requester = Requester()
    print(Requester())