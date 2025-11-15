import socket
import struct

UDP_PORT = 5005
ACK_PORT = 5006

# Create receiver
recv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
recv_sock.bind(("0.0.0.0", UDP_PORT))

# Create ACK sender
ack_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Receiver ready...")

expected_seq = 0

while True:
    packet, addr = recv_sock.recvfrom(8192)

    seq, ptype = struct.unpack("!IB", packet[:5])
    data = packet[5:].decode()

    # Send ACK back immediately
    ack = struct.pack("!IB", seq, 1)
    ack_sock.sendto(ack, (addr[0], ACK_PORT))

    if seq == expected_seq:
        print(f"[OK] {seq}: {data}")
        expected_seq += 1
    else:
        print(f"[OUT-OF-ORDER] got {seq}, expected {expected_seq}")
