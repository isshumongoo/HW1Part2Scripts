# Parameters
RTT = 60  # milliseconds
timeout = 70  # milliseconds
window_size = 4
first_seq = 36
total_packets = 9

# Lost packets for sender and receiver
lost_sender = {3,6,8}
lost_receiver = {1,2}

# Initialize variables
time = 0
seq_num = first_seq
sender_window = []
receiver_ack = []
sender_output = []
receiver_output = []
acks_received = set()

# Function to simulate sender sending packets
def send_packets():
    global time, seq_num
    current_window = []
    for _ in range(window_size):
        if seq_num - first_seq + 1 > total_packets:
            break
        current_window.append(seq_num)
        seq_num += 1
    return current_window

# Function to simulate receiver sending acknowledgements
def receive_acks(sent_packets):
    global time
    ack_window = []
    for packet in sent_packets:
        if packet - first_seq + 1 in lost_receiver:
            ack_window.append(max(acks_received) if acks_received else first_seq - 1)
        else:
            ack_window.append(packet)
            acks_received.add(packet)
    return ack_window

# Simulate transmission
while len(sender_output) < total_packets:
    sender_window = send_packets()
    sender_output.extend(sender_window)
    
    # Check if packets are lost at the sender side
    sender_window = [p for p in sender_window if p - first_seq + 1 not in lost_sender]
    
    # After RTT, simulate receiver acknowledging
    time += RTT
    receiver_ack = receive_acks(sender_window)
    receiver_output.extend(receiver_ack)
    
    # Check if all packets have been sent and acknowledged
    if len(sender_output) >= total_packets:
        break
    
    # Timeout handling
    if time >= timeout:
        seq_num = min(sender_window)  # Go back to the first unacknowledged packet
        time = 0  # Reset time for new round of packet sending

# Display results
print(f"Sender: {','.join(map(str, sender_output))};Receiver: {','.join(map(str, receiver_output))}")
