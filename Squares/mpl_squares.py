import matplotlib.pyplot as plt
input_values=range(1,1001)#default x value starts with 0, so we explicitly defined out x
squares = [x**2 for x in input_values]
plt.style.use('seaborn-v0_8')#inbluild style 
fig,ax = plt.subplots() #figures collection of plots, ax is single plot
ax.plot(input_values,squares,linewidth=3)
ax.scatter(input_values,squares,c=squares,cmap=plt.cm.Blues,s=10)#use to group points,s is size of point
#set range of axis
ax.axis([0,1100,0,1_100_000])
ax.ticklabel_format(style='plain')
#Set char title and label axes.
ax.set_title("Square title", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
#set size of tick labels
ax.tick_params(labelsize=14)
plt.show()
#plt.savefig('square_plot.png',bbox_inches='tight')