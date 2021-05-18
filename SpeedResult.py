import speedtest

from utils import *


class SpeedResult:
    def __init__(self):
        self.upload = 0.0
        self.download = 0.0
        self.ping = 0.0
        self.Server = Server()

    def getSpeed(self):
        st = speedtest.Speedtest()
        closest_servers = st.get_closest_servers()

        self.Server.filterDict(closest_servers[1])
        self.download = toMegaBytes(st.download())
        self.upload = toMegaBytes(st.upload())
        self.ping = formatIntoTwoDigits(st.results.ping)


class Server:
    def __init__(self):
        self.Location = ""
        self.Name = ""
        self.url = ""

    def filterDict(self, dic):
        self.Location = dic.get("name")
        self.Name = dic.get("sponsor")
        self.url = dic.get("url")
