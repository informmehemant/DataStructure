def funChallenge(input):
    a = 10  # o(1)
    a = 50 + 3  # o(1)
    for i in range(len(input)):  # o(n)
        anotherFuntion()  # o(n)
        strange = True  # o(n)
        a += 1  # o(n)
        return a  # o(1)


funChallenge([1, 2, 4, 5, 6])
# what is the bigONotations ??

# O(3 + 4n)