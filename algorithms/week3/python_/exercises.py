# Exercise 1

def order_price(kilos):
  subtotal = kilos * 3
  if subtotal > 50:
    subtotal -= 1.50

  return int((subtotal + 4.99) * 100)

# Exercise 2

def maximum_heart_rate(age):
  return int(208 - (0.7 * age))

def training_zone(age, rate):
  m = maximum_heart_rate(age)

  if rate >= 0.9 * m:
    print("Interval training")
  elif rate >= 0.7 * m and rate < 0.9 * m:
    print("Threshold training")
  elif rate >= 0.5 * m and rate < 0.7 * m:
    print("aerobic training")
  else:
    print("Couch potato")

# Exercise 3:

def is_valid_password(password, min_length, has_upper, has_lower, has_numeric):
  if len(password) < min_length:
    return False
  # ---
  if has_upper and not any(char.isupper() for char in password):
    return False
  
  if has_lower and not any(char.islower() for char in password):
    return False
  
  if has_numeric and not any(char.isnumeric() for char in password):
    return False
  
  if not all(char.isalnum() for char in password):
    return False
  
  return True

test_cases = [
    {
        "password": "hello",
        "min_length": 4,
        "require_upper": False,
        "require_lower": False,
        "require_digit": False,
        "expected": True,
        "message": "hello is longer than 4 characters so should be true."
    },
    {
        "password": "hel",
        "min_length": 4,
        "require_upper": False,
        "require_lower": False,
        "require_digit": False,
        "expected": False,
        "message": "hello is shorter than minimum which is 4"
    },
    {
        "password": "Hello",
        "min_length": 4,
        "require_upper": True,
        "require_lower": False,
        "require_digit": False,
        "expected": True,
        "message": "Hello contains a capital letter and upper flag is raised."
    },
    
    {
        "password": "hello",
        "min_length": 4,
        "require_upper": False,
        "require_lower": False,
        "require_digit": False,
        "expected": True,
        "message": "hello is longer than 4 characters so should be true."
    },]

for case in test_cases:
    result = is_valid_password(
        case["password"],
        case["min_length"],
        case["require_upper"],
        case["require_lower"],
        case["require_digit"]
    )
    assert result == case["expected"], case["message"]