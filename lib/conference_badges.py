def badge_maker(name):
    return (f"Hello, my name is {name}.")

def batch_badge_creator(names):
    badge_names = []
    for name in names:
        badge_names.append(f"Hello, my name is {name}.")
    return badge_names

def assign_rooms(names):
    rooms = 1
    badge_names = []
    for name in names:
        badge_names.append(f"Hello, {name}! You'll be assigned to room {rooms}!")
        rooms += 1
    return badge_names

def printer(names):
    badge = batch_badge_creator(names)
    room = assign_rooms(names)
    for b in badge:
        print(b)
    for r in room:
        print(r)
