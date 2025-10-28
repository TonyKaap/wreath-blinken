import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# scan for wifi networks
import wifi
networks = []
for network in wifi.radio.start_scanning_networks():
    networks.append(network)
wifi.radio.stop_scanning_networks()
networks = sorted(networks, key=lambda net: net.rssi, reverse=True)
for network in networks:
    print("ssid:",network.ssid, "rssi:",network.rssi)

# Wait for connect or fail
import os, wifi
print("connecting...")
print("connecting...")
wifi.radio.connect(ssid=os.getenv('CIRCUITPY_WIFI_SSID'),
                   password=os.getenv('CIRCUITPY_WIFI_PASSWORD'))
print("my IP addr:", wifi.radio.ipv4_address)

# code.py
import os, wifi
print("connecting...")
wifi.radio.connect(ssid=os.getenv('CIRCUITPY_WIFI_SSID'),
                   password=os.getenv('CIRCUITPY_WIFI_PASSWORD'))
print("my IP addr:", wifi.radio.ipv4_address)

# Just blink and print
counter = 0
print_count_limit=5
while True:
    counter += 1
    if counter % print_count_limit == 0:
        print("Hello World - fast blinks")
        for i in range(5):
            led.value = True
            time.sleep(0.1)
            led.value = False
            time.sleep(0.1)
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
