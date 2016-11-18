def abracadabra(s):
    result = ''
    for i in range(len(s)+1):
        result += s[:i]
    return result

if __name__ == '__main__':
    user_s = str(input("Please enter a string: "))
    print(abracadabra(user_s))
