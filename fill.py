import requests
url="https://docs.google.com/forms/d/e/1FAIpQLSfxsg59ggPdonbOLakPTwn_qQk-P0euw531kGt2pdDxSlnB9Q/formResponse"
for i in range(100):	
	data={"entry.1156409":"Aniket Kumar",
				"entry.210055283":190134,
				"entry.192452008":"Yes",
				"entry.446099277":"https://github.com/aniketkar1/autofill100"}
	result=requests.post(url,data=data)
	print (result)