import platform
import cpuinfo
import socket
import os


# System class
class System:
    #Constructor method
    def init(self):
        self.system = platform.system()
        self.architecture = platform.architecture()
        self.processor = cpuinfo.get_cpu_info()["brand_raw"]
        self.hostname = socket.gethostname()
        self.ip = socket.gethostbyname(self.hostname)
        self.username = os.getlogin()
 
    # to_array method to return a python dictionary with all the variables of the constructor
    def to_dict(self):
        return {
            "system": self.system,
            "architecture": self.architecture,
            "cpu": self.processor,
            "hostname": self.hostname,
            "ip_address": self.ip,
            "user": self.username
        }