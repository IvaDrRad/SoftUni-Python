from collections import deque

petrol_pumps = int(input())
pumps = deque()

for _ in range(petrol_pumps):
    pump_info = [int(x) for x in input().split()]
    pumps.append(pump_info)

for attempt in range(petrol_pumps):
    trunk = 0
    for pump in pumps:
        petrol, distance = pump
        trunk = trunk + petrol - distance
        if trunk < 0:
            pumps.append(pumps.popleft())
            break
    else:
       print(attempt)
       break

