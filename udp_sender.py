import socket
import time
import struct

UDP_IP = "10.187.41.1"   
UDP_PORT = 4443
ACK_PORT = 3001

# Sockets
send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ack_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ack_sock.bind(("0.0.0.0", ACK_PORT))
ack_sock.settimeout(0.2)  # 2ms

# Load telemetry data
with open("telemetry.csv") as f:
    next(f)  # skip header
    rows = f.readlines()

seq = 0

for line in rows:
    data = line.strip().encode()

    packet = struct.pack("!IB", seq, 0) + data

    send_sock.sendto(packet, (UDP_IP, UDP_PORT))

    try:
        ack, _ = ack_sock.recvfrom(1024)
        ack_seq, ack_type = struct.unpack("!IB", ack[:5])

        # Print ACK received
        print(f"[ACK RECEIVED] seq={ack_seq}, type={ack_type}")
        print(seq)
        if ack_type != 1 or ack_seq != seq:
            print("[WRONG ACK] Resending...")
            send_sock.sendto(packet, (UDP_IP, UDP_PORT))

    except socket.timeout:
        print(f"[TIMEOUT] No ACK for seq={seq}, resending...")
        send_sock.sendto(packet, (UDP_IP, UDP_PORT))

    seq += 1
    time.sleep(0.01)
