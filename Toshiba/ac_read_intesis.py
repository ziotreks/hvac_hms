import sys
# minimalmodbus: https://pypi.python.org/pypi/MinimalModbus
import minimalmodbus
import time

# os com port identifier
# e.g.
# Windows: COM3
# Linux: /dev/ttyS2
# COM_PORT = '/dev/ttyUSB0'
COM_PORT = '/dev/ttymxc2'

# slave device id
DEVICE_ID = 1
#DEVICE_ID = 2
#DEVICE_ID = 201
#DEVICE_ID = 202

# create modbus instrument object
#minimalmodbus.Instrument<id=0xb7437b2c, address=1, close_port_after_each_call=False, debug=False, serial=Serial<id=0xb7437b6c, open=True>(port='/dev/ttyUSB0', baudrate=19200, bytesize=8, parity='N', stopbits=1, timeout=0.05, xonxoff=False, rtscts=False, dsrdtr=False)>

instrument = minimalmodbus.Instrument(COM_PORT, DEVICE_ID)
# instrument.serial.baudrate = 19200 # mSensor, BBus adapter
instrument.serial.baudrate = 9600 # default, Intesis
instrument.serial.timeout = 1.0
instrument.serial.bytesize = 8
instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
# instrument.byteorder = minimalmodbus.BYTEORDER_BIG
# instrument.byteorder = minimalmodbus.BYTEORDER_LITTLE
#instrument.debug = True
# print(instrument)

"""
Intesis Interface:
All registers are type “16-bit unsigned Holding Register” 
and they use the Modbus big endian notation.

Read Input Registers (FC=04)
Read Holding Registers (FC=03)
Write Single Register (FC=06) 
"""
FC03 = 3
FC04 = 4
FC06 = 6

# read_register(registeraddress: int, number_of_decimals: int = 0, functioncode: int = 3, signed: bool = False) -> Union[int, float]

def read_power(register=0):
    power_status = instrument.read_register(register, number_of_decimals=0, functioncode=FC03)
    print("Register {1} (power status): 0x{0:x}, {0}".format(power_status, register))

def read_unit_mode(register=1):
    unit_mode = instrument.read_register(register, number_of_decimals=0, functioncode=FC03)
    print("Register {1} (unit mode): 0x{0:x}, {0}".format(unit_mode, register))

def read_unit_fan_speed(register=2):
    unit_fan_speed = instrument.read_register(register, number_of_decimals=0, functioncode=FC03)
    print("Register {1} (unit fan speed): 0x{0:x}, {0}".format(unit_fan_speed, register))

def read_unit_temp_setpoint(register=4):
    unit_temp_setpoint = instrument.read_register(register, number_of_decimals=0, functioncode=FC03)
    print("Register {1} (unit temp setpoint): 0x{0:x}, {0}".format(unit_temp_setpoint, register))

def read_unit_temp_ref(register=5):
    unit_temp_ref = instrument.read_register(register, number_of_decimals=0, functioncode=FC03)
    print("Register {1} (unit temp ref): 0x{0:x}, {0}".format(unit_temp_ref, register))

def read_indoor_unit_amb_temp(register=22):
    indoor_unit_amb_temp = instrument.read_register(register, number_of_decimals=0, functioncode=FC03)
    print("Register {1} (indoor unit amb temp): 0x{0:x}, {0}".format(indoor_unit_amb_temp, register))

def read_ac_real_temp_setpoint(register=23):
    ac_real_temp_setpoint = instrument.read_register(register, number_of_decimals=0, functioncode=FC03)
    print("Register {1} (ac real temp setpoint): 0x{0:x}, {0}".format(ac_real_temp_setpoint, register))

def read_error_code(register=11):
    error_code = instrument.read_register(register, number_of_decimals=0, functioncode=FC03)
    print("Register {1} (error code): 0x{0:x}, {0}".format(error_code, register))

def read_any_register(register=0):
    any_register = instrument.read_register(register, number_of_decimals=0, functioncode=FC03)
    print("Register {1} (any register): 0x{0:x}, {0}".format(any_register, register))


def read_register_loop(register):
    while True:
        read_any_register(0)
        read_error_code()
        time.sleep(1)

if __name__ == '__main__':
    print("args: ", sys.argv)
    print("Read Intesis AC unit registers")
    # read_voltage()
    """
    read_any_register(0)
    read_error_code()
    """

    read_power()
    read_unit_mode()
    read_unit_fan_speed()
    read_unit_temp_setpoint()
    read_unit_temp_ref()
    read_indoor_unit_amb_temp()
    read_ac_real_temp_setpoint()
    read_error_code()

