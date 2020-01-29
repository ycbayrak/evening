from flask import request


def before_request_handler():
    print(request.data)
    request.headers.get("IAM_HEADER")
    if request.method == "POST":
        print(request.json)
        request.json["accountId"] = "BLANK"
        print(request.json)
    print("before_request is running!")
    print(request.url)
    return