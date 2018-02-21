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

# set figure parameters
linestyles = {'cp':'--', 'hivtrace':':', 'cp2':'-', 'hiv_lanl':'--', 'hiv_sd':'-'}
pal = {'max':'#000000', 'avg':'#555555', 'sl':'#AAAAAA'}
handles = [Patch(color=pal['max'],label="Max Clade"), Patch(color=pal['avg'],label="Average Clade"), Patch(color=pal['sl'],label="Single Linkage Clade")]

# plot time vs. n
fig,ax = plt.subplots()
sns.pointplot(x=data['n'], y=data['time_cp'], color='#000000', linestyles=(linestyles['cp']))
sns.pointplot(x=data['n'], y=data['time_hivtrace'], color='#000000', linestyles=(linestyles['hivtrace']))
sns.pointplot(x=data['n'], y=data['time_cp2'], color='#000000', linestyles=(linestyles['cp2']))
ax.set_yscale('log')
ax.text(4, 250, 'Cluster Picker', fontsize=10)
ax.text(4, 3.9, 'HIV-TRACE', fontsize=10)
ax.text(4, 0.3, 'TreeCluster', fontsize=10)
sns.plt.title("Execution Time (s) vs. Number of Taxa",fontsize=18,y=1.05)
sns.plt.xlabel("Number of Taxa")
sns.plt.ylabel("Execution Time (s)")
sns.plt.show()
fig.savefig('time_vs_n.pdf', format='pdf', bbox_inches='tight')
plt.close()

# plot num singletons vs. t
fig,ax = plt.subplots()
plt.plot(data['thresh'], data['HIV_LANL_max_singletons'], color=pal['max'], linestyle=linestyles['hiv_lanl'])
plt.plot(data['thresh'], data['HIV_LANL_avg_singletons'], color=pal['avg'], linestyle=linestyles['hiv_lanl'])
plt.plot(data['thresh'], data['HIV_LANL_single_linkage_singletons'], color=pal['sl'], linestyle=linestyles['hiv_lanl'])
plt.plot(data['thresh'], data['HIV_SD_max_singletons'], color=pal['max'], linestyle=linestyles['hiv_sd'])
plt.plot(data['thresh'], data['HIV_SD_avg_singletons'], color=pal['avg'], linestyle=linestyles['hiv_sd'])
plt.plot(data['thresh'], data['HIV_SD_single_linkage_singletons'], color=pal['sl'], linestyle=linestyles['hiv_sd'])
plt.xlim(xmin=0,xmax=0.1)
ax.text(0.07, 3200, 'Dashed:  Los Alamos\nSolid:      San Diego', fontsize=10, bbox=dict(facecolor='none', edgecolor='lightgrey'))
sns.plt.title("Number of Singletons vs. Threshold",fontsize=18,y=1.05)
sns.plt.xlabel("Threshold")
sns.plt.ylabel("Number of Singletons")
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.show()
fig.savefig('num_singletons_vs_threshold.pdf', format='pdf', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot prop singletons vs. t
fig,ax = plt.subplots()
plt.plot(data['thresh'], data['HIV_LANL_max_singletons_prop'], color=pal['max'], linestyle=linestyles['hiv_lanl'])
plt.plot(data['thresh'], data['HIV_LANL_avg_singletons_prop'], color=pal['avg'], linestyle=linestyles['hiv_lanl'])
plt.plot(data['thresh'], data['HIV_LANL_single_linkage_singletons_prop'], color=pal['sl'], linestyle=linestyles['hiv_lanl'])
plt.plot(data['thresh'], data['HIV_SD_max_singletons_prop'], color=pal['max'], linestyle=linestyles['hiv_sd'])
plt.plot(data['thresh'], data['HIV_SD_avg_singletons_prop'], color=pal['avg'], linestyle=linestyles['hiv_sd'])
plt.plot(data['thresh'], data['HIV_SD_single_linkage_singletons_prop'], color=pal['sl'], linestyle=linestyles['hiv_sd'])
plt.xlim(xmin=0,xmax=0.1)
ax.text(0.07, 0.75, 'Dashed:  Los Alamos\nSolid:      San Diego', fontsize=10, bbox=dict(facecolor='none', edgecolor='lightgrey'))
sns.plt.title("Proportion of Singletons vs. Threshold",fontsize=18,y=1.05)
sns.plt.xlabel("Threshold")
sns.plt.ylabel("Proportion of Singletons")
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.show()
fig.savefig('prop_singletons_vs_threshold.pdf', format='pdf', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot num clusters vs. t
fig,ax = plt.subplots()
plt.plot(data['thresh'], data['HIV_LANL_max_clusters'], color=pal['max'], linestyle=linestyles['hiv_lanl'])
plt.plot(data['thresh'], data['HIV_LANL_avg_clusters'], color=pal['avg'], linestyle=linestyles['hiv_lanl'])
plt.plot(data['thresh'], data['HIV_LANL_single_linkage_clusters'], color=pal['sl'], linestyle=linestyles['hiv_lanl'])
plt.plot(data['thresh'], data['HIV_SD_max_clusters'], color=pal['max'], linestyle=linestyles['hiv_sd'])
plt.plot(data['thresh'], data['HIV_SD_avg_clusters'], color=pal['avg'], linestyle=linestyles['hiv_sd'])
plt.plot(data['thresh'], data['HIV_SD_single_linkage_clusters'], color=pal['sl'], linestyle=linestyles['hiv_sd'])
plt.xlim(xmin=0,xmax=0.15)
ax.text(0.11, 1100, 'Dashed:  Los Alamos\nSolid:      San Diego', fontsize=10, bbox=dict(facecolor='none', edgecolor='lightgrey'))
sns.plt.title("Number of Clusters vs. Threshold",fontsize=18,y=1.05)
sns.plt.xlabel("Threshold")
sns.plt.ylabel("Number of Clusters")
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.show()
fig.savefig('num_clusters_vs_threshold.pdf', format='pdf', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot prop clusters vs. t
fig,ax = plt.subplots()
plt.plot(data['thresh'], data['HIV_LANL_max_clusters_prop'], color=pal['max'], linestyle=linestyles['hiv_lanl'])
plt.plot(data['thresh'], data['HIV_LANL_avg_clusters_prop'], color=pal['avg'], linestyle=linestyles['hiv_lanl'])
plt.plot(data['thresh'], data['HIV_LANL_single_linkage_clusters_prop'], color=pal['sl'], linestyle=linestyles['hiv_lanl'])
plt.plot(data['thresh'], data['HIV_SD_max_clusters_prop'], color=pal['max'], linestyle=linestyles['hiv_sd'])
plt.plot(data['thresh'], data['HIV_SD_avg_clusters_prop'], color=pal['avg'], linestyle=linestyles['hiv_sd'])
plt.plot(data['thresh'], data['HIV_SD_single_linkage_clusters_prop'], color=pal['sl'], linestyle=linestyles['hiv_sd'])
plt.xlim(xmin=0,xmax=0.15)
ax.text(0.11, 0.25, 'Dashed:  Los Alamos\nSolid:      San Diego', fontsize=10, bbox=dict(facecolor='none', edgecolor='lightgrey'))
sns.plt.title("Proportion of Clusters vs. Threshold",fontsize=18,y=1.05)
sns.plt.xlabel("Threshold")
sns.plt.ylabel("Proportion of Clusters")
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.show()
fig.savefig('prop_clusters_vs_threshold.pdf', format='pdf', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()