from collections import deque


def read_robots():
    result = {}
    robots_input = input().split(';')
    for r_input in robots_input:
        robots_details = r_input.split('-')
        name = robots_details[0]
        processing_time = int(robots_details[1])
        result[name] = processing_time
    return result


def to_str_time(time_in_seconds):
    hours = time_in_seconds // 3600
    minutes = (time_in_seconds % 3600) // 60
    seconds = (time_in_seconds % 3600) % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def read_products():
    result = deque()
    while True:
        product = input()
        if product == 'End':
            break
        result.append(product)
    return result


robots = read_robots()
available_robots = [r for r in robots.keys()]
processing_robots = {}

start_time = [int(x) for x in input().split(':')]
time_in_seconds = start_time[0] * 3600 + start_time[1] * 60 + start_time[2]

products = read_products()

while products:
    current_product = products.popleft()
    time_in_seconds = (time_in_seconds + 1) % (24 * 60 * 60)

    for robot_name in [k for k in processing_robots.keys()]:
        processing_robots[robot_name] -= 1
        if processing_robots[robot_name] <= 0:
            processing_robots.pop(robot_name)
    for robot_name in available_robots:
        if robot_name not in processing_robots:
            print(f"{robot_name} - {current_product} [{to_str_time(time_in_seconds)}]")
            processing_robots[robot_name] = robots[robot_name]
            break
    else:
        products.append(current_product)