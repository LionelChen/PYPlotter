__author__ = 'lionel'
import random
list = ['米Feel','冒菜','BurgerKing','达美乐','必胜客','好麦道','饺子','嘉禾']
output = random.randint(0,len(list)-1)

# Change output avoid having pizza for two times

print(list[output])