import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from checker import b
db= b.db
#getting data from csv file
class a:

    data=[]
    var_xList=[]
    var_yList=[]
    var_pList=[]


    for i in range(1, 16):

        data.append(np.genfromtxt("database/"+str(db)+"/"+str(i)+".csv", delimiter=',', names=['s', 'x', 'y', 'p' ]))

        #data

        #calculating dx and dy and dp
        dx = np.diff(data[i-1]['x'])
        dy = np.diff(data[i-1]['y'])
        dp = np.diff(data[i-1]['p'])
        #print dx
        mean_x = (np.sum(dx)/len(dx))
        mean_y = (np.sum(dx)/len(dy))
        mean_p = (np.sum(dx)/len(dp))

        #print mean_x
        #print mean_y
        #print mean_p
        N= len(dx)
        #variance for dx
        var_x = (np.sum(dx)-(N * mean_x))/N
        #print var_x
        var_xList.append(var_x)
        #print var_xList
        #variance for dy
        var_y = (np.sum(dy)-(N * mean_y))/N
        var_yList.append(var_y)

        #print var_yList
        #variance for dp
        var_p = (np.sum(dp)-(N * mean_p))/N
        var_pList.append(var_p)




    mean_fx = (np.sum(var_xList)/len(var_xList))
    #print mean_fx
    mean_fy= (np.sum(var_yList)/len(var_yList))
    #print mean_fy
    mean_fp = (np.sum(var_pList)/len(var_pList))
    #print mean_fp

    mod_T = np.sqrt((mean_fx ** 2) + (mean_fy ** 2) + (mean_fp ** 2))

    var_fx = (np.sum(var_xList)-(N * mean_fx))/N
    #print var_fx
    var_fy = (np.sum(var_yList)-(N * mean_fy))/N

    var_fp = (np.sum(var_pList)-(N * mean_fp))/N

    mod_V = np.sqrt((var_fx ** 2) + (var_fy ** 2) + (var_fp ** 2))

    print mod_T
    #print mod_V
    t = mod_T-mod_V
    print t
    th = t * 7

        #modF=np.sqrt((var_x ** 2) + (var_y ** 2) + (var_p ** 2))
    #print var_xList

    #print var_yList
    #print var_pList
