net_data = {
    "device_name": "mydevice",
    "device_type": "cisco_ios",
    "interfaces": [
        {"GigabitEthernet0/0": {"ip": "10.10.10.1", "subnet": "255.255.255.0"}},
        {"GigabitEthernet0/1": {"ip": "10.10.20.1", "subnet": "255.255.255.0"}},
        {"GigabitEthernet0/2": {"ip": "10.10.30.1", "subnet": "255.255.255.0"}},
    ],
}

ip_addr = net_data["interfaces"][0]["GigabitEthernet0/0"]["ip"]
subnet_mask = net_data["interfaces"][0]["GigabitEthernet0/0"]["subnet"]

ios_command = f"ip address {ip_addr} {subnet_mask}"

print(ios_command)
