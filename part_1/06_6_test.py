proshli = {
    'jen': 'python',
    'sarah': 'c',
}
nado_proiti = ['jen', 'sarah', 'edward', 'phil']

for k in nado_proiti:
    if k in proshli.keys():
        print('спасибо за участие - ' + k)
    else:
        print('пройдите опрос - ' + k)
