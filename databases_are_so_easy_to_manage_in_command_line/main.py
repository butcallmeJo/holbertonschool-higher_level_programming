import sys

if len(sys.argv) < 2:
	print "Please enter an action"

action_list = ["create", "print", "insert", "delete"]

if len(sys.argv) > 1 and sys.argv[1] not in action_list:
	print "Undefined action " + str(sys.argv[1])
else:
	print sys.argv[1]
