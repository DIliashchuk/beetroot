import random

java_production = 150

python_worker = {
    'min_production': 90,
    'max_production': 180,  # Reduced max_production during music
    'time_to_max': 45,
    'current_production': 0,
    'total_production': 0,
    'loss_of_concentration': random.randint(5, 15),
    'music_start_time': random.randint(10, 25)
}

js_worker = {
    'min_production': 80,
    'max_production': 180,
    'time_to_max': 50,
    'current_production': 0,
    'total_production': 0,
    'reduction_start_time': python_worker['music_start_time']  # Start reducing with music
}

time_to_work = 60
title = " time | java_current_production | python_current_production | js_current_production | java_total_production | python_total_production | js_total_production"

python_change_per_second = (python_worker['max_production'] - python_worker['min_production']) / python_worker['time_to_max']
python_change_per_second = round(python_change_per_second)
python_timeline = []

js_change_per_second = (js_worker['max_production'] - js_worker['min_production']) / js_worker['time_to_max']
js_change_per_second = round(js_change_per_second)
js_timeline = []

for sec in range(time_to_work):
    if sec > python_worker['time_to_max']:
        python_timeline.append(python_worker['max_production'])
    else:
        current_prod = python_worker['min_production'] + sec * python_change_per_second
        if current_prod < python_worker['max_production']:
            python_timeline.append(current_prod)
        else:
            python_timeline.append(python_worker['max_production'])

for sec in range(time_to_work):
    if sec >= js_worker['reduction_start_time']:
        current_prod = js_worker['max_production'] - (sec - js_worker['reduction_start_time']) * js_change_per_second
        js_timeline.append(max(current_prod, js_worker['min_production']))
    else:
        current_prod = js_worker['max_production']
        js_timeline.append(current_prod)

java_total, python_total, js_total = 0, 0, 0

print(title)
for sec in range(time_to_work):
    time = sec
    python_worker['current_production'] = python_timeline[sec]

    # Simulate Python worker's faster form with music
    if python_worker['music_start_time'] <= sec < python_worker['music_start_time'] + 10:
        python_worker['current_production'] *= 2
        python_worker['max_production'] = 150  # Reduced max_production during music
    else:
        python_worker['max_production'] = 180

    # Ensure that python_current_production does not exceed max_production
    python_worker['current_production'] = min(python_worker['current_production'], python_worker['max_production'])

    # Add random fluctuation to Java worker's productivity
    java_production += random.randint(-10, 10)

    js_worker['current_production'] = js_timeline[sec]

    # Simulate Java worker's loss of average productivity
    if sec == python_worker['loss_of_concentration']:
        java_production *= 0.8

    java_total = java_total + java_production
    python_total = python_total + python_worker['current_production']
    js_total = js_total + js_worker['current_production']

    print(f'{str(time).center(6)}| {str(round(java_production)).center(24)}| {str(round(python_worker["current_production"])).center(26)}| {str(round(js_worker["current_production"])).center(26)}| {str(round(java_total)).center(22)}| {str(round(python_total)).center(24)}| {str(round(js_total)).center(24)}')
