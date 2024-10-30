from utils.function import add

def count_word(string, ch):
    assert isinstance(string,str)
    assert isinstance(ch, str) and len(ch) == 1
    count = 0
    for i in string:
        if i == ch:
            count = add(count, 1)
    return count