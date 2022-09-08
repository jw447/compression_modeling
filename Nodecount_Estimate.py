import numpy as np

error = ["1E-9", "1E-8", "1E-7", "1E-6", "1E-5", "1E-4", "1E-3", "1E-2", "1E-1"]

def nodecount_estimate(fname):

    nodecount = []
    qf0 = []
    with open("log/sz/sz_qf/"+fname+"-1E-1-qf.log") as inputfile:
        for line in inputfile:
            if ("SZ" not in line) & ("compress" not in line) & ("func" not in line):
                qf0.append(float(line.strip('\n')))

    s = set()
    for j in qf0:
        if int(j) != 0:
            if int(j) in s:
                continue
            else:
                s.add(int(j))
    nodecount.append(len(s))

    for i in range(1,len(error)-1):
        qf0=[]
        f_name0 = fname+"-1E-"+str(i)+"-qf.log"
        print(f_name0)
        with open("log/sz/sz_qf/"+f_name0) as inputfile:
            for line in inputfile:
                if ("SZ" not in line) & ("compress" not in line) & ("func" not in line):
                    qf0.append(float(line.strip('\n')))

        qf1=[]
        f_name1 = fname+"-1E-"+str(i+1)+"-qf.log"

        with open("log/sz/sz_qf/"+f_name1) as inputfile:
            for line in inputfile:
                if ("SZ" not in line) & ("compress" not in line) & ("func" not in line):
                    qf1.append(float(line.strip('\n')))

        s = set()
        for j in qf1:
            if int(j) != 0:
                if int(j) in s:
                    continue
                else:
                    s.add(int(j))
        nodecount.append(len(s))


        tmp_data = []
        for j in range(0,len(qf1)-2):
            if(qf0[j]!=0 and qf1[j]==0):
                tmp_data.append(qf0[j])

        qf0 = np.array(qf0)
        qf0 = qf0[qf0.nonzero()]
        qf1 = np.array(qf1)
        qf1 = qf1[qf1.nonzero()]

        v_esti = (np.sum(np.power(qf0-np.mean(qf0),2))-np.sum(np.power(np.array(tmp_data)-np.mean(qf0),2)))/len(qf1)
        qf_esti = np.random.normal(loc=np.mean(qf0), scale=np.sqrt(v_esti), size=len(qf1))

    return nodecount
