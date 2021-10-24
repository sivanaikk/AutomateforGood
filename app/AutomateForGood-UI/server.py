import gevent.pywsgi

app_server = gevent.pywsgi.WSGIServer(('0.0.0.0', 5001), ./app)
app_server.serve_forever()
