def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    x = 1
    room_assignment = []
    for name in names:
        room_assignment.append(f"Hello, {name}! You'll be assigned to room {x}!")
        x += 1 
    return room_assignment

def printer(names):
    badge_list = batch_badge_creator(names)
    room_assignment = assign_rooms(names)
    for badge in badge_list:
        print(badge)
    for room in  room_assignment:
        print(room)

