#!/usr/bin/env python3
while(True):
    message = 'Please enter a routing protocol'
    print('what routing Protocol are you using ?')
    connection = (input())
    if connection == "rip":
        message2 =  'The Hop count for RIP is 15.'
    elif connection == "ospf":
        message2 =  'the AD for OSPF is 110.'
    elif connection == "EIGRP":
        message2 =  'the maxe AD for EIGRP is 255.'
    elif connection == "BGP":
        message2 =  'BGP AD uses Path Vector.'
    elif connection == "q":
        break

    else:
        message2 =  'Please enter  a routing protocol.'
    print(message2)

