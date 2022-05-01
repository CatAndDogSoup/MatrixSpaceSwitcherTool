"""

"""

# SYSTEM IMPORTS

# STANDARD LIB IMPORTS
from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2 import QtCore
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
import pymel.core as pm
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui

# LOCAL APP IMPORTS
from . import MatrixSpaceSwitchFunctional

def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)

class MatrixSpaceSwitchUI(MayaQWidgetDockableMixin, QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(MatrixSpaceSwitchUI, self).__init__()
        self.create_widget()

    def create_widget(self):
        self.setWindowFlags(QtCore.Qt.Tool)

        self.setParent(maya_main_window())
        self.setWindowFlags(QtCore.Qt.Window)

        # Set the object name
        self.setObjectName('MatrixSpaceSwitchUI_UniqueId')
        self.setWindowTitle('Matrix Space Switcher Tool')
        self.setMinimumSize(600, 600)
        self.setMaximumSize(600, 600)

        self.add_driver_button = QtWidgets.QPushButton(self, text="Add Driver Object")
        self.add_driver_button.clicked.connect(MatrixSpaceSwitchFunctional.MatrixSpaceSwitchFunctional.hello_world_test)
        self.rem_driver_button = QtWidgets.QPushButton(self, text="Remove Driver Object")

        self.driven_list = QtWidgets.QListWidget()
        self.driven_list.setFixedSize(280, 400)  # Width, Height
        self.driver_list = QtWidgets.QListWidget()
        self.driver_list.setFixedSize(280, 400)  # Width, Height

        # Create text labels and centre align the text
        self.driver_list_text = QtWidgets.QLabel(self, text="Driver list")
        self.driver_list_text.setAlignment(QtCore.Qt.AlignCenter)
        self.driven_list_text = QtWidgets.QLabel(self, text="Driven list")
        self.driven_list_text.setAlignment(QtCore.Qt.AlignCenter)

        # DRIVER LAYOUT
        self.driver_layout = QtWidgets.QVBoxLayout()
        self.driver_layout.addWidget(self.driven_list_text)
        self.driver_layout.addWidget(self.driven_list)
        self.driver_layout.addStretch()

        # DRIVEN LAYOUT
        self.driven_layout = QtWidgets.QVBoxLayout()

        self.driven_layout.addWidget(self.driver_list_text)
        self.driven_layout.addWidget(self.driver_list)
        self.driven_layout.addStretch()

        self.driven_layout.addWidget(self.add_driver_button)
        self.driven_layout.addWidget(self.rem_driver_button)

        # FINAL LAYOUT
        self.h_layout = QtWidgets.QHBoxLayout()
        self.h_layout.addLayout(self.driver_layout)
        self.h_layout.addLayout(self.driven_layout)
        self.h_layout.addStretch()

        self.setLayout(self.h_layout)


try:
    pass
    #ui.deleteLater()
except NameError as e:
    pass

if pm.window("MatrixSpaceSwitchUI_UniqueIdWorkspaceControl", exists=True):
    pm.deleteUI("MatrixSpaceSwitchUI_UniqueIdWorkspaceControl")

ui = MatrixSpaceSwitchUI()
ui.show(dockable=True)