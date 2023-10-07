#Unhash this to test the fake shit
# table = {
#     "id" : [100,200,300,400],
#     "question1": [1, 3, 2, 2],
#     "question2": [1, 3, 2, 2],
#     "question3": [1, 3, 3, 1],
#     "question4": [1, 3, 2, 2],
#     "question5": [3, 3, 2, 2],
#     "question6": [1, 1, 2, 2],
#     "question7": [3, 2, 2, 1]
# }


#Unhash this to legit shit
# table = db.execute("SELECT * from Questionnaire")



#Each dictionary key represents a planet
tally_count = {
    1:0,
    2:0,
    3:0
}

questions = []
for column in table:
    questions.append(column)

questions.pop(0)




for i in range(len(table["id"])):
    id_number = table["id"][i]
    for question in questions:
        tally_count[table[question][i]] += 1
    planet_to_visit = 1
    if tally_count[2] > tally_count[1]:
        if tally_count[2] > tally_count[3]:
            planet_to_visit = 2
    elif tally_count[3] > tally_count[1]:
        planet_to_visit = 3
    
    print(f"for id number {id_number} the optimal planet is planet number {planet_to_visit}")
    print(tally_count)
    tally_count[1] = 0
    tally_count[2] = 0
    tally_count[3] = 0




