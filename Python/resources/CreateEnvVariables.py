import os
enviroment = "Development" 

if enviroment == "Production":
	os.environ["SECRET_KEY"] = '_a6pi7$y68=x3sizhs_j@r(*03gq9g+#*-&7et($ya3cz7o%5_'
	os.environ["DEBUG"] = "False"
	os.environ["ALLOWED_HOSTS"] = ''
elif enviroment == "Testing":
	os.environ["SECRET_KEY"] = '_a6pi7$y68=x3sizhs_j@r(*03gq9g+#*-&7et($ya3cz7o%5_'
	os.environ["DEBUG"] = "True"
	os.environ["ALLOWED_HOSTS"] = '*'
else:
	os.environ["SECRET_KEY"] = '_a6pi7$y68=x3sizhs_j@r(*03gq9g+#*-&7et($ya3cz7o%5_'
	os.environ["DEBUG"] = "True"
	os.environ["ALLOWED_HOSTS"] = '*'
print ("Setting up "+enviroment+" env variables")