import sys
sys.setrecursionlimit(60)

def first(string):
    first_ = set()
    if string in nont:
        alternatives = productions_dict[string]
        for alternative in alternatives:
            first_2 = first(alternative)
            first_ = first_ |first_2

    elif string in terminals:
        first_ = {string}

    elif string=='' or string=='e':
        first_ = {'e'}
    
    else:
        first_2 = first(string[0])
        if 'e' in first_2:
            i = 1
            while 'e' in first_2:
                first_ = first_ | (first_2 - {'e'})
                if string[i:] in terminals:
                    first_ = first_ | {string[i:]}
                    break
                elif string[i:] == '':
                    first_ = first_ | {'e'}
                    break
                first_2 = first(string[i:])
                first_ = first_ | first_2 - {'e'}
                i += 1
        else:
            first_ = first_ | first_2
    return  first_

terminals=['+','-','*','(',')','a','b','c']
no_of_productions = int(input("Enter no of productions: "))
productions = []
print("Enter the productions:")
for _ in range(no_of_productions):
    productions.append(input())
productions_dict = {}
nont=[]
for nT in productions:
    if nT[0].isupper():
        nont.append(nT[0])
        productions_dict[nT[0]] = []
s=productions[0][0]
#print(s)
print("Non Terminals:", nont)
print("productions_dict",productions_dict)
for production in productions:
    nonterm_to_prod = production.split("->")
    alternatives = nonterm_to_prod[1].split("/")
    for alternative in alternatives:
        productions_dict[nonterm_to_prod[0]].append(alternative)
        
print()
print("productions_dict",productions_dict)

FIRST = {}
for non_terminal in nont:
    FIRST[non_terminal] = set()
for non_terminal in nont:
    FIRST[non_terminal] = FIRST[non_terminal] | first(non_terminal)
print()
print("FIRST: ",FIRST)
