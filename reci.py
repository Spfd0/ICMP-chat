from scapy.all import sniff, IP, ICMP, Raw
from colorama import init, Fore, Back, Style
import os
import time
import threading
import socket

# Initialize colorama
init(autoreset=True)

# Global flag to control the sniffing loop
keep_sniffing = True

# Set to store processed packet IDs
processed_packets = set()

# The IP address you're expecting messages from
SENDER_IP = None

# Get your own IP address
MY_IP = socket.gethostbyname(socket.gethostname())

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = f"""
    {Fore.CYAN}
    ╔═══════════════════════════════════════════╗
    ║  _____  _____ __  __ _____    _____ _     ║
    ║ |_   _|/ ____|  \/  |  __ \  / ____| |    ║
    ║   | | | |    | \  / | |__) || |    | |    ║
    ║   | | | |    | |\/| |  ___/ | |    | |    ║
    ║  _| |_| |____| |  | | |     | |____| |___ ║
    ║ |_____|\\_____|_|  |_|_|      \_____|_____|║
    ║                                           ║
    ║        {Fore.GREEN}Covert Message Receiver{Fore.CYAN}            ║
    ╚═══════════════════════════════════════════╝
    """
    print(banner)

def process_packet(packet):
    global SENDER_IP
    if packet.haslayer(ICMP) and packet.haslayer(Raw):
        icmp_type = packet[ICMP].type
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        
        # Only process Echo Request (type 8) packets
        if icmp_type == 8:  # Echo Request
            # Ignore packets originating from your own IP
            if src_ip == MY_IP:
                return
            
            message = packet[Raw].load.decode('utf-8', errors='ignore').strip()
            
            # Create a unique identifier for this message
            message_id = (message, src_ip, dst_ip)
            
            # Check if we've already processed this message
            if message_id not in processed_packets:
                processed_packets.add(message_id)
                
                # Determine how to display the sender
                display_ip = SENDER_IP if src_ip == SENDER_IP else src_ip
                
                print(f"{Fore.YELLOW}[{time.strftime('%Y-%m-%d %H:%M:%S')}] {Fore.GREEN}Message from {Fore.CYAN}{display_ip}{Fore.GREEN}:")
                print(f"{Fore.WHITE}{message}\n")

def sniff_packets():
    global keep_sniffing
    while keep_sniffing:
        sniff(filter="icmp", prn=process_packet, store=0, timeout=1)

def start_receiver():
    global keep_sniffing, SENDER_IP
    clear_screen()
    print_banner()
    
    SENDER_IP = input(f"{Fore.YELLOW}Enter the IP address you're chatting with: {Fore.CYAN}")
    
    print(f"\n{Fore.GREEN}Monitoring ICMP messages...")
    print(f"{Fore.YELLOW}Type 'quit' and press Enter to stop.\n")

    # Start sniffing in a separate thread
    sniff_thread = threading.Thread(target=sniff_packets)
    sniff_thread.start()

    # Main loop to check for quit command
    while True:
        command = input().strip().lower()
        if command == 'quit':
            keep_sniffing = False
            break

    print(f"\n{Fore.RED}Stopping ICMP monitor...")
    sniff_thread.join()
    print(f"{Fore.GREEN}ICMP monitor stopped. Goodbye!")

if __name__ == "__main__":
    start_receiver()
