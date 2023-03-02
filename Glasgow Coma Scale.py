#PROJECT 1
#Implementing a medical calculator in Python

#Calculator reference-
#https://www.mdcalc.com/glasgow-coma-scale-score-gcs#why-use

eyeResponses = {
    "Not testable (NT)" : 0,
    "No eye opening (+1)" : 1,
    "To pain (+2)" : 2,
    "To verbal command (+3)": 3,
    "Spontaneously (+4)" : 4
 
}

verbalResponse = {
    "Not testable/intubated (NT)" : 0,
    "No verbal response (+1)" : 1,
    "Incomprehensible sounds (+2)" : 2, 
    "Inappropriate words (+3)" : 3,
    "Confused (+4)" : 4,
    "Oriented (+5)" : 5
}

motorResponses = {
    "Not testable (NT)" : 0,
    "No motor response (+1)" : 1,
    "Extension to pain (+2)" : 2,
    "Flexion to pain (+3)" : 3,
    "Withdrawal from pain (+4)" : 4,
    "Localizes pain (+5)" : 5,
    "Obeys commands (+6)" : 6
}

covidStatus = {
    "Confirmed negative" : 0,
    "Unlikely" : 1,
    "Suspected" : 2,
    "Confirmed positive" : 3
}

print("**** Glasgow Coma Scale/Score (GCS)**** \n")

print("## Best eye response \nIf local injury, edema, or otherwise unable to \nbe assessed, mark \"Not testable (NT)\"")
print("\noptions:")

keysEye = list(eyeResponses.keys())
counter = 0
for key in keysEye:
    print(counter, ": ", key,sep="")
    counter = counter + 1

inputEye = int(input("Select an option: "))

print("\n\n## Best verbal response\nIf intubated or otherwise unable to\nbe assessed, mark \"Not testable (NT)\"")
print("\noptions:")

keysVerb = list(verbalResponse.keys())
counter = 0
for key in keysVerb:
    print(counter, ": ", key,sep="")
    counter = counter + 1

inputVerb = int(input("Select an option: "))


print("\n\n## Best motor response\nIf on sedation/paralysis or unable to\nbe assessed, mark \"Not testable (NT)\"")
print("\noptions:")

keysMotor = list(motorResponses.keys())
counter = 0
for key in keysMotor:
    print(counter, ": ", key,sep="")
    counter = counter + 1

inputMotor = int(input("Select an option: "))


print("\n\n## Is this a COVID-19 patient?\nFor research purposes only; \nanswer does NOT impact results.")
print("\noptions:")

keysCovid = list(covidStatus.keys())
counter = 0
for key in keysCovid:
    print(counter, ": ", key,sep="")
    counter = counter + 1

inputCovid = int(input("Select an option: "))

score = inputEye + inputVerb + inputMotor

print("\nGlasgow Coma Score:", score, "points")
print("E(%d) V(%d) M(%d) and Covid status: %s" % (inputEye, inputVerb, inputMotor, keysCovid[inputCovid]))










