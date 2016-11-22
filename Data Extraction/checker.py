import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from threshold import a
#getting data from csv file
class b:
    data=[]
    db = "1"
    #t= a.mod_T - a.th
    #h = a.mod_T + a.th
    #print t
    #print h
    for i in range(1, 16):

        data.append(np.genfromtxt("database/"+str(db)+"/"+str(i)+".csv", delimiter=',', names=['s', 'x', 'y', 'p' ]))

        #data

        #calculating dx and dy and dp
        dx = np.diff(data[i-1]['x'])
        dy = np.diff(data[i-1]['y'])
        dp = np.diff(data[i-1]['p'])

        mean_x = (np.sum(dx)/len(dx))

        mean_y = (np.sum(dx)/len(dy))
        mean_p = (np.sum(dx)/len(dp))


        N= len(dx)
        #variance for dx
        var_x = (np.sum(dx)-(N * mean_x))/N
        #print var_x


        #print var_xList
        #variance for dy
        var_y = (np.sum(dy)-(N * mean_y))/N


        #print var_yList
        #variance for dp
        var_p = (np.sum(dp)-(N * mean_p))/N

        modF=np.sqrt((var_x ** 2) + (var_y ** 2) + (var_p ** 2))

        print ">>", modF




        #if modF >=t and modF <=h :
        #    print 'signature is VERIFIED'

        #else:
        #    print 'signature is FORGED'


    #print th
