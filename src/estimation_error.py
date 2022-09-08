import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# plt.clf()
plt.rc('font', size=55)          # controls default text sizes
plt.rc('axes', titlesize=55)     # fontsize of the axes title
plt.rc('axes', labelsize=50)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=40)    # fontsize of the tick labels
plt.rc('ytick', labelsize=40)    # fontsize of the tick labels
plt.rc('legend', fontsize=50)    # legend fontsize
# plt.rc('figure', titlesize=50)
plt.figure(figsize=(30,30))

barWidth = 0.3

x1 = [1,2,3,4,5]
xtick = np.array(["1e-9", "1e-8", "1e-7", "1e-6", "1e-5", "1e-4", "1e-3", "1e-2", "1e-1"])
fig, axarr = plt.subplots(3, 3,sharey=True,sharex=True)
fig.set_size_inches((30,30))

for x in range(0,3):
    for y in range(0,3):
        real_cr = (input_size[3*x+y])*8/(real[3*x+y][[0,2,4,6,8]]+12)
        modeled_cr = (input_size[3*x+y])*8/(d_modeled[3*x+y][[0,2,4,6,8]]+12)
        if(x*3+y < 6):
            plt.setp(axarr[x,y].get_xticklabels(), visible=False)
            
        modeled_cr[0] = real_cr[0]
        axarr[x,y].bar(x1,np.absolute(modeled_cr - real_cr)/real_cr, barWidth,color='dodgerblue')
        
        value = np.absolute(modeled_cr - real_cr)/real_cr
        for i in range(0,len(value)):
            axarr[x,y].annotate(str('{:,.2%}'.format(round(value[i],2))),xy=(x1[i]*0.9,value[i]*1.01),fontsize=30)
            
        axarr[x,y].set_title(fname[3*x+y])
#         axarr[x,y].yaxis.set_major_formatter(formatter)
#         axarr[x,y].set_yticks([1,2,3])
#         vals = axarr[x,y].get_yticks()
#         axarr[x,y].set_yticklabels(['{:,.2%}'.format(i) for i in vals])
        axarr[x,y].set_xticks(x1)
        axarr[x,y].set_xticklabels(xtick[[0,2,4,6,8]])
        
fig.text(0.5, 0.00, 'Relative error bound', ha='center')
fig.text(0.00, 0.5, 'Relative estimation error', va='center', rotation='vertical')

axarr[0,0].set_yticks([0,.2,.4,.6,.8,1])
axarr[0,1].set_yticks([0,.2,.4,.6,.8,1])
axarr[0,2].set_yticks([0,.2,.4,.6,.8,1])
axarr[1,0].set_yticks([0,.2,.4,.6,.8,1])
axarr[1,1].set_yticks([0,.2,.4,.6,.8,1])
axarr[1,2].set_yticks([0,.2,.4,.6,.8,1])
axarr[2,0].set_yticks([0,.2,.4,.6,.8,1])
axarr[2,1].set_yticks([0,.2,.4,.6,.8,1])
axarr[2,2].set_yticks([0,.2,.4,.6,.8,1])

plt.tight_layout()
plt.savefig("Estimation_error_SZ.pdf")
plt.show()
plt.clf()