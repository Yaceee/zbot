from register import register

NB_REGISTER = 10

if __name__ == '__main__':
    print("Z BOT")
    for i in range(NB_REGISTER):
        print('[{}/{}]: '.format(i+1, NB_REGISTER), end='')
        res = register()
        toShowResult = '✅' if res else '❌' 
        print(toShowResult)
    print('Fin du batch')