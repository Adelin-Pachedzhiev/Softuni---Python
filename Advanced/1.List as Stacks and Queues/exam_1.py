from collections import deque


def find_free_robot(robots, time):
    for robot_info in robots:
        if not robot_info.is_busy(time):
            robot_info.give_job(time)
            return robot_info
    return None


class Time:
    def __init__(self, h, m, s):
        self.hours = h
        self.minutes = m
        self.seconds = s

    def add_time(self, seconds_added):
        time_in_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds
        time_in_seconds += seconds_added

        if time_in_seconds >= 86400:
            time_in_seconds -= 86400

        self.minutes, self.seconds = divmod(time_in_seconds, 60)
        self.hours, self.minutes = divmod(self.minutes, 60)

    def get_in_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def to_string(self):
        return f'{"0" if self.hours < 10 else ""}{self.hours}:{"0" if self.minutes < 10 else ""}{self.minutes}:' \
               f'{"0" if self.seconds < 10 else ""}{self.seconds}'


class Robot:
    def __init__(self, name, processing_time, current_time):
        self.name = name
        self.processing_time = processing_time
        self.end_of_work = Time(current_time.hours, current_time.minutes, current_time.seconds)

    def is_busy(self, current_time):
        return self.end_of_work.get_in_seconds() > current_time.get_in_seconds()

    def give_job(self, current_time):
        self.end_of_work = Time(current_time.hours, current_time.minutes, current_time.seconds)
        self.end_of_work.add_time(self.processing_time)


robots_info = input().split(';')
robots = []
products_queue = deque()

time_raw = input().split(':')
time = Time(int(time_raw[0]), int(time_raw[1]), int(time_raw[2]))

for robot in robots_info:
    robot_name, robot_process_time = robot.split('-')
    new_robot = Robot(robot_name, int(robot_process_time), time)
    robots.append(new_robot)

while True:
    command = input()
    if command == "End":
        break

    product = command

    products_queue.appendleft(product)

while len(products_queue):
    product = products_queue.pop()
    time.add_time(1)

    robot_found = find_free_robot(robots, time)
    if robot_found is not None:
        print(f'{robot_found.name} - {product} [{time.to_string()}]')
        continue

    products_queue.appendleft(product)
