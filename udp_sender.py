import socket
import time
import struct

UDP_IP = "127.0.0.1"   # LOCALHOST (same laptop)
UDP_PORT = 5005
ACK_PORT = 5006

# Sockets
send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ack_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ack_sock.bind(("0.0.0.0", ACK_PORT))
ack_sock.settimeout(0.002)  # 2ms

# Load telemetry data
with open("cleaned_telemetry.csvz") as f:
    next(f)  # skip header
    rows = f.readlines()

seq = 0

for line in rows:
    data = line.strip().encode()

    packet = struct.pack("!IB", seq, 0) + data

    # Send packet
    send_sock.sendto(packet, (UDP_IP, UDP_PORT))

    # Wait for ACK
    try:
        ack, _ = ack_sock.recvfrom(1024)
        ack_seq, ack_type = struct.unpack("!IB", ack[:5])

        if ack_type != 1 or ack_seq != seq:
            # Wrong ACK? → resend
            send_sock.sendto(packet, (UDP_IP, UDP_PORT))

    except:
        # Timeout → resend
        send_sock.sendto(packet, (UDP_IP, UDP_PORT))

    seq += 1
    time.sleep(0.001)  # 1ms pacing
