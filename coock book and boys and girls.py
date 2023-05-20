

cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],
      ]
  ]
]

person = int(input('введите количество персон'))
sequence_number = 0
for i in cook_book:
    print(i[0])
    for c in cook_book[sequence_number][1]:
        c[1] = c[1]*person
        print(c)
    sequence_number = sequence_number + 1


print()
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha',]

sequence_number = 0
if len(boys) != len(girls):
    print('мы не сможем вас познакомить')
else:
    boys.sort()
    girls.sort()
    print(boys)
    print(girls)
    print('лучшие пары', '\n',)
    while sequence_number != len(boys):
        print(boys[sequence_number],'+', girls[sequence_number])
        sequence_number += 1
