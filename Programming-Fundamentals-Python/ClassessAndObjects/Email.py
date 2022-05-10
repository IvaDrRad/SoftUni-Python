class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
chat = input()
while chat != "Stop":
    current_chat = chat.split()
    sender = current_chat[0]
    receiver = current_chat[1]
    content = current_chat[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    chat = input()

sent_emails = list(map(lambda x: int(x), input().split(', ')))
for x in sent_emails:
    emails[x].send()

for email in emails:
    print(email.get_info())