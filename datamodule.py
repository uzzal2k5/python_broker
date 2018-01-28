import cron
import gc
import multiprocessing as mp

data_file = "datafile.txt"
datafile = "data2.txt"
num = int(input())
print(num)
cron.mem()
for i in range(num):
    data = cron.read_data(data_file)
    cron.write_data(datafile, data)

    li = ['https://www.youtube.com/watch?v=Y07dnUKwqyw',
          'https://www.youtube.com/watch?v=Y07dnUKwqyw',
          'https://www.youtube.com/watch?v=Y07dnUKwqyw',
          'https://youtu.be/Y07dnUKwqyw']
    # link = ['http://www.quotedb.com/quote/quote.php?action=random_quote']
    #map(cron.urllink, li)
    mp.Process(target=map(cron.urllink, li))
    print("Contents:\n" + data)
    cron.word_search(data)
    #cron.memory_release()
    # print(gc.collect())
    # cron.memory_release()
    # proc = mp.Process(target=memoryhog)
cron.mem()
