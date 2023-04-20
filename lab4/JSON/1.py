import json 

my_json = open(r"C:\Users\user\PycharmProjects\week 3\week 3\function2\lab4\JSON\sample-data.json")


print('Interface Status')
print('================================================================================')
print('DN                                                 Description           Speed    MTU')
print('-------------------------------------------------- --------------------  ------  ------')

data = json.load(my_json)
for eren in data["imdata"]:
    if ('33' in eren["l1PhysIf"]["attributes"]["dn"]) or ('34' in eren["l1PhysIf"]["attributes"]["dn"]) or ('35' in eren["l1PhysIf"]["attributes"]["dn"]):
        print(eren["l1PhysIf"]["attributes"]["dn"] + "                              " + eren["l1PhysIf"]["attributes"]["fecMode"] + "   " + eren["l1PhysIf"]["attributes"]["mtu"])
