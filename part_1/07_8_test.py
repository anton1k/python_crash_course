sandwich_orders = ['sandwich1', 'sandwich2', 'sandwich3', 'sandwich4', 'sandwich5']
finished_sandwiches = []

while sandwich_orders:
    current = sandwich_orders.pop().title()
    print('проверено {0}'.format(current))
    finished_sandwiches.append(current)

res = ', '.join(finished_sandwiches)

if not sandwich_orders:
    print('Обработанно: {0}'.format(res))



    


