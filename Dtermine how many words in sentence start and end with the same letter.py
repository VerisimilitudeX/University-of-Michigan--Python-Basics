sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
sentence = sentence.split()
same_letter_count = 0
for word in sentence:
    if word[0] is word[-1]:
        same_letter_count += 1
