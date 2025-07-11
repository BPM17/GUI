import requests

class Requester():
    def __init__(self):
        self.url = ""
        self.method = ""

    def __str__(self):
        response = requests.request("GET", "http://127.0.0.1:8000/")
        return response.text
    
    def Get(self, url, headers, payload):
        response = requests.request('GET', "http://127.0.0.1:8000/" + url, headers=headers, data= payload)
        print(response, response.text)

    def Put(self, url, headers, payload):
        response = requests.request('PUT', "http://127.0.0.1:8000/" + url, headers=headers, data= payload)
        print(response, response.text)

if __name__ == "__main__":
    requester = Requester()
    print(Requester())