import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gdk
from unit import Unit
import os, sys

APP_DIR = os.path.realpath(__file__)
APP_DIR = APP_DIR[:APP_DIR.rfind('/') + 1]
UI_FILE =  APP_DIR + "unitconverter.ui"

class GUI:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(UI_FILE)

        self.length = Unit(self, "length")
        self.weight = Unit(self, "weight")

        self.builder.connect_signals(self)

        window = self.builder.get_object('window')
        window.show_all()

    def convertLength(self, widget):
        self.length.convert()

    def convertWeight(self, widget):
        self.weight.convert()

    def switchLength(self, widget):
        self.length.switch()

    def switchWeight(self, widget):
        self.weight.switch()

    def destroy(window, self):
        Gtk.main_quit()

def main():
    app = GUI()
    Gtk.main()

if __name__ == "__main__":
    sys.exit(main())
