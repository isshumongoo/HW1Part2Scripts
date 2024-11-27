import math

#Enter each Subnet below in format 1.2.3.4
Subnet_IP_1 = 233
Subnet_IP_2 = 172
Subnet_IP_3 = 192
Subnet_IP_4 = 0
Subnet_Number = 18
First_Tier = 8
Second_Tier = 1

ISP_IP_Hosts = 2**(32-Subnet_Number)
First_Tier_IPs = (ISP_IP_Hosts // 2) // First_Tier
First_Tier_Hosts = First_Tier_IPs - 2
Second_Tier_IPs = (ISP_IP_Hosts // 2) // Second_Tier
Second_Tier_Hosts = Second_Tier_IPs - 2
#-2 because can't use first and second

First_Tier_Subnet_Mask = int(32 - math.log(First_Tier_IPs,2))

Update_Value = 32 - First_Tier_Subnet_Mask
IP_Column_Position = 1
while Update_Value >= 8:
  Update_Value -= 8
  IP_Column_Position += 1

print(str(Subnet_IP_1)+"."+str(Subnet_IP_2)+"."+str(Subnet_IP_3)+"."+str(Subnet_IP_4)+"/"+str(First_Tier_Subnet_Mask))

i = 2
while i <= First_Tier+1:
  if IP_Column_Position == 1:
    Subnet_IP_4 += 2**Update_Value
  elif IP_Column_Position == 2:
    Subnet_IP_3 += 2**Update_Value
  elif IP_Column_Position == 3:
    Subnet_IP_2 += 2**Update_Value
  else:
    Subnet_IP_1 += 2**Update_Value
  
  if i != First_Tier+1:
    print(str(Subnet_IP_1)+"."+str(Subnet_IP_2)+"."+str(Subnet_IP_3)+"."+str(Subnet_IP_4)+"/"+str(First_Tier_Subnet_Mask))
  i += 1

Second_Tier_Subnet_Mask = int(32 - math.log(Second_Tier_IPs,2))

Update_Value = 32 - Second_Tier_Subnet_Mask
IP_Column_Position = 1
while Update_Value >= 8:
  Update_Value -= 8
  IP_Column_Position += 1

print(str(Subnet_IP_1)+"."+str(Subnet_IP_2)+"."+str(Subnet_IP_3)+"."+str(Subnet_IP_4)+"/"+str(Second_Tier_Subnet_Mask))

i = 2
while i <= Second_Tier:
  if IP_Column_Position == 1:
    Subnet_IP_4 += 2**Update_Value
  elif IP_Column_Position == 2:
    Subnet_IP_3 += 2**Update_Value
  elif IP_Column_Position == 3:
    Subnet_IP_2 += 2**Update_Value
  else:
    Subnet_IP_1 += 2**Update_Value
  
  #TODO FIX THE FORMAT OF HOW THIS IS PRINTED
  print(str(Subnet_IP_1)+"."+str(Subnet_IP_2)+"."+str(Subnet_IP_3)+"."+str(Subnet_IP_4)+"/"+str(Second_Tier_Subnet_Mask))
  i += 1

print(First_Tier_Hosts, Second_Tier_Hosts)