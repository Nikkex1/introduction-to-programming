# Write your solution here
import csv
from datetime import datetime, timedelta

def cheaters():
    acceptable_dictionary = {}
    with open("start_times.csv") as start_file:
        for line in csv.reader(start_file, delimiter=";"):
            start_time = datetime.strptime(line[1], "%H:%M")
            add = timedelta(hours=3)
            acceptable_end_time = start_time + add
            acceptable_dictionary[line[0]] = acceptable_end_time
    cheaters = []
    with open("submissions.csv") as submission_file:
        for line in csv.reader(submission_file, delimiter=";"):
            end_time = datetime.strptime(line[3], "%H:%M")
            if acceptable_dictionary[line[0]] < end_time:
                if line[0] not in cheaters:
                    cheaters.append(line[0])

    #print(acceptable_dictionary)
    return cheaters

if __name__ == "__main__":
    print(cheaters())