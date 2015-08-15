from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
	# check that we get a 404 on the / URL
	resp = app.request("/game")
	assert_response(resp, status="200")
	resp = app.request("/")
	assert_response(resp, status="303")
	
def test_request_paths():
	data = "action=tell+a+joke"
	resp = app.request("/game", method="POST", data=data)
	#print resp
	assert_response(resp, status="303 See Other")
	assert("webpy_session_id=" in resp.headers['Set-Cookie'])

	resp = app.request("/hello")
	#print resp
	assert_response(resp, status="404 Not Found")

	resp = app.request("/hello", method="POST")
	#print resp
	assert_response(resp, status="404 Not Found")
	assert("webpy_session_id=" in resp.headers['Set-Cookie'])

	'''
	# test our first GET request to /hello
	resp = app.request("/hello")
	assert_response(resp)

	# make sure default values work for the form
	resp = app.request("/hello", method="POST")
	assert_response(resp, contains="Nobody")

	# test that we get expected values
	data = {'name': 'Zed', 'greet': 'Hola'}
	resp = app.request("/hello", method="POST", data=data)
	assert_response(resp, contains="Zed")
	'''