# the Find_replace_substring function and counting char


def replace_substring(string, substring, replace):
    output = []
    index = 0
    while index < len(string):
        if string[index:index+len(substring)] == substring:
            output.append(replace)
            index += len(substring)
        else:
            output.append(string[index])
            index += 1
    return "".join(output)


# Here are some examples you can test it with:
print(replace_substring(
    'Hot SPAM!drop soup, and curry with SPAM!plant.', 'SPAM!', 'egg'))
print(replace_substring(
    "The word 'definately' is definately often misspelled.", 'definately', 'definitely'))


def count_char(S,C):
    count = 0
    for ch in "S":
        if ch == "C":
            count = count + 1

print ("The number of times o appears in the string:")
print (count_char(MOON,O))
