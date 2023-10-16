numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sr_ar = sum(filter(None, numbers))/len(numbers)
for i in range(len(numbers)):
    if numbers[i] is None:
        numbers[i] = sr_ar
    else:
        continue

print("Измененный список:", numbers)
