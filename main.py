myWebsite = {"myWebsiteName":None, "url": None, "description": None, "rating": None }
for myWebsiteName in myWebsite.keys():
  myWebsite[myWebsiteName]= input(f"{myWebsiteName}:")
print()
for mywebsiteName,value in myWebsite.items():
  print(f"{myWebsiteName} : {value}")







