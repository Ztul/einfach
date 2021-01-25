while True:
    print('Wie ist dein Name')
    name=input()
    if name != 'Lord':
        continue

    print ('Moin, Lord, Gib mal dein Password:')
    password = input()

    if password == 'lili':
        break

print('Zugang Gestattet')