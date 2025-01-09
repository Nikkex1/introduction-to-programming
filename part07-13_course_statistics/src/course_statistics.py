# Write your solution here
import json
import urllib.request

def retrieve_all():
    list = []
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = json.loads(my_request.read()) #read from the variable
    for item in data:
        if item["enabled"]:
            list.append((item["fullName"],item["name"],item["year"],sum(item["exercises"])))
    return list

def retrieve_course(course_name: str):
    dictionary = {}

    url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    my_request = urllib.request.urlopen(url)
    week_data = json.loads(my_request.read()) #read from the variable
    hours_sum = 0
    total_ex = 0
    dictionary["weeks"] = len(week_data)
    dictionary["students"] = 0
    for key, value in week_data.items():
        if value["students"] > dictionary["students"]:
            dictionary["students"] = value["students"]
        hours_sum += value["hour_total"]
        dictionary["hours"] = hours_sum
        dictionary["hours_average"] = int(hours_sum / dictionary["students"])
        total_ex += value["exercise_total"]
        dictionary["exercises"] = total_ex
        dictionary["exercises_average"] = int(dictionary["exercises"] / dictionary["students"])

    return dictionary

if __name__ == "__main__":
    print(retrieve_all())
    print(retrieve_course("docker2019"))