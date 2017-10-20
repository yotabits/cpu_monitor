import glob
import time
import os
import re

def get_proc_list():
    proc_list = glob.glob("/proc/[0-9]*")
    proc_stat_list = []
    for i in range(0, len(proc_list)):
        proc_stat_list.append(proc_list[i] + "/stat")
    return proc_stat_list


def generate_proc_stat_fp(previous_proc_list, actual_proc_list, proc_stat_fp_dict):
    actual_proc_list_tmp = list(actual_proc_list)
    if (previous_proc_list != actual_proc_list):
        if (previous_proc_list is not None):
            for element in previous_proc_list:
                if element not in actual_proc_list:
                    proc_stat_fp_dict[element].close()
                    proc_stat_fp_dict.pop(element)
                    print element + " closed"

        for element in actual_proc_list_tmp:
            if (previous_proc_list is not None):
                if element not in previous_proc_list:
                    print element + " opened"
                    try:
                        proc_stat_fp_dict[element] = open(element)
                    except IOError:
                        #element does not exist anymore
                        actual_proc_list.remove(element)
                        print element + " not exist anymore"
                        pass
    return actual_proc_list


def get_cpu_tick_per_second():
    return os.sysconf('SC_CLK_TCK')


def get_provided_values_list():
    # http://man7.org/linux/man-pages/man5/proc.5.html
    values = ['pid', 'comm', 'state', 'ppid', 'pgrp', 'session', 'tty_nr', 'tpgid', 'flags', 'minflt', 'cminflt',
              'majflt', 'cmajflt', 'utime', 'stime', 'cutime', 'cstime', 'priority', 'nice', 'num_threads',
              'itrealvalue', 'starttime', 'vsize', 'rss', 'rsslim', 'startcode', 'endocode', 'startstack', 'kstkesp',
              'kstkeip', 'signal', 'blocked', 'sigignore', 'sigcatch', 'wchan', 'nswap', 'cnswap', 'exit_signal',
              'processor', 'rt_priority', 'policy', 'delayacct_blkio_ticks', 'guest_time', 'cguest_time', 'start_data',
              'end_data', 'start_brk', 'arg_start', 'arg_end', 'env_start', 'env_end', 'exit_code']
    return values


def print_proc_stat_dict(proc_stat_dict):
    for element in get_provided_values_list():
        value = proc_stat_dict.get(element)
        if value:
            print element + ":" + value


def parse_process_stat(stat_file_fp):
    if (stat_file_fp):
        data_dict= {}
        data_names = get_provided_values_list()
        data = stat_file_fp.read()
        stat_file_fp.seek(0)
        print data
        name = re.findall(" \(.*\) ", data)
        try:#ask forgiveness not permission
            name = name[0]
        except IndexError:
            name = "no_name"
            print "no name_found ??"
        ##name = name.group(1)


        # PLZ IMPROVE ME
        data_list = re.split('\(.*\)',data)
        data_list = re.split(' *',data_list[0])  + re.split(' *',data_list[1])
        data_list.insert(1, name)

        data_names_counter = 0
        for data in data_list:

            print len(data_names)
            print data_names_counter

            data_name = data_names[data_names_counter]
            data_dict[data_name] = data
            data_names_counter += 1
        print data_dict
        return data_dict



def main():
    proc_fp_dict = {}
    previous_proc_list = []
    while True:
        proc_list = get_proc_list()
        previous_proc_list = generate_proc_stat_fp(previous_proc_list, proc_list, proc_fp_dict)

        for key,file_pointer in proc_fp_dict.iteritems():
            data_dict = parse_process_stat(file_pointer)
            print_proc_stat_dict(data_dict)
        time.sleep(1)

main()