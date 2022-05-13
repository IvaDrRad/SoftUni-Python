number = int(input())
registered = {}
for _ in range(number):
    command = input().split()
    if command[0] == 'register':
        name = command[1]
        plate_number = command[2]
        if name not in registered:
            registered[name] = plate_number
            print(f"{name} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_number}")
    elif command[0] == 'unregister':
        username = command[1]
        if username not in registered:
            print(f"ERROR: user {username} not found")
        else:
            del registered[username]
            print(f"{username} unregistered successfully")

for name, number in registered.items():
    print(f"{name} => {number}")