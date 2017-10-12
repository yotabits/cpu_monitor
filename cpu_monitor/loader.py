import threading
import random
import time
import signal
from multiprocessing import Pool

def load_cpu_func(x):
    nb_op = 0
    start = time.time()
    spent = 0
    while spent < 1:
        spent = time.time() - start
        x * x
        nb_op += 1
    return nb_op

def load_cpu_until_death(x):
    while True:
        x * x

#sad story https://stackoverflow.com/questions/1408356/keyboard-interrupts-with-pythons-multiprocessing-pool
def launch_cpu_load(display, standalone, no_of_cpu_to_be_consumed=1):
    p = Pool(processes=no_of_cpu_to_be_consumed)
    if(standalone):
        while True:
            perf_list = p.map_async(load_cpu_func, range(no_of_cpu_to_be_consumed)).get(9999999)
            op_per_sec = 0
            for nb_op in perf_list:
                op_per_sec += nb_op
            if(display):
                print ("%i operation per second") % (op_per_sec)
    else:
        p.map_async(load_cpu_until_death, range(no_of_cpu_to_be_consumed))


def manage_death(thread_pool):
    thread_pool.terminate()
