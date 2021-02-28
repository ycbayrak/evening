def before_request_handler():
    """
    Simple hook for executing before every request.
    :return: None
    """
    print("before_request_handler is running!")
    return


def after_request_handler(response):
    """
    Simple hook for executing before every request.
    :return: None
    """
    print("after_request_handler is running!")
    return response
