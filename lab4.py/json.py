import json

with open("data.json") as f:
    data = json.load(f)

print("Interface Status")
print("="*79)
print(f"{'DN':<50} {'Description':<20} {'Speed':<6} {'MTU':<6}")
print("-"*50, "-"*20, "-"*6, "-"*6)

for intf in data['imdata']:
    attrs = intf['l1PhysIf']['attributes']
    dn = attrs['dn']
    descr = attrs.get('descr', '')
    speed = attrs.get('speed', '')
    mtu = attrs.get('mtu', '')
    print(f"{dn:<50} {descr:<20} {speed:<6} {mtu:<6}")


