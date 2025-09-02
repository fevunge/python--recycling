from sys import argv

if len(argv[1:]):
    express = ' '.join(argv[1:])
else:
    express = input("phrase:: ")

if express[::-1] == express:
    print("Is polydrome!")
else:
    print("Is not polydrome!")
