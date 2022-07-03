addition_str = "2+5+10+20"
sum_val = sum(int(num) for num in addition_str.split('+'))
print(sum_val)
