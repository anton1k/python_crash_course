sandwich_orders = ['sandwich1', 'pastrami', 'sandwich2', 'pastrami', 'sandwich3', 'sandwich4', 'sandwich5', 'pastrami']
finished_sandwiches = []

print('pastrami больще нет')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current = sandwich_orders.pop().title()
    print('проверено {0}'.format(current))
    finished_sandwiches.append(current)

res = ', '.join(finished_sandwiches)

if not sandwich_orders:
    print('Обработанно: {0}'.format(res))



    


