import os
from bottle import route, run

@route('/')
def index():
    return "hello"


if __name__ == "__main__":
    port = int(os.getenv("PORT", 9099))
    run(host='0.0.0.0', port=port)
