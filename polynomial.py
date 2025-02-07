class Polynomial:
    def __init__(self, polynomial):
        self.polynomial = polynomial # list reprents a polynomial where polynomial[i] is the coefficient for that term

    def substitution(self, a: int) -> int: 
        # Direct Substitution
        sum = 0
        for i in range(len(self.polynomial)):
            sum += self.polynomial[i]*(a**(len(self.polynomial) - (i+1)))
        return sum
        
        # Synthetic Substitution 
        resid = self.polynomial[0]

        for i in range(1, len(self.polynomial)):
            resid *= a
            resid += self.polynomial[i]
        return resid
    
    def differentiate(self):
        deriviative = self.polynomial[:]
        for i in range(len(deriviative)):
            deriviative.append(deriviative[i] * (len(deriviative) - (i+1)))
        del deriviative[-1]
        return deriviative

    def differentiate_at_a_point(self, pt: int):
        return self.differentiate().substitution(pt)
    
    def integrate(self):
        return
    
    def definite_integral(self, a: int, b: int):
        return
    
    def poly_solver(self):
        #tryna do with rational root theorem; it dont work :(
        roots = []
        po = Polynomial(self.polynomial[:])
        p_factors = [i for i in range(1, abs(int((self.polynomial[-1]))+1)) if self.polynomial[-1] % i == 0]
        q_factors = [i for i in range(1, abs(int((self.polynomial[0]))+1)) if self.polynomial[0] % i == 0]
        print(p_factors)
        print(q_factors)

        possible_roots = {p/q for p in p_factors for q in q_factors}
        possible_roots.update(-p/q for p in p_factors for q in q_factors)
        
        for num in possible_roots:
            print(num, po.substitution(num))
            while -0.01 <= po.substitution(num) <= 0.01 :
                for i in range(1,len(po.polynomial)):
                    po.polynomial[i] = po.polynomial[i-1] * num + po.polynomial[i]
                del po.polynomial[-1]
                roots.append(num)

        return roots
    
        #newtons method



poly = Polynomial([1,4,4])

print(poly.poly_solver())