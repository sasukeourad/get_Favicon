import mmh3, sys, requests, codecs
#import requests
#import codecs

if len(sys.argv) != 2:
   print("[*] usage: python3 %s <favicon url>" % sys.argv[0]) 
   sys.exit(-1)
       
url = sys.argv[1] 
response = requests.get(url,verify=False)
favicon = codecs.encode(response.content,"base64")
hash = mmh3.hash(favicon)
print("[+] Favicon Hash is: %s" % hash)




