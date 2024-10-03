#9 answer question
class InternetPathSolution:
    def __init__(self, transmission_rate: int,
                 number_of_links: int,
                 number_of_routers: int,
                 length_of_link: int,
                 signal_propagation_speed: int,
                 webpage_size: int,
                 number_of_images: int,
                 image_size: int,
                 max_pkt_size: int):
        self.transmission_rate = transmission_rate
        self.number_of_links = number_of_links
        self.number_of_routers = number_of_routers
        self.length_of_link = length_of_link
        self.signal_propagation_speed = signal_propagation_speed
        self.webpage_size = webpage_size
        self.number_of_images = number_of_images
        self.image_size = image_size
        self.max_pkt_size = max_pkt_size

        self.round_trip_time = self._calculate_round_trip_time()

    def _calculate_round_trip_time(self) -> float:
        total_length_of_links = self.number_of_links * self.length_of_link
        propagation_delay = total_length_of_links / self.signal_propagation_speed
        return propagation_delay * 2
    
    def _calculate_first_packet_arrival_time(self) -> float:
        time_for_tcp_connection = self._calculate_round_trip_time()
        time_for_request = time_for_tcp_connection / 2
        first_transmission_delay = self.max_pkt_size / self.transmission_rate
        first_propagation_delay_till_router = self.length_of_link / self.signal_propagation_speed
        return time_for_tcp_connection + time_for_request + \
            first_transmission_delay + first_propagation_delay_till_router
    

    def _calculate_first_packet_arrival_time_two_hops(self) -> float:
        time_till_one_hop_away = self._calculate_first_packet_arrival_time()
        second_transmission_delay = self.max_pkt_size / self.transmission_rate
        second_propagation_delay_till_router = self.length_of_link / self.signal_propagation_speed
        extra_time = second_propagation_delay_till_router + second_transmission_delay
        total_time_two_hops = extra_time + time_till_one_hop_away
        return total_time_two_hops
    
    def _calculate_time_http_client_receives_first_packet(self) -> float:
        time_for_tcp_connection = self.round_trip_time
        time_for_request = time_for_tcp_connection / 2
        propagation_delay = self.number_of_links * \
            (self.length_of_link / self.signal_propagation_speed)
        transmission_delay_for_first_packet = (
            self.number_of_routers + 1) * (self.max_pkt_size / self.transmission_rate)
        return time_for_tcp_connection + time_for_request + \
            propagation_delay + transmission_delay_for_first_packet
    
    def _calculate_time_to_receive_the_whole_web_page(self) -> float:
        time_for_tcp_connection = self.round_trip_time
        time_for_request = time_for_tcp_connection / 2
        propagation_delay = self.number_of_links * (self.length_of_link /
                                               self.signal_propagation_speed)

        num_packets_of_max_size = self.webpage_size // self.max_pkt_size
        transmission_delay_for_packets_of_max_size = (
            num_packets_of_max_size + self.number_of_routers) * (self.max_pkt_size / self.transmission_rate)
        num_packets_of_rem_bytes = self.webpage_size % self.max_pkt_size
        transmission_delay_for_rem_bytes = num_packets_of_rem_bytes / self.transmission_rate
        return time_for_tcp_connection + time_for_request + propagation_delay + \
            transmission_delay_for_packets_of_max_size + transmission_delay_for_rem_bytes
    
    def _calculate_time_elapses_to_receive_first_image(self) -> float:
        time_to_get_webpage = self._calculate_time_to_receive_the_whole_web_page()
        time_for_tcp_connection = self.round_trip_time
        time_for_request = time_for_tcp_connection / 2
        propagation_delay = self.number_of_links * (self.length_of_link /
                                               self.signal_propagation_speed)

        num_packets_for_images_of_max_size = self.image_size // self.max_pkt_size
        transmission_delay = (num_packets_for_images_of_max_size +
                              self.number_of_routers) * (self.max_pkt_size / self.transmission_rate)
        num_packets_of_rem_bytes = self.image_size % self.max_pkt_size
        transmission_delay_for_rem_bytes = num_packets_of_rem_bytes / self.transmission_rate
        time_to_receive_first_image = time_for_tcp_connection + time_for_request + \
            propagation_delay + transmission_delay + transmission_delay_for_rem_bytes
        return time_to_receive_first_image + time_to_get_webpage
    
    def _calculate_time_for_webpage_to_be_displayed(self) -> float:
        time_to_get_webpage = self._calculate_time_to_receive_the_whole_web_page()
        time_for_tcp_connection = self.round_trip_time
        time_for_request = time_for_tcp_connection / 2
        propagation_delay = self.number_of_links * \
            (self.length_of_link / self.signal_propagation_speed)

        number_of_pkts = self.image_size // self.max_pkt_size
        transmission_delay = (number_of_pkts + self.number_of_routers) * (
            self.max_pkt_size / self.transmission_rate)
        num_packets_of_rem_bytes = self.image_size % self.max_pkt_size
        transmission_delay_for_rem_bytes = num_packets_of_rem_bytes / self.transmission_rate
        time_to_get_all_images = (time_for_tcp_connection + time_for_request + propagation_delay +
                                  transmission_delay +
                                  transmission_delay_for_rem_bytes) * self.number_of_images
        return time_to_get_webpage + time_to_get_all_images
    
    def _calculate_time_elapsed_to_display_webpage_all_tcp_connections(self) -> float:
        time_to_get_webpage = self._calculate_time_to_receive_the_whole_web_page()
        time_for_tcp_connection = self.round_trip_time
        time_for_request = time_for_tcp_connection / 2
        propagation_delay = self.number_of_links * \
            (self.length_of_link / self.signal_propagation_speed)

        total_packets_formed_from_all_images_of_max_size = (
            self.image_size * self.number_of_images) // self.max_pkt_size
        total_transmission_delay = (total_packets_formed_from_all_images_of_max_size +
                                    self.number_of_routers) * (self.max_pkt_size / self.transmission_rate)
        packets_formed_of_less_than_max_size = (
            self.image_size * self.number_of_images) % self.max_pkt_size
        transmission_delay_for_packets_formed_of_less_than_max_size = packets_formed_of_less_than_max_size / self.transmission_rate
        time_to_receive_all_images_simultaneously = time_for_tcp_connection + time_for_request + \
            propagation_delay + total_transmission_delay + \
            transmission_delay_for_packets_formed_of_less_than_max_size
        return time_to_get_webpage + \
            time_to_receive_all_images_simultaneously
    
    def _calculate_time_to_display_entire_webpage(self) -> float:
        time_to_get_webpage = self._calculate_time_to_receive_the_whole_web_page()
        time_for_tcp_connection = self.round_trip_time
        time_for_request = time_for_tcp_connection / 2
        propagation_delay = self.number_of_links * \
            (self.length_of_link / self.signal_propagation_speed)
        total_packets_formed_from_all_images_of_max_size = (
            self.image_size * self.number_of_images) // self.max_pkt_size
        total_transmission_delay = (total_packets_formed_from_all_images_of_max_size +
                                    self.number_of_routers) * (self.max_pkt_size / self.transmission_rate)
        packets_formed_of_less_than_max_size = (
            self.image_size * self.number_of_images) % self.max_pkt_size
        transmission_delay_for_packets_formed_of_less_than_max_size = packets_formed_of_less_than_max_size / self.transmission_rate
        time_to_receive_all_images_simultaneously = time_for_request + propagation_delay + \
            total_transmission_delay + transmission_delay_for_packets_formed_of_less_than_max_size
        return time_to_get_webpage + \
            time_to_receive_all_images_simultaneously
      


    def solve(self) -> str:
        return f"{round(self._calculate_round_trip_time(), 3)},{round(self._calculate_first_packet_arrival_time(), 3)},{round(self._calculate_first_packet_arrival_time_two_hops(), 3)},{round(self._calculate_time_http_client_receives_first_packet(), 3)},{round(self._calculate_time_to_receive_the_whole_web_page(), 3)},{round(self._calculate_time_elapses_to_receive_first_image(), 3)},{round(self._calculate_time_for_webpage_to_be_displayed(), 3)},{round(self._calculate_time_elapsed_to_display_webpage_all_tcp_connections(), 3)},{round(self._calculate_time_to_display_entire_webpage(), 3)}"

