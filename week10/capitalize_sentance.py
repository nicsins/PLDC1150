

def get_input():
    while True:
        sentances=input("Please Enter three sentences, end each sentence with a period, no need to capitalize anything:").split('.')
        if len(sentances)!=4 and [words.isalpha() is True for words in sentances]:
            print('must Enter three sentences, end each sentence with a period, and there must only be letters no numbers ')
            continue
        else:
            break

    return sentances


def capitolize(sentances):
    sentances.pop(len(sentances)-1)#removes blank line or none element in list created (you know its there because of the '.')
    #[words.lstrip(' ')for words in sentances]
    for words in sentances:
        if words.startswith(' '):
            words.lstrip(' ')
        else:
            continue
        print(f'{words.capitalize()}.')
    # [print(sentance.capitalize()) for sentance in sentances] another way to do it


if __name__ == '__main__':
    try:
        sentances=get_input()
        capitolize(sentances)
    except Exception as e:
        print(e)