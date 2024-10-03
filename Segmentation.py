import math

def calculate_transmission_time(message_size, link_speed, num_links):
    """Calculate transmission time for a message."""
    return (message_size * 8 / link_speed) * num_links

def calculate_segmented_transmission_time(message_size, num_packets, link_speed, num_links):
    """Calculate transmission time for segmented message."""
    packet_size = message_size / num_packets
    time_per_packet = (packet_size * 8) / link_speed
    return time_per_packet * num_links + time_per_packet * (num_packets - 1)

def find_minimum_header_size(message_size, num_packets, link_speed, num_links, time_without_segmentation):
    """Find minimum header size that eliminates segmentation benefit."""
    packet_size = message_size / num_packets
    x = 0
    while True:
        time_with_header = calculate_segmented_transmission_time(message_size + x * num_packets, num_packets, link_speed, num_links)
        if time_with_header > time_without_segmentation:
            return x * 8  # Convert bytes to bits
        x += 1

def calculate_average_retransmissions(message_size, error_probability):
    """Calculate average number of retransmissions."""
    success_probability = (1 - error_probability) ** (message_size * 8)
    return 1 / success_probability - 1

# Problem parameters
message_size = 3750  # bytes
link_speed = 170000  # bps
num_links = 3
num_packets = 50
error_probability = 1e-5

# 1. Time without segmentation
time_without_segmentation = calculate_transmission_time(message_size, link_speed, num_links)

# 2. Time with segmentation
time_with_segmentation = calculate_segmented_transmission_time(message_size, num_packets, link_speed, num_links)

# 3. Minimum header size
min_header_size = find_minimum_header_size(message_size, num_packets, link_speed, num_links, time_without_segmentation)

# 4. Average retransmissions without segmentation
retransmissions_without_segmentation = calculate_average_retransmissions(message_size, error_probability)

# 5. Average retransmissions with segmentation
packet_size = message_size / num_packets
retransmissions_per_packet = calculate_average_retransmissions(packet_size, error_probability)
retransmissions_with_segmentation = retransmissions_per_packet * num_packets

# Print results
print(f"{time_without_segmentation:.2f},{time_with_segmentation:.2f},{min_header_size:.2f},{retransmissions_without_segmentation:.2f},{retransmissions_with_segmentation:.2f}")