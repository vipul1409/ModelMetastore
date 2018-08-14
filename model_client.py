import requests


class ModelClient(object):

    def __init__(self, host="https://infinite-mountain-66126.herokuapp.com", port="443"):
        self.host = host
        self.port = port
        self.base_url = self.host + ":" + self.port

    def post_model(self, data):
        resp = requests.post(self.base_url + "/models/", data)
        return resp.text

    def get_model(self, id):
        url = self.base_url + "/models/" + id + "/?format=json"
        return requests.get(url)

