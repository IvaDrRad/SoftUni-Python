# влиза в безкраен цикъл
from collections import deque

price_per_bullet = int(input())
size_of_gun_barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence = int(input())
not_enough_bullets = False
total_bullets = 0

while bullets or locks:
    total_bullets += 1
    to_shoot = bullets[-1]
    current_lock = locks[0]
    if total_bullets % size_of_gun_barrel == 0 and len(bullets) == 0:
        not_enough_bullets = True
        break
    else:
        if to_shoot <= current_lock:
            bullets.pop()
            print('Bang!')
            locks.popleft()
        else:
            bullets.pop()
            print('Ping!')
        if total_bullets % size_of_gun_barrel == 0 and len(bullets) >= 1:
            print('Reloading!')
        if len(locks) == 0:
            break
    if len(bullets) < 1 or len(locks) < 1:
        break

if not_enough_bullets or len(locks) > 0:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    money_earned = intelligence - total_bullets * price_per_bullet
    print(f'{len(bullets)} bullets left. Earned ${money_earned}')



