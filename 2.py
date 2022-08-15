import random
def main():
    capitals={"Washington":"Olympia","Oregon":"Salem",\
                    "California":"Sacramento","Ohio":"Columbus",\
                    "Nebraska":"Lincoln","Colorado":"Denver",\
                    "Michigan":"Lansing","Massachusetts":"Boston",\
                    "Florida":"Tallahassee","Texas":"Austin",\
                    "Oklahoma":"Oklahoma City","Hawaii":"Honolulu",\
                    "Alaska":"Juneau","Utah":"Salt Lake City",\
                    "New Mexico":"Santa Fe","North Dakota":"Bismarck",\
                    "South Dakota":"Pierre","West Virginia":"Charleston",\
                    "Virginia":"Richmond","New Jersey":"Trenton",\
                    "Minnesota":"Saint Paul","Illinois":"Springfield",\
                    "Indiana":"Indianapolis","Kentucky":"Frankfort",\
                    "Tennessee":"Nashville","Georgia":"Atlanta",\
                    "Alabama":"Montgomery","Mississippi":"Jackson",\
                    "North Carolina":"Raleigh","South Carolina":"Columbia",\
                    "Maine":"Augusta","Vermont":"Montpelier",\
                    "New Hampshire":"Concord","Connecticut":"Hartford",\
                    "Rhode Island":"Providence","Wyoming":"Cheyenne",\
                    "Montana":"Helena","Kansas":"Topeka",\
                    "Iowa":"Des Moines","Pennsylvania":"Harrisburg",\
                    "Maryland":"Annapolis","Missouri":"Jefferson City",\
                    "Arizona":"Phoenix","Nevada":"Carson City",\
                    "New York":"Albany","Wisconsin":"Madison",\
                    "Delaware":"Dover","Idaho":"Boise",\
                    "Arkansas":"Little Rock","Louisiana":"Baton Rouge"}

    wrong=[]

    print ("STATE TEST \n")

    incorrect_answers = False

    while len(capitals)>0:
        pick=random.choice(list(capitals.keys()))
        correct_answer=capitals.get(pick)
        print ("What is the capital city of",pick,"?")
        answer=input("Your answer: ")
        if answer.lower()==correct_answer.lower():
            print ("That's Correct!\n")
        else:
            print ("That's Incorrect.")
            print ("The correct answer is",correct_answer)
            wrong.append(pick)
            incorrect_answers = True
    del capitals[pick]

    print ("You missed",len(wrong),"states.\n")


    if incorrect_answers:
        print ("Here are the ones that you may want to brush up on:\n")
        for each in wrong:
            print (each)
    else:
        print ("Perfect!")
main()