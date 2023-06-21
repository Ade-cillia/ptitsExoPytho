LogIps = [
  ("10.255.14.6","255.255.255.0"),
  ("10.255.19.9","255.255.0.0"),
  ("10.255.14.10","255.255.255.0")
]

LogIps.sort(key=lambda a: a[0])
print(LogIps)


def IpIn(listIps,searchIp):
  areIn = False
  for logIp, logMask in listIps:
    if checkNetwork(searchIp,logIp,logMask) : areIn = True
  return areIn

def checkNetwork(searchIp,logIp,logMask):
  searchIpSp = searchIp.split(".")
  logIpSp = logIp.split(".")
  logMaskSp = logMask.split(".")
  for i in range(4):
    if int(searchIpSp[i]) & int(logMaskSp[i]) != int(logIpSp[i]) & int(logMaskSp[i]):
      return False
  return True


print(IpIn(LogIps,"10.254.4.7"))
