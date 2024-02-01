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
while True:
    current_email = input()
    if current_email == "Stop":
        send_email_indices = [int(x) for x in input().split(", ")]
        break

    info = current_email.split(" ")
    current_sender, current_receiver, current_content = info[0], info[1], info[2]
    email_ = Email(current_sender, current_receiver, current_content)
    emails.append(email_)


for x in send_email_indices:
    emails[x].send()

print("\n".join([email.get_info() for email in emails]))

# for email in emails:
#     print(email.get_info())




##
# class Email:
#     def __init__(self, sender, receiver, content):
#         self.sender = sender
#         self.receiver = receiver
#         self.content = content
#         self.is_sent = False

#     def send(self):
#         self.is_sent = True

#     def get_info(self):
#         return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

# emails = []

# line = input()
# while line != 'Stop':
#     tokens = line.split(" ")
#     sender = tokens[0]
#     receiver = tokens[1]
#     content = tokens[2]
#     email = Email(sender, receiver, content)
#     emails.append(email)
#     line = input()

# send_emails = list(map(lambda x: int(x), input().split(", ")))

# for x in send_emails:
#     emails[x].send()

# for email in emails:
#     print(email.get_info())



##
# class Email:
#     def __init__(self, sender, receiver, content):
#         self.sender = sender
#         self.receiver = receiver
#         self.content = content
#         self.is_sent = False

#     def send(self):
#         self.is_sent = True

#     def get_info(self):
#         return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


# emails = []
# indices = []

# while True:
#     data = input().split()
#     if data[0] == 'Stop':
#         break

#     sender, receiver, content = data
#     email = Email(sender, receiver, content)
#     emails.append(email)

# indices = [int(i) for i in input().split(', ')]

# for index in indices:
#     if 0 <= index < len(emails):
#         emails[index].send()

# for email in emails:
#     print(email.get_info())
