# Aaron Stacey - 
from math import ceil

# Dictionary key: "symptom" : "weight"
symptoms = {
    "COUGH" : 2,
    "FEVER" : 2,
    "FATIGUE" : 1,
    "SORE THROAT" : 2,
    "HEADACHES" : 1,
    "RUNNY NOSE" : 1,
    "SHORTNESS OF BREATH" : 3,
    "BODY ACHES" : 1,
    "LOSS OF TASTE AND/OR SMELL" : 10,
    "RED SWOLLEN EYES" : 10
}


def questionnare():
    """Asks the user questions about the symptoms he is having and calculates the percentage chance"""
    total = 0
    l_symptoms = list(symptoms)
    l_weights = list(symptoms.values())
    for i, n in enumerate(l_symptoms):
        print()
        print(f"Have you experienced the following symptom '{n}'")
        while True:
            uIn = input("Type in 'yes' or 'no' > ").upper()            
            if uIn == "YES":
                total += l_weights[i]
                break
            elif uIn == "NO":
                break

    total = ceil(total / sum(symptoms.values()) * 100)
    return total


def main():
    """Starts the program"""
    per = questionnare()
    print()
    print(f"There is a {per}% of you having covid.")
    print(f"You should self isolate and get a PCR test.") if per > 45 else print("You dont need to get a PCR test.")


if __name__ == "__main__":
    main()
