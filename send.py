from scapy.all import IP, ICMP, Raw, send
import time
import os
from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = f"""
    {Fore.GREEN}
    ╔══════════════════════════════════════════╗
    ║  _____  _____ __  __ _____    _____ _    ║
    ║ |_   _|/ ____|  \/  |  __ \  / ____| |   ║
    ║   | | | |    | \  / | |__) || |    | |   ║
    ║   | | | |    | |\/| |  ___/ | |    | |   ║
    ║  _| |_| |____| |  | | |     | |____| |__ ║
    ║ |_____|\\_____|_|  |_|_|      \_____|____|║
    ║                                          ║
    ║        {Fore.CYAN}Covert Communication Tool{Fore.GREEN}         ║
    ╚══════════════════════════════════════════╝
    """
    print(banner)

def send_custom_ping(destination, message):
    if len(message) > 16:
        print(f"{Fore.RED}Error: Message must be 16 characters or less.")
        return

    padded_message = message.ljust(16)
    packet = IP(dst=destination) / ICMP() / Raw(load=padded_message)

    print(f"\n{Fore.YELLOW}Sending ping to {Fore.CYAN}{destination}{Fore.YELLOW}...")
    send(packet, verbose=False)
    print(f"{Fore.GREEN}Ping sent successfully!")
    print(f"{Fore.YELLOW}Message: {Fore.CYAN}{padded_message}")

def chat_with_ip(destination):
    print(f"\n{Fore.CYAN}Chatting with {destination}")
    print(f"{Fore.CYAN}Enter messages (max 16 chars). Type 'back' to return to main menu.")
    
    while True:
        message = input(f"{Fore.YELLOW}Message {Fore.GREEN}➜ {Fore.CYAN}")
        
        if message.lower() == 'back':
            break
        
        send_custom_ping(destination, message)

def main():
    while True:
        clear_screen()
        print_banner()

        destination = input(f"\n{Fore.YELLOW}Enter destination IP (or 'exit' to quit) {Fore.GREEN}➜ {Fore.CYAN}")
        
        if destination.lower() == 'exit':
            break
        
        chat_with_ip(destination)

    print(f"\n{Fore.GREEN}Exiting ICMP Chat. Stay stealthy!")
    time.sleep(2)

if __name__ == "__main__":
    main()
