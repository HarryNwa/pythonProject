student = ["male", "female", "female", "Male", "male", "male", "Female", "male", "female", "male", "female", "male",
           "female"]


def check_gender(gender_list):
    m_match = {"male": 0, "female": 0}

    for gender in gender_list:
        if gender.casefold() == "male":
            m_match ["male"] += 1
        if gender.casefold() == "female":
            m_match ["female"] += 1

    return list(m_match.items())


print(check_gender(student))


