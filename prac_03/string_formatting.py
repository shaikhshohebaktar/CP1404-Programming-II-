"""
CP1404 Practical 03 - String Formatting
"""
name = "Gibson L-5 CES"
year = 1922
cost = 16035.999
print(f"{year} {name} for about ${cost:,.0f}!")
for n in range(0, 11):
    print(f"2 ^ {n:2} is {2 ** n:4}")
