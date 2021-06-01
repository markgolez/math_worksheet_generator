import userInput
import generateQuestions
import template as generateWorksheet


# Ask user input
'''details =[
['Polynomial','Identifying Polynomial','instruction',5], 
['Polynomial','Multiplying Polynomial','instruction',5], 
['Polynomial','Dividing Polynomial','instruction',5], 
['Conic','Properties of Circle','instruction',5],
['Conic','Properties of Ellipse','instruction',5]]
'''
details = userInput.main()
# generate equations
details = generateQuestions.main(details)
print(details)
'''details =[
['Polynomial','Identifying Polynomial','instruction',5,[[givQuesAns],] ], 
['Polynomial','Multiplying Polynomial','instruction', [[givQuesAns],] ], 
['Polynomial','Diiding Polynomial','instruction', [[givQuesAns],] ], 
['Conic','Properties of Circle','instruction', [[givQuesAns],] ],
['Conic','Properties of Ellipse','instruction', [[givQuesAns],] ]
]
'''
# generate worksheets
generateWorksheet.main(details)


# def spaces(no_of_spaces):
#     x = r'\\'
#     for i in range(no_of_spaces-1):
#         x += r' \\'d

#     return x


# def main():
#     filename = 'polynomial'

#     worksheet = {'Filename': filename,
#                  }

#     Topics = tis.main()


# # print(Topics)
#     topics = []
#     ans_Keys = []

#     # loop through main topics
#     for main_topic_key in Topics:
#         # loop through subtopics
#         if main_topic_key == 'polynomial':
#             for each_sub_topics_key in Topics[main_topic_key]:
#                 equations, ans_key = equation_generator(
#                     each_sub_topics_key, Topics[main_topic_key][each_sub_topics_key], 'polynomial')
#                 topics.append(
#                     (equations, tis.instructions['conics'][each_sub_topics_key]))
#                 ans_Keys.append(
#                     (ans_key, tis.instructions['conics'][each_sub_topics_key]))
#         elif main_topic_key == 'conics':
#             for each_sub_topics_key in Topics[main_topic_key]:
#                 equations, ans_key = equation_generator(
#                     each_sub_topics_key, Topics[main_topic_key][each_sub_topics_key], 'conics')
#                 topics.append(
#                     (equations, tis.instructions['conics'][each_sub_topics_key]))
#                 ans_Keys.append(
#                     (ans_key, tis.instructions['conics'][each_sub_topics_key]))

#     # checks if the same filename exists in the directory
#     files = os.listdir()
#     i = 1
#     temp = filename
#     while temp+'.pdf' in files:
#         temp = filename
#         temp += str(i)
#         i += 1
#     filename = temp

# # print(topics)
#     template.main(topics, filename, spaces(9))
#     template.main(ans_Keys, filename+'_anskey', spaces(7))


# main()
