#! /usr/bin/env python3
from sys import argv
if len(argv) != 2:
    print("USAGE: python figures.py <data.json>"); exit(1)
data = eval(open(argv[1]).read())

# set up seaborn
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import seaborn as sns
sns.set_style("ticks")
from matplotlib import rcParams
rcParams['font.family'] = 'serif'

# plot time vs. n
fig, ax = plt.subplots()
sns.pointplot(x=data['n'], y=data['time_cp'], color='#000000', linestyles=('--'))
sns.pointplot(x=data['n'], y=data['time_hivtrace'], color='#000000', linestyles=(':'))
sns.pointplot(x=data['n'], y=data['time_cp2'], color='#000000', linestyles=('-'))
ax.set_yscale('log')
ax.text(4, 250, 'Cluster Picker', fontsize=10)
ax.text(4, 3.9, 'HIV-TRACE', fontsize=10)
ax.text(4, 0.3, 'ClusterPicker-II', fontsize=10)
sns.plt.title("Execution Time (s) vs. Number of Taxa",fontsize=18,y=1.05)
sns.plt.xlabel("Number of Taxa")
sns.plt.ylabel("Execution Time (s)")
sns.plt.show()
fig.savefig('time_vs_n.pdf', format='pdf', bbox_inches='tight')
plt.close()