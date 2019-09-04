vocabulary = {
    'nile': 'egipet',
    'vytka': 'kirov',
    'volga': 'rasha'
}
for k, z in vocabulary.items():
    print('Река - {0}, пункт - {1}'.format(k, z))

for k in vocabulary.keys():
    print('река - {0}'.format(k))

for v in vocabulary.values():
    print('пункт - {0}'.format(v))