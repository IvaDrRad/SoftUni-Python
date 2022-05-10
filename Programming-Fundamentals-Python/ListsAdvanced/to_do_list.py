to_do_notes = [0] * 10

command = input()
while not command == 'End':
    importance, activity = command.split('-')
    priority = int(importance) - 1
    to_do_notes.pop(priority)
    to_do_notes.insert(priority, activity)
    command = input()

while 0 in to_do_notes:
    to_do_notes.remove(0)
print(to_do_notes)
