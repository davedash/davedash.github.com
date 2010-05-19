import urllib

f = file('_urls')

for line in f:
    url = "http://localhost:4000" + line.strip()
    call = urllib.urlopen(url)
    if call.getcode() != 200:
        print "Failure for %s: %d" % (url, call.getcode())
