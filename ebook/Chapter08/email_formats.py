emails = ("a@example.com", "b@example.com")
message = {
    "subject": "You Have Mail!",
    "message": "Here's some mail for you!",
}

formatted = f"""
From: <{emails[0]}>
To: <{emails[1]}>
Subject: {message['subject']}
{message['message']}"""
print(formatted)


message["emails"] = emails

formatted = f"""From: <{message['emails'][0]}>
To: <{message['emails'][1]}>
Subject: {message['subject']}
{message['message']}"""
print(formatted)


class EMail:
    def __init__(self, from_addr, to_addr, subject, message):
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.subject = subject
        self._message = message

    def message(self):
        return self._message


email = EMail(
    "a@example.com",
    "b@example.com",
    "You Have Mail!",
    "Here's some mail for you!",
)

formatted = f"""
From: <{email.from_addr}>
To: <{email.to_addr}>
Subject: {email.subject}

{email.message()}"""
print(formatted)


tuandemo = EMail(
    "tuann193@gmail.com",
    "tuan193@gmail.com",
    "Hello is it me!",
    "Nothing gone to change my love for u."
)

email = f"""From : <{tuandemo.from_addr}>
To : <{tuandemo.to_addr}>
Subject : {tuandemo.subject}
Message : {tuandemo.message()}
"""

print(email)