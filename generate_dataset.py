import random
import pandas as pd

# Words list for email generation (spam and ham)
words = ["hello", "free", "winner", "buy", "click", "subscribe", "offer", "money", "discount", "urgent",
         "meeting", "project", "schedule", "invoice", "report", "update", "team", "account", "credit", "important"]

def generate_email(is_spam):
    length = random.randint(5, 20)
    email = []
    for _ in range(length):
        if is_spam:
            email.append(random.choice(words[:10] + words[10:]*2))
        else:
            email.append(random.choice(words[10:] + words[:10]*0))
    return ' '.join(email)

num_instances = 75000
labels = []
emails = []

for _ in range(num_instances):
    label = random.choice(['ham', 'spam'])
    labels.append(label)
    emails.append(generate_email(is_spam=(label == 'spam')))

spam_data = pd.DataFrame({'label': labels, 'text': emails})
spam_data.to_csv('Emails.csv', index=False)
