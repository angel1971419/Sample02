def calc_bmi(weight, height):
    return round(weight/(height**2))

def bmi_to_result(bmi):
    if bmi < 18.5:
        return "痩せ気味"
    elif (bmi >= 18.5) and (bmi < 25):
        return "標準"
    elif (bmi >= 25) and (bmi < 30):
        return "肥満気味"
    else:
        return "肥満"

bmi = calc_bmi(73.8, 1.57)

result = bmi_to_result(bmi)

print("BMI: ", bmi)
print("判定結果: ", result)
