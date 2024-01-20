def badge_maker(name):
    return "Hello, my name is {}.".format(name)

def generate_badges(names):
    badges = []
    for name in names:
        badges.append(badge_maker(name))
    return badges

def badge_maker(name):
    return "Hello, my name is {}.".format(name)

def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append(badge_maker(name))
    return badges

def assign_rooms(speakers):
    room_assignments = []
    for i, speaker in enumerate(speakers, start=1):
        room_assignments.append("Hello, {}! You'll be assigned to room {}!".format(speaker, i))
    return room_assignments

def printer(speakers):
    badges = batch_badge_creator(speakers)
    for badge in badges:
        print(badge)
    
    room_assignments = assign_rooms(speakers)
    for assignment in room_assignments:
        print(assignment)