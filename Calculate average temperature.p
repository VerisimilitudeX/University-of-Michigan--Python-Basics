week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"

temp_list = week_temps_f.split(',')
lst=[float(i) for i in temp_list]

avg_temp = sum(lst)/len(lst)
