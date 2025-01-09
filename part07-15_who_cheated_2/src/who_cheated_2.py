# Write your solution here
import csv
from datetime import datetime, timedelta

def final_points():
    #Find cheaters:
    acceptable_dictionary = {}
    with open("start_times.csv") as start_file:
        for line in csv.reader(start_file, delimiter=";"):
            start_time = datetime.strptime(line[1], "%H:%M")
            add = timedelta(hours=3)
            acceptable_end_time = start_time + add
            acceptable_dictionary[line[0]] = acceptable_end_time

    total_points = {}
    with open("submissions.csv") as submission_file:
        for line in csv.reader(submission_file, delimiter=";"):
            end_time = datetime.strptime(line[3], "%H:%M")
            if acceptable_dictionary[line[0]] > end_time: #if within timelimit
                if (line[0],line[1]) not in total_points: #if submission is not present
                    total_points[line[0],line[1]] = line[2]
                elif line[2] > total_points[line[0],line[1]]: #if the grade is greater
                    total_points[line[0],line[1]] = line[2]

    total_points = dict(sorted(total_points.items()))
    
    final = {}
    p_sum = 0
    for key, value in total_points.items():
        p_sum += int(value)
        final[key[0]] = p_sum
        if int(key[1]) == 8:
            p_sum = 0

    return final

if __name__ == "__main__":
    print(final_points())