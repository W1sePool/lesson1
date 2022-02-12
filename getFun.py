from ast import Return


def get_summ(one, two, delimiter='&'):
   return upper(f'{str(one)}{delimiter}{str(two)}')

def upper(item):
    return item.upper()

x = get_summ("Learn","Python")
print(x)