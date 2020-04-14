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
# Python  v3.7.5
#
# Michael Würtenberger
# (c) 2019
#
# Licence APL2.0
#
###########################################################
# standard libraries
import time

# external packages
import numpy as np
from astropy.io import fits

# local imports
from mw4.base.alpacaClass import AlpacaClass
from mw4.base.alpacaBase import Camera
from mw4.base.tpool import Worker
from mw4.base.transform import JNowToJ2000


class CameraAlpaca(AlpacaClass):
    """
    the class Dome inherits all information and handling of the Dome device. there will be
    some parameters who will define the slewing position of the dome relating to the
    mount.dome = DomeAlpaca(app=None)
    """

    __all__ = ['CameraAlpaca',
               ]

    # specific timing for device
    CYCLE_DEVICE = 3000
    CYCLE_DATA = 1000

    def __init__(self, app=None, signals=None, data=None):
        super().__init__(app=app, data=data)

        # as we have in the base class only the base client there, we will get more
        # specialized with Dome (which is derived from the base class)
        self.client = Camera()
        self.signals = signals
        self.data = data
        self.imagePath = ''

        self.client.signals.deviceConnected.connect(self.getInitialConfig)

    def getInitialConfig(self):
        """

        :return: true for test purpose
        """

        self.dataEntry(self.client.cameraxsize(), 'CCD_INFO.CCD_MAX_X')
        self.dataEntry(self.client.cameraysize(), 'CCD_INFO.CCD_MAX_Y')
        self.dataEntry(self.client.canfastreadout(), 'CAN_FAST')
        # self.dataEntry(self.client.canstopexposure(), 'CAN_ABORT')
        self.dataEntry(self.client.pixelsizex(), 'CCD_INFO.CCD_PIXEL_SIZE_X')
        self.dataEntry(self.client.pixelsizey(), 'CCD_INFO.CCD_PIXEL_SIZE_Y')
        self.dataEntry(self.client.maxbinx(), 'CCD_BINNING.HOR_BIN_MAX')
        self.dataEntry(self.client.maxbiny(), 'CCD_BINNING.VERT_BIN_MAX')
        self.dataEntry(self.client.binx(), 'CCD_BINNING.HOR_BIN')
        self.dataEntry(self.client.biny(), 'CCD_BINNING.VERT_BIN')
        self.dataEntry(self.client.startx(), 'CCD_FRAME.X')
        self.dataEntry(self.client.starty(), 'CCD_FRAME.Y')

        return True

    def workerPollData(self):
        """

        :return: true for test purpose
        """

        self.dataEntry(self.client.camerastate(),
                       'CAMERA.STATE')
        self.dataEntry(self.client.ccdtemperature(),
                       'CCD_TEMPERATURE.CCD_TEMPERATURE_VALUE')
        self.dataEntry(self.client.fastreadout(),
                       'READOUT_QUALITY.QUALITY_LOW',
                       'READOUT_QUALITY.QUALITY_HIGH')
        return True

    def pollData(self):
        """

        :return: success
        """

        if not self.deviceConnected:
            return False

        worker = Worker(self.workerPollData)
        self.threadPool.start(worker)
        return True

    def sendDownloadMode(self, fastReadout=False):
        """
        setDownloadMode sets the readout speed of the camera

        :return: success
        """

        suc = self.data['CAN_FAST']
        if suc and fastReadout:
            self.client.fastreadout(FastReadout=True)
        quality = 'High' if self.data.get('READOUT_QUALITY.QUALITY_HIGH', True) else 'Low'
        self.log.info(f'camera has readout quality entry: {quality}')

        return suc

    def workerExpose(self,
                     imagePath='',
                     expTime=3,
                     binning=1,
                     fastReadout=True,
                     posX=0,
                     posY=0,
                     width=1,
                     height=1,
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
        :return: success
        """

        self.imagePath = imagePath
        binning = int(binning)
        posX = int(posX)
        posY = int(posY)
        width = int(width)
        height = int(height)

        suc = self.sendDownloadMode(fastReadout=fastReadout)
        if not suc:
            self.log.info('Camera has no download quality settings')

        # set binning
        self.client.binx(BinX=binning)
        self.client.biny(BinY=binning)

        # set frame sizes
        self.client.startx(StartX=posX)
        self.client.starty(StartY=posY)
        self.client.numx(NumX=width)
        self.client.numy(NumY=height)

        # start exposure
        self.client.startexposure(Duration=expTime, Light=True)

        # wait for finishing
        timeLeft = expTime
        while not self.client.imageready():
            text = f'expose {timeLeft:3.0f} s'
            time.sleep(1)
            if timeLeft >= 1:
                timeLeft -= 1
            else:
                timeLeft = 0
            self.signals.message.emit(text)
        self.signals.integrated.emit()

        # download image
        self.signals.message.emit('download')
        data = np.array(self.client.imagearray(), dtype=np.uint16)
        data = np.transpose(data)

        # creating a fits file and saving the image
        self.signals.message.emit('saving')
        hdu = fits.PrimaryHDU(data=data)
        header = hdu.header
        header['OBJECT'] = 'skymodel'
        header['FRAME'] = 'Light'
        header['EQUINOX'] = 2000
        header['PIXSIZE1'] = self.data['CCD_INFO.CCD_PIXEL_SIZE_X']
        header['PIXSIZE2'] = self.data['CCD_INFO.CCD_PIXEL_SIZE_Y']
        header['XPIXSZ'] = self.data['CCD_INFO.CCD_PIXEL_SIZE_X']
        header['YPIXSZ'] = self.data['CCD_INFO.CCD_PIXEL_SIZE_Y']
        # todo fl has to be changed and automatically set !
        header['SCALE'] = self.data['CCD_INFO.CCD_PIXEL_SIZE_X'] / 570 * 206.265
        header['XBINNING'] = binning
        header['YBINNING'] = binning
        header['EXPTIME'] = expTime
        header['OBSERVER'] = 'MW4'
        header['DATE-OBS'] = self.app.mount.obsSite.timeJD.utc_iso()

        if self.app.deviceStat['mount']:
            ra, dec = JNowToJ2000(self.app.mount.obsSite.raJNow,
                                  self.app.mount.obsSite.decJNow,
                                  self.app.mount.obsSite.timeJD)
            header['OBJCTRA'] = ra.hstr()
            dec = dec.dstr()
            dec = dec.replace('deg', '').replace("'", '').replace('"', '')
            header['OBJCTDEC'] = dec
            header['RA'] = ra.hours
            header['DEC'] = dec.degrees
            header['TELESCOP'] = self.app.mount.firmware.product

        hdu.writeto(self.imagePath, overwrite=True)

        self.signals.message.emit('')
        self.signals.saved.emit(self.imagePath)

        return suc

    def expose(self,
               imagePath='',
               expTime=3,
               binning=1,
               fastReadout=True,
               posX=0,
               posY=0,
               width=1,
               height=1,
               ):
        """

        :return: success
        """

        if not self.deviceConnected:
            return False

        worker = Worker(self.workerExpose,
                        imagePath=imagePath,
                        expTime=expTime,
                        binning=binning,
                        fastReadout=fastReadout,
                        posX=posX,
                        posY=posY,
                        width=width,
                        height=height)
        # worker.signals.result.connect(self.emitStatus)
        self.threadPool.start(worker)
        return True

    def abort(self):
        """
        abort cancels the exposing

        :return: success
        """

        if not self.deviceConnected:
            return False

        canAbort = self.data.get('CAN_ABORT', False)
        if canAbort:
            self.client.stopexposure()

        return True
