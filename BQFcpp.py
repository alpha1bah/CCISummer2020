from BQF import BQF

def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)



def reduce(v1, v2, v3, v4):
    g = GCD(abs(v1), GCD(abs(v2), GCD(abs(v3), GCD(abs(v4)))))
    v1 /= g
    v2 /= g
    v3 /= g
    v4 /= g

def reduce(v1, v2, v3, v4, v5):
    g = GCD(abs(v1), GCD(abs(v2), GCD(abs(v3), GCD(abs(v4), GCD((V5))))))
    v1 /= g
    v2 /= g
    v3 /= g
    v4 /= g
    v5 /= g


myBQF = BQF
myBQF.create_child(v, a, r, s, b, c, n):


    # Step 1 Trivial Rejection
    num = n - r * s - b * c - b * s - c * r
    if num % a != 0:
        return
    else:
        return n1 = num / a
        This BQF = BQF(a, r+b, s+c, n)


    # Step 2: uv substitution
    ThisBQF.a2 = a
    ThisBQF.b2 = c + s
    ThisBQF.c2 = b + r
    ThisBQF.n2 = n1
    reduce(ThisBQF.a2, ThisBQF.b2,    ThisBQF.c2 ,ThisBQF.n2)


    #Step3: L-substitution
    ThisBQF.a3 = -ThisBQF.a2
    ThisBQF.b3 = ThisBQF.a2
    ThisBQF.c3 = -2 * (ThisBQF.b2 - ThisBQF.a2)
    ThisBQF.d3 = 2 * (ThisBQF.b2 + ThisBQF.a2)
    ThisBQF.n3 = 4 * ThisBQF.n2
    reduce(ThisBQF.a3, ThisBQF.b3, ThisBQF.c3, ThisBQF.d3, ThisBQF.n3)


    #Step4: Reduction
    ThisBQF.n4 = 4 * ThisBQF.a3
    ThisBQF.b4 = -4 * ThisBQF.a3
    ThisBQF.c4 = -2 * ThisBQF.c3
    ThisBQF.d4 = ThisBQF.c3 + ThisBQF.d3
    ThisBQF.n4 = ThisBQF.n3
    reduce(ThisBQF.n4, ThisBQF.b4, ThisBQF.c4, ThisBQF.d4, ThisBQF.n4)


    g = GCD(ThisBQF.n4, GCD(abs(ThisBQF.a4), abs(ThisBQF.c4)))
    ThisBQF.n4 /= g
    ThisBQF.n4 /= g
    ThisBQF.n4 /= g


    if ThisBQF.n4 < 0:
        return v.append(ThisBQF)



myBQF.create_children(v):
    create_child(v, a * 2, r, s, 0, 0, n)
    create_child(v, a * 2, r, s, a, a, n)
    create_child(v, a * 2, r, s, a, 0, n)
    create_child(v, a * 2, r, s, 0, a, n)



