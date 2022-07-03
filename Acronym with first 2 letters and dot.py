stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
acro = ""
lst = sent.split()

for i in lst:
    if i in stopwords:
        lst.remove(i)

for j in lst:
    acro = acro + j[0] + j[1]
    if j != lst[-1]:
        acro += ". "

acro = acro.upper()
print(acro)
