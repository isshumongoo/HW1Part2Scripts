
Bandwidth = 1.4 * 10 ** 9
Propogation_Speed = 2 * 10 ** 8
Packet_Size = 1000 * 8
Window_Size = 600
Channel_Utilization = 50 * 0.01 #Percentage

Time_to_send_Packet = Packet_Size / Bandwidth

Min_RTT = ((Window_Size * Time_to_send_Packet) / Channel_Utilization) - Time_to_send_Packet

Min_Length = Min_RTT * Propogation_Speed / 2
Min_Length /= 1000 #To Km
print(Min_Length )