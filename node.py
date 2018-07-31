class Node(object):

    def __init__(self,id,rowNumber,columnNumber,status,nextStatus=False):
        self.id = id
        self.rowNumber = rowNumber
        self.columnNumber = columnNumber
        self.status = status
        self.nextStatus = nextStatus

    def update(self,newStatus):
        self.nextStatus =  newStatus

    def clearNextStatus(self):
        self.nextStatus = False

    def updateLeft(self):

        column = (self.id-1) // self.rowNumber
        row = (self.id-1) % self.rowNumber
        # 左边的点
        index_node_row_left = row
        index_node_column_left = (column+self.columnNumber-1)%self.columnNumber
        return self.composeIndex(index_node_row_left,index_node_column_left)

    def updateRight(self):

        column = (self.id-1) // self.rowNumber
        row = (self.id-1) % self.rowNumber
        # 右边的点
        index_node_row_right = row
        index_node_column_right = (column+self.columnNumber+1)%self.columnNumber
        return self.composeIndex(index_node_row_right,index_node_column_right)

    def updateUpper(self):
        column = (self.id-1) // self.rowNumber
        row = (self.id-1) % self.rowNumber
        # 上边的点
        index_node_row_upper = (row+self.rowNumber-1)%self.rowNumber
        index_node_column_upper = column
        return self.composeIndex(index_node_row_upper,index_node_column_upper)

    def updateBottom(self):
        column = (self.id-1) // self.rowNumber
        row = (self.id-1) % self.rowNumber
        # 下边的点
        index_node_row_bottom = (row+self.rowNumber+1)%self.rowNumber
        index_node_column_bottom = column
        return self.composeIndex(index_node_row_bottom,index_node_column_bottom)
    
    def updateUpperLeft(self):
        column = (self.id-1) // self.rowNumber
        row = (self.id-1) % self.rowNumber
        # left_upper
        index_node_row_upper_left = (row+self.rowNumber-1)%self.rowNumber
        index_node_column_upper_left = (column+self.columnNumber-1)%self.columnNumber
        return self.composeIndex(index_node_row_upper_left,index_node_column_upper_left)

    def updateUpperRight(self):
        column = (self.id-1) // self.rowNumber
        row = (self.id-1) % self.rowNumber
        # right_upper
        index_node_row_upper_right = (row+self.rowNumber-1)%self.rowNumber
        index_node_column_upper_right = (column+self.columnNumber+1)%self.columnNumber
        return self.composeIndex(index_node_row_upper_right,index_node_column_upper_right)

    def updateLeftBottom(self):
        column = (self.id-1) // self.rowNumber
        row = (self.id-1) % self.rowNumber
        # left_bottom
        index_node_row_left_bottom = (row+self.rowNumber+1)%self.rowNumber
        index_node_column_left_bottom = (column+self.columnNumber-1)%self.columnNumber
        return self.composeIndex(index_node_row_left_bottom,index_node_column_left_bottom)

    def updateRightBottom(self):
        column = (self.id-1) // self.rowNumber
        row = (self.id-1) % self.rowNumber
        # right_bottom
        index_node_row_right_bottom = (row+self.rowNumber+1)%self.rowNumber
        index_node_column_right_bottom = (column+self.columnNumber+1)%self.columnNumber
        return self.composeIndex(index_node_row_right_bottom,index_node_column_right_bottom)    

    def composeIndex(self,row,column):
        number = column*self.rowNumber+row+1     
        return number         

            





            

