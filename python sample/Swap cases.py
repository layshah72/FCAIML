#How to swap all uppercase characters to lowercase and vice versa? 
def swap_case(swap):
    string = ''

    for char in swap:
        if char.islower():
            string += char.upper()
        else:
            string += char.lower()
        
    return string

if __name__=='__main__':
    swap=input('Enter string: ')
    result=swap_case(swap)
    print('Swapped string: '+result)








