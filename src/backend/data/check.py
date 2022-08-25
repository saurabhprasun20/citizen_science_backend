import json,os

json_file = open("src/backend/data/question_list.json")
question_data = json.load(json_file)
print(question_data["0"])
question_list = [0]*500
sum = 0

for i in range(0,50):
    temp_list = question_data[str(i)]
    temp_list.sort()
    print("Printing list ",i)
    print(temp_list, "and length", len(temp_list))
    sum+=len(temp_list)
    for question_no in temp_list:
        question_list[question_no//3] += 1

print(question_list)
print(sum)