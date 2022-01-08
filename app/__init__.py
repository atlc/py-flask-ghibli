from main import app
from gevent.pywsgi import WSGIServer
import os


PORT = int(os.environ.get('PORT', 5000))
http_server = WSGIServer(('', PORT), app)
http_server.serve_forever()
