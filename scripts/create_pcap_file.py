import scapy.all as scapy
import ijson
import sys
import os

def generate_packet(source_ip, dest_ip, size_mb):
    # Create an IP packet with payload based on size_mb
    packet = scapy.IP(src=source_ip, dst=dest_ip) / scapy.Raw(load='A' * int(size_mb))
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

def generate_trace_from_json(json_file):
    with open(json_file, 'r') as f:
        json_parser = ijson.items(f, 'coflows.item')

        trace_packets = []
        for coflow in json_parser:
            print(f"Generating packets for coflow {coflow['coflow_id']}")
            trace_packets.extend(generate_coflow_packets(coflow))

            # Adjust the condition based on your needs
            if len(trace_packets) > 1000:
                yield trace_packets
                trace_packets = []

        yield trace_packets

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
    pcap_file = base_name

    pcap_dir = os.path.expanduser("~/workload-generator/pcap_traces")
    if not os.path.exists(pcap_dir):
        os.makedirs(pcaps_dir)

    # create full file path
    pcap_file_path = os.path.join(pcap_dir, base_name)

    trace_packets = generate_trace_from_json(json_file)
    save_trace_to_pcap(trace_packets, pcap_file_path)
