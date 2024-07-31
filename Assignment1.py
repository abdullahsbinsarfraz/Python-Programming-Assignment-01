# Age Assignments Based on the Riddle

Anton_age:int = 5
Beth_age:int= Anton_age + 6
Chen_age:int=Beth_age + 20
Drew_age:int= Chen_age + Anton_age
Ethan_age:int= Chen_age

print(f"Anton is {Anton_age}")
print(f"Beth is {Beth_age}")
print(f"Chen is {Chen_age}")
print(f"Drew is {Drew_age}")
print(f"Ethan is {Ethan_age}")

# 2. **Formatted String Interpolation**

name:str = "Alice"     
age:int = 30
city:str = "New York"
print(f"{name} is {age} years old and lives in {city}")

# 3. **String Manipulation**

s:str = "hElLo WoRlD"
print(s.capitalize())
print(s.upper())
print(s.lower())

# 4. **Substring Search**

s1:str ="the quick brown fox jumps over the lazy dog"
print(s1.index("fox"))
print(s1.count("the"))

# 5. **String Replacement**

s2:str ="I love programming in Python"
print(s2.replace("Python", "Java"))

# 6. **String Splitting and Joining**

s3:str ="apple,banana,cherry,dates"
x = s3.split(",")
print(x)
print(" ".join(x))

# 7. **String Stripping and Justifying**

s4 ="   Python is fun!   "
x = s4.strip()
print(x)
print(x.ljust(20, "*"))
print(x.rjust(20, "*"))

# **Convert an integer to its binary representation**

num:int = 45
print(bin(num))

# **Calculate Powers of Numbers.**

base:int = 3
exponent:int = 4
print(base**exponent)

# 10. **Round floating-point numbers**

value:float = 12.34567
print(round(value))
print(round(value, 2))
