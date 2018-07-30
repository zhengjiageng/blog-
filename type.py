import pymysql

con = pymysql.connect('127.0.0.1','root','123456','test')
con.set_charset('utf8')
cursor = con.cursor()

#添加顶级分类
def addTopType():
    typeName = input('输入类别名称')
    sql = 'insert into type values(null,"{}",0,"0,")'.format(typeName)
    cursor.execute(sql)
    con.commit()
    if cursor.rowcount:
        print('顶级分类 添加成功')


#添加子分类
def addSonType():
    id = input('输入类别id')
    sql = 'select * from type where id={}'.format(id)
    cursor.execute(sql)
    result = cursor.fetchone()
    # (1,‘服装’,0,‘0,’)
    typeName = input('输入类别名称')
    sql = 'insert into type values(null,"{}",{},"{}")'.format(typeName,result[0],result[-1]+str(result[0])+',')
    print(sql)
    cursor.execute(sql)
    con.commit()
    if cursor.rowcount:
        print('顶级分类 添加成功')


#展示分类
def showType():
    sql = 'select * from type order by concat(path,id)'
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        repeat = row[-1].count(',')*'|-'
        print(repeat,row[0],row[1],row[-1])



while True:
    print('***1 添加顶级分类*********')
    print('***2 添加子分类*********')
    print('***3 查看分类*********')

    choose = input('输入你要选择的类别')
    if choose == '1':
        addTopType()
    elif choose == '2':
        addSonType()
    else:
        showType()