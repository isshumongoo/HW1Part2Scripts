import time

class DNSSimulator:
    def __init__(self, cache_duration, one_way_time):
        self.cache_duration = cache_duration
        self.cache = {}
        self.one_way_time = one_way_time

    def resolve(self, domain, start_time):
        if domain in self.cache and time.time() - self.cache[domain] < self.cache_duration:
            return start_time + 2 * self.one_way_time, None, None, None
        
        current_time = start_time + self.one_way_time  # Local host to local DNS
        
        # Local DNS to root server and back
        current_time += 2 * self.one_way_time
        root_response_time = current_time
        
        # Local DNS to TLD server and back
        current_time += 2 * self.one_way_time
        tld_response_time = current_time
        
        # Local DNS to authoritative server and back
        current_time += 2 * self.one_way_time
        auth_response_time = current_time
        
        # Local DNS back to local host
        current_time += self.one_way_time
        
        self.cache[domain] = time.time()
        
        return current_time, root_response_time, tld_response_time, auth_response_time

def main(cache_duration, one_way_time, query_times):
    simulator = DNSSimulator(cache_duration, one_way_time)
    domain = "web.cs.umass.edu"
    results = []
    
    for start_time in query_times:
        end_time, root_time, tld_time, auth_time = simulator.resolve(domain, start_time)
        
        if root_time is not None:
            results.append(f"{start_time + one_way_time},{root_time},{tld_time},{auth_time},{end_time}")
        else:
            results.append(f"{end_time}")
    
    print(",".join(results))

if __name__ == "__main__":
    # These values can be changed as needed
    cache_duration = 60
    one_way_time = 3
    query_times = [0, 60032, 120029]
    
    main(cache_duration, one_way_time, query_times)