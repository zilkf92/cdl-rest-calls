import rest_calls
import json
import time
import passwords


token = ""
for x in range(5):
    # returns {"detail":"Invalid token."} or {"detail":"Invalid token header. No credentials provided."} if no or wrong credentials
    # returns KeyError: 'experimentId' if no experiment is in Queue
    task = rest_calls.getexp_fromqueue(
        token)
    # print(task)

    if "detail" not in task:
        print("Credentials are valid")
        # print(task["experimentId"])
        if "experimentId" in task:
            print("There is also a new experiment in the queue")
            print(task)
            experimentId = task["experimentId"]
            print("Running")
            rest_calls.poststatus_running(
                token, experimentId)

            # Here: execute task
            print("Experiment performed")
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
            print("Results determined")
            rest_calls.post_result(
                token, result)
            print("Results posted to API")
            rest_calls.poststatus_done(
                token, experimentId)
            print("Status of " + experimentId + " updated")

        else:
            print("Empty queue")
    elif "detail" in task:
        print("Invalid credentials, generating new ...")
        credentials = rest_calls.login(passwords.email, passwords.password)
        # print(credentials)
        token = credentials["token"]
        print("New token for you!")
        # print(token)
    else:
        pass
    time.sleep(5)
