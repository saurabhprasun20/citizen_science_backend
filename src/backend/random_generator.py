from random import randrange
import sys,os,json

sys.path.append(os.path.join(os.path.dirname(__file__), 'data'))

sibB = os.path.join(os.path.dirname(__file__), 'data')
question_list = [0]*500
print(len(question_list))
filename = "question_list.json"
sum = 0
while(True):
    set_1= set(question_list)
    print(set_1)
    if len(set_1) == 1: 
        if 3 in set_1:
            print(question_list)
            break
    choice = randrange(1, 1501)
    if(choice%3 != 1):
        continue
    if(question_list[choice//3] == 3):
        print(question_list)
        continue
    
    file_choice_flag = 0
    while(file_choice_flag == 0):
        array_choice = str(randrange(0,50))
        with open(os.path.join(sibB, filename), "r+") as jsonFile:
            data = json.load(jsonFile)
            if array_choice in data:
                # print("data[array_choice]")
                # print(data[array_choice])
                if choice in data[array_choice]:
                    continue
                if len(data[array_choice]) == 30:
                    continue
                data[array_choice].append(choice)
                question_list[choice//3] += 1
                file_choice_flag = 1
            else:
                data[array_choice] = [choice]
                question_list[choice//3] += 1
                file_choice_flag = 1
            
            jsonFile.seek(0)  # rewind
            json.dump(data, jsonFile)
            jsonFile.truncate()
    


print("Completed")

