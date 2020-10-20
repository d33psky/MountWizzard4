############################################################
# -*- coding: utf-8 -*-
#
#       #   #  #   #   #    #
#      ##  ##  #  ##  #    #
#     # # # #  # # # #    #  #
#    #  ##  #  ##  ##    ######
#   #   #   #  #   #       #
#
# Python-based Tool for interaction with the 10micron mounts
# GUI with PyQT5 for python
#
# written in python 3, (c) 2019, 2020 by mworion
#
# Licence APL2.0
#
###########################################################
# standard libraries

# external packages
import wakeonlan

# local import


class SettMount(object):
    """
    the main window class handles the main menu as well as the show and no show part of
    any other window. all necessary processing for functions of that gui will be linked
    to this class. SettMount is a mixin feature for this class
    """

    def __init__(self, app=None, ui=None, clickable=None):
        if app:
            self.app = app
            self.ui = ui
            self.clickable = clickable

        self.ui.mountOn.clicked.connect(self.mountBoot)
        self.ui.mountOff.clicked.connect(self.mountShutdown)
        self.ui.mountHost.editingFinished.connect(self.mountHost)
        self.ui.mountMAC.editingFinished.connect(self.mountMAC)
        self.ui.bootRackComp.clicked.connect(self.bootRackComp)
        self.app.mount.signals.settingDone.connect(self.setMountMAC)
        self.app.mount.signals.firmwareDone.connect(self.updateFwGui)
        self.ui.settleTimeMount.valueChanged.connect(self.setMountSettlingTime)

    def initConfig(self):
        """

        :return:
        """

        config = self.app.config['mainW']
        self.ui.mountHost.setText(config.get('mountHost', ''))
        self.mountHost()
        self.ui.mountMAC.setText(config.get('mountMAC', ''))
        self.mountMAC()
        self.ui.rackCompMAC.setText(config.get('rackCompMAC', ''))
        self.ui.settleTimeMount.setValue(config.get('settleTimeMount', 0))

        return True

    def storeConfig(self):
        """

        :return:
        """

        config = self.app.config['mainW']
        config['mountHost'] = self.ui.mountHost.text()
        config['mountMAC'] = self.ui.mountMAC.text()
        config['rackCompMAC'] = self.ui.rackCompMAC.text()
        config['settleTimeMount'] = self.ui.settleTimeMount.value()

        return True

    def mountBoot(self):
        if self.app.mount.bootMount():
            self.app.message.emit('Sent boot command to mount', 0)
            return True

        else:
            self.app.message.emit('Mount cannot be booted', 2)
            return False

    def mountShutdown(self):
        if self.app.mount.shutdown():
            self.app.message.emit('Shutting mount down', 0)
            return True

        else:
            self.app.message.emit('Mount cannot be shutdown', 2)
            return False

    def checkFormatMAC(self, value):
        """
        checkFormatMAC makes some checks to ensure that the format of the string is ok for
        WOL package.

        :param      value: string with mac address
        :return:    checked string in upper cases
        """

        if not value:
            self.log.warning('wrong MAC value: {0}'.format(value))
            return None

        if not isinstance(value, str):
            self.log.warning('wrong MAC value: {0}'.format(value))
            return None

        value = value.upper()
        value = value.replace('.', ':')
        value = value.split(':')
        if len(value) != 6:
            self.log.warning('wrong MAC value: {0}'.format(value))
            return None

        for chunk in value:
            if len(chunk) != 2:
                self.log.warning('wrong MAC value: {0}'.format(value))
                return None

            for char in chunk:
                if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                                'A', 'B', 'C', 'D', 'E', 'F']:
                    self.log.warning('wrong MAC value: {0}'.format(value))
                    return None

        # now we build the right format
        value = '{0:2s}:{1:2s}:{2:2s}:{3:2s}:{4:2s}:{5:2s}'.format(*value)
        return value

    def bootRackComp(self):
        """

        :return:
        """

        MAC = self.ui.rackCompMAC.text()
        MAC = self.checkFormatMAC(MAC)
        if MAC is not None:
            wakeonlan.send_magic_packet(MAC)
            self.app.message.emit('Sent boot command to rack computer', 0)
            return True
        else:
            self.app.message.emit('Rack computer cannot be booted', 2)
            return False

    def mountHost(self):
        """

        :return: true for test purpose
        """
        self.app.mount.host = self.ui.mountHost.text()
        return True

    def mountMAC(self):
        """

        :return: true for test purpose
        """
        self.app.mount.MAC = self.ui.mountMAC.text()
        return True

    def setMountMAC(self, sett=None):
        """

        :param sett:
        :return: true for test purpose
        """
        if sett is None:
            return False

        if sett.addressLanMAC is None:
            return False
        if not sett.addressLanMAC:
            return False
        self.app.mount.MAC = sett.addressLanMAC

        if self.app.mount.MAC is None:
            return False
        self.ui.mountMAC.setText(self.app.mount.MAC)

        return True

    def setMountSettlingTime(self):
        """

        :return: true for test purpose
        """

        self.app.mount.settlingTime = self.ui.settleTimeMount.value()

        return True

    def updateFwGui(self, fw):
        """
        updateFwGui write all firmware data to the gui.

        :return:    True if ok for testing
        """

        self.guiSetText(self.ui.product, 's', fw.product)
        self.guiSetText(self.ui.vString, 's', fw.vString)
        self.guiSetText(self.ui.fwdate, 's', fw.date)
        self.guiSetText(self.ui.fwtime, 's', fw.time)
        self.guiSetText(self.ui.hardware, 's', fw.hardware)

        return True
