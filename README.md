# ICMP Covert Communication Tool

This project consists of two Python scripts that enable covert communication using ICMP packets. The scripts allow users to send and receive hidden messages within ICMP Echo Request packets.

## Scripts

1. `icmp_receiver.py`: Listens for incoming ICMP packets and extracts hidden messages.
2. `icmp_sender.py`: Sends custom ICMP packets with hidden messages to a specified IP address.

## Features

- Covert communication using ICMP packets
- Colorful console interface using colorama
- Real-time message display for the receiver
- Simple chat-like interface for the sender

## Requirements

- Python 3.6+
- scapy
- colorama

## Installation

1. Clone this repository:
   git clone https://github.com/yourusername/icmp-covert-communication.git
   cd icmp-covert-communication

2. Install the required packages:
   pip install scapy colorama

## Usage

### Receiver (icmp_receiver.py)

1. Run the script with administrator/root privileges:
   sudo python icmp_receiver.py

2. Enter the IP address of the sender when prompted.

3. The script will start monitoring for incoming ICMP messages.

4. Type 'quit' and press Enter to stop the receiver.

### Sender (icmp_sender.py)

1. Run the script:
   python icmp_sender.py

2. Enter the destination IP address when prompted.

3. Type your messages (max 16 characters) and press Enter to send.

4. Type 'back' to return to the main menu or 'exit' to quit the program.

## Security Considerations

This tool is for educational purposes only. Be aware that:

- ICMP traffic may be blocked or monitored by firewalls and intrusion detection systems.
- The messages are not encrypted and can be read if intercepted.
- Excessive use of this tool may be detected as suspicious network activity.

## Disclaimer

Use this tool responsibly and only on networks and systems you have permission to test. The authors are not responsible for any misuse or damage caused by this tool.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
