#!/usr/bin/env python3
#create dictonary
switch = {'hostname':'sw1', 'ip':'10.0.0.1', 'version':'1.2','vendor': 'ciscp'}
print(switch['hostname'])
print(switch['ip'])
print("First test - 'get()")
print(switch.get('lynx'))
print ("second test - .get()")
print(switch.get('lynx', " THE kEY IS IN ANOTHER CASTLE!"))
print("Third test - .get()")
print(switch.get("version"))
