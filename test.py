import pandas as pd
import numpy as np
import h5py
from tqdm import tqdm
import pdb; pdb.set_trace()

data_dir = "./data/clusterdata-2011-2/"

task_events_header = ['timestamp','missing_info', 'job_id','task_index','machine_id','event_type',
                      'user_name','sched_class','priority','cpu_req','ram_req','space_req','diff_machine']

machine_events_header = ['timestamp','machine_id','event_type','platform_id','cpu_cap','mem_cap']

task_usage_header = ['start_time','end_time','job_id','task_index','machine_id', 'mean_cpu_usage',
                     'canon_memory_usage', 'assign_memory_usage', 'unmapped_cache', 'total_cache', 
                     'max_mem', 'mean_io', 'mean_space', 'max_cpu', 'max_io', 'cpi', 'mai', 'sample',
                     'agg_type', 'sample_cpu_usage']



hf = h5py.File('./data/machines_in_100.h5','r')
all_machines = np.array(hf['ids'])
hf.close()

hf = h5py.File('./data/time_stamps.h5','r')
ts = np.array(hf.get('time'))
hf.close()

start_time = ts[0]
end_time = ts[1]

cols = range(start_time,end_time)

import gc
gc.collect()

# print("hoga")
# machine_usage = pd.DataFrame(index=np.array(all_machines), columns=cols,dtype=np.float16)
# print("hua")


# for i in tqdm(range(50)):
#     df = pd.read_csv(data_dir + "task_usage/part-%05d-of-00500.csv.gz" % i,header=None)
#     df.columns = task_usage_header
#     df = df[['start_time','machine_id','mean_cpu_usage']]
#     df['start_time'] = df['start_time']/1000000
#     df['start_time'].astype(np.int)
#     df = df[df['machine_id'].isin(all_machines)].groupby(['start_time', 'machine_id']).sum()
#     df.reset_index(level=['machine_id'],inplace=True)
#     start_times = df.index.unique()
#     for j in start_times:
#         dummy = df.loc[j,['machine_id','mean_cpu_usage']].as_matrix().T
#         machine_usage[j][dummy[0]] = dummy[1]
#     del df
#     gc.collect()

print("ho gaya finally")