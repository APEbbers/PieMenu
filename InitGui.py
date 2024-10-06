import os
import FreeCAD as App
import FreeCADGui as Gui
import PieMenu


def QT_TRANSLATE_NOOP(context, text):
    return text


translate = App.Qt.translate

try:
    mw = Gui.getMainWindow()
    mw.workbenchActivated.connect(PieMenu.pieMenuStart)
except Exception as e:
    print(e)

Gui.addLanguagePath(os.path.join(os.path.dirname(PieMenu.__file__), "translations"))
Gui.updateLocale()
