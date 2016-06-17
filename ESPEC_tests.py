# -*- coding: utf-8 -*-
"""ESPEC_tests.py: Simple test routine for pyUART wrapper functions

__author__ = "Jason M. Battle"
__copyright__ = "Copyright 2016, Jason M. Battle"
__license__ = "MIT"
__email__ = "jason.battle@gmail.com"
"""

from ESPEC import SH241

if __name__ == '__main__':

    test = SH241()
    test.OpenChannel()
    if test.GetMode() == 'OFF':
        test.SetPowerOn()
    # Read Commands    
#    test.GetROMVersion()
#    test.GetIntStatus()
#    test.GetIntMask()
#    test.GetAlarmStat()
#    test.GetKeyProtStat()
#    test.GetType()
#    test.GetMode()
#    test.GetCondition()
#    test.GetTemp()
#    test.GetHumid()
#    test.GetRefrigeCtl()
#    test.GetRelayStat()
#    test.GetHeaterStat()
#    test.GetProgStat()
#    test.GetProgData()
#    test.GetProgStepData(1)    
    # Write Commands
    test.SetIntMask(0b01000000)
    test.ResetIntStatus()
    test.SetKeyProtectOn()
    test.SetKeyProtectOff()
    test.SetPowerOff()
    test.SetPowerOn()
    test.SetTemp(25.0)
    test.SetHighTemp(155.0)
    test.SetLowTemp(-45.0)
    test.SetHumid(50.0)
    test.SetHighHumid(100)
    test.SetLowHumid(0)
    test.SetHumidOff()
    test.SetRefrigeCtl(9)
    test.SetRelayOn(1)
    test.SetRelayOff(1)
    test.SetModeOff()
    test.SetModeStandby()
    test.SetModeConstant()
    test.ProgramWrite()
    test.SetModeProgram()
    test.ProgramAdvance()
    test.ProgramEnd()
    test.SetModeStandby()
    test.ProgramErase()
    test.SetModeOff()
    test.CloseChannel()
    