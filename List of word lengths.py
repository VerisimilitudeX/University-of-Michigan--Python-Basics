original_str = "The quick brown rhino jumped over the extremely lazy fox"

original_list = list(original_str.split())
num_words = len(original_list)
num_words_list = []
for i in original_list:
    num_words_list.append((len(i)))

print(num_words_list)
