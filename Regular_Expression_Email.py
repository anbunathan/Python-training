# Example: 
import re
pattern = re.compile(r"\[(on|off)\]") # Slight optimization
print(re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]"))
# Returns a Match object!
print(re.search(pattern, "Nada...:-([on]"))
# Doesn't return anything.
# End Example

# Exercise: make a regular expression that will match an email
def test_email(your_pattern):
    pattern = re.compile(your_pattern)
    emails = ["From: john@example.com", "From: python-list@python.org", "From: wha.t.`1an?ug{}ly@email.com"]
    for email in emails:
        if not re.match(pattern, email):
            print("You failed to match %s" % (email))
        elif not your_pattern:
            print("Forgot to enter a pattern!")
        else:
            print("Pass")
pattern = r"^(From|To|Cc).*?python-list@python.org" # Your pattern here!
test_email(pattern)