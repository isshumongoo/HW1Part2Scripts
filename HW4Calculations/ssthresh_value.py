ssthresh = 32
ad_receiver_window_size = 81
segment_size = 1
cwnd = 11
#Q1
received_in_row = 24
#Q2
Before_TCP_window_size = 37
#Q3
After_TCP_window_size = 52
New_Consecutive_ACKs = 52
last_ad_window_size = 42
#Q4 & Q5 & Q6
Duplicate_ACKs = 4

#Answer 1
congestion_window_size = cwnd + received_in_row 
print(min(ad_receiver_window_size, congestion_window_size))

#Answer 2
New_ACKs_needed = ssthresh - cwnd
n = ssthresh
while n < Before_TCP_window_size:
  New_ACKs_needed += n
  n += 1
print(New_ACKs_needed)

#Answer 3
congestion_window_size = After_TCP_window_size
n = New_Consecutive_ACKs
while n > 0:
  if (n // congestion_window_size > 0):
    congestion_window_size += 1
    n = n - congestion_window_size
placeholder = min(ad_receiver_window_size, congestion_window_size)
print(min(placeholder, last_ad_window_size))

#Answer 4 - Tahoe
Extra_ACKs = Duplicate_ACKs
if not Extra_ACKs < 3:
  congestion_window_size = 0
else:
  congestion_window_size = cwnd + Duplicate_ACKs
while not Extra_ACKs < Duplicate_ACKs:
  Extra_ACKs = Duplicate_ACKs - 3
  congestion_window_size += 1
print(min(congestion_window_size, ad_receiver_window_size))

#Answer 5 - Reno
Extra_ACKs = Duplicate_ACKs
Change_ssthresh = After_TCP_window_size
if not Extra_ACKs < 3:
  Change_ssthresh = Change_ssthresh // 2
  congestion_window_size = Change_ssthresh + 3
else:
  congestion_window_size = cwnd + Duplicate_ACKs
while not Extra_ACKs < Duplicate_ACKs:
  Extra_ACKs = Duplicate_ACKs - 3
  congestion_window_size += 1
print(min(congestion_window_size, ad_receiver_window_size))

#Answer 6
congestion_window_size = 1
Change_ssthresh = After_TCP_window_size // 2
New_ACKs_needed = Change_ssthresh - congestion_window_size
n = New_ACKs_needed + 1
if (After_TCP_window_size > ad_receiver_window_size):
  After_TCP_window_size = ad_receiver_window_size
while n < After_TCP_window_size:
  New_ACKs_needed += n
  n += 1
print(New_ACKs_needed)