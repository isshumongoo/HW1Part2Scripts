# Constants
PACKET_SIZE = 800  # bytes
BUFFER_SIZE = 40 * 10**6  # 64 megabytes in bytes
FIRST_LINK_RATE = 110 * 10**6  # 180 Mbps in bps
SECOND_LINK_RATE = 90 * 10**6  # 130 Mbps in bps

# Calculate packets that fit in buffer
packets_in_buffer = BUFFER_SIZE / PACKET_SIZE
print(f"Packets that fit in buffer: {packets_in_buffer}")

# Calculate rate difference
rate_difference = FIRST_LINK_RATE - SECOND_LINK_RATE
print(f"Rate difference: {rate_difference / 10**6} Mbps")

# Calculate accumulation rate
accumulation_rate = rate_difference / 8  # Convert bits to bytes
print(f"Accumulation rate: {accumulation_rate / 10**6:.2f} MB/s")

# Calculate time to overflow
time_to_overflow = BUFFER_SIZE / accumulation_rate
print(f"Time to overflow: {time_to_overflow:.2f} seconds")

# Calculate packets sent before overflow
packets_sent = (FIRST_LINK_RATE * time_to_overflow) / (PACKET_SIZE * 8)
print(f"Packets sent before overflow: {int(packets_sent)}")

# The first packet to be lost is the next one after the buffer is full
first_lost_packet = int(packets_sent) - 1
print(f"First packet to be lost: {first_lost_packet}")