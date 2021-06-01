from sympy import *
import numpy as np
import scipy as sy
import random
import math

x, y, r1, a, b = symbols('x y r1 a b')
pl = Symbol('+')
pm = Symbol('±', real=True)


def to_latex_wrapper(exprs, no_newline):
    newline = ''
    for i in range(no_newline):
        newline += '\\ '
    expr = latex(exprs)
    expr = '\('+expr+newline+'\)'

    return expr


def inline_wrapper(exprs):
    expr = latex(exprs)
    expr = '\\left('+expr+'\\right)'

    return expr


def pm(a, b):
    x = str(a)
    y = str(b)
    temp = x+'\pm '+y
    return temp

# from random import choices
# population = [1, 2, 3, 4, 5, 6]
# weights = [0.1, 0.05, 0.05, 0.2, 0.4, 0.2]
# choices(population, weights)


def genExc(a, b):
    x = random.randint(a, b)
    while x == 0:
        x = random.randint(a, b)
    return x


def gen(a, b):
    x = random.randint(a, b)
# while x == 0:
# x = random.randint(-5, 6)
    return x

# possible for fractional roots


def genPoly(no_fact):
    polynom = a*x+b
    polynom = polynom.subs({a: genExc(-1, 2), b: gen(-2, 1)})
    for i in range(no_fact-1):
        polynom *= (a*x+b)
        polynom = polynom.subs({a: genExc(-1, 2), b: genExc(-1, 3)})
        polynom = expand(polynom)
    return polynom

# integer roots only


def gen_polynomial():

    degree = gen(3, 5)
    rationalRoots = [gen(-3, 5) for i in range(degree)]
    factoredForm = (x-r1)
    factoredForm = factoredForm.subs({r1: rationalRoots[0]})
    for i in range(degree-1):
        factoredForm *= (x-r1)
        factoredForm = factoredForm.subs({r1: rationalRoots[i+1]})

    factored_form = 'y = '+str(factoredForm)
    gen_form = 'y = '+str(expand(factoredForm))

    return (factored_form, gen_form, rationalRoots, degree)


def gen_deg(operation):
    if operation == 'product':
        deg = [2, gen(1, 2)]
    elif operation == 'add' or operation == 'minus':
        deg = [gen(2, 3), gen(2, 3)]
    else:
        deg = [gen(3, 4), gen(0, 1)]

    return deg


def operations(operation):

    op = {'add': '+',
          'minus': '-',
          'product': '*',
          'quotient': '/'
          }
    prod = []
    deg = gen_deg(operation)

    for i in deg:
        prod.append(genPoly(i+1))

    polEq = inline_wrapper(prod[0])+op[operation]+inline_wrapper(prod[1])
    # polEq = '('+str(prod[0])+')'+op[operation]+'('+str(prod[1])+')'
    if operation == 'quotient':
        quo_rem = polys.polytools.div(prod[0], prod[1])
        expanded = quo_rem[0] + (quo_rem[1]/prod[1])
        constant_term = quo_rem[0].subs({x: 0})
        deg_ans = degree(expanded, gen=0)
        lead_coef = polys.polytools.LC(expanded)
        leading_term = polys.polytools.LT(expanded)
        remainder = '' if (quo_rem[1]/prod[1]
                           ) == 0 else '+'+str(quo_rem[1]/prod[1])
        expanded = str(quo_rem[0]) + remainder
    else:
        if operation == 'product':
            expanded = expand(prod[0]*prod[1])
        elif operation == 'add':
            expanded = expand(prod[0]+prod[1])
        elif operation == 'minus':
            expanded = expand(prod[0]-prod[1])

        constant_term = expanded.subs({x: 0})
        deg_ans = degree(expanded, gen=0)
        lead_coef = polys.polytools.LC(expanded)
        leading_term = polys.polytools.LT(expanded)
        expanded = str(expanded)

    properties = {'Simpliest Form:   ': expanded,
                  'Leading Term:   ': leading_term,
                  'Degree:  ': deg_ans,
                  'Leading Coefficient:   ': lead_coef,
                  'Constant Term:   ': constant_term

                  }
    props = list(properties.keys())

    for each in props:
        properties[each] = latex(properties[each])
    anskeys = [x + latex(properties[x]) for x in props]

    return (polEq, props, anskeys)


# a, b, c = operations('quotient')
# print(a)
# print(b)
# print(c)


def factor_remainder_theorem():
    return


def fta_drs_rrt():

    factored_form, gen_form, rationalRoots, degree = gen_polynomial()

    properties = {'Fundamental Theorem of Algebra:  ': 'Atmost ' + str(degree),
                  "Descartes' Rule of Sign:   ": '',
                  'Rational Root Theorem:   ': '',
                  'Actual Roots:     ': rationalRoots
                  }

    prop_keys = properties.keys()

    for each in prop_keys:
        properties[each] = to_latex_wrapper(properties[each], 4)

    props = [x + str(properties[x]) for x in prop_keys]

    return (gen_form, properties, props)


def finding_roots():

    factored_form, gen_form, rationalRoots, degree = gen_polynomial()
    properties = {'FTA:  ': 'Atmost ' + str(degree),
                  'roots:   ': rationalRoots,
                  'factored form:   ': factored_form
                  }

    prop_keys = properties.keys()

    for each in prop_keys:
        properties[each] = to_latex_wrapper(properties[each], 1)

    props = [x + str(properties[x]) for x in prop_keys]

    return (gen_form, properties, props)


def pol_ineq():
    # solveset(x**2-3*x+2 < 0, x, S.Reals)
    degree = gen(3, 5)
    rationalRoots = [gen(-3, 5) for i in range(degree)]
    factoredForm = (x-r1)
    factoredForm = factoredForm.subs({r1: rationalRoots[0]})
    for i in range(degree-1):
        factoredForm *= (x-r1)
        factoredForm = factoredForm.subs({r1: rationalRoots[i+1]})

    factored_form = 'y = '+latex(factoredForm)
    gen_form = 'y = '+latex(expand(factoredForm))

    return (factored_form, gen_form, rationalRoots, degree)


def main(subTopic, items):
    given_question_ans = []
    if subTopic == 'Identifying Polynomial':
        pass

    elif subTopic == 'Adding and Subtracting Polynomial':
        for i in range(items):
            operation = 'add' if i <= i//2 else 'minus'
            qiven, question, ans = operations(operation)
            item = [qiven, question, ans]
            given_question_ans.append(item)

    return given_question_ans
