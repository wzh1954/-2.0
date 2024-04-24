import glob
import os
import shutil
print("在开始拷贝前，先要把索尼相机“USB链接”选项改为“海量存储器”！")
k=input("相机存储卡所在的盘符：（直接输入A、B或者C，即分区的名称即可）")
while True:
    xz=input("1、查询是否有照片\n2、复制\n")
    if xz=="1":
        if os.path.exists(k+":\\"):
            os.chdir(k+":\\DCIM")
            n1=glob.glob("*")
            for n in n1:
                os.chdir(k+":\\DCIM\\"+n)
                n2=glob.glob("*")
                for nn in n2:
                    print (nn)
            os.chdir(k+":\\PRIVATE\\AVCHD\\BDMV\\STREAM")
            n11=glob.glob("*")
            for ns in n11:
                print (ns)
        else:
            print("相机未连接哦！")
    elif xz=="2":
        mb_n=input("放在桌面哪个文件夹里？")
        if os.path.exists("C:\\Users\\Administrator\\OneDrive\\Desktop\\"+mb_n):
             print("文件夹已存在啦！")
        else:
            print("正在拷贝文件，请耐心等候！")
            os.makedirs("C:\\Users\\Administrator\\OneDrive\\Desktop\\"+mb_n)
            os.chdir(k+":\\DCIM")
            nc1=glob.glob("*")
            for nc_1 in nc1:
                os.chdir(k+":\\DCIM\\"+nc_1)
                nc2=glob.glob("*")
                for ncn in nc2:
                    cn=k+":\\DCIM\\"+nc_1+"\\"+ncn
                    shutil.copy(cn,"C:\\Users\\Administrator\\OneDrive\\Desktop\\"+mb_n)
            os.chdir(k+":\\PRIVATE\\AVCHD\\BDMV\\STREAM")
            n22=glob.glob("*")
            for cns in n22:
                cns_n=k+":\\PRIVATE\\AVCHD\\BDMV\\STREAM"+"\\"+"\\"+cns
                shutil.copy(cns_n,"C:\\Users\\Administrator\\OneDrive\\Desktop\\"+mb_n)
            print("拷贝完成啦！")
    else:
        print("你想干嘛？")