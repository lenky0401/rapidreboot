rapidreboot--https://github.com/lenky0401/rapidreboot
===========

利用kexec进行快速重启，这个重启过程和普通重启基本一致，但跳过了BIOS自检和GRUB选择两步，这样看来，其实也没多快，哈哈。
该工具不影响其他方式的重启，比如从系统菜单里选择重启或执行reboot命令等，那些操作都将进行普通方式的重启。

需要先安装python和kexec-tools

再按如下方式安装rapidreboot：

lenky@ubuntuS:~/lenky/work/rapidreboot$ mkdir build

lenky@ubuntuS:~/lenky/work/rapidreboot$ cd build/

lenky@ubuntuS:~/lenky/work/rapidreboot/build$ cmake ../

lenky@ubuntuS:~/lenky/work/rapidreboot/build$ sudo make install

无需做make，都是脚本程序，只是做文件替换和拷贝。
