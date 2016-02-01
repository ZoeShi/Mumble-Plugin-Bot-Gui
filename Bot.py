#!/usr/bin/python3

from gi.repository import Gtk
import subprocess
class ButtonWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Bot")
        self.set_border_width(10)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        button = Gtk.Button.new_with_label("Bot starten")
        button.connect("clicked", self.on_click_me_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("Bot updaten")
        button.connect("clicked", self.on_open_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("Bot killen")
        button.connect("clicked", self.on_close_clicked)
        hbox.pack_start(button, True, True, 0)

    def on_click_me_clicked(self, button):
        subprocess.Popen('/home/rollidoc/bot-python/Bot_Starten.sh', shell=True)

    def on_open_clicked(self, button):
        subprocess.Popen('/home/rollidoc/bot-python/Bot_Updaten.sh', shell=True)

    def on_close_clicked(self, button):
        subprocess.Popen('/home/rollidoc/bot-python/Bot_Killen.sh', shell=True)
        #Gtk.main_quit()

win = ButtonWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
