import glob
import time
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






def main():
    proc_fp_dict = {}
    previous_proc_list = []
    while True:
        proc_list = get_proc_list()
        previous_proc_list = generate_proc_stat_fp(previous_proc_list, proc_list, proc_fp_dict)
        time.sleep(0.01)

main()