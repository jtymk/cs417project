#! /usr/bin/env python3

from functions import (interpolate, least)

# Initialize vectors for data from input file
time = [0]
readings_core_0 = []
readings_core_1 = []
readings_core_2 = []
readings_core_3 = []

# Read data from text file and store 
with open('sensors1.txt', 'r') as infile:
    for line in infile:
        values = line.strip().split()
        
        readings_core_0.append(float(values[0]))
        readings_core_1.append(float(values[1]))
        readings_core_2.append(float(values[2]))
        readings_core_3.append(float(values[3]))

        values = time[-1] + 30
        time.append(values)

interpolate(time, readings_core_0)

least(time, readings_core_0)

with open('time.txt', 'w') as outfile:
    for value in time:
        outfile.write(str(value) + '\n')

with open('core0.txt', 'w') as outfile:
    for value in readings_core_0:
        outfile.write(str(value) + '\n')

with open('core1.txt', 'w') as outfile:
    for value in readings_core_1:
        outfile.write(str(value) + '\n')

with open('core2.txt', 'w') as outfile:
    for value in readings_core_2:
        outfile.write(str(value) + '\n')

with open('core3.txt', 'w') as outfile:
    for value in readings_core_3:
        outfile.write(str(value) + '\n')


# Original functions for interpolation and least sqaures
        # for i in range(len(readings_core_0)):
        #     co = []
        #     c1 = []
        #     time_temp = [int(i) for i in time]
        #     reading_temp = [int(i) for i in readings_core_0]
        #     #readings_temp[i] = int(readings_core_0[i])
        #     #time[i] = int(time[i])
        #     k = len(time_temp)
        #     total_x = sum(time_temp)
        #     total_y = sum(reading_temp)
        #     xy = [time[i]*reading_temp[i] for time_temp[i], reading_temp[i] in zip(time_temp,reading_temp)]
        #     total_xy = sum(xy)
        #     total_x2 = sum([time_temp[i]**2 for i, time_temp[i] in enumerate(time_temp)])

        #     c11 = (k * total_xy - total_x * total_y) / (k * total_x2 - total_x**2)
        #     #c1.append(c11)
        #     # c1[i] = int(c1[i])
        #     c00 = (total_y / k) - (c1 * total_x / k)
        #     # co.append(c00)
            

        #     print(f"(x) = {c11}x + {c00}")

        # # For loop to calculate inter
        # for i in range(len(readings_core_0)):
        #     # Convert float vector to int vector to permit calculations
        #     readings_core_0[i] = int(readings_core_0[i])
        #     slope = (readings_core_0[i] - readings_core_0[i-1]) / (time[i] - time[i-1])
        #     inters = readings_core_0[i-1] - slope + time[i-1]
        #     inter.append(inters)

#least = least_squares(time, readings_core_0)

# Write the data into separate text files
# with open('inter.txt', 'w') as outfile:
#     for i in range(len(time) - 1):
#         outfile.write(str(time[i]) + '  <= x <      ' + str(time[i+1]) + '  y_0    ' + 
#                       '  =    ' + str(inter[i]) + ' interpolation \n')


