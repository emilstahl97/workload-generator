import os
import sys
import scapy.all as scapy
import json

def generate_packet(source_ip, dest_ip, size_mb):
    # Create an IP packet with payload based on size_mb
    packet = scapy.IP(src=source_ip, dst=dest_ip) / scapy.Raw(load='A' * int(size_mb * 1024 * 1024))
    return packet

def generate_coflow_packets(coflow):
    for flow in coflow["flows"]:
        source_id = int(flow["source_id"])
        dest_id = int(flow["dest_id"])
        size_mb = float(flow["size_mb"])
        
        source_ip = f"192.168.1.{source_id}"
        dest_ip = f"192.168.1.{dest_id}"
        
        packet = generate_packet(source_ip, dest_ip, size_mb)
        yield packet

def generate_trace_from_json(json_file, chunk_size=10):
    with open(json_file, 'r') as f:
        data = json.load(f)

    trace_packets = []
    for coflow in data["coflows"]:
        trace_packets.extend(generate_coflow_packets(coflow))

    for i in range(0, len(trace_packets), chunk_size):
        yield trace_packets[i:i+chunk_size]

def save_trace_to_pcap(trace_packets, pcap_file):
    for i, chunk in enumerate(trace_packets):
        pcap_file_chunked = f"{pcap_file}_chunk_{i}.pcap"
        scapy.wrpcap(pcap_file_chunked, chunk)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    # Get the file path from the command line argument
    json_file = sys.argv[1]
    base_name = os.path.splitext(os.path.basename(json_file))[0]
    pcap_file = f"{base_name}.pcap"
    chunk_size = 10

    trace_packets = generate_trace_from_json(json_file, chunk_size=chunk_size)
    save_trace_to_pcap(trace_packets, pcap_file)
