# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './mw4/gui/widgets/simulator.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SimulatorDialog(object):
    def setupUi(self, SimulatorDialog):
        SimulatorDialog.setObjectName("SimulatorDialog")
        SimulatorDialog.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SimulatorDialog.sizePolicy().hasHeightForWidth())
        SimulatorDialog.setSizePolicy(sizePolicy)
        SimulatorDialog.setMinimumSize(QtCore.QSize(800, 600))
        SimulatorDialog.setMaximumSize(QtCore.QSize(1600, 1230))
        SimulatorDialog.setSizeIncrement(QtCore.QSize(10, 10))
        SimulatorDialog.setBaseSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        SimulatorDialog.setFont(font)
        self.horizontalLayout = QtWidgets.QHBoxLayout(SimulatorDialog)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.simulator = QtWidgets.QHBoxLayout()
        self.simulator.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.simulator.setSpacing(0)
        self.simulator.setObjectName("simulator")
        self.gridLayout.addLayout(self.simulator, 0, 1, 2, 1)
        self.groupBox = QtWidgets.QGroupBox(SimulatorDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setProperty("large", True)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(8, 10, 16, 4)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topView = QtWidgets.QPushButton(self.groupBox)
        self.topView.setMinimumSize(QtCore.QSize(0, 25))
        self.topView.setObjectName("topView")
        self.verticalLayout.addWidget(self.topView)
        self.topWestView = QtWidgets.QPushButton(self.groupBox)
        self.topWestView.setMinimumSize(QtCore.QSize(0, 25))
        self.topWestView.setObjectName("topWestView")
        self.verticalLayout.addWidget(self.topWestView)
        self.westView = QtWidgets.QPushButton(self.groupBox)
        self.westView.setMinimumSize(QtCore.QSize(0, 25))
        self.westView.setObjectName("westView")
        self.verticalLayout.addWidget(self.westView)
        self.topEastView = QtWidgets.QPushButton(self.groupBox)
        self.topEastView.setMinimumSize(QtCore.QSize(0, 25))
        self.topEastView.setObjectName("topEastView")
        self.verticalLayout.addWidget(self.topEastView)
        self.eastView = QtWidgets.QPushButton(self.groupBox)
        self.eastView.setMinimumSize(QtCore.QSize(0, 25))
        self.eastView.setObjectName("eastView")
        self.verticalLayout.addWidget(self.eastView)
        self.telescopeView = QtWidgets.QPushButton(self.groupBox)
        self.telescopeView.setMinimumSize(QtCore.QSize(0, 25))
        self.telescopeView.setObjectName("telescopeView")
        self.verticalLayout.addWidget(self.telescopeView)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(SimulatorDialog)
        self.groupBox_2.setProperty("large", True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setContentsMargins(8, 10, 16, 4)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkDomeTransparent = QtWidgets.QCheckBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkDomeTransparent.sizePolicy().hasHeightForWidth())
        self.checkDomeTransparent.setSizePolicy(sizePolicy)
        self.checkDomeTransparent.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.checkDomeTransparent.setFont(font)
        self.checkDomeTransparent.setObjectName("checkDomeTransparent")
        self.verticalLayout_2.addWidget(self.checkDomeTransparent)
        self.checkShowPointer = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkShowPointer.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.checkShowPointer.setFont(font)
        self.checkShowPointer.setObjectName("checkShowPointer")
        self.verticalLayout_2.addWidget(self.checkShowPointer)
        self.checkShowLaser = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkShowLaser.setMinimumSize(QtCore.QSize(0, 25))
        self.checkShowLaser.setObjectName("checkShowLaser")
        self.verticalLayout_2.addWidget(self.checkShowLaser)
        self.checkShowBuildPoints = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkShowBuildPoints.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.checkShowBuildPoints.setFont(font)
        self.checkShowBuildPoints.setObjectName("checkShowBuildPoints")
        self.verticalLayout_2.addWidget(self.checkShowBuildPoints)
        self.checkShowNumbers = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkShowNumbers.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.checkShowNumbers.setFont(font)
        self.checkShowNumbers.setObjectName("checkShowNumbers")
        self.verticalLayout_2.addWidget(self.checkShowNumbers)
        self.checkShowSlewPath = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkShowSlewPath.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.checkShowSlewPath.setFont(font)
        self.checkShowSlewPath.setObjectName("checkShowSlewPath")
        self.verticalLayout_2.addWidget(self.checkShowSlewPath)
        self.checkShowHorizon = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkShowHorizon.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.checkShowHorizon.setFont(font)
        self.checkShowHorizon.setObjectName("checkShowHorizon")
        self.verticalLayout_2.addWidget(self.checkShowHorizon)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(SimulatorDialog)
        QtCore.QMetaObject.connectSlotsByName(SimulatorDialog)

    def retranslateUi(self, SimulatorDialog):
        _translate = QtCore.QCoreApplication.translate
        SimulatorDialog.setWindowTitle(_translate("SimulatorDialog", "Mount Simulation View"))
        self.groupBox.setToolTip(_translate("SimulatorDialog", "<html><head/><body>\n"
"<p>Left mouse button:<br> \n"
"While the left mouse button is pressed, mouse movement along x-axis moves the camera left and right and movement along y-axis moves it up and down.</p>\n"
"<p>Right mouse button:<br> \n"
"While the right mouse button is pressed, mouse movement along x-axis pans the camera around the camera view center and movement along y-axis tilts it around the camera view center.</p>\n"
"<p>Both left and right mouse button: <br>\n"
"While both the left and the right mouse button are pressed, mouse movement along y-axis zooms the camera in and out without changing the view center.</p>\n"
"<p>Mouse scroll wheel:<br> \n"
"Zooms the camera in and out without changing the view center.</p>\n"
"<p>Arrow keys:<br> \n"
"Move the camera vertically and horizontally relative to camera viewport.</p>\n"
"<p>Page up and page down keys: <br>\n"
"Move the camera forwards and backwards.</p>\n"
"<p>Shift key: <br>\n"
"Changes the behavior of the up and down arrow keys to zoom the camera in and out without changing the view center. The other movement keys are disabled.</p>\n"
"<p>Alt key: <br>\n"
"Changes the behovior of the arrow keys to pan and tilt the camera around the view center. Disables the page up and page down keys.</p>\n"
"<p>Escape: <br>\n"
"Moves the camera so that entire scene is visible in the camera viewport.</p>\n"
"</html></head/></body>"))
        self.groupBox.setTitle(_translate("SimulatorDialog", "Select View"))
        self.topView.setToolTip(_translate("SimulatorDialog", "<html><head/><body><p>When pressed, show top view of scene.</p></body></html>"))
        self.topView.setText(_translate("SimulatorDialog", "Top View"))
        self.topWestView.setToolTip(_translate("SimulatorDialog", "<html><head/><body><p>When pressed, show view from top west to telecope scene.</p></body></html>"))
        self.topWestView.setText(_translate("SimulatorDialog", "Top West View"))
        self.westView.setToolTip(_translate("SimulatorDialog", "<html><head/><body><p>When pressed, show view from west to telecope scene.</p></body></html>"))
        self.westView.setText(_translate("SimulatorDialog", "West View"))
        self.topEastView.setToolTip(_translate("SimulatorDialog", "<html><head/><body><p>When pressed, show view from top east to telecope scene.</p></body></html>"))
        self.topEastView.setText(_translate("SimulatorDialog", "Top East View"))
        self.eastView.setToolTip(_translate("SimulatorDialog", "<html><head/><body><p>When pressed, show view from east to telecope scene.</p></body></html>"))
        self.eastView.setText(_translate("SimulatorDialog", "East View"))
        self.telescopeView.setToolTip(_translate("SimulatorDialog", "<html><head/><body><p>When pressed, show view from telecope to sphere.</p></body></html>"))
        self.telescopeView.setText(_translate("SimulatorDialog", "Telescope View"))
        self.groupBox_2.setTitle(_translate("SimulatorDialog", "Show Settings"))
        self.checkDomeTransparent.setToolTip(_translate("SimulatorDialog", "<html><head/><body><p>Show dome transparent.</p></body></html>"))
        self.checkDomeTransparent.setText(_translate("SimulatorDialog", "Dome transp."))
        self.checkShowPointer.setToolTip(_translate("SimulatorDialog", "<html><head/><body><p>Show intersection point from line of sight and dome sphere.</p></body></html>"))
        self.checkShowPointer.setText(_translate("SimulatorDialog", "Intersect Point"))
        self.checkShowLaser.setToolTip(_translate("SimulatorDialog", "<html><head/><body><p>Show line of sight from telescope.</p></body></html>"))
        self.checkShowLaser.setText(_translate("SimulatorDialog", "Laser"))
        self.checkShowBuildPoints.setToolTip(_translate("SimulatorDialog", "<html><head/><body><p>Show build points on outer sphere.</p></body></html>"))
        self.checkShowBuildPoints.setText(_translate("SimulatorDialog", "Build Points"))
        self.checkShowNumbers.setToolTip(_translate("SimulatorDialog", "<html><head/><body><p>Show build point number close to build point.</p></body></html>"))
        self.checkShowNumbers.setText(_translate("SimulatorDialog", "Numbers"))
        self.checkShowSlewPath.setToolTip(_translate("SimulatorDialog", "<html><head/><body><p>Show slew path between build points.</p></body></html>"))
        self.checkShowSlewPath.setText(_translate("SimulatorDialog", "Slew Path"))
        self.checkShowHorizon.setToolTip(_translate("SimulatorDialog", "<html><head/><body><p>Show horizon in scene.</p></body></html>"))
        self.checkShowHorizon.setText(_translate("SimulatorDialog", "Horizon"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SimulatorDialog = QtWidgets.QWidget()
    ui = Ui_SimulatorDialog()
    ui.setupUi(SimulatorDialog)
    SimulatorDialog.show()
    sys.exit(app.exec_())
