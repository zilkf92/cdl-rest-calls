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

def getexp_fromqueue():
    """ """
    url = "http://127.0.0.1:8000/api/experiments/queue"

    payload = {}
    headers = {
        'Authorization': 'Token 1b6b72258eb0af05b6dc81fd67032900c71cc53d032b9bd08085adeebe9ad0e3',
        'Cookie': 'csrftoken=a6IwyqS4I5vjwcNAT5Tm70PuiK7AFjcDVPHbyZy3I189V7eX5iK2m0AwJQoYyVUb; sessionid=5g4v77efjv0r99nziiourrzqocruyasl'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)


def poststatus_running():
    """ """
    url = "http://127.0.0.1:8000/api/experiments/68c64b96-73ed-4184-9ac1-c2d3bab0e068"

    payload = {'status': 'RUNNING'}
    files = [

    ]
    headers = {
        'Authorization': 'Token 1b6b72258eb0af05b6dc81fd67032900c71cc53d032b9bd08085adeebe9ad0e3',
        'Cookie': 'csrftoken=a6IwyqS4I5vjwcNAT5Tm70PuiK7AFjcDVPHbyZy3I189V7eX5iK2m0AwJQoYyVUb; sessionid=5g4v77efjv0r99nziiourrzqocruyasl'
    }

    response = requests.request(
        "PATCH", url, headers=headers, data=payload, files=files)

    print(response.text)


# post_running()

def post_result():
    """ """
    url = "http://127.0.0.1:8000/api/results"

    payload = json.dumps({
        "totalCounts": "50000",
        "numberOfDetectors": "4",
        "singlePhotonRate": "1500.00",
        "totalTime": "3",
        "experiment": "68c64b96-73ed-4184-9ac1-c2d3bab0e068",
        "experimentData": {
            "countratePerDetector": {
                "d1": "123",
                "d2": "123",
                "d3": "456",
                "d4": "123",
                "d5": "123",
                "d6": "456",
                "d7": "123",
                "d8": "123"
            },
            "encodedQubitMeasurements": {
                "c00": "0.123",
                "c10": "0.123",
                "c01": "0.56",
                "c11": "0.34"
            }
        }
    })
    headers = {
        'Authorization': 'Token 1b6b72258eb0af05b6dc81fd67032900c71cc53d032b9bd08085adeebe9ad0e3',
        'Content-Type': 'application/json',
        'Cookie': 'csrftoken=a6IwyqS4I5vjwcNAT5Tm70PuiK7AFjcDVPHbyZy3I189V7eX5iK2m0AwJQoYyVUb; sessionid=5g4v77efjv0r99nziiourrzqocruyasl'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


# post_result()
def poststatus_done():
    """ """
    url = "http://127.0.0.1:8000/api/experiments/68c64b96-73ed-4184-9ac1-c2d3bab0e068"

    payload = {'status': 'DONE'}
    files = [

    ]
    headers = {
        'Authorization': 'Token 1b6b72258eb0af05b6dc81fd67032900c71cc53d032b9bd08085adeebe9ad0e3',
        'Cookie': 'csrftoken=a6IwyqS4I5vjwcNAT5Tm70PuiK7AFjcDVPHbyZy3I189V7eX5iK2m0AwJQoYyVUb; sessionid=5g4v77efjv0r99nziiourrzqocruyasl'
    }

    response = requests.request(
        "PATCH", url, headers=headers, data=payload, files=files)

    print(response.text)


def poststatus_failed():
    """ """
    url = "http://127.0.0.1:8000/api/experiments/68c64b96-73ed-4184-9ac1-c2d3bab0e068"

    payload = {'status': 'FAILED'}
    files = [

    ]
    headers = {
        'Authorization': 'Token 1b6b72258eb0af05b6dc81fd67032900c71cc53d032b9bd08085adeebe9ad0e3',
        'Cookie': 'csrftoken=a6IwyqS4I5vjwcNAT5Tm70PuiK7AFjcDVPHbyZy3I189V7eX5iK2m0AwJQoYyVUb; sessionid=5g4v77efjv0r99nziiourrzqocruyasl'
    }

    response = requests.request(
        "PATCH", url, headers=headers, data=payload, files=files)

    print(response.text)
