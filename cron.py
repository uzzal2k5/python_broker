import urllib
import webbrowser
import re
import os
import gc
import multiprocessing as mp
import resource


# import psutil


def read_data(df):
    try:
        rf = open(df, "r")
        if rf.mode == "r":
            contents = rf.read()
            print("Content as it was data file\n")
            print(contents)
        rf.close()
    except IOError:
        print("File Not Found")
    return contents


def write_data(filename, text):
    f = open(filename, "a+")
    f.write(text)
    f.close()
    return f


def urllink(url):
    req = urllib.Request(url)
    response = urllib.urlopen(req)
    the_page = response.read()
    print(the_page)
    webbrowser.get(using='google-chrome').open(url)
    if not gc.isenabled():
        gc.enable()
    else:
        gc.collect()


def word_search(contents):
    match = re.search(r'([\w.-]+)@([\w.-]+)', contents)
    find = re.findall(r'[\w\.-]+@[\w\.-]+', contents)
    for email in find:
        print(email)
    if match:
        data = match.group()
        # data = match.lastindex
        print(data)


def kwarg_func(**kwargs):
    for i, j in kwargs.items():
        print(i, j)


# data_file = "datafile.txt"
# datafile = "data2.txt"
# data = read_data(data_file)
# write_data(datafile, data)


def mem():
    print('Memory usage         : % 2.2f MB' % round(
        resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0, 1)
          )


def memory_release():
    proc = getattr(os.getegid())
    gc.collect()
    mem0 = proc.get_memory_info().rss
    foo = ['abc' for x in range(10 ** 7)]
    mem1 = proc.get_memory_info().rss

    del foo, x
    mem2 = proc.get_memory_info().rss

    gc.collect()
    mem3 = proc.get_memory_info().rss

    pd = lambda x2, x1: 100.0 * (x2 - x1) / mem0
    print("Allocation: %0.2f%%" % pd(mem1, mem0))
    print("Unreference: %0.2f%%" % pd(mem2, mem1))
    print("Collect: %0.2f%%" % pd(mem3, mem2))
    print("Overall: %0.2f%%" % pd(mem3, mem0))
