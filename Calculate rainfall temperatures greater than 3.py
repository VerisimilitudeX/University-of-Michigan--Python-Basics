rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
vals = rainfall_mi.split()
num_rainy_months = 0
for val in vals:
    val = val.split(",")
    val = float(val[0])
    if val > 3:
        num_rainy_months += 1
print(num_rainy_months)
