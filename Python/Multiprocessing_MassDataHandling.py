# Combining 1 billion rows from multiple files
import random
import multiprocessing
import threading
import queue
import time

list =["small_file1_100000000.txt","small_file1_200000000.txt","small_file1_300000000.txt","small_file1_400000000.txt","small_file1_500000000.txt","small_file1_600000000.txt","small_file1_700000000.txt","small_file1_800000000.txt","small_file1_900000000.txt","small_file1_1000000000.txt"]
list2 =["small_file2_100000000.txt","small_file2_200000000.txt","small_file2_300000000.txt","small_file2_400000000.txt","small_file2_500000000.txt","small_file2_600000000.txt","small_file2_700000000.txt","small_file2_800000000.txt","small_file2_900000000.txt","small_file2_1000000000.txt"]
write_queue = queue.Queue()


def file_process(file1, file2,i, lock):
    name = "Hugefile_whole_multi_"+str(i)+".txt"
    f3 = open(name,'a')
    with open(str(file1),"r") as f:
            with open(str(file2),"r") as f2:
                line = f.readline()
                line2 = f2.readline()
                while line: 
                    j = int(line.rstrip()) + int(line2.rstrip())
                    with lock:
                        f3.write(str(j)+"\n")
                    line= f.readline()
                    line2 = f2.readline()
    f3.close()

if __name__ == '__main__':
    lock = multiprocessing.Lock()
    start = time.time()
    
    processes = [multiprocessing.Process(target=file_process,args=(list[i],list2[i],i, lock,)) for i in range(10)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    with open("Hugefile_whole_multi_final.txt",'a') as ff:
        for i in range(10):
            name = "Hugefile_whole_multi_"+str(i)+".txt"
            ft = open(name,'a')
            text = ft.read()
            ff.write(text)
        ff.close()
    end = time.time()
    total_time = end - start
    message = "The process took " + str(total_time) + " seconds to complete"
    print(message)