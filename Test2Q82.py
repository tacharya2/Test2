def getSum():
    token1 = 5
    token2 = 6

    def add1():
        token3 = 7
        token1 = 10
        # this token1 is hiding the value
        # defined in the parent subprogram

        def add2():
            def add3():
                token4 = 8
                return token1 + token2 + token3 + token4
            return add3()
        return add2()
    return add1()


print(getSum())