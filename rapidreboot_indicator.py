#!/usr/bin/python
# -*- coding: utf-8 -*-

import gtk, pygtk
pygtk.require('2.0')
import appindicator
import os

def showabout(w):
	showtext = gtk.AboutDialog()
	showtext.set_name("快速重启 V0.1")
#	showtext.set_version("V0.1")
#	showtext.set_logo(gtk.gdk.pixbuf_new_from_file("/usr/local/share/rapidreboot/rapidreboot.png"))
	showtext.set_website("https://github.com/lenky0401/rapidreboot")
	showtext.set_copyright("利用kexec进行快速重启，这个重启过程和普通重启基本一致，但\n跳过了BIOS自检和GRUB选择两步，这样看来，其实也没多快，哈哈。\n该工具不影响其他方式的重启，比如从系统菜单里选择重启或执行\nreboot命令等，那些操作都将进行普通方式的重启。")
	showtext.connect("response", closeabout)
	showtext.show()

def closeabout(showtext, event=None):
	showtext.destroy()

def mainexit(w):
	window = gtk.MessageDialog(type=gtk.MESSAGE_QUESTION, buttons=gtk.BUTTONS_YES_NO)
	window.set_markup("确定需要退出吗?")
	ret = window.run()
	if ret == gtk.RESPONSE_YES:
		window.destroy()
		gtk.gdk.exit(0)
	window.destroy()

def rapidreboot(w):
	window = gtk.MessageDialog(type=gtk.MESSAGE_QUESTION, buttons=gtk.BUTTONS_YES_NO)
	window.set_markup("确定需要重启机器吗?")
	ret = window.run()
	if ret == gtk.RESPONSE_YES:
		os.system('touch /tmp/rapidrebootflag')
		os.system('dbus-send --system --print-reply --dest=org.freedesktop.ConsoleKit /org/freedesktop/ConsoleKit/Manager org.freedesktop.ConsoleKit.Manager.Restart')
	window.destroy()

if __name__ == "__main__":
	ind = appindicator.Indicator ("rapidreboot", "/usr/local/share/rapidreboot/rapidreboot.png", appindicator.CATEGORY_OTHER)
	ind.set_status (appindicator.STATUS_ACTIVE)
	mainmenu = gtk.Menu()
	rapidrebootmenu = gtk.MenuItem("快速重启")
	rapidrebootmenu.connect("activate", rapidreboot)
	mainmenu.append(rapidrebootmenu)
	rapidrebootmenu.show()
	aboutmenu = gtk.MenuItem("关于...")
	aboutmenu.connect("activate", showabout)
	mainmenu.append(aboutmenu)
	aboutmenu.show()
	exitmenu = gtk.MenuItem("退出")
	exitmenu.connect("activate", mainexit)
	mainmenu.append(exitmenu)
	exitmenu.show()
	ind.set_menu(mainmenu)
	gtk.main()
	gtk.gdk.threads_leave()


