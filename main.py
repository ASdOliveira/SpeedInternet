#example of usage
from SpeedResult import SpeedResult

speed = SpeedResult()
speed.getSpeed()

print(speed.download, speed.upload, speed.ping)
print(speed.Server.Name, speed.Server.Location, speed.Server.url)


