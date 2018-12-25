'''
攻击类型划分
'''
specific = {
        'normal.': 0,
        'ipsweep.': 1,
        'mscan.': 1,
        'nmap.': 1,
        'portsweep.': 1,
        'saint.': 1,
        'satan.': 1,
        'apache2.': 2,
        'back.': 2,
        'mailbomb.': 2,
        'neptune.': 2,
        'pod.': 2,
        'land.': 2,
        'processtable.': 2,
        'smurf.': 2,
        'teardrop.': 2,
        'udpstorm.': 2,
        'buffer_overflow.': 3,
        'loadmodule.': 3,
        'perl.': 3,
        'ps.': 3,
        'rootkit.': 3,
        'sqlattack.': 3,
        'xterm.': 3,
        'ftp_write.': 4,
        'guess_passwd.': 4,
        'httptunnel.': 3,  # disputation resolved
        'imap.': 4,
        'multihop.': 4,  # disputation resolved
        'named.': 4,
        'phf.': 4,
        'sendmail.': 4,
        'snmpgetattack.': 4,
        'snmpguess.': 4,
        'worm.': 4,
        'xlock.': 4,
        'xsnoop.': 4,
        'spy.': 4,
        'warezclient.': 4,
        'warezmaster.': 4  # disputation resolved
}
index2major ={
    0:'NORMAL',
    1:'PROBE',
    2:'DOS',
    3:'U2R',
    4:'R2L'
}

def attack2majorindex(colLabel):
    '''
    :colLabel: a list of specific classes
    :return: a list of index of 5 major classes
    map normal to 0
    map others to 1,2,3,4
    '''
    l = []
    for val in colLabel:
        l.append(specific[val])
    return l

def mapper_attack2majorindex(label):
    '''
    :return: attack_type to index in [0,1,2,3,4]
    '''
    return specific[label]


def majorindex2string(index):
    '''
    :index: in [0,1,2,3,4]
    :return: String: NORMAL,PROBE,DOS,U2R,R2L
    '''
    return index2major[index]



'''
合并稀疏特征
'''
def mapper_mergeSparseFeatureInService(serviceType):
    '''
    :serviceType: string. a specific service type
    :return: original input, 'normal_service_group', or 'satan_service_group'
    映射：
    ntp_u,urh_i,tftp_u,red_i 为 normal_service_group
    pm_dump,http_2784,harvest,aol,http_8001 为 satan_service_group
    '''
    if serviceType in ['ntp_u','urh_i','tftp_u','red_i']:
        return 'normal_service_group'
    if serviceType in ['pm_dump','http_2784','harvest','aol','http_8001']:
        return 'satan_service_group'
    return serviceType

def mergeSparseFeatureInService(colService):
    '''
    :colService: a columns of Service
    :return: a list of original input, 'normal_service_group', or 'satan_service_group'
    映射：
    ntp_u,urh_i,tftp_u,red_i 为 normal_service_group
    pm_dump,http_2784,harvest,aol,http_8001 为 satan_service_group
    '''
    group={
        # normal
        'ntp_u':'normal_service_group',
        'urh_i':'normal_service_group',
        'tftp_u':'normal_service_group',
        'red_i':'normal_service_group',
        # satan
        'pm_dump':'satan_service_group',
        'http_2784':'satan_service_group',
        'harvest':'satan_service_group',
        'aol':'satan_service_group',
        'http_8001':'satan_service_group'
    }
    result = []
    for val in colService:
        if val in group:
            result.append(group[val])
        else:
            result.append(val)
    return result      



'''
绘制混淆矩阵
'''
from sklearn.metrics import confusion_matrix

def drawConfusionMatrix(true,pred,labels):
    '''
    :true: true label list
    :pre:  predict label list
    :label: label, decide order of x , y
    :return: confusion matrix, plt
    '''
    from sklearn.metrics import confusion_matrix # 根据true和pred，lebals，生成混淆矩阵
    import matplotlib.pyplot as plt

    cm = confusion_matrix(true,pred,labels)
    plt.matshow(cm,cmap=plt.cm.Pastel1)
    plt.colorbar()     # 颜色标签
    '''
    annotate:主要在图形中添加注释
    第一个参数添加注释
    第一个参数是注释的内容
    xy设置箭头尖的坐标
    horizontalalignment水平对齐
    verticalalignment垂直对齐
    '''
    for x in range(len(cm)):
        for y in range(len(cm)):
            plt.annotate(cm[x,y],xy=(y,x),horizontalalignment='center',verticalalignment='center')
    plt.ylabel('True label')# 坐标轴标签
    plt.xlabel('Predicted label')# 坐标轴标签    
    return cm,plt

def getConfusionMatrix(true,pred,labels):
    return confusion_matrix(true,pred,labels)

def calculatePrecision(cm):
    '''
    :return: a dict (label:value) recording recall rate
    '''
    result={}
    for x in range(len(cm)):
        tp = cm[x,x]
        s = sum(cm[:,x])
        result[x]= tp/s if s is not 0 else 0
    return result          

def calculateRecall(cm):
    '''
    :return: a dict (label:value) recording precision rate
    '''
    result={}
    for x in range(len(cm)):
        tp = cm[x,x]
        s = sum(cm[x,:])
        result[x]= tp/s if s is not 0 else 0
    return result            

def preAndRec(cm,labels):
    '''
    根据输入混淆矩阵和labels，计算各类Precision和Recall并打印
    '''
    solve = calculatePrecision(cm=cm)
    print('-'*30)
    print("Precision:")
    for i in range(len(solve)):
        print("%s : \t %f"%( labels[i], solve[i]))
    solve = calculateRecall(cm=cm)
    print()
    print("Recall:")
    for i in range(len(solve)):
        print("%s : \t %f"%( labels[i], solve[i]))
    print('-'*30)