1. 两个linux系统怎么传文件？ Linux查看磁盘命令？
    当两台LINUX主机之间要互传文件时可使用SCP命令来实现
    scp local_file remote_username@remote_ip:remote_folder 
    scp -r www.runoob.com:/home/root/others/ /home/space/music/

    统计磁盘整体情况，包括磁盘大小，已使用，可用。命令“df”

2. 根据进程名称查看进程号
    ps -ef|grep 进程名
    ps是processes的缩写，是对当前系统进程进行监控
    -ef 是用标准的格式显示进程
    grep 进程名 表示搜索这个进程


    根据进行id查看占用端口号
    netstat -a|grep 23297
    -a 表示all



3. 查找名字为test的文件或目录
    find ./ -name test


Linux 在文件中查找某字符串
命令：

    grep 'word' filename

vi:
    命令模式下输入“/字符串”，例如“/Section 3”
