# li=list(map(str,n))

# # print(li.count("[")==li.count("]"))
# # print(li.count("{")==li.count(")"))
# # print(li.count("(")==li.count(")"))
# ans=[li.count("[")==li.count("]"),li.count("{")==li.count("}"),li.count("(")==li.count(")")]
# print(all(ans))
# def bstack(n):
#     stack = []
#     for i in n:
#         if i in ['[', '{', '(']:
#             stack.append(i)
#         else:
#             if not stack:
#                 return False
#             n = stack.pop()
#             if n == "]":
#                 if i != "[":
#                     return False
#             if n == "}":
#                 if i != "{":
#                     return False
#             if n == ")":
#                 if i != "(":
#                     return False
    # return True

# n = input()
# li=list(map(str,n))

# def bstack(m):
#     stack = []
#     for i in m:
#         if i in ['[', '{', '(']:
#             stack.append(i)
#             continue
#         else:
#             n=stack.pop()
#             if i ==")":
#                 if n=="(":
#                     return True
#             if i =="]":
#                 if n=="[":
#                     return True
#             if i =="{":
#                 if n=="}":
#                     return True
#     return False
# print(bstack(li))


# if bstack!=None:
#     print(True)
# else:
#     print("False")

n=input()
li=list(map(str,n))

def bstack(li):
    stack=[]
    for i in li:
        if i in ( "[" ,"{", "(" ):
            stack.append(i)
        else:
            if not stack:
                return False
            top=stack.pop()
            if top=="[" and i != "]" :
                return False
            elif top=="{" and i!="}":
                return False
            elif top=="(" and i!=")":
                return False
    return True

print(bstack(li))

