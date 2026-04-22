
def tunnelRequest(idx):
    tunnelId=(idx%6)
    tunnel=f"T{tunnelId}"
    return tunnel

print(tunnelRequest(12))