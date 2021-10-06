# Oscilloscope Class written by Krishna 2021 based on Old Code in Z drive#
import pyvisa as visa 
import numpy as np
import struct
from parameters import * 
# from app import channels_used

class Oscilloscope():
    """
    Oscilloscope Class running on TekVISA
    """
    def __init__(self):
        visa_addr = visa_address
        rm = visa.ResourceManager()
        # print(rm.list_resources())
        self.instr = rm.open_resource(visa_addr)
        print("")
        print("Oscilloscope Communication Resource Opened. Instrument Details:")
        print(self.instr.query('*IDN?'))
        self.params={"datastart":10,"nsamps":10000,"data_width":1}

        self.instr.write("data:enc rpb")
        self.instr.write("data:width " + str(self.params['data_width']))
        self.instr.write("data:start " + str(self.params['datastart']))
        self.instr.write("data:stop " + str(self.params['datastart']+self.params['nsamps']))
        self.ymult_dict,self.yzero_dict,self.yoffst_dict,self.xincr_dict={},{},{},{}
        self.channels=[1,2,3,4]
        for chn in self.channels:
            self.instr.write("data:source ch" + str(chn))
            self.ymult_dict[chn] = float(self.instr.query("wfmpre:ymult?"))
            self.yzero_dict[chn] = float(self.instr.query("wfmpre:yzero?"))
            self.yoffst_dict[chn] = float(self.instr.query("wfmpre:yoff?"))
            self.xincr_dict[chn] = float(self.instr.query("wfmpre:xincr?"))
    
    def get_channel_data(self,chn):
        self.instr.write("data:source ch" + str(chn))
        ymult = float(self.instr.query("wfmpre:ymult?"))
        yzero = float(self.instr.query("wfmpre:yzero?"))
        yoffst = float(self.instr.query("wfmpre:yoff?"))
        xincr = float(self.instr.query("wfmpre:xincr?"))

        self.instr.write("curve?")
        data = self.instr.read_raw()
        headerlen = 2 + int(data[1])
        header = data[:headerlen]
        adc_levels = data[headerlen:-1]
        adc_levels = np.array(struct.unpack('%sB' % len(adc_levels), adc_levels))
        voltages = (adc_levels - yoffst) * ymult + yzero
        return voltages

    def get_channel_data_fast(self, chn):
        self.instr.write("data:source ch" + str(chn))
        ymult = self.ymult_dict[chn]
        yzero = self.yzero_dict[chn]
        yoffst = self.yoffst_dict[chn]
        xincr = self.xincr_dict[chn]
        self.instr.write("curve?")
        data = self.instr.read_raw()
        headerlen = 2 + int(data[1])
        header = data[:headerlen]
        adc_levels = data[headerlen:-1]
        adc_levels = np.array(struct.unpack('%sB' % len(adc_levels), adc_levels))
        voltages = (adc_levels - yoffst) * ymult + yzero
        # print(type(voltages))
        return voltages
    
    def get_channel_param(self,chn):
        values = []
        values= values + [self.ymult_dict[chn],self.yzero_dict[chn],self.yoffst_dict[chn],self.xincr_dict[chn]]
        return values
