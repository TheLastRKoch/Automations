import os
import webbrowser

Continue = True

while Continue:
	os.system("cls")
	print ("Welcome to the GBS Ideas Collector Search Engine")
	IdeaID = input ("Please type the idea ID: \n")
	URL = "https://bat.sharepoint.com/sites/GBSIdeasCollector/Lists/Ideas%20Collector%20IHub%20List/AllItems.aspx?FilterField1=ID&FilterValue1="+IdeaID+"&FilterType1=Counter&sortField=ID&isAscending=false&viewid=d7068689%2D98a4%2D4e8c%2Db3d1%2D4d660c3856d8"
	#HTTP open page 
	webbrowser.open(URL, new=2)
	print("Opening...."+IdeaID)
	Result = input("Do it again? (y/n)")
	if Result == "n":
		Continue = False
		print("Good bye.....")
		os.system("cls")


