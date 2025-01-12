# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './mw4/gui/widgets/image.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ImageDialog(object):
    def setupUi(self, ImageDialog):
        ImageDialog.setObjectName("ImageDialog")
        ImageDialog.resize(800, 600)
        ImageDialog.setMinimumSize(QtCore.QSize(800, 600))
        ImageDialog.setMaximumSize(QtCore.QSize(1600, 1230))
        ImageDialog.setSizeIncrement(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        ImageDialog.setFont(font)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ImageDialog)
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupImageActions = QtWidgets.QGroupBox(ImageDialog)
        self.groupImageActions.setProperty("large", True)
        self.groupImageActions.setObjectName("groupImageActions")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupImageActions)
        self.gridLayout_4.setContentsMargins(5, 10, 5, 5)
        self.gridLayout_4.setHorizontalSpacing(10)
        self.gridLayout_4.setVerticalSpacing(5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.solve = QtWidgets.QPushButton(self.groupImageActions)
        self.solve.setEnabled(False)
        self.solve.setMinimumSize(QtCore.QSize(95, 21))
        self.solve.setObjectName("solve")
        self.gridLayout_4.addWidget(self.solve, 3, 0, 1, 1)
        self.exposeN = QtWidgets.QPushButton(self.groupImageActions)
        self.exposeN.setEnabled(False)
        self.exposeN.setMinimumSize(QtCore.QSize(95, 21))
        self.exposeN.setObjectName("exposeN")
        self.gridLayout_4.addWidget(self.exposeN, 1, 1, 1, 1)
        self.expose = QtWidgets.QPushButton(self.groupImageActions)
        self.expose.setEnabled(False)
        self.expose.setMinimumSize(QtCore.QSize(95, 21))
        self.expose.setObjectName("expose")
        self.gridLayout_4.addWidget(self.expose, 1, 0, 1, 1)
        self.load = QtWidgets.QPushButton(self.groupImageActions)
        self.load.setMinimumSize(QtCore.QSize(95, 21))
        self.load.setObjectName("load")
        self.gridLayout_4.addWidget(self.load, 0, 0, 1, 1)
        self.abortExpose = QtWidgets.QPushButton(self.groupImageActions)
        self.abortExpose.setEnabled(False)
        self.abortExpose.setMinimumSize(QtCore.QSize(95, 21))
        self.abortExpose.setObjectName("abortExpose")
        self.gridLayout_4.addWidget(self.abortExpose, 1, 2, 1, 1)
        self.abortSolve = QtWidgets.QPushButton(self.groupImageActions)
        self.abortSolve.setEnabled(False)
        self.abortSolve.setMinimumSize(QtCore.QSize(95, 21))
        self.abortSolve.setObjectName("abortSolve")
        self.gridLayout_4.addWidget(self.abortSolve, 3, 1, 1, 1)
        self.embedData = QtWidgets.QCheckBox(self.groupImageActions)
        self.embedData.setMinimumSize(QtCore.QSize(100, 21))
        self.embedData.setObjectName("embedData")
        self.gridLayout_4.addWidget(self.embedData, 3, 3, 1, 1)
        self.autoSolve = QtWidgets.QCheckBox(self.groupImageActions)
        self.autoSolve.setMinimumSize(QtCore.QSize(100, 21))
        self.autoSolve.setObjectName("autoSolve")
        self.gridLayout_4.addWidget(self.autoSolve, 3, 2, 1, 1)
        self.timeTagImage = QtWidgets.QCheckBox(self.groupImageActions)
        self.timeTagImage.setMinimumSize(QtCore.QSize(100, 0))
        self.timeTagImage.setObjectName("timeTagImage")
        self.gridLayout_4.addWidget(self.timeTagImage, 1, 3, 1, 1)
        self.slewCenter = QtWidgets.QPushButton(self.groupImageActions)
        self.slewCenter.setEnabled(True)
        self.slewCenter.setMinimumSize(QtCore.QSize(95, 21))
        self.slewCenter.setObjectName("slewCenter")
        self.gridLayout_4.addWidget(self.slewCenter, 0, 1, 1, 1)
        self.horizontalLayout_5.addWidget(self.groupImageActions)
        self.groupBox = QtWidgets.QGroupBox(ImageDialog)
        self.groupBox.setProperty("large", True)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setContentsMargins(5, 15, 15, 5)
        self.gridLayout_3.setVerticalSpacing(5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.aspectLocked = QtWidgets.QCheckBox(self.groupBox)
        self.aspectLocked.setMinimumSize(QtCore.QSize(105, 0))
        self.aspectLocked.setObjectName("aspectLocked")
        self.gridLayout_3.addWidget(self.aspectLocked, 1, 0, 1, 1)
        self.showCrosshair = QtWidgets.QCheckBox(self.groupBox)
        self.showCrosshair.setMinimumSize(QtCore.QSize(105, 21))
        self.showCrosshair.setObjectName("showCrosshair")
        self.gridLayout_3.addWidget(self.showCrosshair, 2, 0, 1, 1)
        self.flipH = QtWidgets.QCheckBox(self.groupBox)
        self.flipH.setMinimumSize(QtCore.QSize(60, 0))
        self.flipH.setObjectName("flipH")
        self.gridLayout_3.addWidget(self.flipH, 1, 1, 1, 1)
        self.flipV = QtWidgets.QCheckBox(self.groupBox)
        self.flipV.setMinimumSize(QtCore.QSize(60, 0))
        self.flipV.setObjectName("flipV")
        self.gridLayout_3.addWidget(self.flipV, 2, 1, 1, 1)
        self.color = QtWidgets.QComboBox(self.groupBox)
        self.color.setMinimumSize(QtCore.QSize(100, 21))
        self.color.setObjectName("color")
        self.color.addItem("")
        self.color.addItem("")
        self.color.addItem("")
        self.color.addItem("")
        self.color.addItem("")
        self.gridLayout_3.addWidget(self.color, 0, 0, 1, 1)
        self.horizontalLayout_5.addWidget(self.groupBox)
        self.photometryGroup = QtWidgets.QGroupBox(ImageDialog)
        self.photometryGroup.setCheckable(True)
        self.photometryGroup.setProperty("large", True)
        self.photometryGroup.setObjectName("photometryGroup")
        self.Imageview = QtWidgets.QGridLayout(self.photometryGroup)
        self.Imageview.setContentsMargins(10, 15, 15, 5)
        self.Imageview.setHorizontalSpacing(10)
        self.Imageview.setVerticalSpacing(5)
        self.Imageview.setObjectName("Imageview")
        self.snTarget = QtWidgets.QComboBox(self.photometryGroup)
        self.snTarget.setMinimumSize(QtCore.QSize(120, 21))
        self.snTarget.setObjectName("snTarget")
        self.snTarget.addItem("")
        self.snTarget.addItem("")
        self.snTarget.addItem("")
        self.snTarget.addItem("")
        self.snTarget.addItem("")
        self.Imageview.addWidget(self.snTarget, 0, 1, 1, 2)
        self.isoLayer = QtWidgets.QCheckBox(self.photometryGroup)
        self.isoLayer.setMinimumSize(QtCore.QSize(100, 0))
        self.isoLayer.setObjectName("isoLayer")
        self.Imageview.addWidget(self.isoLayer, 1, 1, 1, 2)
        self.showValues = QtWidgets.QCheckBox(self.photometryGroup)
        self.showValues.setMinimumSize(QtCore.QSize(100, 0))
        self.showValues.setObjectName("showValues")
        self.Imageview.addWidget(self.showValues, 2, 1, 1, 2)
        self.horizontalLayout_5.addWidget(self.photometryGroup)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.horizontalLayout_5.setStretch(3, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(5, 0, 0, 0)
        self.gridLayout_2.setSpacing(4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabImage = QtWidgets.QTabWidget(ImageDialog)
        self.tabImage.setMinimumSize(QtCore.QSize(140, 0))
        self.tabImage.setElideMode(QtCore.Qt.ElideNone)
        self.tabImage.setMovable(False)
        self.tabImage.setObjectName("tabImage")
        self.Image = QtWidgets.QWidget()
        self.Image.setObjectName("Image")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.Image)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.image = ImageBar(self.Image)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        self.image.setMinimumSize(QtCore.QSize(0, 0))
        self.image.setObjectName("image")
        self.gridLayout_5.addWidget(self.image, 0, 0, 1, 1)
        self.tabImage.addTab(self.Image, "")
        self.HFR = QtWidgets.QWidget()
        self.HFR.setObjectName("HFR")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.HFR)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 10)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.hfr = ImageBar(self.HFR)
        self.hfr.setObjectName("hfr")
        self.gridLayout_11.addWidget(self.hfr, 0, 0, 1, 1)
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setContentsMargins(20, -1, -1, 0)
        self.gridLayout_15.setHorizontalSpacing(10)
        self.gridLayout_15.setVerticalSpacing(0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.hfrPercentile = QtWidgets.QLineEdit(self.HFR)
        self.hfrPercentile.setMaximumSize(QtCore.QSize(30, 16777215))
        self.hfrPercentile.setObjectName("hfrPercentile")
        self.gridLayout_15.addWidget(self.hfrPercentile, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_15.addItem(spacerItem2, 0, 9, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.HFR)
        self.label_13.setMinimumSize(QtCore.QSize(0, 0))
        self.label_13.setObjectName("label_13")
        self.gridLayout_15.addWidget(self.label_13, 1, 2, 1, 1)
        self.medianHFR = QtWidgets.QLineEdit(self.HFR)
        self.medianHFR.setMaximumSize(QtCore.QSize(60, 16777215))
        self.medianHFR.setObjectName("medianHFR")
        self.gridLayout_15.addWidget(self.medianHFR, 0, 3, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.HFR)
        self.label_17.setMinimumSize(QtCore.QSize(0, 0))
        self.label_17.setObjectName("label_17")
        self.gridLayout_15.addWidget(self.label_17, 0, 0, 1, 1)
        self.numberStars = QtWidgets.QLineEdit(self.HFR)
        self.numberStars.setMaximumSize(QtCore.QSize(60, 16777215))
        self.numberStars.setObjectName("numberStars")
        self.gridLayout_15.addWidget(self.numberStars, 1, 3, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.HFR)
        self.label_19.setMinimumSize(QtCore.QSize(0, 0))
        self.label_19.setObjectName("label_19")
        self.gridLayout_15.addWidget(self.label_19, 0, 2, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_15, 1, 0, 1, 1)
        self.gridLayout_11.setRowStretch(0, 1)
        self.tabImage.addTab(self.HFR, "")
        self.TiltSquare = QtWidgets.QWidget()
        self.TiltSquare.setObjectName("TiltSquare")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.TiltSquare)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 10)
        self.gridLayout_9.setHorizontalSpacing(10)
        self.gridLayout_9.setVerticalSpacing(0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.tiltSquare = ImageBar(self.TiltSquare)
        self.tiltSquare.setObjectName("tiltSquare")
        self.gridLayout_9.addWidget(self.tiltSquare, 0, 0, 1, 1)
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setContentsMargins(20, -1, -1, -1)
        self.gridLayout_13.setHorizontalSpacing(10)
        self.gridLayout_13.setVerticalSpacing(0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_18 = QtWidgets.QLabel(self.TiltSquare)
        self.label_18.setMinimumSize(QtCore.QSize(0, 0))
        self.label_18.setObjectName("label_18")
        self.gridLayout_13.addWidget(self.label_18, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.TiltSquare)
        self.label_5.setObjectName("label_5")
        self.gridLayout_13.addWidget(self.label_5, 1, 3, 1, 1)
        self.textSquareTiltOffAxis = QtWidgets.QLineEdit(self.TiltSquare)
        self.textSquareTiltOffAxis.setMinimumSize(QtCore.QSize(140, 0))
        self.textSquareTiltOffAxis.setObjectName("textSquareTiltOffAxis")
        self.gridLayout_13.addWidget(self.textSquareTiltOffAxis, 1, 1, 1, 1)
        self.textSquareTiltHFR = QtWidgets.QLineEdit(self.TiltSquare)
        self.textSquareTiltHFR.setMinimumSize(QtCore.QSize(140, 0))
        self.textSquareTiltHFR.setObjectName("textSquareTiltHFR")
        self.gridLayout_13.addWidget(self.textSquareTiltHFR, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem3, 0, 7, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.TiltSquare)
        self.label_16.setMinimumSize(QtCore.QSize(0, 0))
        self.label_16.setObjectName("label_16")
        self.gridLayout_13.addWidget(self.label_16, 0, 0, 1, 1)
        self.squareNumberStars = QtWidgets.QLineEdit(self.TiltSquare)
        self.squareNumberStars.setMinimumSize(QtCore.QSize(0, 0))
        self.squareNumberStars.setMaximumSize(QtCore.QSize(60, 16777215))
        self.squareNumberStars.setObjectName("squareNumberStars")
        self.gridLayout_13.addWidget(self.squareNumberStars, 1, 4, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.TiltSquare)
        self.label_23.setObjectName("label_23")
        self.gridLayout_13.addWidget(self.label_23, 0, 3, 1, 1)
        self.squareMedianHFR = QtWidgets.QLineEdit(self.TiltSquare)
        self.squareMedianHFR.setMaximumSize(QtCore.QSize(60, 16777215))
        self.squareMedianHFR.setObjectName("squareMedianHFR")
        self.gridLayout_13.addWidget(self.squareMedianHFR, 0, 4, 1, 1)
        self.gridLayout_13.setColumnStretch(7, 1)
        self.gridLayout_9.addLayout(self.gridLayout_13, 1, 0, 1, 1)
        self.gridLayout_9.setRowStretch(0, 1)
        self.tabImage.addTab(self.TiltSquare, "")
        self.TiltTriangle = QtWidgets.QWidget()
        self.TiltTriangle.setObjectName("TiltTriangle")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.TiltTriangle)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 10)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.tiltTriangle = ImageBar(self.TiltTriangle)
        self.tiltTriangle.setObjectName("tiltTriangle")
        self.gridLayout_17.addWidget(self.tiltTriangle, 0, 0, 1, 1)
        self.gridLayout_18 = QtWidgets.QGridLayout()
        self.gridLayout_18.setContentsMargins(20, -1, -1, 0)
        self.gridLayout_18.setHorizontalSpacing(10)
        self.gridLayout_18.setVerticalSpacing(0)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.label_14 = QtWidgets.QLabel(self.TiltTriangle)
        self.label_14.setObjectName("label_14")
        self.gridLayout_18.addWidget(self.label_14, 1, 2, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.TiltTriangle)
        self.label_21.setMinimumSize(QtCore.QSize(0, 0))
        self.label_21.setObjectName("label_21")
        self.gridLayout_18.addWidget(self.label_21, 0, 0, 1, 1)
        self.triangleNumberStars = QtWidgets.QLineEdit(self.TiltTriangle)
        self.triangleNumberStars.setMinimumSize(QtCore.QSize(0, 0))
        self.triangleNumberStars.setMaximumSize(QtCore.QSize(60, 16777215))
        self.triangleNumberStars.setObjectName("triangleNumberStars")
        self.gridLayout_18.addWidget(self.triangleNumberStars, 1, 3, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.TiltTriangle)
        self.label_22.setMinimumSize(QtCore.QSize(0, 0))
        self.label_22.setObjectName("label_22")
        self.gridLayout_18.addWidget(self.label_22, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_18.addItem(spacerItem4, 0, 6, 1, 1)
        self.offsetTiltAngle = QtWidgets.QDoubleSpinBox(self.TiltTriangle)
        self.offsetTiltAngle.setMaximumSize(QtCore.QSize(60, 16777215))
        self.offsetTiltAngle.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.offsetTiltAngle.setDecimals(0)
        self.offsetTiltAngle.setMaximum(120.0)
        self.offsetTiltAngle.setSingleStep(10.0)
        self.offsetTiltAngle.setObjectName("offsetTiltAngle")
        self.gridLayout_18.addWidget(self.offsetTiltAngle, 0, 5, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.TiltTriangle)
        self.label_20.setMinimumSize(QtCore.QSize(0, 0))
        self.label_20.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_20.setObjectName("label_20")
        self.gridLayout_18.addWidget(self.label_20, 0, 4, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.TiltTriangle)
        self.label_24.setObjectName("label_24")
        self.gridLayout_18.addWidget(self.label_24, 0, 2, 1, 1)
        self.triangleMedianHFR = QtWidgets.QLineEdit(self.TiltTriangle)
        self.triangleMedianHFR.setMaximumSize(QtCore.QSize(60, 16777215))
        self.triangleMedianHFR.setObjectName("triangleMedianHFR")
        self.gridLayout_18.addWidget(self.triangleMedianHFR, 0, 3, 1, 1)
        self.textTriangleTiltOffAxis = QtWidgets.QLineEdit(self.TiltTriangle)
        self.textTriangleTiltOffAxis.setMinimumSize(QtCore.QSize(140, 0))
        self.textTriangleTiltOffAxis.setObjectName("textTriangleTiltOffAxis")
        self.gridLayout_18.addWidget(self.textTriangleTiltOffAxis, 1, 1, 1, 1)
        self.textTriangleTiltHFR = QtWidgets.QLineEdit(self.TiltTriangle)
        self.textTriangleTiltHFR.setMinimumSize(QtCore.QSize(140, 0))
        self.textTriangleTiltHFR.setObjectName("textTriangleTiltHFR")
        self.gridLayout_18.addWidget(self.textTriangleTiltHFR, 0, 1, 1, 1)
        self.gridLayout_18.setColumnStretch(6, 1)
        self.gridLayout_17.addLayout(self.gridLayout_18, 1, 0, 1, 1)
        self.gridLayout_17.setRowStretch(0, 1)
        self.tabImage.addTab(self.TiltTriangle, "")
        self.Roundness = QtWidgets.QWidget()
        self.Roundness.setObjectName("Roundness")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.Roundness)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 10)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.roundness = ImageBar(self.Roundness)
        self.roundness.setObjectName("roundness")
        self.gridLayout_8.addWidget(self.roundness, 0, 0, 1, 1)
        self.gridLayout_16 = QtWidgets.QGridLayout()
        self.gridLayout_16.setContentsMargins(20, -1, -1, 0)
        self.gridLayout_16.setHorizontalSpacing(10)
        self.gridLayout_16.setVerticalSpacing(0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem5, 0, 2, 1, 1)
        self.aspectRatioPercentile = QtWidgets.QLineEdit(self.Roundness)
        self.aspectRatioPercentile.setMaximumSize(QtCore.QSize(30, 16777215))
        self.aspectRatioPercentile.setObjectName("aspectRatioPercentile")
        self.gridLayout_16.addWidget(self.aspectRatioPercentile, 0, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.Roundness)
        self.label_15.setObjectName("label_15")
        self.gridLayout_16.addWidget(self.label_15, 0, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_16, 1, 0, 1, 1)
        self.gridLayout_8.setRowStretch(0, 1)
        self.tabImage.addTab(self.Roundness, "")
        self.Aberration = QtWidgets.QWidget()
        self.Aberration.setObjectName("Aberration")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.Aberration)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.aberration = ImageBar(self.Aberration)
        self.aberration.setObjectName("aberration")
        self.gridLayout_12.addWidget(self.aberration, 0, 0, 1, 1)
        self.tabImage.addTab(self.Aberration, "")
        self.Sources = QtWidgets.QWidget()
        self.Sources.setObjectName("Sources")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.Sources)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.imageSource = ImageBar(self.Sources)
        self.imageSource.setObjectName("imageSource")
        self.gridLayout_10.addWidget(self.imageSource, 0, 0, 1, 1)
        self.tabImage.addTab(self.Sources, "")
        self.Back = QtWidgets.QWidget()
        self.Back.setObjectName("Back")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.Back)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.background = ImageBar(self.Back)
        self.background.setObjectName("background")
        self.gridLayout_6.addWidget(self.background, 0, 0, 1, 1)
        self.tabImage.addTab(self.Back, "")
        self.BackRMS = QtWidgets.QWidget()
        self.BackRMS.setObjectName("BackRMS")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.BackRMS)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.backgroundRMS = ImageBar(self.BackRMS)
        self.backgroundRMS.setObjectName("backgroundRMS")
        self.gridLayout_7.addWidget(self.backgroundRMS, 0, 0, 1, 1)
        self.tabImage.addTab(self.BackRMS, "")
        self.gridLayout_2.addWidget(self.tabImage, 1, 2, 3, 1)
        self.headerGroup = QtWidgets.QGroupBox(ImageDialog)
        self.headerGroup.setMinimumSize(QtCore.QSize(120, 0))
        self.headerGroup.setMaximumSize(QtCore.QSize(0, 16777215))
        self.headerGroup.setProperty("large", True)
        self.headerGroup.setObjectName("headerGroup")
        self.gridLayout = QtWidgets.QGridLayout(self.headerGroup)
        self.gridLayout.setContentsMargins(4, 15, 4, 4)
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.binX = QtWidgets.QLineEdit(self.headerGroup)
        self.binX.setEnabled(True)
        self.binX.setReadOnly(True)
        self.binX.setObjectName("binX")
        self.gridLayout.addWidget(self.binX, 26, 0, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.headerGroup)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setObjectName("line_7")
        self.gridLayout.addWidget(self.line_7, 16, 0, 1, 2)
        self.line_11 = QtWidgets.QFrame(self.headerGroup)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setObjectName("line_11")
        self.gridLayout.addWidget(self.line_11, 27, 0, 1, 2)
        self.scale = QtWidgets.QLineEdit(self.headerGroup)
        self.scale.setEnabled(True)
        self.scale.setReadOnly(True)
        self.scale.setObjectName("scale")
        self.gridLayout.addWidget(self.scale, 15, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.headerGroup)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 2, 0, 1, 2)
        self.line_6 = QtWidgets.QFrame(self.headerGroup)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 10, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.headerGroup)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 2)
        self.sqm = QtWidgets.QLineEdit(self.headerGroup)
        self.sqm.setEnabled(True)
        self.sqm.setReadOnly(True)
        self.sqm.setObjectName("sqm")
        self.gridLayout.addWidget(self.sqm, 32, 0, 1, 2)
        self.rotation = QtWidgets.QLineEdit(self.headerGroup)
        self.rotation.setEnabled(True)
        self.rotation.setReadOnly(True)
        self.rotation.setObjectName("rotation")
        self.gridLayout.addWidget(self.rotation, 15, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.headerGroup)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 13, 0, 1, 1)
        self.ccdTemp = QtWidgets.QLineEdit(self.headerGroup)
        self.ccdTemp.setEnabled(True)
        self.ccdTemp.setReadOnly(True)
        self.ccdTemp.setObjectName("ccdTemp")
        self.gridLayout.addWidget(self.ccdTemp, 23, 1, 1, 1)
        self.dec = QtWidgets.QLineEdit(self.headerGroup)
        self.dec.setEnabled(True)
        self.dec.setReadOnly(True)
        self.dec.setObjectName("dec")
        self.gridLayout.addWidget(self.dec, 8, 0, 1, 2)
        self.expTime = QtWidgets.QLineEdit(self.headerGroup)
        self.expTime.setEnabled(True)
        self.expTime.setReadOnly(True)
        self.expTime.setObjectName("expTime")
        self.gridLayout.addWidget(self.expTime, 20, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.headerGroup)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.object = QtWidgets.QLineEdit(self.headerGroup)
        self.object.setEnabled(True)
        self.object.setReadOnly(True)
        self.object.setObjectName("object")
        self.gridLayout.addWidget(self.object, 1, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.headerGroup)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 2)
        self.binY = QtWidgets.QLineEdit(self.headerGroup)
        self.binY.setEnabled(True)
        self.binY.setReadOnly(True)
        self.binY.setObjectName("binY")
        self.gridLayout.addWidget(self.binY, 26, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.headerGroup)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 31, 0, 1, 2)
        self.raFloat = QtWidgets.QLineEdit(self.headerGroup)
        self.raFloat.setEnabled(True)
        self.raFloat.setReadOnly(True)
        self.raFloat.setObjectName("raFloat")
        self.gridLayout.addWidget(self.raFloat, 5, 0, 1, 2)
        self.filter = QtWidgets.QLineEdit(self.headerGroup)
        self.filter.setEnabled(True)
        self.filter.setReadOnly(True)
        self.filter.setObjectName("filter")
        self.gridLayout.addWidget(self.filter, 23, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.headerGroup)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 19, 0, 1, 2)
        self.line_5 = QtWidgets.QFrame(self.headerGroup)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 6, 0, 1, 2)
        self.line_9 = QtWidgets.QFrame(self.headerGroup)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setObjectName("line_9")
        self.gridLayout.addWidget(self.line_9, 21, 0, 1, 2)
        self.label_12 = QtWidgets.QLabel(self.headerGroup)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 25, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.headerGroup)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 13, 1, 1, 1)
        self.line_10 = QtWidgets.QFrame(self.headerGroup)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setObjectName("line_10")
        self.gridLayout.addWidget(self.line_10, 24, 0, 1, 2)
        self.ra = QtWidgets.QLineEdit(self.headerGroup)
        self.ra.setEnabled(True)
        self.ra.setReadOnly(True)
        self.ra.setObjectName("ra")
        self.gridLayout.addWidget(self.ra, 4, 0, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.headerGroup)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 25, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.headerGroup)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 22, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.headerGroup)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 22, 0, 1, 1)
        self.decFloat = QtWidgets.QLineEdit(self.headerGroup)
        self.decFloat.setEnabled(True)
        self.decFloat.setReadOnly(True)
        self.decFloat.setObjectName("decFloat")
        self.gridLayout.addWidget(self.decFloat, 9, 0, 1, 2)
        self.gridLayout_2.addWidget(self.headerGroup, 1, 0, 2, 1)
        self.groupMouseCoord = QtWidgets.QGroupBox(ImageDialog)
        self.groupMouseCoord.setMinimumSize(QtCore.QSize(120, 0))
        self.groupMouseCoord.setMaximumSize(QtCore.QSize(120, 16777215))
        self.groupMouseCoord.setProperty("large", True)
        self.groupMouseCoord.setObjectName("groupMouseCoord")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.groupMouseCoord)
        self.gridLayout_14.setContentsMargins(4, 15, 4, 4)
        self.gridLayout_14.setHorizontalSpacing(4)
        self.gridLayout_14.setVerticalSpacing(0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.label_25 = QtWidgets.QLabel(self.groupMouseCoord)
        self.label_25.setObjectName("label_25")
        self.gridLayout_14.addWidget(self.label_25, 0, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.groupMouseCoord)
        self.label_26.setObjectName("label_26")
        self.gridLayout_14.addWidget(self.label_26, 4, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_14.addItem(spacerItem6, 7, 0, 1, 1)
        self.decMouse = QtWidgets.QLineEdit(self.groupMouseCoord)
        self.decMouse.setEnabled(True)
        self.decMouse.setReadOnly(True)
        self.decMouse.setObjectName("decMouse")
        self.gridLayout_14.addWidget(self.decMouse, 5, 0, 1, 1)
        self.decMouseFloat = QtWidgets.QLineEdit(self.groupMouseCoord)
        self.decMouseFloat.setEnabled(True)
        self.decMouseFloat.setReadOnly(True)
        self.decMouseFloat.setObjectName("decMouseFloat")
        self.gridLayout_14.addWidget(self.decMouseFloat, 6, 0, 1, 1)
        self.raMouse = QtWidgets.QLineEdit(self.groupMouseCoord)
        self.raMouse.setEnabled(True)
        self.raMouse.setReadOnly(True)
        self.raMouse.setObjectName("raMouse")
        self.gridLayout_14.addWidget(self.raMouse, 1, 0, 1, 1)
        self.raMouseFloat = QtWidgets.QLineEdit(self.groupMouseCoord)
        self.raMouseFloat.setEnabled(True)
        self.raMouseFloat.setReadOnly(True)
        self.raMouseFloat.setObjectName("raMouseFloat")
        self.gridLayout_14.addWidget(self.raMouseFloat, 2, 0, 1, 1)
        self.line_12 = QtWidgets.QFrame(self.groupMouseCoord)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setObjectName("line_12")
        self.gridLayout_14.addWidget(self.line_12, 3, 0, 1, 1)
        self.gridLayout_14.setRowStretch(4, 1)
        self.gridLayout_2.addWidget(self.groupMouseCoord, 3, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout_2.setStretch(2, 1)

        self.retranslateUi(ImageDialog)
        self.tabImage.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ImageDialog)

    def retranslateUi(self, ImageDialog):
        _translate = QtCore.QCoreApplication.translate
        ImageDialog.setWindowTitle(_translate("ImageDialog", "Imaging"))
        self.groupImageActions.setTitle(_translate("ImageDialog", "Image actions"))
        self.solve.setText(_translate("ImageDialog", "Solve"))
        self.exposeN.setText(_translate("ImageDialog", "Expose N"))
        self.expose.setText(_translate("ImageDialog", "Expose 1"))
        self.load.setText(_translate("ImageDialog", "Load"))
        self.abortExpose.setText(_translate("ImageDialog", "Exp. Abort"))
        self.abortSolve.setText(_translate("ImageDialog", "Solve Abort"))
        self.embedData.setText(_translate("ImageDialog", "Embed WCS"))
        self.autoSolve.setText(_translate("ImageDialog", "Auto Solve"))
        self.timeTagImage.setToolTip(_translate("ImageDialog", "<html><head/><body><p>If checked, the filename of the image is extended with the actual time to make it unique. Otherwise the file get just &quot;exposure&quot; and will be overwritten.</p></body></html>"))
        self.timeTagImage.setText(_translate("ImageDialog", "Add time tags"))
        self.slewCenter.setText(_translate("ImageDialog", "Slew Center"))
        self.groupBox.setTitle(_translate("ImageDialog", "Image View"))
        self.aspectLocked.setText(_translate("ImageDialog", "Lock aspect"))
        self.showCrosshair.setToolTip(_translate("ImageDialog", "<html><head/><body><p>Showing a red cross hair in the center of the image.</p></body></html>"))
        self.showCrosshair.setText(_translate("ImageDialog", "Crosshair  "))
        self.flipH.setText(_translate("ImageDialog", "Flip H"))
        self.flipV.setText(_translate("ImageDialog", "Flip V"))
        self.color.setItemText(0, _translate("ImageDialog", "Grey"))
        self.color.setItemText(1, _translate("ImageDialog", "Rainbow"))
        self.color.setItemText(2, _translate("ImageDialog", "Cividis"))
        self.color.setItemText(3, _translate("ImageDialog", "Magma"))
        self.color.setItemText(4, _translate("ImageDialog", "Extreme"))
        self.photometryGroup.setTitle(_translate("ImageDialog", "Photometry"))
        self.snTarget.setItemText(0, _translate("ImageDialog", "Star norm"))
        self.snTarget.setItemText(1, _translate("ImageDialog", "Star plus"))
        self.snTarget.setItemText(2, _translate("ImageDialog", "Star extended"))
        self.snTarget.setItemText(3, _translate("ImageDialog", "Star max"))
        self.snTarget.setItemText(4, _translate("ImageDialog", "Star extreme"))
        self.isoLayer.setText(_translate("ImageDialog", "2D contour"))
        self.showValues.setText(_translate("ImageDialog", "Show values"))
        self.tabImage.setTabText(self.tabImage.indexOf(self.Image), _translate("ImageDialog", "Image"))
        self.label_13.setText(_translate("ImageDialog", "Number of stars"))
        self.label_17.setText(_translate("ImageDialog", "10% Percentile [HFR]"))
        self.label_19.setText(_translate("ImageDialog", "Median [HFR]"))
        self.tabImage.setTabText(self.tabImage.indexOf(self.HFR), _translate("ImageDialog", "HFR"))
        self.label_18.setText(_translate("ImageDialog", "Off-Axis aberration [HFR]"))
        self.label_5.setText(_translate("ImageDialog", "Number stars"))
        self.label_16.setText(_translate("ImageDialog", "Tilt square [HFR]"))
        self.label_23.setText(_translate("ImageDialog", "Median HFR"))
        self.tabImage.setTabText(self.tabImage.indexOf(self.TiltSquare), _translate("ImageDialog", "Tilt Square"))
        self.label_14.setText(_translate("ImageDialog", "Number stars"))
        self.label_21.setText(_translate("ImageDialog", "Tilt triangle [HFR]"))
        self.label_22.setText(_translate("ImageDialog", "Off-Axis aberration [HFR]"))
        self.label_20.setText(_translate("ImageDialog", "Offset tilt angle"))
        self.label_24.setText(_translate("ImageDialog", "Median HFR"))
        self.tabImage.setTabText(self.tabImage.indexOf(self.TiltTriangle), _translate("ImageDialog", "Tilt Triangle"))
        self.label_15.setText(_translate("ImageDialog", "10% Percentile [aspect ratio]"))
        self.tabImage.setTabText(self.tabImage.indexOf(self.Roundness), _translate("ImageDialog", "Roundness"))
        self.tabImage.setTabText(self.tabImage.indexOf(self.Aberration), _translate("ImageDialog", "Aberration Inspect"))
        self.tabImage.setTabText(self.tabImage.indexOf(self.Sources), _translate("ImageDialog", "Image + Source"))
        self.tabImage.setTabText(self.tabImage.indexOf(self.Back), _translate("ImageDialog", "Back"))
        self.tabImage.setTabText(self.tabImage.indexOf(self.BackRMS), _translate("ImageDialog", "Back RMS"))
        self.headerGroup.setTitle(_translate("ImageDialog", "Fits Header"))
        self.label_3.setText(_translate("ImageDialog", "DEC [deg]"))
        self.label_6.setText(_translate("ImageDialog", "Rot [deg]"))
        self.label.setText(_translate("ImageDialog", "Object Name"))
        self.label_2.setText(_translate("ImageDialog", "RA [hours]"))
        self.label_4.setText(_translate("ImageDialog", "SQM [mpas]"))
        self.label_8.setText(_translate("ImageDialog", "Exposure Time [s]"))
        self.label_12.setText(_translate("ImageDialog", "Bin Y"))
        self.label_7.setText(_translate("ImageDialog", "Scale"))
        self.label_11.setText(_translate("ImageDialog", "Bin X"))
        self.label_9.setText(_translate("ImageDialog", "Temp"))
        self.label_10.setText(_translate("ImageDialog", "Filter"))
        self.groupMouseCoord.setTitle(_translate("ImageDialog", "Mouse Coords"))
        self.label_25.setText(_translate("ImageDialog", "RA [hours]"))
        self.label_26.setText(_translate("ImageDialog", "DEC [deg]"))
from gui.utilities.tools4pyqtgraph import ImageBar


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ImageDialog = QtWidgets.QWidget()
    ui = Ui_ImageDialog()
    ui.setupUi(ImageDialog)
    ImageDialog.show()
    sys.exit(app.exec_())
