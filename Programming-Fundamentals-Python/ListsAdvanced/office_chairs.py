number_of_rooms = int(input())
free_chairs = 0
there_are_free_chairs = True

for room in range(1, number_of_rooms + 1):
    chair_info = input().split()
    chairs, people = chair_info
    difference = abs(len(chairs) - int(people))
    if len(chairs) < int(people):
        there_are_free_chairs = False
        print(f'{difference} more chairs needed in room {room}')
        free_chairs = 0
    elif len(chairs) >= int(people):
        free_chairs += difference

if there_are_free_chairs:
    print(f'Game On, {free_chairs} free chairs left')




