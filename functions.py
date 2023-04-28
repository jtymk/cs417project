#! /usr/bin/env python3

def interpolate(time, readings_core_0):
    # Ensure vector is not empty
    inter = []
    if not readings_core_0:
        return inter
    # Store time and core in temp vectors
    timeTemp = [int(i) for i in time]
    readingTemp = [int(i) for i in readings_core_0]
    
    with open('inter.txt', 'w') as outfile:
        for i in range(len(readings_core_0)):
            # Calculate interpolation
            slope = (readingTemp[i] - readingTemp[i-1]) / (timeTemp[i] - timeTemp[i-1])
            inters = readingTemp[i-1] - slope + timeTemp[i-1]
            inter.append(inters)
            # Output
            outfile.write(str(time[i]) + '  <= x <      ' + str(time[i+1]) + '  y_0    ' + 
                      '  =    ' + str(inter[i]) + ' interpolation \n')
        
    return inter

def least(time, readings_core_0):
    with open('least.txt', 'w') as outfile:
        for i in range(len(readings_core_0)):
            # Store time and core in temp vectors
            time_temp = [int(i) for i in time]
            reading_temp = [int(i) for i in readings_core_0]
            # Get the number of time values
            k = len(time_temp)
            # Get the total sum of time and core values
            total_x = sum(time_temp)
            total_y = sum(reading_temp)
            # Calculate components of matrix
            xy = [time[i]*reading_temp[i] for time_temp[i], reading_temp[i] in zip(time_temp,reading_temp)]
            total_xy = sum(xy)
            total_x2 = sum([time_temp[i]**2 for i, time_temp[i] in enumerate(time_temp)])
            # Calculate c0 and c1
            c1 = (k * total_xy - total_x * total_y) / (k * total_x2 - total_x**2)
            c0 = (total_y / k) - (c1 * total_x / k)
            # Output 
            outfile.write('f(x) = ' + str(c1) + 'x + (' + str(c0) + ')' + '\n')