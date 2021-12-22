import rest_calls
import json
import time


token = ""
for x in range(4):
    # returns KeyError: 'experimentId' if no experiment is in Queue
    task = rest_calls.getexp_fromqueue(
        token)
    # print(task)
    # if "detail":"Invalid token." or {"detail":"Invalid token header. No credentials provided."}
    if "detail" in task:
        print("invalid credentials, generate new")
        credentials = rest_calls.login("zilk.felix@gmail.com", "123")
        # print(credentials)
        token = credentials["token"]
        print("new token for you")
        # print(token)
    else:
        print("this time credentials are valid")
        # print(task["experimentId"])
        if "experimentId" in task:
            print("there is also an experiment in the queue")
            experimentId = task["experimentId"]
            rest_calls.poststatus_running(
                token, experimentId)

            # Here: execute task

            # Here: retrieve result

            result = json.dumps({
                "experiment": experimentId,
                # "startTime": "2021-12-21T17:16:19.304243Z",
                "totalCounts": 50000,
                "numberOfDetectors": 4,
                "singlePhotonRate": "1500.00",
                "totalTime": 3,
                "experimentData": {
                    "countratePerDetector": {
                        "d1": 123,
                        "d2": 123,
                        "d3": 456,
                        "d4": 123,
                        "d5": 123,
                        "d6": 456,
                        "d7": 123,
                        "d8": 123
                    },
                    "encodedQubitMeasurements": {
                        "c00": 0.123,
                        "c01": 0.56,
                        "c10": 0.123,
                        "c11": 0.34
                    }
                }
            })
            print("results determined")
            rest_calls.post_result(
                token, result)
            print("results posted")
            rest_calls.poststatus_done(
                token, experimentId)
            print("status updated")

        else:
            print("empty queue")
    time.sleep(5)
