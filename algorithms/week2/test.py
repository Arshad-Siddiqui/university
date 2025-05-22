# marks = [60, 80, 60, 75]
# for grade in marks:
#   print(grade)

## 2.4 Exercises
## https://onlinestudy.york.ac.uk/courses/1637/pages/2-dot-4-programming-exercises?module_item_id=128902

# kilos = float(input("how many kilos of nanas you want?\n"))
# price = kilos * 3

# if price > 50:
#   print(price + 3.49)
# else:
#   print(f"Total is {price + 4.99}")

## Exercise 2:

age = int(input("Age: "))
rate = int(input("Rate: "))

max_rate = 208 - (0.7 * age)

if rate >= 0.9 * max_rate:
    print("Interval training")
elif 0.7 * max_rate <= rate < 0.9 * max_rate:
    print("Threshold training")
elif 0.5 * max_rate <= rate < 0.7 * max_rate:
    print("Aerobic training")
else:
    print("Couch potato")

## There are a couple other challenges which look fun
## but i cba for now.