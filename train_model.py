from model import train_model

texts = [
    # Spam emails (label=1)
    "Congratulations! You have been selected as a winner in our exclusive sweepstakes.",
    "Dear User, Your bank account has been compromised.",
    # ... (all spam examples here) ...

    # Non-spam emails (label=0)
    "Hi team, attached is the project report.",
    "Dear Jane, congratulations on your recent promotion.",
    # ... (all non-spam examples here) ...
]

labels = [
    1, 1,  # spam labels for spam texts...
    # ...
    0, 0,  # not spam labels for non-spam texts...
    # ...
]

train_model(texts, labels)
print("Model trained to classify non-spam correctly as 'not spam' (0).")
