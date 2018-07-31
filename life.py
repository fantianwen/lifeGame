import sys
import time
import tkinter
import sys
from node import Node

# config
L = ["#f00", "#fff","#0f0"]
worlds = {}

def composeIndex(column,rowNumber,row):
    return column*rowNumber+row+1

#read config
f = open(sys.argv[1], 'r')
k=[]
row_conf = 0
for line in f:
    # row
    row_conf =  row_conf+1
    k.append(list(line))
f.close()    
#column
column_conf = len(k[0])-1

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=column_conf*10, height=row_conf*10)
canvas.pack()

#initial config
rowNumber = 0
columnNumber = 0

initialNodes = []

for kk in k:
    rowNumber = rowNumber + 1
    columnNumber = 0
    for n in kk:
        columnNumber = columnNumber + 1
        if n == '#':
            initialNodes.append(composeIndex(columnNumber-1,row_conf,rowNumber-1))

for row in range(column_conf):
    for column in range(row_conf):
        id = canvas.create_rectangle(row*10, column*10, (row+1)*10, (column+1)*10, fill="#000")
        if id in initialNodes:
            node = Node(id,row_conf,column_conf,True,True)
        else:
            node = Node(id,row_conf,column_conf,False)    
        worlds[id] = node

def next():
    for key in worlds.keys():
        node = worlds.get(key)

        leftIndex = node.updateLeft()
        rightIndex = node.updateRight()
        uppder = node.updateUpper()
        bottom = node.updateBottom()
        upperLeft = node.updateUpperLeft()
        upperRight = node.updateUpperRight()
        leftBottom = node.updateLeftBottom()
        rightBottom = node.updateRightBottom()

        neighorLifes = 0
        if worlds[leftIndex].status:
            neighorLifes = neighorLifes+1
        if worlds[rightIndex].status:
            neighorLifes = neighorLifes+1
        if worlds[uppder].status:
            neighorLifes = neighorLifes+1
        if worlds[bottom].status:
            neighorLifes = neighorLifes+1
        if worlds[upperLeft].status:
            neighorLifes = neighorLifes+1
        if worlds[upperRight].status:
            neighorLifes = neighorLifes+1
        if worlds[leftBottom].status:
            neighorLifes = neighorLifes+1
        if worlds[rightBottom].status:
            neighorLifes = neighorLifes+1
        
        if node.status == True:
            if neighorLifes<2:
                node.update(False)
            if neighorLifes ==3: 
                node.update(True)
            if neighorLifes >3:
                node.update(False)
            if neighorLifes == 2:
                node.update(True)    
        else:
            if neighorLifes == 3:
                node.update(True)
            else:
                node.update(False)    
        worlds[key] = node
    refresh()
    root.after(500, next)  # calls next() after 500 ms       

def refresh():
    for key in worlds.keys():
        node = worlds.get(key)
        node.status = node.nextStatus
        if node.nextStatus == True:
            canvas.itemconfig(key, fill=L[2])
        else:
            canvas.itemconfig(key, fill=L[1])


root.after(500, next)  # calls next() after 1 second
root.mainloop()

