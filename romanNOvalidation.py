############################3  using roman ########################
# import roman
# x=input()
# try:
#     if (roman.fromRoman(x)>0 and roman.fromRoman(x)<4000):
#         print("True")
#     else:
#         print("False")
# except:
#     print("False")

# # print(roman.toRoman(4))

######################## 2nd method ###################
n=input()
l=['x','i','v','l','d','c','m']
ansbool=True
for i in n:
    if i.lower() not in l:
        ansbool=False
print(ansbool)