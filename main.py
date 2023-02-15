import time
import os
from threading import Thread

limit_list = []

def check(seed, num):
    try:
        balance = os.popen(f"node ./wallet.js '{seed}'").read()
        if str(balance).replace('\n', '') == "0":
            print(f'{num} balance: {balance}')
        else:
            b1 = int(str(balance).replace('\n' , ''))
            res = open('jooonz.txt', 'a')
            res.write(seed + '\n')
            res.close()
            print(f'{num} balance: {balance}')
    except:
        print('error')

def thread_limit():
    for i in limit_list:
        if i.is_alive() == True:
            return False
    limit_list.clear()
    return True

def main():
    num = 0
    word_list = open('list.txt' , 'r').read().splitlines()
    for i in word_list:
        while True:
            if len(limit_list) > 3:
                time.sleep(2)
                thread_limit()
            else:
                break 
        num = num + 1        
        tr = Thread(
            target=check,
            args=[i , num]
        )
        limit_list.append(tr)      
        tr.start()

if __name__ == '__main__':
    main()
