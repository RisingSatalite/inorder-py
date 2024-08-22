def contains(letter, list):
    for item in list:
        if(item == letter):
            return True
    return False

def is_alt(s):
    vowels = ['a','e','i','o','u']
    vowelIndex = 0
    constants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    constantIndex = 0
    flag = True
    
    for letter in s:
        if(contains(letter, vowels)):
            while(vowelIndex < len(vowels)):
                if(letter == vowels[vowelIndex]):
                    flag = True
                    break
                vowelIndex += 1
        if(contains(letter, constants)):
            while(constantIndex < len(constants)):
                if(letter == constants[constantIndex]):
                    flag = True
                    break
                constantIndex += 1
        if(flag):
            flag = False
        else:
            return False
    return True
