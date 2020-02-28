#!/usr/bin/env python3
# coding: utf-8

import argparse
import os
import matplotlib
import matplotlib.pyplot
import pandas
from matplotlib.ticker import EngFormatter


parser = argparse.ArgumentParser(description="Generator plots of cpu utilisation")
parser.add_argument("csv_file_name", metavar='path_to_csv_file', type=str, help="Path to csv file with results")
parser.add_argument("monitored_process_name", metavar='monitored_process_name', type=str, help="Name of process which was monitored")
args = parser.parse_args()

file_name = getattr(args, "csv_file_name").replace(".csv", "")
monitored_process_name = getattr(args, "monitored_process_name")

# In this part below format:
# 3k;1G
# 3,0
# 4,0
# 5,0
# 9,0
# Is changed to:
# 3000,1000000000,3.0
# 3000,1000000000,4.0
# etc

file = open(file_name + ".csv")
file_content = file.read()

last_prefix = None
new_file_content = ""
for line in file_content.split("\n"):
    line_fragments = line.split(";")
    if len(line_fragments) == 2:
        last_prefix = line. \
            replace("k", "000"). \
            replace("G", "000000000")   # Change units
    else:
        new_file_content += last_prefix + ";" + line + "\n"
        
new_file_content = new_file_content.replace(",", ".").replace(";", ",")
header = "datagram_size,bandwidth,cpu_utilisation\n"
with open(file_name + "_m.csv", "w") as destiny_file:
    destiny_file.write(header)
    destiny_file.write(new_file_content)

# Another part- visualisation

raw_dataframe = pandas.read_csv(file_name + "_m.csv")

grouped = raw_dataframe.groupby(["bandwidth", "datagram_size"])

median = grouped.median()

y_label = "cpu_utilisation"
matplotlib.pyplot.xscale("log")

fig = matplotlib.pyplot.figure(1)
def get_label(value, unit):
    unit_scale_map = {1000000000: "G",
                      1000000: "M",
                      1000: "K",
                      1: ""}
    for scale in unit_scale_map.keys():
        scaled_value = value * 1.0 / scale
        if scaled_value >= 1:
            scaled_value_with_unit = str(scaled_value) + \
                                    " " + unit_scale_map[scale] + unit
            return scaled_value_with_unit
    
ax = fig.axes[0]
for bandwidth in median.index.levels[0]:
    data = median.loc[(bandwidth,)]
    label = get_label(bandwidth, "bit")
    data.plot(y=y_label, label=label, ax=ax)

formatter0 = EngFormatter(unit='bytes')
ax.xaxis.set_major_formatter(formatter0)
ax.grid(True, which='major', axis='x' )
ax.grid(True, which='major', axis='y' )
ax.set_xlabel("datagram size [log]")
ax.set_title(monitored_process_name + " cpu utilisation of receiver in different bandwidth\nDefault settings, 3 senders : 1 receiver")
ax.set_ylabel("Cpu utilisation [%]")
ax.set_yticks([i for i in range(0, 110, 10)])
ax.set_xticks([1000, 2000, 4000, 8000, 16000, 32000, 60000])        # To do- adjust for every data
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(12, 8)
matplotlib.pyplot.savefig(monitored_process_name + "_cpu_utilisation.png")
