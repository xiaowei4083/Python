#登录系统
#导入模块
import pymysql
import os
import pygame

deng=True
zhu=True
xitong=True
while xitong:#设置循环
    # 连接database数据库
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="2841521", database="zhanghao_db",
                           charset="utf8")
    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()
    jin=int(input("欢迎登录：\n登录输入1\n注册输入0:1/0\n"))
    if jin==1:
        while deng:
            zhanghao = input(str("请输入账号：\n"))
            mima = input(str("请输入密码：\n"))

            sql = 'select * from user where zhanghao=%s and mima=%s;' # 定义要执行的SQL语句1
            ret = cursor.execute(sql, [zhanghao, mima]) # 执行SQL语句
            cursor.close() # 关闭光标对象
            conn.close() # 关闭数据库连接
            if ret:
                print("登录中。。。")
                xitong = False
                #调用另一个PY文件
                os.system("python 007.py")

                break
            else:
                print("密码错误")
                deng=False
    if jin==0:
        while zhu:
            sql = "insert into user (zhanghao,mima) VALUES (%s,%s);"# 定义要执行的SQL语句 （写入数据库）
            zhanghao = str(input("请输入注册账号：\n"))
            mima = str(input("请输入注册密码：\n"))
            Mima = str(input("请输入确认密码：\n"))
            if mima != Mima:
                print("确认密码与注册密码不一致，请重输：")
                continue
            elif mima == Mima:
                cursor.execute(sql,[zhanghao,mima]) # 执行SQL语句
                conn.commit() # 提交事务
                cursor.close() ## 关闭光标对象
                conn.close() # 关闭数据库连接
                print("注册成功返回登录")
                zhu=False




