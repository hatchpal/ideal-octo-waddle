#Command Line Arguments for manage.py
# #--------------------------------------
import utils
import sys
command = sys.argv[1]
print(command)
print("This is argv:", sys.argv)

if command == "build":
	print("Build was specified")
	utils.main()
elif command == "new":
	print("New page was specified")
	open('content/new_content_page.html', 'w+').write("New Content Page Created")
else:
	print("Please specify 'build' or 'new'")

