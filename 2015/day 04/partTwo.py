import hashlib

questionInput = "bgvyzdsv"
test = 0

while 1:
    testInput = questionInput + str(test)

    if hashlib.md5(testInput.encode()).hexdigest().startswith("000000"):
        print(test)
        break

    test += 1