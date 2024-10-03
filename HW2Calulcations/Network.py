class InstitutionalNetworkResponseTimeSolution:
    def __init__(self, network_bandwidth: float, access_link_bandwidth: float, web_object_size: float, average_request_rate: float, response_time: float, cache_percentage: float, invalid_cache_percentage: float):
        self.network_bandwidth = network_bandwidth
        self.access_link_bandwidth = access_link_bandwidth
        self.web_object_size = web_object_size
        self.average_request_rate = average_request_rate
        self.response_time = response_time
        self.cache_percentage = cache_percentage
        self.invalid_cache_percentage = invalid_cache_percentage

        # Delta: time to send an object over the access link in seconds
        self.delta = self.web_object_size / self.access_link_bandwidth

        self.access_delay = self.delta / \
            (1 - (self.average_request_rate * self.delta))  # in seconds

        self.transmission_delay = self.web_object_size / \
            self.network_bandwidth  # in seconds

        self.total_response_time = self.access_delay + \
            self.transmission_delay + self.response_time  # in seconds

        self.valid_cache = self.cache_percentage * \
            (1 - self.invalid_cache_percentage / 100) / 100  # convert to decimal

        self.arrival_rate = self.average_request_rate * \
            (1 - self.valid_cache)  # objects per second

        self.access_delay_with_proxy = self.delta / \
            (1 - (self.arrival_rate * self.delta))  # in seconds

        self.response_time_one = self.web_object_size / \
            self.network_bandwidth  # time for a cached object in seconds
        self.response_time_two = self.access_delay_with_proxy + self.response_time + \
            self.response_time_one  # time for a non-cached object in seconds

        self.average_response_time_with_proxy = (self.valid_cache * self.response_time_one) + (
            (1 - self.valid_cache) * self.response_time_two)  # in seconds

        self.access_delay_ms = self.access_delay * 1000  # milliseconds
        self.total_response_time_ms = self.total_response_time * 1000  # milliseconds
        self.access_delay_with_proxy_ms = self.access_delay_with_proxy * 1000  # milliseconds
        self.average_response_time_with_proxy_ms = self.average_response_time_with_proxy * \
            1000  # milliseconds

    def solve(self) -> str:
        return f"{self.access_delay_ms:.1f},{self.total_response_time_ms:.1f},{self.access_delay_with_proxy_ms:.1f},{self.average_response_time_with_proxy_ms:.1f}"

if __name__ == "__main__":
    
    network_bandwidth = 1.5 * 10 ** 9  # Gbps to bits
    access_link_bandwidth = 15 * 10 ** 6  # Mbps to bits
    web_object_size = 190 * 10 ** 3  # Kbits to bits
    average_request_rate = 45  # requests per second
    response_time = 0.5 # seconds
    cache_percentage = 40  # percentage of objects in cache
    invalid_cache_percentage = 20  # percentage of cached objects that are invalid

    response_time = InstitutionalNetworkResponseTimeSolution(network_bandwidth,
                                                             access_link_bandwidth,
                                                             web_object_size,
                                                             average_request_rate,
                                                             response_time,
                                                             cache_percentage,
                                                             invalid_cache_percentage)
    print(response_time.solve())
