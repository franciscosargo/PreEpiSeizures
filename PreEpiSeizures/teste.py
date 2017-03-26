# -*- coding: utf-8 -*-
"""
This example demonstrates many of the 2D plotting capabilities
in pyqtgraph. All of the plots may be panned/scaled by dragging with 
the left/right mouse buttons. Right click on any plot to show a context menu.
"""

from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
import socket
from refresh import *

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

#QtGui.QApplication.setGraphicsSystem('raster')
app = QtGui.QApplication([])
#mw = QtGui.QMainWindow()
#mw.resize(800,800)

win = pg.GraphicsWindow(title="Basic plotting examples")
win.resize(1000,600)
win.setWindowTitle('pyqtgraph example: Plotting')

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

# Initialize the data
data = np.zeros(12*10000)
data = data.reshape(10000,12)

# Initialize the plots
dvA_plots = []
dvB_plots = []

# Set the name of the channels of Module A
dvA_names = ["EDA", "BVP", "EMG", "Acc X", "Acc Y", "Acc Z"]

# Set the name of the channels of Module B
dvB_names = ["EOG", "ECG", "PZT", "Acc X", "Acc Y", "Acc Z"]


# Set tthe curves for the plots
for i in range(0,6):
    p = win.addPlot(title = dvA_names[i])
    p.setYRange(0, 100)
    curve = p.plot(pen='y')
    dvA_plots.append(curve)
    p = win.addPlot(title = dvB_names[i])
    print i
    print dvB_names[i]
    p.setYRange(0, 100)
    curve = p.plot(pen='y')
    dvB_plots.append(curve)
    win.nextRow()
    


def update():

    global curve, ptr, p6, UDP_IP, UDP_PORT, data, dvA_plots, dvB_plots

    # recieve data from socket
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))
    dat, addr = sock.recvfrom(15000) # buffer size is 1024 bytes

    # create numpy array
    a = np.matrix(dat).reshape(100,22)

    # refresh arrays
    data = refresh(data, a)
    
    for  i in range(0,6):
        dvA_plots[i].setData(data[:,i])

    for i in range(6,12):
        dvB_plots[i-6].setData(data[:,i])
  



print 'HELLLO'
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(0)


## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    print('here')
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
        print 'HEHFES'
