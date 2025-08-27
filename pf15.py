# pf15.py — Fully Patched Scapy for Termux (No Root Needed)
import sys
import types
# Step 1: Create fake rtnetlink module
fake_rtnetlink = types.ModuleType("scapy.arch.linux.rtnetlink")
# Step 2: Add all required dummy functions and data
def _sr1_rtrequest(*args, **kwargs):
    raise PermissionError("Blocked kernel bind in Termux")
def read_routes():
    return []
def read_routes6():
    return []
def read_interfaces():
    return {}
def in6_getifaddr():
    return []
def _get_if_list():
    return {}
# Step 3: Assign to fake module
fake_rtnetlink._sr1_rtrequest = _sr1_rtrequest
fake_rtnetlink.read_routes = read_routes
fake_rtnetlink.read_routes6 = read_routes6
fake_rtnetlink.read_interfaces = read_interfaces
fake_rtnetlink.in6_getifaddr = in6_getifaddr
fake_rtnetlink._get_if_list = _get_if_list
# Step 4: Inject into Python runtime
sys.modules["scapy.arch.linux.rtnetlink"] = fake_rtnetlink
# Step 5: Safe Scapy import
from scapy.all import IP, TCP, Raw, wrpcap
# Step 6: Create and save a simple packet
pkt = IP(dst="1.1.1.1") / TCP(dport=80) / Raw(load="GET / HTTP/1.1\r\n\r\n")
pkt.show()
wrpcap("packet.pcap", pkt)
print("✅ Packet saved to packet.pcap.")

