# import sys
#
# max_num = 10 ** 7
#
# nums_1 = [num for num in range(1, max_num + 1)]
# print(f'{sum(nums_1)} - {sys.getsizeof(nums_1)}')
#
# nums_2 = (num for num in range(1, max_num + 1))
# print(f'{sum(nums_2)} - {sys.getsizeof(nums_2)}')

basket = ['452.1', '543.4', '5798.2', '4578.4', '458.2']
workers = ['Loren', 'Kate', 'Jess']

basket_gen = (a for a in basket)
workers_gen = (a for a in workers)

# for product, worker in zip(basket_gen, workers_gen):
for worker, product in zip(workers_gen, basket_gen):
    print((worker, product))

for product in basket_gen:
    print((product, None))

# txt = ''
# for prod in basket:
#     txt += prod
#     txt += ', '
# print(txt.strip(', '))

if [] or {} or 0:
    txt = 'Name'
    print(txt[:-2])

print([] or [] or [])
