#!/usr/bin/env python3
proto = ["ssh", "http","https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append('dns') #this line will add "din" th the end of  our list protoa.apped)'dns')# this line will add "dns" to the  end of the list 
print(proto)
proto2 = [22,80,443,53] # a list of common ports
proto.extend(proto2)
print(proto)
protoa.append (proto2) #pass protp2 as an argument to the append method
print(protoa)
