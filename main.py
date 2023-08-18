def multiply(x, y):
    return x * y


def normal_value(a):
    if a < 5:
        return "Low Cardiac Output"
    elif a > 6:
        return "High Cardiac Output"
    else:
        return "Normal Cardiac Output"


SV = float(input("Stroke Volume in ml: "))
HR = float(input("Heart Rate in bpm: "))
pre = multiply(SV, HR)
result = pre * 0.001
print("Cardiac Output = " + str(result) + " L/min")

status = normal_value(result)
print("Cardiac Output Status: " + status)
