journal_of_items = input().split(', ')

command = input()
while command != 'Craft!':
    command = command.split(' - ')
    what_to_do = command[0]
    if what_to_do == 'Collect':
        item = command[1]
        if item not in journal_of_items:
            journal_of_items.append(item)
    elif what_to_do == 'Drop':
        item = command[1]
        if item in journal_of_items:
            journal_of_items.remove(item)
    elif what_to_do == 'Combine Items':
        old_item, new_item = command[1].split(':')
        if old_item in journal_of_items:
            # index = journal_of_items[old_item]
            index = journal_of_items.index(old_item)
            journal_of_items.insert(index + 1, new_item)
    elif what_to_do == 'Renew':
        item = command[1]
        if item in journal_of_items:
            # index = journal_of_items.index(item)
            # index = journal_of_items[-1]
            same_item = item
            journal_of_items.remove(item)
            journal_of_items.append(item)

    command = input()
print(*journal_of_items, sep=', ')