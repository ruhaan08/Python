import time
t = int(input('Long a minute or a second(If second type 1 if minute type 60).'))
limit = int(input('What is the limit?'))
def countdown(limit):
    if limit == 0:
        print('!DONE!')
    else:
        print(limit)
        print(('*'*limit))
        time.sleep(t)
        countdown(limit-1)
countdown(limit)