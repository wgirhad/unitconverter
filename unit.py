import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gdk
import os, sys

APP_DIR = os.path.realpath(__file__)
APP_DIR = APP_DIR[:APP_DIR.rfind('/') + 1]

class Unit:

    def __init__(self, app, dim):
        unitFile = open(APP_DIR + dim + '.lst', 'r')
        text = unitFile.read()
        passwd = None
        buf = text.split("\n")

        formulas = []
        names = []

        self.unitA = 0
        self.unitB = 0

        for line in buf:
            if line == '':
                continue

            line = line.split(';')

            name = line[0]
            unit = line[1]
            form = line[2]

            names.append(name.title())
            formulas.append(form)

            if unit == 'a':
                self.unitA = float(form)

            if unit == 'b':
                self.unitB = float(form)

        unitFile.close()
        text = None
        buf = None

        self.combo1 = app.builder.get_object('combo' + dim.capitalize() + '1')
        self.combo2 = app.builder.get_object('combo' + dim.capitalize() + '2')
        for name in names:
            self.combo1.append_text(name)
            self.combo2.append_text(name)

        self.formula1 = Gtk.ComboBoxText()
        self.formula2 = Gtk.ComboBoxText()
        for formula in formulas:
            self.formula1.append_text(formula)
            self.formula2.append_text(formula)

        self.formula1.set_entry_text_column(0)
        self.formula2.set_entry_text_column(0)

        self.entry1 = app.builder.get_object('entry' + dim.capitalize() + '1')
        self.entry2 = app.builder.get_object('entry' + dim.capitalize() + '2')

        self.combo1.set_active(0)
        self.combo2.set_active(1)

    def switch(self):
        x = self.combo1.get_active()
        self.combo1.set_active(self.combo2.get_active())
        self.combo2.set_active(x)

    def convert(self):
        self.formula1.set_active(self.combo1.get_active())
        self.formula2.set_active(self.combo2.get_active())

        result = ""

        try:
            a = self.unitA
            b = self.unitB
            value1 = float(self.entry1.get_text())
            formula1 = self.formula1.get_active_text()
            formula2 = self.formula2.get_active_text()
            unit1 = float(eval(formula1))
            unit2 = float(eval(formula2))
            result = value1 * unit1 / unit2
        except (ValueError, TypeError):
            pass

        self.entry2.set_text(str(result))
