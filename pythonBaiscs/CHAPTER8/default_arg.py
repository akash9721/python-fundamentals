def webInfo(url,port=80,timeout=120):
    print(f"website info is : url {url} port {port} timeout {timeout}sec")

webInfo("www.google.com")
webInfo("www.google.com",443)
webInfo("www.google.com",21,600)