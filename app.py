# edited
import os
import threading
from flask import Flask
from flask import render_template
from pyftpdlib import authorizers
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

app = Flask("PrintingCompany")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/order")
def order():
    return render_template("order.html")

def run_ftp_server():
    ftp_dir = os.getcwd()

    authorizer = DummyAuthorizer()
    authorizer.add_user('student', '123', ftp_dir, perm='elradfmw')

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer(('0.0.0.0', 2121), handler)
    server.serve_forever()

if __name__ == "__main__":
    ftp_thread = threading.Thread(target=run_ftp_server, daemon=True)
    ftp_thread.start()

    app.run(debug=True, port=5000, host='0.0.0.0')
