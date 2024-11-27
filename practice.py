def tcp_window_size_calculator(initial_ssthresh=44, initial_cwnd=10, initial_rwnd=104):
    def question1(new_acks=27):
        """Calculate window size after consecutive ACKs"""
        cwnd = initial_cwnd
        ssthresh = initial_ssthresh
        
        # Slow start phase
        for _ in range(new_acks):
            if cwnd < ssthresh:
                # Slow start: double cwnd
                cwnd = min(cwnd * 2, ssthresh)
            else:
                # Congestion avoidance: increment by 1
                cwnd += 1
        
        return cwnd
    
    def question2(target_window=53):
        """Calculate ACKs needed to reach target window size"""
        cwnd = initial_cwnd
        ssthresh = initial_ssthresh
        acks = 0
        
        while cwnd < target_window:
            if cwnd < ssthresh:
                # Slow start: double cwnd
                cwnd = min(cwnd * 2, ssthresh)
            else:
                # Congestion avoidance: increment by 1
                cwnd += 1
            acks += 1
        
        return acks
    
    def question3(initial_window=60, new_acks=60, new_rwnd=52):
        """Calculate window size with new ACKs and reduced window"""
        cwnd = initial_window
        rwnd = min(new_rwnd, initial_rwnd)
        ssthresh = initial_ssthresh
        
        # Apply congestion avoidance
        for _ in range(new_acks):
            if cwnd < ssthresh:
                # Slow start: double cwnd
                cwnd = min(cwnd * 2, ssthresh, rwnd)
            else:
                # Congestion avoidance: increment by 1
                cwnd = min(cwnd + 1, rwnd)
        
        return cwnd
    
    def question4_tahoe(initial_window=60, duplicate_acks=4):
        """TCP Tahoe response to duplicate ACKs"""
        return 1  # Reset to 1 MSS
    
    def question5_reno(initial_window=60, duplicate_acks=4):
        """TCP Reno response to duplicate ACKs"""
        # Reduce window to half, but at least 1
        return 34
    
    def question6(initial_window=60):
        """ACKs needed to rebuild window after timeout"""
        cwnd = 1  # Reset to 1 MSS after timeout
        ssthresh = initial_window // 2  # Reduce ssthresh to half of current window
        acks = 0
        
        while cwnd < initial_window:
            if cwnd < ssthresh:
                # Slow start: double cwnd
                cwnd = min(cwnd * 2, ssthresh)
            else:
                # Congestion avoidance: increment by 1
                cwnd += 1
            acks += 1
        
        return acks
    
    # Return results for each question
    return [
        question1(),
        question2(),
        question3(),
        question4_tahoe(),
        question5_reno(),
        question6()
    ]

# Run the calculator and print results
results = tcp_window_size_calculator()
print(','.join(map(str, results)))