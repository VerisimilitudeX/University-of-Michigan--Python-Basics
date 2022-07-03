inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
for temp in inventory:
    temp = temp.split(',')
    str1="The store has{} {}, each for{} USD."
    str1=str1.format(temp[1],temp[0],temp[2])
    print(str1)
