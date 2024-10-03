import math

def calculate_delays(packet_size, link1_rate, link2_rate, link1_length, link2_length, prop_speed, processing_time):
    # Convert rates to bps
    link1_rate *= 1e6
    link2_rate *= 1e6
    
    # Calculate delays
    transmission_delay1 = (packet_size * 8) / link1_rate * 1e6  # in microseconds
    transmission_delay2 = (packet_size * 8) / link2_rate * 1e6  # in microseconds
    propagation_delay1 = (link1_length * 1000) / prop_speed * 1e6  # in microseconds
    propagation_delay2 = (link2_length * 1000) / prop_speed * 1e6  # in microseconds
    processing_delay = (packet_size / 1000) * processing_time  # in microseconds

    # Calculate total delays
    delay_to_router = transmission_delay1 + propagation_delay1 + processing_delay
    end_to_end_delay = delay_to_router + transmission_delay2 + propagation_delay2

    # Calculate delays for multiple packets
    results = [
        round(delay_to_router, 1),
        round(end_to_end_delay, 1),
        round(end_to_end_delay + transmission_delay1, 1),
        round(end_to_end_delay + 2 * transmission_delay1, 1),
        round(end_to_end_delay + 99 * transmission_delay1, 1)
    ]

    return results

# Problem parameters
packet_size = 900  # bytes
link1_rate = 140  # Mbps
link2_rate = 90   # Mbps
link1_length = 2000  # km
link2_length = 1900  # km
prop_speed = 2e8  # m/s
processing_time = 5  # microseconds per kilobyte

results = calculate_delays(packet_size, link1_rate, link2_rate, link1_length, link2_length, prop_speed, processing_time)

print(f"Results: {','.join(map(str, results))}")