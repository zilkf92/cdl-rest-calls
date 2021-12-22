import requests
import json


def login(useremail, userpassword):

    url = "http://127.0.0.1:8000/api/login"

    payload = {'username': useremail,
               'password': userpassword}
    files = [

    ]
    headers = {
        'Cookie': 'csrftoken=a6IwyqS4I5vjwcNAT5Tm70PuiK7AFjcDVPHbyZy3I189V7eX5iK2m0AwJQoYyVUb; sessionid=5g4v77efjv0r99nziiourrzqocruyasl'
    }

    response = requests.request(
        "POST", url, headers=headers, data=payload, files=files)

    print(response.text)


#login("zilk.felix@gmail.com", "123")

def getexp_fromqueue(token):
    """ """
    auth_token = "Token " + token
    url = "http://127.0.0.1:8000/api/experiments/queue"

    payload = {}
    headers = {
        'Authorization': auth_token,
        # 'Cookie': 'csrftoken=a6IwyqS4I5vjwcNAT5Tm70PuiK7AFjcDVPHbyZy3I189V7eX5iK2m0AwJQoYyVUb; sessionid=5g4v77efjv0r99nziiourrzqocruyasl'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    # returns KeyError: 'experimentId' if no experiment is in Queue

    return response.json()
    # print(response.text)


def poststatus_running(token, experimentId):
    """ """
    auth_token = "Token " + token
    url = f"http://127.0.0.1:8000/api/experiments/{experimentId}"

    payload = {'status': 'RUNNING'}
    files = [

    ]
    headers = {
        'Authorization': auth_token,
        'Cookie': 'csrftoken=a6IwyqS4I5vjwcNAT5Tm70PuiK7AFjcDVPHbyZy3I189V7eX5iK2m0AwJQoYyVUb; sessionid=5g4v77efjv0r99nziiourrzqocruyasl'
    }

    response = requests.request(
        "PATCH", url, headers=headers, data=payload, files=files)

    # print(response.text)


# post_running()

def post_result(token, result):
    """ """
    auth_token = "Token " + token
    url = "http://127.0.0.1:8000/api/results"
    payload = result
    # payload = json.dumps({
    #     "totalCounts": "50000",
    #     "numberOfDetectors": "4",
    #     "singlePhotonRate": "1500.00",
    #     "totalTime": "3",
    #     "experiment": "68c64b96-73ed-4184-9ac1-c2d3bab0e068",
    #     "experimentData": {
    #         "countratePerDetector": {
    #             "d1": "123",
    #             "d2": "123",
    #             "d3": "456",
    #             "d4": "123",
    #             "d5": "123",
    #             "d6": "456",
    #             "d7": "123",
    #             "d8": "123"
    #         },
    #         "encodedQubitMeasurements": {
    #             "c00": "0.123",
    #             "c10": "0.123",
    #             "c01": "0.56",
    #             "c11": "0.34"
    #         }
    #     }
    # })
    headers = {
        'Authorization': auth_token,
        'Content-Type': 'application/json',
        'Cookie': 'csrftoken=a6IwyqS4I5vjwcNAT5Tm70PuiK7AFjcDVPHbyZy3I189V7eX5iK2m0AwJQoYyVUb; sessionid=5g4v77efjv0r99nziiourrzqocruyasl'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


# post_result()
def poststatus_done(token, experimentId):
    """ """
    auth_token = "Token " + token
    url = f"http://127.0.0.1:8000/api/experiments/{experimentId}"

    payload = {'status': 'DONE'}
    files = [

    ]
    headers = {
        'Authorization': auth_token,
        'Cookie': 'csrftoken=a6IwyqS4I5vjwcNAT5Tm70PuiK7AFjcDVPHbyZy3I189V7eX5iK2m0AwJQoYyVUb; sessionid=5g4v77efjv0r99nziiourrzqocruyasl'
    }

    response = requests.request(
        "PATCH", url, headers=headers, data=payload, files=files)

    print(response.text)


def poststatus_failed(token, experimentId):
    """ """
    url = f"http://127.0.0.1:8000/api/experiments/{experimentId}"

    payload = {'status': 'FAILED'}
    files = [

    ]
    headers = {
        'Authorization': token,
        'Cookie': 'csrftoken=a6IwyqS4I5vjwcNAT5Tm70PuiK7AFjcDVPHbyZy3I189V7eX5iK2m0AwJQoYyVUb; sessionid=5g4v77efjv0r99nziiourrzqocruyasl'
    }

    response = requests.request(
        "PATCH", url, headers=headers, data=payload, files=files)

    print(response.text)
