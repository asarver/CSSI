# urlstuff

import urllib

# chart api "...&chds=0,1..."

d = { "chds" : "0,1" }
encoded = urllib.urlencode(d)
