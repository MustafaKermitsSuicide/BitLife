#!usr/env/bin/python3

#BITLIFE ALPHA v0.3
#by Mustafa Abdillahi


import random
import datetime
import time



#Name, surname, birthdate (with the zodiac
#alongside it) and residence generator. With random doctor profession.
#Basically it is a lot of lists.

FIRST_NAMES_MALE = ["Oliver", "Jacob", "Mason", "Harry", "William", "Alfie",
                    "Jayden", "Charlie", "Noah", "Thomas", "Michael",
                    "Ethan", "Joshua", "Alexander", "George", "Aiden", "James",
                    "Daniel", "Jack", "Bruno", "Donald", "Nick", "Harvey",
                    "Alfie", "Archie", "Ollie", "Louie", "Jenson",
                    "Lewis", "Louis", "Callum", "Freddie", "Theo", "Toby",
                    "Harley", "Reuben", "Kian", "Bobby", "Stanley"]
FIRST_NAMES_FEMALE = ["Olivia", "Sophie", "Isabella", "Emily", "Emma", "Lily",
                      "Amelia", "Ava", "Jessica", "Ruby", "Abigail",
                      "Chloe", "Madison", "Grace", "Mia", "Evie", "Laura",
                      "Maisie", "Poppy", "Freya", "Imogen", "Florence", "Rosie",
                      "Hollie", "Isobel", "Niamh", "Harriet", "Tilly", "Maisy",
                      "Holly", "Matilda", "Amelie", "Esme", "Zara", "Tia",
                      "Aimee", "Martha", "Libby"]
SURNAMES = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller",
            "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson",
            "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez",
            "Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker",
            "Hall", "Allen", "Young", "Hernandez", "King", "Wright", "Lopez",
            "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson",
            "Carter", "Mitchell", "Perez", "Roberts", "Turner", "Phillips",
            "Campbell", "Parker", "Evans", "Edwards", "Collins", "Stewart",
            "Sanchez", "Morris", "Rogers", "Reed", "Cook", "Morgan", "Bell",
            "Murphy", "Bailey", "Rivera", "Cooper", "Richardson", "Cox",
            "Howard", "Ward", "Torres", "Peterson", "Gray", "Ramirez", "James",
            "Watson", "Brooks", "Kelly", "Sanders", "Price", "Bennett", "Wood",
            "Barnes", "Ross", "Henderson", "Coleman", "Jenkins", "Perry",
            "Powell", "Log", "Patterson", "Hughes", "Flores", "Washington",
            "Butler", "Simmons", "Foster", "Gonzales", "Bryant", "Alexander",
            "Russell", "Griffin", "Diaz", "Hayes"]
GENDERS = ["Male", "Female"]

MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
CENTURY_LEAPS = ["1900", "2100", "2200", "2300", "2500", "2600", "2700",
                 "2900", "3000"]

ILLNESSES_CHILDREN = ["The Common Cold", "Diarrhoea", "Measles", "A Fever",
                      "Chickenpox", "Rubella", "Mumps", "A Whooping Cough",
                      "A Sore Throat", "Urinary Tract Infection",
                      "Bronchitis", "Bronchiolitis", "Bacterial Sinusitis",
                      "Asthma", "Cancer", "Diabetes", "Epilepsy", "Depression",
                      "Anxiety"]
ILLNESSES_ADULTS = ["Diabetes", "Epilepsy", "Anaemia", "Hypertension",
                    "Depression", "Hearing Loss", "Lung Disease",
                    "Kidney Diease", "Parkinson's", "Osteoporosis",
                    "Bursitis", "Tendonitis", "High Cholesterol",
                    "An Aging Eye", "Cataracts", "Glaucoma",
                    "Macular Degenration", "Menopause", "High Fatigue",
                    "Anxiety"]
ILLNESSES_ELDERLY = ["Arthritis", "Hypertension", "Blindless", "Myopia",
                     "Cancer", "Chronic Bronchitis", "Coronary Heart Disease",
                     "Dementia", "Diabetes", "Motor Neurone Disease",
                     "Multiple Sclerosis", "Osteoporosis",
                     "Paget's Disease of the Bone", "Parkinson's",
                     "Chronic Kidney Diease", "Deep Vein Thrombosis",
                     "Shingles", "High Cholesterol", "Depression",
                     "Hearing Loss"]

CITIES = ["London, England", "Birmingham, England", "Glasgow, Scotland",
             "Edinburgh, Scotland", "Liverpool, England", "Bristol, England",
             "Cardiff, Wales", "Leicester, England", "Nottingham, England",
             "Coventry, England", "Luton, England", "Aberdeen, Scotland",
             "Brighton, England", "Oxford, England", "Dundee, Scotland",
             "Ipswich, England", "Cambridge, England", "Bath, England",
             "Chester, England", "New York City, New York, USA",
             "Los Angeles, California, USA", "Chicago, Illinois, USA",
             "Houston, Texas, USA", "Philadelphia, Pennyslvania, USA",
             "Phoenix, Arizona, USA", "San Antonio, Texas, USA",
             "San Diego, California, USA", "Dallas, Texas, USA",
             "San Jose, California, USA", "Austin, Texas, USA",
             "San Francisco, California, USA", "Jacksonville, Florida, USA",
             "Indianapolis, Indiana, USA", "Columbus, Ohio, USA",
             "Fort Worth, Texas, USA", "Charlotte, North Carolina, USA",
             "Detroit, Michigan, USA", "Nashville, Tennessee, USA"]

DOCTOR_PROFESSIONS = ["Doctor", "Nurse"]
JOB = []

LIQUOR = ["Red Wine", "White Wine", "Whiskey", "Rum", "Slivovitz", "Absinthe",
          "Spirit", "Cocktails", "Brandy", "Gin", "Vodka", "Schnapps"]
LIQUOR_TYPE = []
DEATHCAUSE = []
YEARZ = []

FAMILY = ["Mother", "Father"]


age = -1


gender = random.choice(GENDERS)

if gender == "Male":
    first_name = random.choice(FIRST_NAMES_MALE)

else:
    first_name = random.choice(FIRST_NAMES_FEMALE)

surname = random.choice(SURNAMES)

year_of_birth = str(datetime.datetime.now().year)
month_of_birth = random.choice(MONTHS)

if (month_of_birth == "January" or "March" or "May" or "July" or "August" or
    "October" or "December"):
    day_of_birth = random.randint(1, 31)
elif month_of_birth == "April" or "June" or "September" or "November":
    day_of_birth = random.randint(1, 30)
elif ((month_of_birth == "February") and (year % 4 == 0) and (year not in
                                                            CENTURY_LEAPS)):
    day_of_birth = random.randint(1, 29)
else:
    day_of_birth = random.randint(1, 28)



if (day_of_birth >= 23 and month_of_birth == "August") or (day_of_birth <= 22
                                                           and month_of_birth
                                                           == "September"):
    zodiac = "Virgo"

elif (day_of_birth >= 23 and month_of_birth == "September") or (day_of_birth
                                                                <= 22 and
                                                                month_of_birth
                                                               == "October"):
    zodiac = "Libra"

elif (day_of_birth >= 23 and month_of_birth == "October") or (day_of_birth
                                                                <= 22 and
                                                                month_of_birth
                                                               == "November"):
    zodiac = "Scorpio"

elif (day_of_birth >= 23 and month_of_birth == "November") or (day_of_birth
                                                                <= 22 and
                                                                month_of_birth
                                                               == "December"):
    zodiac = "Sagittarius"

elif (day_of_birth >= 23 and month_of_birth == "December") or (day_of_birth
                                                                <= 20 and
                                                                month_of_birth
                                                               == "January"):
    zodiac = "Capricorn"

elif (day_of_birth >= 21 and month_of_birth == "January") or (day_of_birth
                                                                <= 18 and
                                                                month_of_birth
                                                               == "February"):
    zodiac = "Aquarius"

elif (day_of_birth >= 21 and month_of_birth == "February") or (day_of_birth
                                                                <= 19 and
                                                                month_of_birth
                                                               == "March"):
    zodiac = "Pisces"

elif (day_of_birth >= 21 and month_of_birth == "March") or (day_of_birth
                                                                <= 19 and
                                                                month_of_birth
                                                               == "April"):
    zodiac = "Aries"
    
elif (day_of_birth >= 21 and month_of_birth == "April") or (day_of_birth
                                                                <= 20 and
                                                                month_of_birth
                                                               == "May"):
    zodiac = "Taurus"

elif (day_of_birth >= 21 and month_of_birth == "May") or (day_of_birth
                                                                <= 21 and
                                                                month_of_birth
                                                               == "June"):
    zodiac = "Gemini"

elif (day_of_birth >= 22 and month_of_birth == "June") or (day_of_birth
                                                                <= 22 and
                                                                month_of_birth
                                                               == "July"):
    zodiac = "Cancer"

else:
    zodiac = "Leo"


residence = random.choice(CITIES)

#States in shell when the player enters a stage of education, e.g. university,
#reception, kindergaten, etc.
if residence[-3:] == "USA":
    nursery_age = 5
    primary_age = 6
    middle_age = 11
    secondary_age = 14
else:
    nursery_age = 3
    primary_age = 4
    secondary_age = 11

university_age = 17  


print("\n***BITLIFE: PYTHON ALPHA v0.3***")

if zodiac == "Aquarius" or zodiac == "Aries":
    print("\n\nMy name is ",first_name," ",surname,". My birthday is ",
          day_of_birth," ",month_of_birth,". I am a ",gender.lower(),". I am",
          " an ",zodiac,". I was born in ",residence,".",sep="")
else:
    print("\n\nMy name is ",first_name," ",surname,". My birthday is ",
          day_of_birth," ",month_of_birth,". I am a ",gender.lower(),". I am",
          " a ",zodiac,". I was born in ",residence,".",sep="")


father_name = random.choice(FIRST_NAMES_MALE)
mother_name = random.choice(FIRST_NAMES_FEMALE)
father_age = random.randint(18, 50)
mother_age = random.randint(16, 45)
mother_maiden = random.choice(SURNAMES)

print("My father is called ",father_name," ",surname,", and he is ",father_age,
      " years old.",sep="")

if mother_maiden == surname:
    print("My mother is called ",mother_name," ",surname," (same maiden",
          " name), and she is ",mother_age," years old.",sep="")

else:
    
    print("My mother is called ",mother_name," ",surname," (née ",mother_maiden,
          ") and she is ",mother_age," years old.",sep="")
#Displays names & ages of parents


time.sleep(6)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",
      "\n\n\n\n") #"Clears" out the shell ("blanks" it)

ab = 1
ba = 1
before_death = "No"
money = 0







#
# - - - - - - - - > FUNCTIONS
#

    


#When player gets ill but lives
def illness():
    
    if age < 18:
        illness = random.choice(ILLNESSES_CHILDREN)
    elif age >= 18 and age < 65:
        illness = random.choice(ILLNESSES_ADULTS)
    else:
        illness = random.choice(ILLNESSES_ELDERLY)

    if illness != "Paget's Disease of the Bone" and illness != "Parkinson's":
            illness_no_caps = illness.lower()
    else:
            illness_no_caps = str(illness)

    if illness != "Cancer":
        
        illness_death = random.randint(1, 5)
        if illness_death == 1:
            before_death = "Yes"
            death()

        else:
            print("I have been diagnosed with ",illness_no_caps,".",sep="")
    else:
        before_death = "Yes"
        death()



#When player gets ill and dies    
def death():

    if before_death == "No":
        if age < 18:
            illness = random.choice(ILLNESSES_CHILDREN)
        elif age >= 18 and age < 65:
            illness = random.choice(ILLNESSES_ADULTS)
        else:
            illness = random.choice(ILLNESSES_ELDERLY)

        if illness != "Paget's Disease of the Bone" and illness != "Parkinson's":
                illness_no_caps = illness.lower()
        else:
                illness_no_caps = str(illness)


    if "Liquor" in DEATHCAUSE:
        print("I have been diagnosed with and died of",LIQUOR_TYPE[0].lower(),
                  "overdose.")
    else:      
        print("I have been diagnosed with and died of ",illness_no_caps,"."
              ,sep="")

    
    print("\n**I, ",first_name.upper()," ",surname.upper(),", HAVE DIED ",
          "AT ",age," YEARS OLD**",sep="")
    time.sleep(1)

    year_of_death = YEARZ[0]

    fn = open("Data_Turtle.txt", "w+")
    fn.write((str(first_name) + " " + str(surname)))
    fn.write(("\n" + str(year_of_birth) + " - " + str(year_of_death)))
    fn.close()

    import TurtleBitLife
    
    quit()

#When parents get ill and die
def death_father():

    if "Father" in FAMILY:
        if before_death == "No":
            if age < 65:
                illness = random.choice(ILLNESSES_ADULTS)
            else:
                illness = random.choice(ILLNESSES_ELDERLY)

            if (illness != "Paget's Disease of the Bone" and
                illness != "Parkinson's"):
                    illness_no_caps = illness.lower()
            else:
                    illness_no_caps = str(illness)
        
        print("My father died of ",illness_no_caps,".",sep="")
        death_number_father = 1000
        FAMILY.remove("Father")

        if len(FAMILY) == 0:
            if age < 18:
                print("I have been adopted by a foster family.")

def death_mother():

    if "Mother" in FAMILY:
        if before_death == "No":
            if age < 18:
                illness = random.choice(ILLNESSES_CHILDREN)
            elif age >= 18 and age < 65:
                illness = random.choice(ILLNESSES_ADULTS)
            else:
                illness = random.choice(ILLNESSES_ELDERLY)

            if (illness != "Paget's Disease of the Bone" and
                illness != "Parkinson's"):
                    illness_no_caps = illness.lower()
            else:
                    illness_no_caps = str(illness)
        
        print("My mother died of ",illness_no_caps,".",sep="")
        death_number_mother = 1000
        FAMILY.remove("Mother")

        if len(FAMILY) == 0:
            if age < 18:
                print("I have been adopted by a foster family.")

death_random = 0

#!
#Events
#!


#KLiquor Event: When friends ask character to go out for random liquor. 1/3
#chance of dying if character accepts invitation.
def liquor_event():

    liquor = random.choice(LIQUOR)
    del LIQUOR_TYPE[0 : len(LIQUOR_TYPE)]
    LIQUOR_TYPE.append(str(liquor))

    choice_event = "Mustafa"

    while choice_event not in {"1", "2"}:

        liquor = random.choice(LIQUOR)
        print("\nSome of your friends have gone out to have some ",
              liquor.lower(),
              ", and have asked you to come with them. Do you...",sep="")
        print("\n1 - Go out for a shot?")
        print("2 - Decline respectfully?")

        choice_event = input("\nWhat do you do? ")

    if choice_event == "1":
        death_random = random.randint(1, 3)

        if death_random == 1:
            DEATHCAUSE.append("Liquor")
            death()
            
            
        else:
            print("\nYou enjoyed the ",liquor.lower(),"!",sep="")
    else:
        random_event_consenquence = random.randint(1, 2)

        if random_event_consenquence == 1:
            print("\nYour friends respected your decision and backed away.")
            
        else:
            print("\nYour friends scolded you for not coming.")




#Heart and soul of the game
def play_a_year():

    

    year = int(year_of_birth) + age
    year_of_death = str(year)

    YEARZ.clear()
    YEARZ.append(str(year_of_death))
    

    print("\n\n**",year,": ",age," YEARS OLD**",sep="")

    death_number = random.randint(1, 100)
    if death_number <= death_rate:
        death()
    else:
        illness_rate = random.randint(1, 15)
        if illness_rate == 1:
            illness()
        else:
            print("I haven't been diagnosed this year!")

    death_number_father = random.randint(1, 100)
    if death_number_father <= death_rate_father:
        death_father()

    death_number_mother = random.randint(1, 100)
    if death_number_mother <= death_rate_mother:
        death_mother()
    

    if age >= 18:
        job = JOB[0]

    
        if residence[-3:] == "USA":
            cash = ("$" + str(money))
        else:
            cash = ("£" + str(money))

        print("Money:",cash)

    
    if age < 18:
        print("I'm too young to work yet.")
    else:
        print("Occupation:",job)

    if age == nursery_age:
        if residence[-3:] == "USA":
            print("I started kindergarten!")
        else:
            print("I started nursery!")

    if age == primary_age:
        if residence[-3:] == "USA":
            print("I started elementary school!")
        else:
            print("I started primary school!")

    if residence [-3:] == "USA":
         if age == middle_age:
             print("I started elementary school!")

    if age == secondary_age:
        print("I started high school!")

    if age == university_age:
        if residence[-3:] == "USA":
            print("I started college!")
        else:
            
            print("I started university!")
    
        job = "Mustafa"

        while job not in {"1", "2", "3", "4", "5"}:
    
            if gender == "Male":
                print("\n1 - Businessman")
            else:
                print("\n1 - Businesswoman")

            print("2 - Lawyer")
            print("3 - Doctor")
            print("4 - Accountant")
            print("5 - Programmer")

            if residence[-3:] == "USA":
                job = input("\nWhat would I like to major in? ")
            else:
                job = input("\nWhat course should I join? ")

            
        if job == "1":
            if gender == "Male":
                job = "Businessman"
            else:
                job = "Businesswoman"

        elif job == "2":
            job = "Lawyer"

        elif job == "3":
            job = random.choice(DOCTOR_PROFESSIONS)

        elif job == "4":
           job = "Accountant"

        elif job == "5":
            job = "Programmer"

        JOB.append(str(job))


    if age >= 18:
        liquor_random = random.randint(1, 5)

        if liquor_random == 1:
            liquor_event()

            

        
#Repeats play_a_year() function until death, then orders shell to terminate       
while (ab + ba == 2):
    time.sleep(1)    
    age += 1
    death_rate = float((((age - 25) * ((2 / 3) * age)) / 20) - 20)
    
    if "Father" in FAMILY:       
        father_age += 1
        death_rate_father = float((((father_age - 25) * ((2 / 3) *
                                                        father_age)) / 20) - 20)
    if "Mother" in FAMILY:
        mother_age += 1
        death_rate_mother = float((((mother_age - 25) * ((2 / 3) *
                                                         mother_age)) / 20) - 20)

    

    if age >= 18:

        job = JOB[0]
    
        if job == "Businessman" or job == "Businesswoman":
            if residence[-3:] == "USA":
                money += 60000
            else:
                money += 48048

        if job == "Lawyer":
            if residence[-3:] == "USA":
                money += 118160
            else:
                money += 94623

        if job == "Doctor" or job == "Nurse":
            if residence[-3:] == "USA":
                money += 166400
            else:
                money += 133254

        if job == "Accountant":
            if residence[-3:] == "USA":
                money += 68150
            else:
                money += 54575

        if job == "Programmer":
            if residence[-3:] == "USA":
                money += 84280
            else:
                money += 67492

    play_a_year()


quit()

#BITLIFE ALPHA v0.3
#By Mustafa Abdillahi
