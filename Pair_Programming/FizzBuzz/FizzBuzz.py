def fizzbuzz_compute(maxnumb):
    fizzbuzz = []
    for i in range(0, maxnumb + 1):
        word = ''
        if i % 3 == 0:
            word += "Fizz"
        if i % 5 == 0:
            word += "Buzz"
        if i % 7 == 0:
            word += "Pop"
        if word == '':
            word += str(i)
        fizzbuzz.append(word)
    return fizzbuzz

print(fizzbuzz_compute(100))
