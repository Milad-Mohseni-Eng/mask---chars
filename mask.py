string = "Python programming"

result = ""

for x in string:
    if x.lower() in "pom":
        result += "*"

    else:
        result += x

print(result)
