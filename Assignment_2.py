from typing import List


names = ["superman", "baa", "spa","ironman"]

for i in range(len(names)):
    if len(names[i]) > 5:
        if "n" in names[i] or "N" in names[i]:
            print(len(names[i]))

while len(names) >= 1:
    names.pop()
print(names)