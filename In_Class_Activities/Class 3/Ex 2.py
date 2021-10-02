Height = float(input("Altura (cm) : "))
Weight = float(input("Peso (kg) : "))

BMI = Weight/(Height/100)**2

print ("Tu índice de masa corporal es: " + str(round(BMI,2)))