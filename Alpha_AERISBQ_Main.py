#import BQF

# Function that generates the first three hundreds primes and drops the first one hundred
def my_primes(primes_counter):
    primes = [2]
    n = 3
    while len(primes) < primes_counter:
        if n % 2 == 1:
            is_prime = True
            for i in range(2, n):
                if n % i == 0:
                    is_prime = False
                    break

            if is_prime:
                primes.append(n)

        n += 2

    """
    for k in range(len(primes)):
        print("Prime #:", k+1, primes[k])
    """

    for j in range(100):
        primes.pop(0)

    """
    print("*****Two hundreds:******")
    for k in range(len(primes)):
        print("Prime #:", k+1, primes[k])
    """

#my_primes(300)


class BQF:
    def __init__(self, a, r, s, n):
        self.a = a
        self.r = r
        self.s = s
        self.n = n


    def create_child(self, v ,a, r, s, b, c, n):
        self.v = v
        self.a = a
        self.r = r
        self.s = sself.b = b
        self.c = c
        self.n = n

    def create_children(self, v):
        self.v = v

myBQF = BQF()



# Function that remove any duplicated BQF
def removeDuplications(BQF):
    for i in range(len(v)):
        r = v[i]
        s = v[i]
        if r > s:
            r, s = s, r  # to swap
            v[i] = r
            v[i] = s

        found = False
        j = 0
        while j < len(v) and not found:
            r = v[i]
            s = v[i]



def factor(N, show_forms):
    if show_forms:
        print("Factoring N=", N)

    v1 = myBQF.v
    v2 = myBQF.v

    v1.append(myBQF(2, 1, 1, N))
    total_forms = 0

    round_number = 0
    found_solution = False

    while not found_solution:
        if show_forms:
            print("Round number =", round_number)
            round_number += 1
        v2.clear()
        for f in v1:
            if show_forms:
                print("\t", "(", a, "x+", r, ")", "(", a, "y+", s, ")=", N)

            total_forms += 1
            p = a + r
            q = 0
            if (N % p == 0):
                q = N / p
                found_solution = True

            else:
                q = a + s
                if (N % q == 0):
                    p = N / q
                    found_solution = True

            if found_solution:
                if p > q:
                    p, q = q, p
                    if show_forms:
                        print("\t\tSolution Found!")
                        print("\t\t", N, "=", p, "x", q)

                    """
                    else:
                        outfile goes here
                
                    """

                break

            create_children(v2)

        if show_forms:
            print("\t\tTotal Forms = ", total_forms)

        if not found_solution:
            removeDuplications(v2)
            v1, v2 =v2, v1

    v1.clear()
    v2.clear()

    """
    delete v1
    delete v2
    """

    """
    if outfile == nullptr:
        exit(0)
    """


factor(45113, True)


