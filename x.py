exp = [(None,2),(None,None),(3,4)]

new_li = []
# for i in exp:
#     if None not in i:
#         new_li.append(i)
# print(new_li)

# print(all(None not in y for y in exp))

for i in exp:
    if all(x is not None for x in i):
        new_li.append(i)
print(new_li)