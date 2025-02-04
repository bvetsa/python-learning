class Polynomial:
    def __init__(self, polynomial):
        self.polynomial = polynomial # list reprents a polynomial where polynomial[i] is the coefficient for that term

    def substitution(self, a: int) -> int: 
        # Direct Substitution
        '''
        sum = 0
        for i in range(len(self.polynomial)):
            sum += self.polynomial[i]*(a**(len(self.polynomial) - (i+1)))
        return sum
        '''
        # Synthetic Substitution 
        resid = self.polynomial[0]

        for i in range (1, len(self.polynomial)):
            resid *= a
            resid += self.polynomial[i]
        return resid

poly = Polynomial([1,1,1])

print(poly.substitution(1))