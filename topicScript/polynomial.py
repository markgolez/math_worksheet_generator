from sympy import *
from sympy.abc import x, y, a, b, c, d, e, f, g, h
from topicsVariable import *
import numpy as np
import scipy as sy
from random import randint
import math

r1 = symbols('r1')
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
    expr = '$\\left('+expr+'\\right)$'

    return expr


def pm(p, q):
    x = str(p)
    y = str(q)
    temp = x+'\pm '+y
    return temp

# from random import choices
# population = [1, 2, 3, 4, 5, 6]
# weights = [0.1, 0.05, 0.05, 0.2, 0.4, 0.2]
# choices(population, weights)


def genExc(p, q, r=0, *args):
    x = randint(p, q)
    while x == r or x in args:
        x = randint(p, q)
    return x


def gen(p, q):
    x = randint(p, q)
    return x


# possible for fractional roots
def genPoly(no_fact, frac_roots=False):
    if frac_roots == False:
        p = genExc(-1, 2)
        q = gen(-2, 1)
    else:
        p = genExc(-3, 2, 0, 1)
        q = genExc(-3, 2, 0, 1)
    polynom = a*x+b
    polynom = polynom.subs({a: p, b: q})
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


def gen_deg(operation, level):
    if operation == 'multiply':
        deg = [2, gen(1, 2)]
    elif operation == 'add' or operation == 'minus':
        deg = [gen(2, 3), gen(2, 3)]
    else:
        if level == 'easy':
            deg = [gen(3, 4), gen(1, 1)]
        elif level == 'hard':
            deg = [gen(3, 4), gen(1, 2)]
    return deg


def operations(operation, level):

    op = {'add': '$+$',
          'minus': '$-$',
          'multiply': '$*$',
          'divide': '$\div$'
          }
    expr = []
    deg = gen_deg(operation, level)

    for i in deg:
        expr.append(genPoly(i+1))

    polEq = inline_wrapper(
        expr[0])+op[operation]+inline_wrapper(expr[1])
    # polEq = '('+str(prod[0])+')'+op[operation]+'('+str(prod[1])+')'
    if operation == 'divide':
        quo_rem = polys.polytools.div(expr[0], expr[1])
        expanded = quo_rem[0] + (quo_rem[1]/expr[1])
        constant_term = quo_rem[0].subs({x: 0})
        deg_ans = degree(expanded, gen=0)
        lead_coef = polys.polytools.LC(expanded)
        leading_term = polys.polytools.LT(expanded)
        remainder = '' if (quo_rem[1]/expr[1]
                           ) == 0 else '+'+str(quo_rem[1]/expr[1])
        expanded = str(quo_rem[0]) + remainder
        properties = {'Quotient:   ': quo_rem[0],
                      'Leading Term:   ': leading_term,
                      'Degree:  ': deg_ans,
                      'Leading Coefficient:   ': lead_coef,
                      'Constant Term:   ': constant_term,
                      'Remainder: ': quo_rem[1]
                      }

    else:
        if operation == 'multiply':
            expanded = expand(expr[0]*expr[1])
        elif operation == 'add':
            expanded = expand(expr[0]+expr[1])
        elif operation == 'minus':
            expanded = expand(expr[0]-expr[1])

        constant_term = expanded.subs({x: 0})
        deg_ans = degree(expanded, gen=0)
        lead_coef = polys.polytools.LC(expanded)
        leading_term = polys.polytools.LT(expanded)
        # expanded = latex(expanded, mode='inline')

        properties = {'Simpliest Form:   ': expanded,
                      'Leading Term:   ': leading_term,
                      'Degree:  ': deg_ans,
                      'Leading Coefficient:   ': lead_coef,
                      'Constant Term:   ': constant_term

                      }
    props = list(properties.keys())

    anskeys = [x + latex(properties[x], mode='inline',
                         fold_short_frac=False) for x in props]

    return (polEq, props, anskeys)


def diffSquare(level):
    r = 1 if level == 'easy' else y
    p = genExc(-3, 1)*x
    q = genExc(-1, 4)
    p *= p
    q *= q
    return (p, -q)


def sumDiffCubes(level):
    r = 1 if level == 'easy' else y
    p = genExc(-3, 1)*x
    q = genExc(-1, 3)
    p *= p*p
    q *= q*q

    return (p, q)


def by_grouping(level):
    if level == 'easy':
        p = genExc(-1, 1)
        q = genExc(-1, 1)

    elif level == 'hard':
        p = genExc(-3, 3)
        q = genExc(-3, 4)

    factored_form = (a*x+b)*(c*x+d)
    factored_form = factored_form.subs(
        {a: p, b: genExc(-9, 4), c: q, d: genExc(-2, 9)})
    polEq = expand(factored_form)

    return (polEq, factored_form)


def factoring(typeIs, level):

    if typeIs == Factoring_By_Grouping:
        polEq, factored_form = by_grouping(level)
        properties = {'Factored Form: ': factored_form}
    elif typeIs == Factoring_using_Mixed_Methods:
        combination = randint(1, 6)
        if combination == 1:
            p, q = diffSquare(level)
            r, s = diffSquare(level)
            polEq = expand((p+q)*(r+s))
        elif combination == 2:
            p, q = sumDiffCubes(level)
            r, s = sumDiffCubes(level)
            polEq = expand((p+q)*(r+s))
        elif combination == 3:
            p, q = sumDiffCubes(level)
            r, s = sumDiffCubes(level)
            polEq = expand((p-q)*(r-s))
        elif combination == 4:
            p, q = sumDiffCubes(level)
            r, s = sumDiffCubes(level)
            polEq = expand((p-q)*(r+s))
        elif combination == 5:
            p, q = diffSquare(level)
            r, s = sumDiffCubes(level)
            polEq = expand((p+q)*(r+s))
        elif combination == 6:
            p, q = diffSquare(level)
            r, s = sumDiffCubes(level)
            polEq = expand((p+q)*(r-s))
        factored_form = factor(polEq)
        properties = {r'Factored Form: \\': factored_form}
    polEq = latex(polEq, mode='inline')

    props = list(properties.keys())
    anskeys = [x + latex(properties[x], mode='inline',
                         fold_short_frac=False) for x in props]

    return (polEq, props, anskeys)


def evaluatePoly(topic, level):
    # expr1 = genPoly(randint(3,6))
    # expr2 = genPoly(1) if level == 'easy' else genPoly(2)
    # quo_rem = polys.polytools.div(expr1, expr2)

    # remainder = '' if (quo_rem[1]/expr[1]
    #                     ) == 0 else '+'+str(quo_rem[1]/expr[1])
    # expanded = str(quo_rem[0]) + remainder
    # properties = {'Quotient:   ': quo_rem[0],
    #                 'Leading Term:   ': leading_term,
    #                 'Degree:  ': deg_ans,
    #                 'Leading Coefficient:   ': lead_coef,
    #                 'Constant Term:   ': constant_term,
    #                 'Remainder: ': quo_rem[1]
    #                 }

    polynomial = genPoly(
        randint(2, 4))
    factor1 = genPoly(1, True)
    divisor = genPoly(1, True)
    r, = solve(divisor, x)
    value = genExc(-7, 7) if level == 'easy' else r
    evaluatedValue = polynomial.subs({x: value})
    if topic == Evaluating_Polynomial:
        properties = {'Evaluated Value: ': evaluatedValue}
        polEq = latex(polynomial, mode='inline') + '   at $x=$ ' + \
            latex(value, mode='inline', fold_short_frac=False)
    elif topic == Remainder_Theorem:
        properties = {'Remainder: ': evaluatedValue}
        polEq = '('+latex(polynomial, mode='inline')+')' + ' $\div$ ' + \
            '('+latex(divisor, mode='inline', fold_short_frac=False)+')'

    elif topic == Factor_Theorem:

        pass

    # polynomial = genPoly(
    #     randint(2, 5))

    # p = genExc(-2, 3)
    # q = genExc(-5, 5)
    # r = a/b
    # r = r.subs({a: p, b: q})
    # value = genExc(-7, 7) if level == 'easy' else genPoly(1)
    # print(value)
    # evaluatedValue = polynomial.subs({x: value})
    # properties = {'Evaluated Value: ': evaluatedValue}
    # polEq = latex(polynomial, mode='inline') + '   at $x=$ ' + \
    #     latex(value, mode='inline', fold_short_frac=False)
    props = list(properties.keys())
    anskeys = [x + latex(properties[x], mode='inline',
                         fold_short_frac=False) for x in props]

    return (polEq, props, anskeys)


def remFacTheorem():

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
    equations = []
    ans_key = []
    given_question_ans = []
    for i in range(items):
        if subTopic == Identifying_Polynomial:
            pass

        elif subTopic == Adding_and_Subtracting_Polynomial:
            operation = 'add' if i <= i//2 else 'minus'
            level = 'easy'
            given, question, ans = operations(operation, level)
            item = [given, question, ans]
            given_question_ans.append(item)

        elif subTopic == Multiplying_Polynomial:
            level = 'easy'
            given, question, ans = operations('multiply', level)
            item = [given, question, ans]
            given_question_ans.append(item)

        elif subTopic == Dividing_Polynomial:
            level = 'easy' if i <= i//2 else 'hard'
            given, question, ans = operations('divide', level)
            item = [given, question, ans]
            given_question_ans.append(item)

        elif subTopic == Factoring_By_Grouping or subTopic == Factoring_using_Mixed_Methods:
            level = 'easy' if i < items//2 else 'hard'
            given, question, ans = factoring(subTopic, level)
            item = [given, question, ans]
            given_question_ans.append(item)

        elif subTopic == Evaluating_Polynomial or subTopic == Remainder_Theorem or subTopic == Factor_Theorem:
            if subTopic == Evaluating_Polynomial:
                level = 'easy' if i < items - 2 else 'hard'
            else:
                level = 'easy' if i < items//2 else 'hard'
            print(level)
            given, question, ans = evaluatePoly(subTopic, level)
            item = [given, question, ans]
            given_question_ans.append(item)

        elif subTopic == Remainder_Theorem or subTopic == Factor_Theorem:
            given, question, ans = remFacTheorem()
            item = [given, question, ans]
            given_question_ans.append(item)

        equations.append((given, question))
        ans_key.append((given, ans))

    return (equations, ans_key)
