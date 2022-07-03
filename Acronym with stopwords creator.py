
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
acro = ""
org = org.split()
for orgx in org:
    orgx = orgx.strip(",")
for word in org:
    if word.lower() not in stopwords:
        acro += word[0].upper()
print(acro)
