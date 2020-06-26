# 由于下载的标签数据集合在一个txt文件中，不适合用于华为云ModelArts的训练
# 因此通过本程序和lebal-create.py进行对标签数据的预处理
# lebal-create.py消除文本中的无关前缀
# 本程序将文本中的照片文件名和分类标签拆分开
# 照片文件名作为新的txt文件名
# 分类标签作为内容写入新的txt文件
def create__file(file_path,msg):   #设置函数，参数分别是新文件的路径和文件名 以及 内容
    f=open(file_path,"a")
    f.write(msg)
    f.close
fopen=open('list.txt','r')
lines=fopen.readlines()  #读取文件中的行数
for line in lines:       #遍历txt文件
    str=line[0:line.rfind('.jpg')]    #获取照片文件名
    label=line.split('.jpg	')[-1]    #获取分类标签
    create__file("./list/"+str+".txt",label)    #创建新的txt文件，即各照片对应的标签信息
