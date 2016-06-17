# -*- coding: utf-8 -*-
"""ESPEC.py: Control ESPEC temperature chambers via RS-485 

__author__ = "Jason M. Battle"
__copyright__ = "Copyright 2016, Jason M. Battle"
__license__ = "MIT"
__email__ = "jason.battle@gmail.com"
"""

import time
from UART import UARTMaster

class SH241():

    def __init__(self):
        self._address = 1
        self._instr = UARTMaster()
        self._instr.CreateDeviceInfoList()
        self._instr.GetDeviceInfoList()

    def OpenChannel(self):
        self._instr.Open()
        self._instr.Purge()
        self._instr.SetBaudRate()
        self._instr.SetDataCharacteristics()
        self._instr.SetFlowControl()
        self._instr.SetTimeouts()

    def GetROMVersion(self):
        self._instr.Write('%i,ROM?' % self._address)
        time.sleep(1)   
        self._romver = ''.join(map(chr, self._instr.Read())).strip(' \r\n').replace(' ', '') 
        print 'ROM Version: %s' % self._romver 
        return self._romver

    def GetIntStatus(self):
        self._instr.Write('%i,SRQ?' % self._address)
        time.sleep(1)   
        self._intstat = ''.join(map(chr, self._instr.Read())).strip('\r\n')
        print 'Chamber Alarm: %s' % ('TRUE' if (int(self._intstat, 2) & 0b01000000) == 64 else 'FALSE')
        print 'Program Start: %s' % ('TRUE' if (int(self._intstat, 2) & 0b00100000) == 32 else 'FALSE')
        print 'Power Cycle: %s' % ('TRUE' if (int(self._intstat, 2) & 0b00010000) == 16 else 'FALSE')
        return self._intstat
        
    def GetIntMask(self):
        self._instr.Write('%i,MASK?' % self._address)
        time.sleep(1)   
        self._intmask = ''.join(map(chr, self._instr.Read())).strip('\r\n')
        print 'Chamber Alarm Interrupts: %s' % ('ON' if (int(self._intmask, 2) & 0b01000000) == 64 else 'OFF')
        print 'Program Start Interrupts: %s' % ('ON' if (int(self._intmask, 2) & 0b00100000) == 32 else 'OFF')
        print 'Power Cycle Interrupts: %s' % ('ON' if (int(self._intmask, 2) & 0b00010000) == 16 else 'OFF')
        return self._intmask

    def GetAlarmStat(self):
        self._instr.Write('%i,ALARM?' % self._address)
        time.sleep(1)   
        self._alarmstat = ''.join(map(chr, self._instr.Read())).strip('\r\n')
        print 'Number of Alarms: %s' % self._alarmstat.split(',')[0]
        for alarm in self._alarmstat.split(',')[1:]:
            print 'Alarm Code: %s' % alarm
        return self._alarmstat

    def GetKeyProtStat(self):
        self._instr.Write('%i,KEYPROTECT?' % self._address)
        time.sleep(1)   
        self._keyprotstat = ''.join(map(chr, self._instr.Read())).strip('\r\n')
        print 'Key Protection Status: %s' % self._keyprotstat
        return self._keyprotstat

    def GetType(self):
        self._instr.Write('%i,TYPE?' % self._address)
        time.sleep(1)   
        self._type = ''.join(map(chr, self._instr.Read())).strip('\r\n')
        print 'Dry-bulb Sensor: %s' % self._type.split(',')[0]
        print 'Wet-bulb Sensor: %s' % self._type.split(',')[1]
        print 'Temperature Controller: %s' % self._type.split(',')[2]
        print 'Maximum Temperature: %s' % self._type.split(',')[3] 
        return self._type

    def GetMode(self):
        self._instr.Write('%i,MODE?' % self._address)
        time.sleep(1)   
        self._mode = ''.join(map(chr, self._instr.Read())).strip('\r\n')
        print 'Mode: %s' % self._mode
        return self._mode

    def GetCondition(self):
        self._instr.Write('%i,MON?' % self._address)
        time.sleep(1)   
        self._cond = ''.join(map(chr, self._instr.Read())).strip('\r\n')
        print 'Temperature: %s' % self._cond.split(',')[0]
        print 'Humidity: %s' % self._cond.split(',')[1]
        print 'Mode: %s' % self._cond.split(',')[2]
        print 'Number of Alarms: %s' % self._cond.split(',')[3]
        return self._cond
        
    def GetTemp(self):
        self._instr.Write('%i,TEMP?' % self._address)
        time.sleep(1)   
        self._temp = ''.join(map(chr, self._instr.Read())).strip('\r\n')
        print 'Present Temperature: %s' % self._temp.split(',')[0]
        print 'Target Temperature: %s' % self._temp.split(',')[1]
        print 'High Limit Temperature: %s' % self._temp.split(',')[2]
        print 'Low Limit Temperature: %s' % self._temp.split(',')[3]
        return self._temp           

    def GetHumid(self):
        self._instr.Write('%i,HUMI?' % self._address)
        time.sleep(1)       
        self._humi = ''.join(map(chr, self._instr.Read())).strip('\r\n')
        print 'Present Humidity: %s' % self._humi.split(',')[0]
        print 'Target Humidity: %s' % self._humi.split(',')[1]
        print 'High Limit Humidity: %s' % self._humi.split(',')[2]
        print 'Low Limit Humidity: %s' % self._humi.split(',')[3]
        return self._humi

    def GetRefrigeCtl(self):
        self._instr.Write('%i,SET?' % self._address)
        time.sleep(1)     
        self._refrigectl = ''.join(map(chr, self._instr.Read())).strip('\r\n')
        if self._refrigectl == 'REF9':
            print 'Refrigerator Control: AUTO'
        elif self._refrigectl == 'REF1':
            print 'Refrigerator Control: MANUAL (FIXED)'
        elif self._refrigectl == 'REF0':
            print 'Refrigerator Control: MANUAL (OFF)' 
        else:
            print 'Chamber is not equipped with a refrigerator'
        return self._refrigectl

    def GetRefrigeStat(self):
        self._instr.Write('%i,REF?' % self._address)
        time.sleep(1)   
        self._refrigestat = ''.join(map(chr, self._instr.Read())).strip('\r\n')
        if self._refrigestat == '0':
            print 'Refrigerator Status: OFF'
        elif self._refrigestat == '1,ON1':
            print 'Refrigerator Status: ACTIVE'
        else:
            print 'Chamber is not equipped with a refrigerator'
        return self._refrigestat

    def GetRelayStat(self):
        self._instr.Write('%i,RELAY?' % self._address)
        time.sleep(1)   
        self._relaystat = ''.join(map(chr, self._instr.Read())).strip('\r\n')
        print 'Number of Active Relays: %s' % self._relaystat.split(',')[0]
        for relay in self._relaystat.split(',')[1:]:
            print 'Relay Number: %s' % relay
        return self._relaystat

    def GetHeaterStat(self):
        self._instr.Write('%i,%%?' % self._address)
        time.sleep(1)   
        self._heaterstat = ''.join(map(chr, self._instr.Read())).strip('\r\n')
        print 'Number of Heaters: %s' % self._heaterstat.split(',')[0]
        print 'Heater Output: %s' % self._heaterstat.split(',')[1]        
        print 'Humidifying Heater Output: %s' % self._heaterstat.split(',')[2]        
        return self._heaterstat

    def GetProgStat(self):
        self._instr.Write('%i,PRGM MON?' % self._address)
        time.sleep(1)   
        self._progstat = ''.join(map(chr, self._instr.Read())).strip('\r\n')
        if self._progstat[:2] != 'NA':
            print 'Program Number: %s' % self._progstat.split(',')[0]
            print 'Step Number: %s' % self._progstat.split(',')[1]
            print 'Target Temperature: %s' % self._progstat.split(',')[2]
            print 'Target Humidity: %s' % self._progstat.split(',')[3]        
            print 'Step Time Remaining: %s' % self._progstat.split(',')[4]        
            print 'Cycles Remaining: %s' % self._progstat.split(',')[5]        
        else:
            print 'No program data exists'            
        return self._progstat

    def GetProgData(self):
        self._instr.Write('%i,PRGM DATA,PGM:1?' % self._address)
        time.sleep(1)   
        self._progdata = ''.join(map(chr, self._instr.Read())).strip('\r\n')
        if self._progdata[:2] != 'NA':
            print 'Total Steps: %s' % self._progdata.split(',')[0]
            print 'Start Repetitions: %s' % self._progdata.split(',')[1].split('.')[0]
            print 'End Repetitions: %s' % self._progdata.split(',')[1].split('.')[1]            
            print 'Cycle Repetitions: %s' % self._progdata.split(',')[1].split('.')[2]            
            print 'End Step: %s' % self._progdata.split(',')[2].split('(')[1].strip(')')
        else:
            print 'No program data exists'
        return self._progdata

    def GetProgStepData(self, step):
        self._instr.Write('%i,PRGM DATA,PGM:1,STEP%i?' % (self._address, step))
        time.sleep(1)   
        self._progstepdata = ''.join(map(chr, self._instr.Read())).strip('\r\n')
        if self._progstepdata[:2] != 'NA':
            print 'Step Number: %s' % self._progstepdata.split(',')[0]
            print 'Target Temperature: %s' % self._progstepdata.split(',')[1][4:]
            print 'Temperature Ramp: %s' % self._progsttepdata.split(',')[2][10:]          
            print 'Target Humidity: %s' % self._progstepdata.split(',')[4]          
            print 'Humidity Ramp: %s' % self._progstepdata.split(',')[5][10:]
            print 'Soak Time: %s' % self._progstepdata.split(',')[6][4:]
            print 'Soak Guarantee: %s' % self._progstepdata.split(',')[7][7:]
            if self._progstepdata.split(',')[8] == 'REF9':
                print 'Refrigerator Control: AUTO'
            elif self._progstepdata.split(',')[8] == 'REF1':
                print 'Refrigerator Control: MANUAL (FIXED)'
            elif self._progstepdata.split(',')[8] == 'REF0':    
                print 'Refrigerator Control: MANUAL (OFF)'             
            print 'Relay Status: %s' % self._progstepdata.split(',')[9][:2]
        else:
            print 'No program step data exists'
        return self._progdata
        
    def SetIntMask(self, mask=0b01000000):
        self._instr.Write('%i,MASK,%s' % (self._address, bin(mask)[2:]))
        time.sleep(1)   
        
    def ResetIntStatus(self):
        self._instr.Write('%i,SRQ,RESET' % self._address)
        time.sleep(1)   
        
    def SetKeyProtectOn(self):
        self._instr.Write('%i,KEYPROTECT,ON' % self._address) 
        time.sleep(1)   
        
    def SetKeyProtectOff(self):
        self._instr.Write('%i,KEYPROTECT,OFF' % self._address)    
        time.sleep(1)   
         
    def SetPowerOn(self):
        self._instr.Write('%i,POWER,ON' % self._address)  
        time.sleep(10)   
         
    def SetPowerOff(self):
        self._instr.Write('%i,POWER,OFF' % self._address)     
        time.sleep(10)   
                 
    def SetTemp(self, temp):
        self._instr.Write('%i,TEMP,S%.1f' % (self._address, temp)) 
        time.sleep(1)   
         
    def SetHighTemp(self, temp):
        self._instr.Write('%i,TEMP,H%.1f' % (self._address, temp))  
        time.sleep(1)   
         
    def SetLowTemp(self, temp):
        self._instr.Write('%i,TEMP,L%.1f' % (self._address, temp))  
        time.sleep(1)   
         
    def SetHumid(self, humi):
        self._instr.Write('%i,HUMI,S%i' % (self._address, humi)) 
        time.sleep(1)   
         
    def SetHighHumid(self, humi):
        self._instr.Write('%i,HUMI,H%i' % (self._address, humi))  
        time.sleep(1)   
         
    def SetLowHumid(self, humi):
        self._instr.Write('%i,HUMI,L%i' % (self._address, humi)) 
        time.sleep(1)   
                 
    def SetHumidOff(self):
        self._instr.Write('%i,HUMI,SOFF' % (self._address))         
        time.sleep(1)   
                 
    def SetRefrigeCtl(self, refcode):
        self._instr.Write('%i,SET,REF%i?' % (self._address, refcode))
        time.sleep(1)   

    def SetRelayOn(self, relay):
        self._instr.Write('%i,RELAY,ON,%i?' % (self._address, relay))
        time.sleep(1)   

    def SetRelayOff(self, relay):
        self._instr.Write('%i,RELAY,OFF,%i?' % (self._address, relay))
        time.sleep(1)   
        
    def SetModeOff(self):
        self._instr.Write('%i,MODE,OFF' % self._address) 
        time.sleep(5)   
         
    def SetModeStandby(self):
        self._instr.Write('%i,MODE,STANDBY' % self._address) 
        time.sleep(5)   
         
    def SetModeConstant(self):
        self._instr.Write('%i,MODE,CONSTANT' % self._address) 
        time.sleep(5)   
         
    def SetModeProgram(self):
        self._instr.Write('%i,MODE,RUN 1' % self._address)  
        time.sleep(5)   
         
    def ProgramWrite(self, program=[(25.0, 'TRAMPON', -1, 'HRAMPOFF', '01:00')], cycles=1):
        self._instr.Write('%i,PRGM DATA WRITE,PGM:1,EDIT START' % self._address)
        time.sleep(1)           
        for idx, step in enumerate(program):
            if step[2] == -1:
                self._instr.Write('%i,PRGM DATA WRITE,PGM:1,STEP%i,TEMP%.1f,%s,HUMI OFF,%s,TIME%s,' % (self._address, idx+1, step[0], step[1], step[3], step[4]))
                time.sleep(1)   
            else:
                self._instr.Write('%i,PRGM DATA WRITE,PGM:1,STEP%i,TEMP%.1f,%s,HUMI%i,%s,TIME%s,' % (self._address, idx+1, step[0], step[1], step[2], step[3], step[4]))     
                time.sleep(1)   
        self._instr.Write('%i,PRGM DATA WRITE,PGM:1,COUNT,(1.1.%i)' % (self._address, cycles))                       
        time.sleep(1)   
        self._instr.Write('%i,PRGM DATA WRITE,PGM:1,END,HOLD' % self._address)       
        time.sleep(1)   
        self._instr.Write('%i,PRGM DATA WRITE,PGM:1,EDIT END' % self._address)
        time.sleep(1)   
         
    def ProgramErase(self):
        self._instr.Write('%i,PRGM ERASE,PGM:1' % self._address)
        time.sleep(1)   

    def ProgramAdvance(self):
        self._instr.Write('%i,PRGM,ADVANCE' % self._address)                 
        time.sleep(1)   
         
    def ProgramEnd(self):
        self._instr.Write('%i,PRGM,END,HOLD' % self._address)
        time.sleep(1)   
         
    def CloseChannel(self):
        self._instr.Close()
         