from topicScript import linear
from topicScript import quadratic
from topicScript import polynomial as pol
from topicScript import expLog
from topicScript import conics
from topicScript import trigo

'''details =[
['Polynomial','Identifying Polynomial','instruction',5], 
['Polynomial','Multiplying Polynomial','instruction',5], 
['Polynomial','Dividing Polynomial','instruction',5], 
['Conic','Properties of Circle','instruction',5],
['Conic','Properties of Ellipse','instruction',5]]
'''


def main(details):
    for each in details:
        print(each)
        if each[0] == 'Linear':
            questions, anskey = linear.main(each[1], each[3])
        elif each[0] == 'Quadratic':
            questions, anskey = quadratic.main(each[1], each[3])
        elif each[0] == 'Polynomial':
            givenQuestionAns = pol.main(each[1], each[3])
        elif each[0] == 'Exponential':
            questions, anskey = expLog.main(each[1], each[3])
        elif each[0] == 'Conic':
            questions, anskey = conics.main(each[1], each[3])
        elif each[0] == 'Trigonometry':
            questions, anskey = trigo.main(each[1], each[3])

        each.append(givenQuestionAns)

    return details


# def equation_generator(each_sub_topics, specific_topic, main_topic):
#     equations = []
#     ans_key = []
#     for i in specific_topic:

#         if main_topic == 'conics':
#             for k in range(i[1]):
#                 if each_sub_topics == 'finding properties':
#                     form = 'standard' if k <= i[1]//3 else 'general'
#                     tex, properties, props = conics.findingProperties(
#                         i[0], form)

#                 elif each_sub_topics == 'finding equations':
#                     tex, properties, props = conics.findingEquations(i[0])

#                 equations.append((tex, properties))
#                 ans_key.append((tex, props))

#         elif main_topic == 'polynomial':
#             # loop for number of items
#             for k in range(i[1]):
#                 if each_sub_topics == 'operations':
#                     parEq, properties, props = pol.operations(i[0])
#                     tex = pol.to_latex_wrapper(parEq, 1)
#                 elif each_sub_topics == 'finding roots':
#                     parEq, properties, props = pol.finding_roots()
#                     tex = pol.to_latex_wrapper(parEq, 1)
#                 elif each_sub_topics == 'fta_drs_rrt':
#                     parEq, properties, props = pol.fta_drs_rrt()
#                     tex = pol.to_latex_wrapper(parEq, 1)
#                 elif each_sub_topics == 'pol_ineq':
#                     parEq, properties, props = pol.fta_drs_rrt()
#                     tex = pol.to_latex_wrapper(parEq, 1)
#                 elif each_sub_topics == 'finding_properties':
#                     parEq, properties, props = conics.findingProperties(i[0])
#                     tex = conics.to_latex_wrapper(parEq)
#                 equations.append((tex, properties))
#                 ans_key.append((tex, props))

#     return (equations, ans_key)
