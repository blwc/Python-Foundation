foo = list('thefiveboxingwizardsjumpquickly')
bar = list('cwmfjordbankglyphsvextquiz')

families = [
    ['tom', 'jerry'],
    ['morticia', 'gomez', 'wednesday', 'lurch'],
    ['charlie', 'bill', 'percy', 'fred', 'george', 'ron', 'ginny']]

def rollcall():
    for family in families:
        print("There are " + str(len(family)) + " members in family " + str(family))
        for person in family:
            print("Hello I am " + str(person))
