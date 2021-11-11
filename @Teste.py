# Função inverte maiúsculas e minúsculas
def swap_case(s):
    sTemp = ''
    if len(s):
        for i in range(0, len(s)):
            if str(s[i]).isalpha():
                if str(s[i]).islower():
                    sTemp += str(s[i]).upper()
                elif str(s[i]).isupper():
                    sTemp += str(s[i]).lower()
            else:
                sTemp += str(s[i])
    return sTemp


# if __name__ == '__main__':
s = input('Digite um texto: ')
result = swap_case(s)
print(result)
