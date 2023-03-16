import platform
import cpuinfo
import socket
import os
from flask import Flask, render_template

# System class
class System:
    # Constructor method 
    def __init__(self):
        self.system = platform.system()
        self.architecture = platform.architecture()
        self.processor = cpuinfo.get_cpu_info()["brand_raw"]
        self.hostname = socket.gethostname()
        self.ip = socket.gethostbyname(self.hostname)
        self.username = os.getlogin()

    # to_array method to return a python array with all the variables of the constructor 
    def to_dict(self):
        return {
            "system": self.system,
            "architecture": self.architecture,
            "cpu": self.processor,
            "host_name": self.hostname,
            "ip_address": self.ip,
            "user": self.username
        }


app = Flask(__name__)


# Default home route in which the System class will be instanciated to return the python array in the html template
@app.route('/')
def index():
    system = System()
    return render_template('index.html', systemdata=system.to_dict())
