class Party:
    def __init__(self):
        self.people = []


party = Party()
names_of_people = input()
while names_of_people != 'End':
    party.people.append(names_of_people)
    names_of_people = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")