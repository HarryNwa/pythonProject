eiResponses = []
eiAResponses = 0
eiBResponses = 0
snResponses = []
snAResponses = 0
snBResponses = 0
tfResponses = []
tfAResponses = 0
tfBResponses = 0
jpResponses = []
jpAResponses = 0
jpBResponses = 0


def entity():
    name = input("What's your name? ")
    if name.casefold():
        print("Continue")
    else:
        print("wrong input")
        entity()
    print("1. A. Expend energy, enjoy groups.\t\t\t B. Conserve energy, one-on-one\n")
    response = input("Choose your answer")
    global eiResponses
    eiResponses.append("Dear " + name + ", you chose")
    if response == "A":
        eiResponses.append("A. Expend energy, enjoy groups.")
        global eiAResponses
        eiAResponses += 1
    elif response == "B":
        eiResponses.append("B. Conserve energy, one-on-one.")
        global eiBResponses
        eiBResponses += 1
    else:
        print("I know this is an error. Please retry again")
        entity()


def question_2():
    global snResponses
    response = input("2. A. Interpret literally. \t\t\t B. Look for meaning and possibilities.\n")
    if response == "A":

        snResponses.append("A. Interpret literally.")
        global snAResponses
        snAResponses += 1
    elif response == "B":
        snResponses.append("B. Look for meaning and possibilities.")
        global snBResponses
        snBResponses += 1
    else:
        print("I know this is an error. Please retry again.")
        question_2()


def question_3():
    global tfResponses
    global tfAResponses, tfBResponses
    response = input("3. A. Logical, thinking, questioning. \t\t\t B. Empathetic, feeling, accommodating")
    if response == ("A"):
        tfResponses.append("A.  Logical, thinking, questioning.")
        tfAResponses += 1
    elif response == ("B"):
        tfResponses.append("B. Empathetic, feeling, accommodating.")
        tfBResponses += 1
    else:
        print("I know this is an error. Please retry again.")
        question_3()


def question_4():
    global jpAResponses, jpBResponses
    response = input("4. A. Organized, orderly. \t\t\t B. Flexible, adaptable")
    if response == ("A"):
        global jpAResponses
        jpResponses.append("A. Organized, orderly.")
        jpAResponses += 1
    elif response == ("B"):
        jpResponses.append("B. Flexible, adaptable.")
        jpBResponses += 1
    else:
        print("I know this is an error. Please retry again.")
        question_4()


def question_5():
    global eiAResponses, eiBResponses
    response = input("5. A. More outgoing, think out loud. \t\t\t B. More reserved, think to yourself.")
    if response == ("A"):
        global eiAResponses
        eiResponses.append("A.  More outgoing, think out loud.")
        eiAResponses += 1
    elif response == ("B"):
        eiResponses.append("B.More reserved, think to yourself.")
        eiBResponses += 1
    else:
        print("I know this is an error. Please retry again.")
        question_5()


def question_6():
    global snAResponses, snBResponses
    response = input("6. A. Practical, realistic, experiential. \t\t\t B. Imagination, innovative, theoretical.")
    if response == ("A"):
        global snResponses
        snResponses.append("A. Practical, realistic, experiential.")
        snAResponses += 1
    elif response == ("B"):
        snResponses.append("B. Imagination, innovative, theoretical.")
        snBResponses += 1
    else:
        print("I know this is an error. Please retry again.")
        question_6()


def question_7():
    global tfAResponses, tfBResponses
    response = input("7. A. Candid, straight forward, frank. \t\t\t B. Tactful, kind, encouraging.")
    if response == ("A"):
        tfResponses.append("A. Candid, straight forward, frank.")
        tfAResponses += 1
    elif response == ("B"):
        tfResponses.append("B. Tactful, kind, encouraging.")
        tfBResponses += 1
    else:
        print("I know this is an error. Please retry again.")
        question_7()


def question_8():
    global jpAResponses, jpBResponses
    response = input("8. A. Plan, schedule. \t\t\t B. Unplanned, spontaneous")
    if response == ("A"):
        global jpResponses
        jpResponses.append("A.  Plan, schedule.")
        jpAResponses += 1
    elif response == ("B"):
        jpResponses.append("B. Unplanned, spontaneous.")
        jpBResponses += 1
    else:
        print("I know this is an error. Please retry again.")
        question_8()


def question_9():
    global eiAResponses, eiBResponses
    response = input("9. A. Seek many tasks, public activities, interaction with others. \t\t\t B. Seek private, " +
                     "solitary activities with quiet to concentrate.")
    if response == ("A"):
        global eiResponses
        eiResponses.append("A. Seek many tasks, public activities, interaction with others.")
        eiAResponses += 1
    elif response == ("B"):
        eiResponses.append("B. Seek private, solitary activities with quiet to concentrate.")
        eiBResponses += 1
    else:
        print("I know this is an error. Please retry again.")
        question_9()


def question_10():
    global snAResponses, snBResponses
    response = input("10. A. Standard, usual, conventional. \t\t\t B. Different, novel, unique.")
    if response == ("A"):
        global snResponses
        snResponses.append("A. Standard, usual, conventional.")
        snAResponses += 1
    elif response == ("B"):
        snResponses.append("B. Different, novel, unique.")
        snBResponses+=1
    else:
        print("I know this is an error. Please retry again.")
        question_10()


def question_11():
    global tfAResponses, tfBResponses
    response = input("11. A. Firm, tend to criticize, hold the line. \t\t\t B. Gentle, tend to appreciate, conciliate.")
    if response == ("A"):
        global tfResponses
        tfResponses.append("A. Firm, tend to criticize, hold the line.")
        tfAResponses+=1
    elif response == ("B"):
        tfResponses.append("B. Gentle, tend to appreciate, conciliate.")
        tfBResponses += 1
    else:
        print("I know this is an error. Please retry again.")
        question_11()


def question_12():
    global jpAResponses, jpBResponses
    response = input("12. A. Regulated, structured. \t\t\t B. Easygoing, live  and let live.")
    if response == ("A"):
        global jpAResponses
        jpResponses.append("A. Regulated, structured.")
        jpAResponses += 1
    elif response == ("B"):
        jpResponses.append("B. Easygoing, live  and let live.")
        jpBResponses += 1
    else:
        print("I know this is an error. Please retry again.")
        question_12()


def question_13():
    global eiAResponses, eiBResponses
    response = input("13. A. External, communicative, express yourself. \t\t\t B. Internal, reticent, keep to yourself.")
    if response == ("A"):
        global eiResponses
        eiResponses.append("A. External, communicative, express yourself.")
        eiAResponses += 1
    elif response == ("B"):
        eiResponses.append("B. Internal, reticent, keep to yourself.")
        eiBResponses += 1
    else:
        print("I know this is an error. Please retry again.")
        question_13()


def question_14():
    global snAResponses, snBResponses
    response = input("14. A. Focus on here-and-now. \t\t\t B. Look to the future, global perspective, big picture.")
    if response == ("A"):
        global snResponses
        snResponses.append("A. Focus on here-and-now.")
        snAResponses += 1
    elif response == ("B"):
        snResponses.append("B. Look to the future, global perspective, big picture.")
        snBResponses += 1
    else:
        print("I know this is an error. Please retry again.")
        question_14()


def question_15():
    global tfAResponses, tfBResponses
    response = input("15. A. Tough minded, just. \t\t\t B. Tender-hearted, merciful.")
    if response == ("A"):
        global tfResponses
        tfResponses.append("A. Tough minded, just.")
        tfAResponses += 1
    elif response == ("B"):
        tfResponses.append("B. Tender-hearted, merciful.")
        tfBResponses += 1
    else:
        print("I know this is an error. Please retry again.")
        question_15()

def question_16():
    global jpAResponses, jpBResponses
    response = input("16. A. Preparation, plan ahead. \t\t\t B. Go with the flow, adapt as you go.")
    if response == ("A"):
        global jpResponses
        jpResponses.append("A. Preparation, plan ahead.")
        jpAResponses += 1
    elif response == ("B"):
        jpResponses.append("B. Go with the flow, adapt as you go.")
        jpBResponses += 1
    else:
        print("I know this is an error. Please retry again.")
        question_16()

def question_17():
    global eiAResponses, eiBResponses
    response = input("17. A. Active, initiate.  \t\t\t  B. Reflective, deliberate.")
    if response == ("A"):
        global eiResponses
        eiResponses.append("A. Active, initiate.")
        eiAResponses += 1
    elif response == ("B"):
        eiResponses.append("B. Reflective, deliberate.")
        eiBResponses += 1
    else:
        print("I know this is an error. Please retry again.")
        question_17()


def question_18():
    global snAResponses, snBResponses
    response = input("18. A. Facts, things, what is. \t\t\t B. Ideas, dreams, 'what could be', philosophical.")
    if response == ("A"):
        snResponses.append("A. Facts, things, what is.")
        snAResponses += 1
    elif response == ("B"):
        snResponses.append("B. Ideas, dreams, 'what could be', philosophical.")
        snBResponses += 1
    else:
        print("I know this is an error. Please retry again.")
        question_18()


def question_19():
    global tfAResponses, tfBResponses
    response = input("19. A. Matter of fact, issue oriented. \t\t\t B. Sensitive, people-oriented, compassionate.")
    if response == ("A"):
        global tfResponses
        tfResponses.append("A. Matter of fact, issue oriented.")
        tfAResponses += 1
    elif response == ("B"):
        tfResponses.append("B. Sensitive, people-oriented, compassionate.")
        tfBResponses += 1
    else:
        print("I know this is an error. Please retry again.")
        question_19()

def question_20():
    global jpAResponses, jpBResponses
    response = input("20. A. Control, govern. \t\t\t B. Latitude, freedom.")
    if response == ("A"):
        global jpResponses
        jpResponses.append("A. Control, govern.")
        jpAResponses += 1
    elif response == ("B"):
        jpResponses.append("B. Latitude, freedom.")
        jpBResponses += 1
    else:
        print("I know this is an error. Please retry again.")
        question_20()

def extrovertedEVsIntrovertedI():
    print()
    for row in eiResponses:
        print(row)


    print("Choice A is selected " + str(eiAResponses) + " time(s)")
    print("Choice B is selected " + str(eiBResponses) + " time(s)")


def sensingSVsIntuitiveI():
    print()
    for row in snResponses:
        print(row)


    print("Choice A is selected " + str(snAResponses) + " time(s)")
    print("Choice B is selected " + str(snBResponses) + " time(s)")


def thinkingTVsFeeling():
    print()
    for row in tfResponses:
        print(row)

    print("Choice A is selected " + str(tfAResponses) + " time(s)")
    print("Choice B is selected " + str(tfBResponses) + " time(s)")



def judgingJVsPerspective():
    print()
    for row in jpResponses:
        print(row)

    print("Choice A is selected " + str(jpAResponses) + " time(s)")
    print("Choice B is selected " + str(jpBResponses) + " time(s)")



def typesOfPersonalities():
    print()
    personality = ""
    if eiAResponses > eiBResponses:
        personality = personality + "E"
    else:
        personality = personality + "I"

    if snAResponses > snBResponses:
        personality = personality + "S"
    else:
        personality = personality + "N"

    if tfAResponses > tfBResponses:
        personality = personality + "T"
    else:
        personality = personality + "F"

    if jpAResponses > jpBResponses:
        personality = personality + "J"
    else:
        personality = personality + "P"

    print("Your type of personality can be represented as " + personality)

    match (personality):
        case "INFP":
            print("A Mediator (INFP) is someone who possesses the Introverted, Intuitive, \n" +
                "Feeling, and Prospecting personality traits. These rare personality types tend to be quiet, \n" +
                "open-minded, and imaginative, and they apply a caring and creative approach to everything they do.")
        case "INTJ":
            print("An Architect (INTJ) is a person with the Introverted, Intuitive, \n" +
                "Thinking, and Judging personality traits. These thoughtful tacticians love perfecting the \n" +
                "details of life, applying creativity and rationality to everything they do. Their inner world \n" +
                "is often a private, complex one.")
        case "INTP":
                print("A Logician (INTP) is someone with the Introverted, Intuitive, Thinking, and \nProspecting " +
                        "personality traits. These flexible thinkers enjoy taking an unconventional approach to many \n" +
                        "aspects of life. They often seek out unlikely paths, mixing willingness to experiment with \n" +
                        "personal creativity.")
        case "ENTJ":
                print("A Commander (ENTJ) is someone with the Extraverted, Intuitive, Thinking, and \nJudging " +
                        "personality traits. They are decisive people who love momentum and accomplishment. They \ngather " +
                        "information to construct their creative visions but rarely hesitate for long before acting \non " +
                        "them.")
        case "ENTP":
                print("A Debater (ENTP) is a person with the Extraverted, Intuitive, Thinking, and \n" +
                        "Prospecting personality traits. They tend to be bold and creative, deconstructing and \n" +
                        "rebuilding ideas with great mental agility. They pursue their goals vigorously despite \nany " +
                        "resistance they might encounter.")
        case "INFJ":
                print("An Advocate (INFJ) is someone with the Introverted, Intuitive, Feeling, and \nJudging " +
                        "personality traits. They tend to approach life with deep thoughtfulness and imagination. \n" +
                        "Their inner vision, personal values, and a quiet, principled version of humanism guide \nthem in " +
                        "all things.")
        case "ENFJ":
                print("A Protagonist (ENFJ) is a person with the Extraverted, Intuitive, \n" +
                "Feeling, and Judging personality traits. These warm, forthright types love helping others, and \n" +
                "they tend to have strong ideas and values. They back their perspective with the creative energy \n" +
                "to achieve their goals.")
        case "ENFP":
                print("A Campaigner (ENFP) is someone with the Extraverted, Intuitive, Feeling, \n" +
                        "and Prospecting personality traits. These people tend to embrace big ideas and actions that \n" +
                        "reflect their sense of hope and goodwill toward others. Their vibrant energy can flow in many \n" +
                        "directions.")
        case "ISTJ":
                print("A Logistician (ISTJ) is someone with the Introverted, Observant, \n" +
                "Thinking, and Judging personality traits. These people tend to be reserved yet willful, with a \n" +
                "rational outlook on life. They compose their actions carefully and carry them out with methodical \n" +
                "purpose.")
        case "ISFJ":
                print("A Defender (ISFJ) is someone with the Introverted, Observant, Feeling, \n" +
                "and Judging personality traits. These people tend to be warm and unassuming in their own steady way." +
                " \nThey’re efficient and responsible, giving careful attention to practical details in their daily \n" +
                "lives.")
        case "ESTJ":
                print("An Executive (ESTJ) is someone with the Extraverted, Observant, \n" +
                "Thinking, and Judging personality traits. They possess great fortitude, emphatically following \n" +
                "their own sensible judgment. They often serve as a stabilizing force among others, able to offer \n" +
                "solid direction amid adversity.")
        case "ESFJ":
                print("A Consul (ESFJ) is a person with the Extraverted, Observant, Feeling, \n" +
                "and Judging personality traits. They are attentive and people-focused, and they enjoy taking part \n" +
                "in their social community. Their achievements are guided by decisive values, and they willingly \n" +
                "offer guidance to others.")
        case "ISTP":
                print("A Virtuoso (ISTP) is someone with the Introverted, Observant, Thinking, \n" +
                "and Prospecting personality traits. They tend to have an individualistic mindset, pursuing goals \n" +
                "without needing much external connection. They engage in life with inquisitiveness and personal \n" +
                "skill, varying their approach as needed.")
        case "ISFP":
                print("An Adventurer (ISFP) is a person with the Introverted, Observant, \n" +
                "Feeling, and Prospecting personality traits. They tend to have open minds, approaching life, \n" +
                "new experiences, and people with grounded warmth. Their ability to stay in the moment helps them \n" +
                "uncover exciting potentials.")
        case "ESTP":
                print("An Entrepreneur (ESTP) is someone with the Extraverted, Observant, \n" +
                "Thinking, and Prospecting personality traits. They tend to be energetic and action-oriented, \n" +
                "deftly navigating whatever is in front of them. They love uncovering life’s opportunities, \n" +
                "whether socializing with others or in more personal pursuits.")
        case "ESFP":
                print("An Entertainer (ESFP) is a person with the Extraverted, Observant, \n" +
                "Feeling, and Prospecting personality traits. These people love vibrant experiences, engaging in \n" +
                "life eagerly and taking pleasure in discovering the unknown. They can be very social, often \n" +
                "encouraging others into shared activities.")

    print()

# entity()
# def test_1():
#     name = input("what is your name")
#     if name.isalpha():
#         return True
#     else:
#         print("wrong input")
#         test_1()
#
# def test_2():
#     name = input("what is your favourite hobbie")
#     if name.isalpha():
#         return True
#     else:
#         print("wrong input")
#         test_1()
#
# test_1()
# test_2()
def main():
    entity()
    question_2()
    question_3()
    question_4()
    question_5()
    question_6()
    question_7()
    question_8()
    question_9()
    question_10()
    question_11()
    question_12()
    question_13()
    question_14()
    question_15()
    question_16()
    question_17()
    question_18()
    question_19()
    question_20()
    extrovertedEVsIntrovertedI()
    sensingSVsIntuitiveI()
    thinkingTVsFeeling()
    judgingJVsPerspective()
    typesOfPersonalities()




if __name__ == "__main__":
    main()
