'''
Here is an example problem:
A NAT router has two IP addresses: 192.128.97.1 and 29.138.101.6. 
To assign ports to the datagrams going toward the Internet from inside the network, the formula (x + 33209) mod 65536 is used, 
where x is the original port number. A TCP segment with the source IP 192.128.97.183, destination IP 112.38.227.8, source port 17989 and destination port 49778 is received and forwarded by the router. 
When the acknowledgement segment arrives at the router, what will be its source IP, destination IP, source port and destination port?

'''


IP_Address_1 = "192.128.135.1"
IP_Address_2 = "77.49.224.11"

plus_x_value = 39849
mod_value = 65536

TCP_Source_IP = "192.128.135.219"
TCP_Dest_IP = "140.178.170.32"
TCP_Source_Port = 10169
TCP_Dest_Port = 52924

# This is for sending the TCP Segment
Source_IP = IP_Address_2
Destination_IP = TCP_Dest_IP
Source_Port = (TCP_Source_Port + plus_x_value) % mod_value
Destination_Port = TCP_Dest_Port

#But answer for the acknowledgement is swapped b/w Source IP and Destination IP and b/w Source Port and Destination Port
Source_IP, Destination_IP, Source_Port, Destination_Port = Destination_IP, Source_IP, Destination_Port, Source_Port
print(Source_IP, Destination_IP, Source_Port, Destination_Port)