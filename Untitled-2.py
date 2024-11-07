#定义矩阵类
class Matrix:
    #定义矩阵自身属性
    def __init__(self,rows,cols):
        self.rows=rows
        self.cols=cols
        self.matrix=[[0 for _ in range(self.cols)]for _ in range(self.rows)]
    #输入矩阵  
    def input_num(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j]=int(input())
    #矩阵加法            
    def add(self,other):
        if self.rows!=other.rows or self.cols!=other.cols:
            print("非同型矩阵")
        else:
            result=[[0 for _ in range(self.cols)]for _ in range(self.rows)]
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i][j]=self.matrix[i][j]+other.matrix[i][j]
            print("矩阵相加结果：")
            for k in result:
                print(k)
    #矩阵减法
    def sub(self,other):
        if self.rows!=other.rows or self.cols!=other.cols:
            print("非同型矩阵")
        else:
            result=[[0 for _ in range(self.cols)]for _ in range(self.rows)]
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i][j]=self.matrix[i][j]-other.matrix[i][j]
            print("矩阵相减结果：")
            for k in result:
                print(k)

    #矩阵相乘
    def mul(self,other):
        if self.cols!=other.rows:
            print("矩阵内标不相等，无法相乘")
        else:
            result=[[0 for _ in range(other.cols)]for _ in range(self.rows)]
            for i in range(self.rows):
                for j in range(other.cols):
                    sum=0
                    for k in range(self.cols):
                        sum=sum+self.matrix[i][k]*other.matrix[k][j]
                    result[i][j]=sum
        for m in result:
            print(m)
#输入矩阵1
rows1=int(input("请输入矩阵1的行数："))
cols1=int(input("请输入矩阵1的列数："))
matrix1=Matrix(rows1,cols1)
matrix1.input_num()
#输入矩阵2
rows2=int(input("请输入矩阵2的行数："))
cols2=int(input("请输入矩阵2的列数："))
matrix2=Matrix(rows2,cols2)
matrix2=Matrix(rows2,cols2)
matrix2.input_num()
#矩阵相加
matrix1.add(matrix2)
#矩阵相减
matrix1.sub(matrix2)
#矩阵相乘
matrix1.mul(matrix2)