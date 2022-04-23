Changelog
=========
The changelog contains the user related function or environment updates. For a
detailed changes list, please refer to the commit list on GitHub.

Ideas for the future
--------------------
- implementing Baader dome control e.g. 10micron dome interface
- split profiles in base and add-on
- receive video indi for sat tracking and horizon setup
- joystick support
- data exchange to EKOS SQLite for Location and horizon through SQLite interface
- SQR calculation
- split imaging tab into operating and statistics
- satellite scheduler

Beta version of MW4
----------------------------
3.0.0b0

- add: all charts zoomable
- add: measure: window has max 5 charts now (from 3)
- add: measure: more values (time delta, focus, etc)
- add: almanac now supports UTC / local time
- add: almanac support set/rise times moon
- add: analyse: charts could show horizon and values for each point
- add: analyse: alt / az charts with iso error curves
- add: sound for connection lost and sat start tracking
- add: model points: multiple variants for edit and move points
- add: model points: set dither on celestial paths
- add: model points: generate from actual used mount model
- add: model points: existing model files could be loaded
- add: hemisphere: show actual model error in background
- add: hemisphere: edit horizon model much more efficient
- add: dome: control azimuth move CW / CCW for INDI
- add: satellites: all time values could be UTC or local time now
- improve: complete rework of charting: performance and functions
- improve: cleanup of gui
- improve: iers download messages
- improve: optimized DSO path generation (always fit, less params)
- remove: matplotlib usage and replace with pyqtgraph

Released version of MW4
-----------------------

Version 2.2
^^^^^^^^^^^
2.2.3

- fix: mount orientation in southern hemisphere

2.2.2

- fix: almanac moon phase drawing error

2.2.1

- update: builtin data for finals200.all
- fix: download iers data: fix file not found feedback

2.2.0

- add: support SGPro camera as device
- add: support N.I.N.A. camera as device
- add: two modes for SGPro and N.I.N.A.: App or MW4 controlled
- add: debayer (4 modes) all platforms (armv7, StellarMate, Astroberry)
- add: filter satellites for twilight visibility settings
- add: setting performance for windows automation (slow / normal / fast)
- add: auto abort imaging when camera device is disconnected
- add: missing cursor in virtual keypad window
- add: support for keyboard usage in virtual keypad window
- add: screenshot as PNG save for actual window with key F5
- add: screenshots as PNG save for all open windows with key F6
- add: query DSO objects for DSO path setting in build model
- improved: flexible satellite handling when mount not connected
- improved: show selected satellite name in satellite windows title
- improved: 3D simulator drawing
- improved: updater now avoids installation into system package
- improved: GUI for imaging tab - disable all invalid interfaces
- improved: redesign analyse window to get more space for further charts
- improved: Tools: move mount: better UI, tooltips, multi steps in alt/az
- improved: gui in image window when displaying different types
- improved: reduced memory consumption if display raw images
- improved: defining park positions with digit and improve gui for buttons
- improved: when pushbutton shows running, invert icons as well
- improve: moon phases in different color schemes
- upgrade: pywin32 library to version 303 (windows)
- upgrade: skyfield library to 1.41
- upgrade: numpy library to 1.21.4
- upgrade: matplotlib to 3.5.1
- upgrade: scipy library to 1.7.3
- upgrade requests library to 2.27.2
- upgrade importlib_metadata library to 4.10.0
- upgrade deepdiff library to 5.7.0
- upgrade wakeonlan library to 2.1.0
- upgrade pybase64 library to 1.2.1
- upgrade websocket-client library to 1.2.3
- fix: simulator in southern hemisphere


Version 2.1
^^^^^^^^^^^
2.1.7

- add: 12 build point option for model generation
- add: grouping updater windows upper left corner
- add: support for languages other than english in automation
- add: minimize cmd window once MW4 is started
- fix: KMTronic Relay messages

2.1.6
- add: explicit logging of automation windows strings for debug
- add: showing now detected updater path and app
- revert: fixes for german as they do not work

2.1.5

- fix: checking windows python version for automation

2.1.4

- add: enabled internal updater for astroberry and stellarmate
- add: temperature measurement for camera
- improved: logging for ASCOM threading
- improved: image handling
- fix: DSLR camera devices

2.1.3

- add: config adjustments for astroberry and stellarmate devices (no debayer)
- improved: logging for UI events

2.1.2

- fix: non connected mount influences camera on ASCOM / ALPACA
- fix: logging string formatting

2.1.1

- fix: for arm64 only: corrected import for virtual keypad
- fix: arrow keys on keypad did accept long mouse press

2.1.0

- add: hemisphere window: help for choosing the right star for polar alignment
- add: hemisphere terrain adjust for altitude of image beside azimuth
- add: angular error ra / dec axis in measurement
- add: device connection similar for ASCOM and ALPACA devices
- add: extended satellite search and filter capabilities (spreadsheet style)
- add: estimation of satellite apparent magnitude
- add: extended satellite tracking and tuning capabilities
- add: enabling loading a custom satellite TLE data file
- add: command window for manual mount commands
- add: sorting for minimal dome slew in build point selection
- add: setting prediction time of almanac (shorter reduces cpu load)
- add: providing 3 different color schemes
- add: virtual keypad available for RPi 3/4 users now
- improve: check if satellite data is valid (avoid error messages)
- improve: better hints when using 10micron updater
- improve: simplified signals generation
- improve: analyse window plots
- improve: rewrite alpaca / ascom interface
- improve: gui for running functions
- improve: test coverage
- remove: push time from mount to computer: in reliable and unstable
- fix: segfault in qt5lib on ubuntu

Version 2.0
^^^^^^^^^^^
2.0.6

- fixes

2.0.5

- fix: bug when running "stop exposure" in ASCOM

2.0.4

- improvement: GUI for earth rotation data update, now downloads
- improvement: performance for threads.
- improvement: added FITS header entries for ALPACA and ASCOM
- fix: removed stopping DAT when starting model

2.0.3

- improvement: GUI for earth rotation data update, now downloads
- improvement: performance for threads.

2.0.2

- fix: robustness against errors in ALPACA server due to memory faults #174
- fix: robustness against filter names / numbers from ALPACA server #174
- fix: cleanup import for pywinauto timings import #175
- improvement: avoid meridian flip #177
- improvement: retry numbers as int #178

2.0.1

- fix: MW4 not shutting down when dome configured, but not connected
- fix mirrored display of points in polar hemisphere view

2.0.0

- add new updater concept
- add mount clock sync feature
- add simulator feature
- add terrain image feature
- add dome following when mount is in satellite tracking mode
- add dome dynamic following feature: reduction of slews for dome
- add setting label support for UPB dew entries
- add auto dew control support for Pegasus UPB
- add switch support for ASCOM/ALPACA Pegasus UPB
- add observation condition support for ASCOM/ALPACA Pegasus UPB
- add feature for RA/DEC FITS writing for INDI server without snooping
- add completely revised satellite tracking menu gui
- add partially satellite tracking before / after possible flip
- add satellite track respect horizon line and meridian limits
- add tracking simulator feature to test without waiting for satellite
- add alt/az pointer to satellite view
- add reverse order for failed build point retry
- add automatic enable webinterface for keypad use
- add broadcast address and port for WOL
- add new IERS and lead second download
- add more functions are available without mount connected
- add change mouse pointer in hemisphere
- add offset and gain setting to imaging
- add disable model point edit during model build run
- update debug standard moved from WARN to INFO
- update underlying libraries
- update GUI improvements
- fix for INDI cameras sending two times busy and exposure=0
- fix slewing message dome when disconnected
- fix retry mechanism for failed build points
- fix using builtins for skyfield and rotation update
- fix plate solve sync function


Version 1.1
^^^^^^^^^^^
1.1.1

- adding fix for INDI cameras sending two times BUSY, EXP=0

1.1.0

- adding release notes showing new capabilities in message window
- adding cover light on / off
- adding cover light intensity settings
- reversing E/W for polar diagram in hemisphere window
- adding push mount time to computer manual / hourly
- adding contour HFD plot to image windows
- adding virtual emergency stop key on time group
- update build-in files if newer ones are shipped
- auto restart MW4 after update
- adding OBJCTRA / OBJCTDEC keywords when reading FITs
- upgrade various libraries

Version 1.0
^^^^^^^^^^^
1.0.7

- bugfix cooler

1.0.6

- checking if camera has cooler
- fixing retry model points

1.0.5

- bugfix check for H18 database

1.0.4
- adding check for ASTAP H17, H18, G17, G18 database
- increasing the solve limit from 9999 arcsec to 36000 arcsec

1.0.3
- bugfix binning setting on large sensors

1.0.2
- bugfix: polar alignment command error

1.0.1
- bugfix: fields index and app in device popup for astrometry and astap were wrong

1.0.0

- first official release
