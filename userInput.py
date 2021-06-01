import Topics


def main():
    # import the entire dictionary
    topics = Topics.mainTopics
    listTopics = {}
    # print all main topic
    for idx, each in enumerate(topics.keys()):
        print(idx+1, ': ', each)
        listTopics[idx+1] = each
    chosenTopics = input(
        'Plese type the number(s) of the chosen topic separated by a comma. ')
    # List of all main topic ['Linear', 'Quadratic',...]
    chosenTopics = [listTopics[int(x)] for x in list(chosenTopics.split(','))]

    data = []
    # print all subtopic
    for each in chosenTopics:
        listSubTopics = {}
        for index, every in enumerate(topics[each]):
            print(index+1, ': ', every)
            listSubTopics[index+1] = every
        chosenSubTopics = input(
            'Please type the numbers of the chosen topic separated by a comma. ')
        # List of all sub topic for each main topic ['Identifying...', 'Simplifying...',...]
        chosenSubTopics = [[each, listSubTopics[int(x)], topics[each][listSubTopics[int(
            x)]]] for x in list(chosenSubTopics.split(','))]
        for each in chosenSubTopics:
            data.append(each)

    # Ask for the number of items per topic
    for idx, each in enumerate(data):
        print('Please type the number of items for the topic ',  each[1], ': ')
        items = int(input())
        each.append(items)

    # items = input(
    #     'Please type the number of questions to be created for each topic. Type NO if you want to set different number of items per topic.')
    # if items != 'NO':
    #     items = int(items)
    #     for each in data:
    #         data[each] = [data[each], items]
    # else:
    #     for each in data:
    #         print(data[each])
    #         items = int(input('Type the number of items.'))
    #         data[each] = [data[each], items]

    #    data = Topics.subTopicSetter(each)
    #     for SubTopicKey indata:
    #         print(SubTopicKey, ': ',data[SubTopicKey])
    #     subTopicLists = input(
    #         'Plese type the numbers of the chosen topic separated by a comma. ')
    #     subTopicLists = list(subTopicLists.split(','))
    #     for i in subTopicLists:
    #         data[each+i] =data[int(i)]

    # print('These are the topics you have chosen.')
    # for idx, each in enumerate(data):
    #     print(idx+1, data[each])
    # items = input(
    #     'Please type the number of questions to be created for each topic. Type NO if you want to set different number of items per topic.')
    # if items != 'NO':
    #     items = int(items)
    #     for each in data:
    #         data[each] = [data[each], items]
    # else:
    #     for each in data:
    #         print(data[each])
    #         items = int(input('Type the number of items.'))
    #         data[each] = [data[each], items]

    return data
