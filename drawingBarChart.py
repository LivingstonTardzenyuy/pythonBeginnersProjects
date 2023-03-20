from matplotlib.pyplot import plott

left=[1,2,3,4,5]
height=[20,30,40,50,2]

tick_label=['one', 'two', 'three', 'four', 'five']

plott.bar(left,height, tick_label=tick_label, width=0.8, color='blue')

plott.xlabel("X-axis")
plott.ylable("Y-axis")

plott.title("Demo-graph-Bar chart")

plott.save()