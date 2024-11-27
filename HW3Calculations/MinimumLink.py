# Given parameters
Bandwidth = 1.1 * 10 ** 9  # Bandwidth in bits per second (bps)
Propagation_Speed = 1.7 * 10 ** 8  # Propagation speed in meters per second
Packet_Size = 1300 * 8  # Packet size in bits (1300 bytes * 8 bits/byte)
Window_Size = 800  # Window size in packets
Channel_Utilization = 50 * 0.01  # Channel utilization as a percentage

# Time to send one packet (Transmission delay)
Time_to_send_Packet = Packet_Size / Bandwidth

# Minimum round-trip time (RTT) calculation
Min_RTT = ((Window_Size * Time_to_send_Packet) / Channel_Utilization) - Time_to_send_Packet

# Minimum cable length calculation (One-way propagation delay)
Min_Length = Min_RTT * Propagation_Speed / 2  # Divide by 2 to get one-way trip time
Min_Length /= 1000  # Convert meters to kilometers

# Output the result
print(round(Min_Length, 1))  # Rounding to the nearest tenth
