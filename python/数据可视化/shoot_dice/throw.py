from create_Die import Die
import plotly.express as px
import pandas


die_1 = Die()
die_2 = Die(10)
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_results = die_1.num_sides + die_2.num_sides
poss_results = range(1, max_results+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

fig = px.bar(x=poss_results, y=frequencies)
title = "Results of rolling a D6 and a D10 50,000 Times"
labels = {'x':"Result", "y":"Frequency of Result"}
fig = px.bar(labels=labels, x=poss_results, y=frequencies, title=title)
fig.update_layout(xaxis_dtick=1)

fig.show()
# fig.write_html('dice_visual_d6d10.html')
