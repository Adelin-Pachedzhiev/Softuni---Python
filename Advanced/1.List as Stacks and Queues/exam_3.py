from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(bullet) for bullet in input().split(' ')]
locks_list = [int(lock) for lock in input().split(' ')]
intelligence = int(input())
bullets_shot = 0

shots_remaining = gun_barrel_size

locks_que = deque()

for lock in locks_list:
    locks_que.appendleft(lock)

while len(locks_que):

    if len(bullets):
        lock_value = locks_que.pop()
        bullet_value = bullets.pop()
        bullets_shot += 1
        shots_remaining -= 1

        if bullet_value <= lock_value:
            print("Bang!")
        else:
            print("Ping!")
            locks_que.append(lock_value)

        if shots_remaining == 0 and len(bullets):
            print("Reloading!")
            if len(bullets) > gun_barrel_size:
                shots_remaining = gun_barrel_size
            else:
                shots_remaining = len(bullets)

    else:
        break

if len(locks_que):
    print(f"Couldn't get through. Locks left: {len(locks_que)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${intelligence - (bullets_shot * bullet_price)}")
