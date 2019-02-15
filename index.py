import os
import json
from bottle import HTTPResponse, route, run
from table import User 
from connector import PostgreSQLConnector


def create_response(body, status=200, err=None):
    body['err'] = err
    r = HTTPResponse(status=status, body=body)
    r.set_header('Content-Type', 'application/json')
    return r


@route('/')
def index():
    return "hello"


@route('/test')
def test():
    return create_response({'msg': 'test'})


@route('/show_env')
def show_env():
    return create_response({'environ': dict(os.environ)})


@route('/test_conn')
def test_conn():
    print(conn.session)
    return create_response({'users': ''})


@route('/adduser')
def add_user():
    user = User()
    user.name = 'hoge'
    conn.session.add(user)
    conn.session.commit()


def _user_to_dict(user):
    return {'id': user.id, 'name': user.name}


@route('/getusers')
def users():
    users = conn.session.query(User).all()
    ret = [_user_to_dict(user) for user in users]
    return create_response({'users': ret})    


def _init_conn():
    services = json.loads(os.getenv('VCAP_SERVICES'))
    postgresql_env = services['postgresql94'][0]
    credentials = postgresql_env['credentials']
    global conn
    conn = PostgreSQLConnector(credentials['uri'])


if __name__ == "__main__":
    _init_conn()
    port = int(os.getenv("PORT", 9099))
    run(host='0.0.0.0', port=port)
