def strange_split_len(string, splitter):
    l = [ x for x in string.split(splitter)]
    return len(l)-1

if __name__ == '__main__':
    s = input("Please enter a catdog string: ")
    print( strange_split_len(s, 'cat') == strange_split_len(s, 'dog') )
