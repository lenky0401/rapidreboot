project(rapidreboot)
cmake_minimum_required(VERSION 2.8.6)

install(DIRECTORY test DESTINATION /usr/local/share/rapidreboot)
install(FILES rapidreboot.png DESTINATION /usr/local/share/rapidreboot)
install(PROGRAMS rapidreboot_indicator.py DESTINATION /usr/bin)
install(PROGRAMS kexec-load DESTINATION /etc/init.d)
install(FILES rapidreboot.desktop DESTINATION /etc/xdg/autostart/)

