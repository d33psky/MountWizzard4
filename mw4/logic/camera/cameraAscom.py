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
# written in python3, (c) 2019-2021 by mworion
#
# Licence APL2.0
#
###########################################################
# standard libraries

# external packages
from astropy.io import fits
from PyQt5.QtTest import QTest
from comtypes.safearray import safearray_as_ndarray

# local imports
from base.ascomClass import AscomClass
from base.tpool import Worker
from base.transform import JNowToJ2000


class CameraAscom(AscomClass):
    """
    the class CameraAscom inherits all information and handling of the Ascom device.
    """

    __all__ = ['CameraAscom',
               ]

    CYCLE_POLL_DATA = 1000

    def __init__(self, app=None, signals=None, data=None):
        super().__init__(app=app, data=data, threadPool=app.threadPool)

        self.signals = signals
        self.data = data
        self.abortExpose = False

    def getInitialConfig(self):
        """
        :return: true for test purpose
        """
        super().getInitialConfig()

        if not self.deviceConnected:
            return False

        self.getAndStoreAscomProperty('CameraXSize', 'CCD_INFO.CCD_MAX_X')
        self.getAndStoreAscomProperty('CameraYSize', 'CCD_INFO.CCD_MAX_Y')
        self.getAndStoreAscomProperty('CanFastReadout', 'CAN_FAST')
        self.getAndStoreAscomProperty('CanAbortExposure', 'CAN_ABORT')
        self.getAndStoreAscomProperty('CanSetCCDTemperature', 'CAN_SET_CCD_TEMPERATURE')
        self.getAndStoreAscomProperty('CanGetCoolerPower', 'CAN_GET_COOLER_POWER')
        self.getAndStoreAscomProperty('PixelSizeX', 'CCD_INFO.CCD_PIXEL_SIZE_X')
        self.getAndStoreAscomProperty('PixelSizeY', 'CCD_INFO.CCD_PIXEL_SIZE_Y')
        self.getAndStoreAscomProperty('MaxBinX', 'CCD_BINNING.HOR_BIN_MAX')
        self.getAndStoreAscomProperty('MaxBinY', 'CCD_BINNING.VERT_BIN_MAX')
        self.getAndStoreAscomProperty('GainMax', 'CCD_INFO.GAIN_MAX')
        self.getAndStoreAscomProperty('GainMin', 'CCD_INFO.GAIN_MIN')
        self.getAndStoreAscomProperty('StartX', 'CCD_FRAME.X')
        self.getAndStoreAscomProperty('StartY', 'CCD_FRAME.Y')
        self.log.debug(f'Initial data: {self.data}')

        return True

    def workerPollData(self):
        """
        :return: true for test purpose
        """
        if not self.deviceConnected:
            return False

        self.getAndStoreAscomProperty('BinX', 'CCD_BINNING.HOR_BIN')
        self.getAndStoreAscomProperty('BinY', 'CCD_BINNING.VERT_BIN')
        self.getAndStoreAscomProperty('CameraState', 'CAMERA.STATE')
        self.getAndStoreAscomProperty('Gain', 'CCD_GAIN.GAIN')
        self.getAndStoreAscomProperty('Offset', 'CCD_OFFSET.OFFSET')
        self.getAndStoreAscomProperty('FastReadout',
                                      'READOUT_QUALITY.QUALITY_LOW',
                                      'READOUT_QUALITY.QUALITY_HIGH')
        self.getAndStoreAscomProperty('CCDTemperature',
                                      'CCD_TEMPERATURE.CCD_TEMPERATURE_VALUE')
        self.getAndStoreAscomProperty('CoolerOn', 'CCD_COOLER.COOLER_ON')
        self.getAndStoreAscomProperty('CoolerPower',
                                      'CCD_COOLER_POWER.CCD_COOLER_VALUE')
        return True

    def sendDownloadMode(self, fastReadout=False):
        """
        setDownloadMode sets the readout speed of the camera
        :return: success
        """
        canFast = self.data.get('CAN_FAST', False)

        if not canFast:
            return False
        if not self.deviceConnected:
            return False
        if fastReadout:
            self.setAscomProperty('FastReadout', True)

        isQualityHigh = self.data.get('READOUT_QUALITY.QUALITY_HIGH', True)
        qualityText = 'High' if isQualityHigh else 'Low'
        self.log.debug(f'camera has readout quality entry: {qualityText}')
        return True

    def workerExpose(self,
                     imagePath='',
                     expTime=3,
                     binning=1,
                     fastReadout=True,
                     posX=0,
                     posY=0,
                     width=1,
                     height=1,
                     focalLength=1,
                     ):
        """
        :param imagePath:
        :param expTime:
        :param binning:
        :param fastReadout:
        :param posX:
        :param posY:
        :param width:
        :param height:
        :param focalLength:
        :return: success
        """
        if not self.deviceConnected:
            return False

        self.sendDownloadMode(fastReadout=fastReadout)
        self.setAscomProperty('BinX', int(binning))
        self.setAscomProperty('BinY', int(binning))
        self.setAscomProperty('StartX', int(posX / binning))
        self.setAscomProperty('StartY', int(posY / binning))
        self.setAscomProperty('NumX', int(width / binning))
        self.setAscomProperty('NumY', int(height / binning))

        isMount = self.app.deviceStat['mount']
        if isMount:
            ra = self.app.mount.obsSite.raJNow
            dec = self.app.mount.obsSite.decJNow
            obsTime = self.app.mount.obsSite.timeJD
            if ra is not None and dec is not None and obsTime is not None:
                ra, dec = JNowToJ2000(ra, dec, obsTime)

        self.client.StartExposure(expTime, True)

        timeLeft = expTime
        while not self.getAscomProperty('ImageReady'):
            text = f'expose {timeLeft:3.0f} s'
            QTest.qWait(100)
            if timeLeft >= 0.1:
                timeLeft -= 0.1

            else:
                timeLeft = 0

            self.signals.message.emit(text)
            if self.abortExpose:
                break

        self.signals.integrated.emit()
        self.signals.message.emit('download')
        with safearray_as_ndarray:
            data = self.client.ImageArray

        if not self.abortExpose:
            self.signals.message.emit('saving')
            hdu = fits.PrimaryHDU(data=data)
            header = hdu.header
            header['OBJECT'] = 'skymodel'
            header['FRAME'] = 'Light'
            header['EQUINOX'] = 2000
            header['PIXSIZE1'] = self.data['CCD_INFO.CCD_PIXEL_SIZE_X'] * binning
            header['PIXSIZE2'] = self.data['CCD_INFO.CCD_PIXEL_SIZE_Y'] * binning
            header['XPIXSZ'] = self.data['CCD_INFO.CCD_PIXEL_SIZE_X'] * binning
            header['YPIXSZ'] = self.data['CCD_INFO.CCD_PIXEL_SIZE_Y'] * binning

            factor = binning / focalLength * 206.265
            header['SCALE'] = self.data['CCD_INFO.CCD_PIXEL_SIZE_X'] * factor
            header['XBINNING'] = binning
            header['YBINNING'] = binning
            header['EXPTIME'] = expTime
            header['OBSERVER'] = 'MW4'
            header['DATE-OBS'] = self.app.mount.obsSite.timeJD.utc_iso()
            header['CCD-TEMP'] = self.data.get('CCD_TEMPERATURE.CCD_TEMPERATURE_VALUE', 0)
            header['SQM'] = self.app.skymeter.data.get('SKY_QUALITY.SKY_BRIGHTNESS', 0)

            if isMount:
                header['RA'] = ra._degrees
                header['DEC'] = dec.degrees
                header['TELESCOP'] = self.app.mount.firmware.product

            hdu.writeto(imagePath, overwrite=True)
            self.log.info(f'Saved Image: [{imagePath}]')

        if self.abortExpose:
            imagePath = ''

        self.signals.saved.emit(imagePath)
        self.signals.message.emit('')

        return True

    def expose(self,
               imagePath='',
               expTime=3,
               binning=1,
               fastReadout=True,
               posX=0,
               posY=0,
               width=1,
               height=1,
               focalLength=1,
               ):
        """
        :return: success
        """
        if not self.deviceConnected:
            return False

        self.abortExpose = False
        worker = Worker(self.workerExpose,
                        imagePath=imagePath,
                        expTime=expTime,
                        binning=binning,
                        fastReadout=fastReadout,
                        posX=posX,
                        posY=posY,
                        width=width,
                        height=height,
                        focalLength=focalLength)

        self.threadPool.start(worker)
        return True

    def abort(self):
        """
        :return: success
        """
        if not self.deviceConnected:
            return False

        self.abortExpose = True
        canAbort = self.data.get('CAN_ABORT', False)
        if not canAbort:
            return False

        self.client.StopExposure()

        return True

    def sendCoolerSwitch(self, coolerOn=False):
        """
        :param coolerOn:
        :return: success
        """
        if not self.deviceConnected:
            return False

        self.setAscomProperty('CoolerOn', coolerOn)
        return True

    def sendCoolerTemp(self, temperature=0):
        """
        :param temperature:
        :return: success
        """
        if not self.deviceConnected:
            return False

        canSetCCDTemp = self.data.get('CAN_SET_CCD_TEMPERATURE', False)
        if not canSetCCDTemp:
            return False

        self.setAscomProperty('SetCCDTemperature', temperature)
        return True

    def sendOffset(self, offset=0):
        """
        :param offset:
        :return: success
        """
        if not self.deviceConnected:
            return False

        self.setAscomProperty('Offset', offset)
        return True

    def sendGain(self, gain=0):
        """
        :param gain:
        :return: success
        """
        if not self.deviceConnected:
            return False

        self.setAscomProperty('Gain', gain)
        return True