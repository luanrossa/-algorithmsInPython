"""
Fuzzy Logic Fuzzification Example

Fuzzy logic is a method of reasoning that deals with approximate values rather than exact ones.
It allows handling uncertainty by assigning degrees of membership (between 0 and 1) to linguistic terms.

In this code, a crisp temperature input is converted into fuzzy sets:
- 'Cold', 'Warm', and 'Hot'
using membership functions. The output shows the degree to which the input belongs
to each fuzzy category.
"""

# No external libraries are required

# Define membership functions
def cold(temp):
    if temp <= 0:
        return 1
    elif 0 < temp < 20:
        return (20 - temp) / 20
    else:
        return 0

def warm(temp):
    if 10 < temp < 30:
        return (temp - 10) / 20
    elif 30 <= temp <= 40:
        return (40 - temp) / 10
    else:
        return 0

def hot(temp):
    if temp <= 30:
        return 0
    elif 30 < temp < 40:
        return (temp - 30) / 10
    else:
        return 1

# Crisp input
temperature = 25

# Fuzzification
fuzzy_cold = cold(temperature)
fuzzy_warm = warm(temperature)
fuzzy_hot = hot(temperature)

print(f"Crisp Input: {temperature}°C")
print(f"Fuzzy Memberships:")
print(f"  Cold: {fuzzy_cold:.2f}")
print(f"  Warm: {fuzzy_warm:.2f}")
print(f"  Hot: {fuzzy_hot:.2f}")
