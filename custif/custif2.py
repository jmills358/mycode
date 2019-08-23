#!/usr/bin/env python3
while(True):
    message = 'Please enter a routing protocol rip ,ospf, eigrp, bgp or q to quit'
   # print('what routing Protocol are you using ?')
    print(message)
    
    connection = (input())
    if connection == "rip":
        print('The Hop count for RIP is 15.')
    elif connection == "ospf":
        print(  'the AD for OSPF is 110.')
    elif connection == "EIGRP":
        print('the maxe AD for EIGRP is 255.')
    elif connection == "BGP":
        print( 'BGP AD uses Path Vector.')
    elif connection == "q":
        break

    else:
       print (message)# =  'Please enter  a routing protocol.'
   

