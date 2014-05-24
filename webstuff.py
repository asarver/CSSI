# webstuff

import httplib

conn = httplib.HTTPConnection("localhost:8080")
conn.request("GET", "/")
resp = conn.getresponse()
print resp.status, resp.reason
data = resp.read()
conn.close()
