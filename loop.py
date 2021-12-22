import rest_calls
import json

# returns KeyError: 'experimentId' if no experiment is in Queue
task = rest_calls.getexp_fromqueue(
    "01a9b596c1b165fa4f15fbccad4092428dc47db76ad4e5dfe3bfee24b66bb432")
# if "detail":"Invalid token." or {"detail":"Invalid token header. No credentials provided."}

print(task["experimentId"])

experimentId = task["experimentId"]
rest_calls.poststatus_running(
    "01a9b596c1b165fa4f15fbccad4092428dc47db76ad4e5dfe3bfee24b66bb432", experimentId)

# execute task

# retrieve result

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


rest_calls.post_result(
    "01a9b596c1b165fa4f15fbccad4092428dc47db76ad4e5dfe3bfee24b66bb432", result)

rest_calls.poststatus_done(
    "01a9b596c1b165fa4f15fbccad4092428dc47db76ad4e5dfe3bfee24b66bb432", experimentId)
