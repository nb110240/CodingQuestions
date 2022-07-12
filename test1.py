
def func(wdlist, word):   #dog in list 
    count = 0
    if wdlist == None or word == None:
        reutrn -1
    for wd in wdlist:
        wd = wd.lower()
        
        if wd == word.lower():
            count += 1
    return count
