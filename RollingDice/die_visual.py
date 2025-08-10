from die import Die
import plotly.express as px

die = Die()
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

#Analyse the results.
frequencies = []
poss_results = range(1,die.num_sides+1) 
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results
fig = px.bar(x=poss_results, y=frequencies)
fig.show()