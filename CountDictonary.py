test_string=input("Enter string:")
l=[]
l=test_string.split("$")
print("l = ",l)
wordfreq=[l.count(p) for p in l]
print("wordfreq = ", wordfreq)
print(dict(zip(l,wordfreq)))