squares = []

for x in range(10):
    if x % 2 == 0:
        squares.append(x * x)

print(squares)

squares2 = [x * x for x in range(10) if x % 2 == 0]
print(squares2)



emails = ["test@example.com", "oops", "bastien@teampanoptes.be", "error", "blobégmail.com"]
valid_emails = [email for email in emails if "@" in email]
print(valid_emails)