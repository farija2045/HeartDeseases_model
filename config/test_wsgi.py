# test_wsgi.py
from config.wsgi import application

def simple_environ():
    return {
        "REQUEST_METHOD": "GET",
        "PATH_INFO": "/",
        "wsgi.input": open("/dev/null", "rb"),
        "CONTENT_LENGTH": "0",
        "SERVER_NAME": "localhost",
        "SERVER_PORT": "8000",
        "wsgi.version": (1, 0),
        "wsgi.url_scheme": "http",
        "wsgi.errors": None,
        "wsgi.multithread": False,
        "wsgi.multiprocess": False,
        "wsgi.run_once": False,
    }

def simple_start_response(status, headers):
    print("STATUS:", status)
    print("HEADERS:", headers)

result = application(simple_environ(), simple_start_response)
print("BODY:", list(result))
