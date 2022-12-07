import shutil
import os

path=r'C:\Test_result\TxBW\Normal'
test_flag=os.path.split(path)[-1]
test_type=os.path.split(os.path.split(path)[0])[-1]

resu=[i for i in os.listdir(path) if len(i)>15 and not '.' in i]

for i in range(len(resu)):
    sn, dat,tim=resu[i].split('_')
    # if int(sn[-3:])<123:continue
    if int(sn[-3:])==188 or int(sn[-3:])==182 or int(sn[-3:])==200 or int(sn[-3:])==192 or int(sn[-3:])==211:
        print(sn)
        time_stamp=dat+'_'+tim
        report_path=os.path.join(path,resu[i])
        print(report_path)
        if not os.path.exists(os.path.join('R:\\',test_flag)):os.mkdir(os.path.join('R:',test_flag))
        if not os.path.exists(os.path.join('R:\\', test_flag,sn)): os.mkdir(os.path.join('R:', test_flag,sn))
        if not os.path.exists(os.path.join('R:\\', test_flag, sn,test_type)): os.mkdir(os.path.join('R:\\', test_flag, sn,test_type))
        if not os.path.exists(os.path.join('R:\\', test_flag, sn, test_type,time_stamp)):
            os.mkdir(os.path.join('R:\\', test_flag, sn, test_type,time_stamp))
            print(os.path.join('R:\\', test_flag, sn, test_type,time_stamp))
        # else:
        #     continue
        network_path=os.path.join('R:\\',test_flag,sn,test_type,time_stamp)
        print(network_path)
        shutil.copytree(report_path, network_path,dirs_exist_ok=True)

print('Done')