from pylatex.position import VerticalSpace
import quantities as pq
from sympy import *
from pylatex.base_classes import Environment
from pylatex.package import Package
from pylatex import Document, Section, Subsection, Command, Math, Quantity, PageStyle, Head, MiniPage, Foot, LargeText, \
    MediumText, LineBreak, simple_page_number, Enumerate, Center
from pylatex.utils import bold, NoEscape
import os


# def headerTemplate():
#     header = PageStyle("header", header_thickness=5)
#     # Create left header
#     with header.create(Head("L")):
#         header.append(bold("Name ___________________ Student No.___ G__/___ "))
#         header.append(LineBreak())
#         header.append(bold("Nickname: _________________"))
#     # Create right header
#     with header.create(Head("R")):
#         header.append(bold("Date: ________Score: ____"))
#         header.append(LineBreak())
#         header.append(bold("\nWorksheet No.: _____ No. of items done: ____"))

#     return header


def spaces(no_of_spaces):
    x = r'\\'
    for i in range(no_of_spaces-1):
        x += r' \\'

    return x


''' details = [['Polynomial',
            'Adding and Subtracting Polynomial',
            'Perform the given operations and give the simpliest form.',
            3,
            [
                ['(2*x**3 + 2*x**2 - 4*x)+(8*x**4 + 4*x**3 - 12*x**2 - 4*x + 4)', ['Simpliest Form:   ', 'Leading Term:   ', 'Degree:  ', 'Leading Coefficient:   ', 'Constant Term:   '],
                 ['Simpliest Form:   8*x**4 + 6*x**3 - 10*x**2 - 8*x + 4', 'Leading Term:   8*x**4', 'Degree:  4', 'Leading Coefficient:   8', 'Constant Term:   4']],
                ['(-2*x**3 + 5*x**2 - 4*x + 1)-(-2*x**3 - 7*x**2 - 8*x - 3)', ['Simpliest Form:   ', 'Leading Term:   ', 'Degree:  ', 'Leading Coefficient:   ',
                                                                               'Constant Term:   '], ['Simpliest Form:   12*x**2 + 4*x + 4', 'Leading Term:   12*x**2', 'Degree:  2', 'Leading Coefficient:   12', 'Constant Term:   4']],
                ['(-2*x**3 + 6*x**2 + 2*x - 6)-(2*x**3 + 3*x**2 - 2*x - 3)', ['Simpliest Form:   ', 'Leading Term:   ', 'Degree:  ', 'Leading Coefficient:   ', 'Constant Term:   '],
                 ['Simpliest Form:   -4*x**3 + 3*x**2 + 4*x - 3', 'Leading Term:   -4*x**3', 'Degree:  3', 'Leading Coefficient:   -4', 'Constant Term:   -3']]
            ]
            ]
           ]
'''


def worksheet(details, filename):
    for i in range(2):
        print(i)
        geometry_options = {
            "head": "12pt",
            "margin": "0.4in",
            "bottom": "0.5in"
        }

        doc = Document(geometry_options=geometry_options)

        doc.preamble.append(Command('renewcommand', arguments=[
                            NoEscape('\\thesection'), NoEscape('\Alph{section}')]))
        doc.preamble.append(Command('renewcommand', arguments=[NoEscape(
            '\\thesubsection'), NoEscape('\\Alph{subsection}.')]))

        with doc.create(MiniPage(align='l')):

            doc.append(MediumText(
                'Name ___________________  Student No.___ G__/___ Date: ________Score: ____ '))
            doc.append(NoEscape(r'\\'))
            doc.append(MediumText(
                'Nickname: ___________________   Worksheet No.: _____ '))
            # doc.append(NoEscape(r' \\ \\'))

        doc.packages.append(Package('ragged2e'))
        doc.packages.append(Package('multicol'))

    # loop for worksheet and answer key

        # loop of each main topic
        if i == 0:
            pass
        else:
            filename = filename+'anskey'

        for each in details:
            '''details =[
            ['Polynomial','Identifying Polynomial','instruction',5,[[givQues],[givAns]] ],
            ['Polynomial','Multiplying Polynomial','instruction',5,[[givQuesAns],]]
            ]
            '''

            # givQuesAns = [ ['given', ['questions',], ['quesANs',] ], ]
            mainTopic, subTopic, instruction, items, givQuesAns = each
            # Diplay Centered Topic
            doc.append(VerticalSpace('0.1in'))
            # doc.append(NoEscape(r'\\'))
            doc.append(NoEscape(r'\begin{Center}'))
            doc.append(LargeText(bold(subTopic)))
            doc.append(NoEscape(r'\end{Center}'))

            with doc.create(Subsection(NoEscape(instruction))):

                with doc.create(Enumerate(enumeration_symbol=r"\arabic*)",
                                          options={'start': 1})) as enum:
                    doc.append(NoEscape(r'\enlargethispage{\baselineskip}'))
                    doc.append(NoEscape(r'\begin{multicols}{2}'))
                    for item in givQuesAns[i]:

                        enum.add_item(NoEscape(item[0]))
                        doc.append(NoEscape(spaces(7)))
                        for k in item[1]:
                            doc.append(NoEscape(k))
                            doc.append(NoEscape(r' \\'))
                    doc.append(NoEscape(r'\end{multicols}'))
            doc.append(NoEscape(r'\newpage'))

        doc.generate_pdf(filename, clean_tex=True)
        print('end')


def main(details):

    # checks if the same filename exists in the directory
    files = os.listdir('output')

    i = 1
    temp = 'pol'
    while temp+'.pdf' in files:
        temp = 'pol'
        temp += str(i)
        i += 1
    filename = 'output/' + temp
    # question = details
    # print(len(question))
    # print(len(details))

    # question.pop()
    # print(len(question))
    # print(len(details))

    # anskey = details.pop(-2)
    # worksheet(question, filename)
    worksheet(details, filename)
