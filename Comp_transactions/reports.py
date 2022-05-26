from datetime import date

def recordTrans(thistrans):
    today = date.today()
    todayfile = f'coffeetrans_{today}.txt'
    with open(todayfile, 'a') as log:
        log.write(thistrans + '\n')

# consider shelve to store transactions as json objects not text files