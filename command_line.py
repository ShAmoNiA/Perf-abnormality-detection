import os
from datetime import datetime
import time
import datetime
import shutil
import numpy as np
import pandas as pd
import subprocess as sp
import threading
    
def run(pid):
    try:
        os.makedirs(str(currentDate)+"/"+str(current_time)+"/"+action+"/"+ str(pid)) 
    except:
        pass

    
    # print("perf record for pidof : "+pid+" start")
    Data_path_item = str(currentDate)+"/"+str(current_time)+"/"+action+"/"+pid
    os.system("cd "+ Data_path_item + " && sudo perf record -e 'syscalls:sys_*' -F 99 -p "+pid+" sleep "+str(sleep_time) +" > /dev/null 2>&1")
    output = sp.getoutput("cd "+Data_path_item+' && sudo perf report -f')
    # if hold_null in output:
    #     # shutil.rmtree(str(currentDate)+"/"+str(current_time)+"/"+action+"/"+ str(pid))
    #     print("**********folder is empty**********")
    # else:
    os.system("cd "+ Data_path_item+' && sudo perf script > perf.data.txt -f')
    mylist = []
    f = open(Data_path_item+"/perf.data.txt", "r")
    lines = f.readlines()
    for line in lines:
        # if str(pid) in line:
        split = line.split(":")
        for counter_ in range(len(split)):
            if("syscalls" in split[counter_]):
                mylist.append(split[counter_+1])

    unique, counts = np.unique(np.array(mylist), return_counts=True)
    hold = dict(zip(unique, counts))

    main_list.append({"pid":pid}|hold)




output_list = []
hold_null = 'Error:\nThe perf.data data has no samples!\n'
account = ["empty","main"]
sleep_time = 5
action = "syscalls"

period_time = 10

pid = (os.popen('pidof Discord').read()).split()

print(pid)
    

path = "cd /media/shayan/Local\ Disk/university/Main\ Proj"
for counter in range(period_time):
    main_list = []
    currentDate = datetime.date.today() 
    tim = time.localtime()
    current_time = time.strftime("%H_%M_%S", tim)
    try:
        os.makedirs(str(currentDate)) 
    except:
        pass

    Data_path = "cd "+str(currentDate)


    list_threads = []
    list_txt = []

    for i in range(len(pid)):
        list_threads.append(threading.Thread(target=run, args=(pid[i],)))

    for member in list_threads:
        member.start()

    for member in list_threads:
        member.join()



    output = pd.DataFrame()
    for hold in main_list:
        df_dictionary = pd.DataFrame([hold])
        output = pd.concat([output, df_dictionary], ignore_index=True)
        output_list.append(output)
    # print(output.head())

    np_list = output.to_numpy()
 
    
    for counter in range(len(np_list)):
        item = np_list[counter]
        hold = item
        where_are_NaNs = np.isnan(hold.astype(np.float64))
        hold[where_are_NaNs] = 0
        np_list[counter] = hold
    np_list = np_list.ravel()
    print(np_list.shape)

    # dist = np.linalg.norm(np_list[3][1:] - np_list[4][1:])
    # print(dist)
    # print(dist)
    # for item in main_list:
    #     print((list(item.values())))

    # for col in output.columns:
    #     print(col)
    


output.to_excel('res_perf.xlsx')




