import pyads

# Define AMS Net ID and IP address of the target
AMS_NET_ID = '192.168.1.1.1.1'
IP_ADDRESS = '192.168.1.1'
PORT = 851

# Connect to the PLC
plc = pyads.Connection(AMS_NET_ID, PORT, IP_ADDRESS)
plc.open()
try:
    plc.write_by_name('Main.q[0]', 3.3, pyads.PLCTYPE_REAL)
    print(plc.read_by_name('Main.q[0]', pyads.PLCTYPE_REAL))
except:
    print("ERROR: closing")
    plc.close()
