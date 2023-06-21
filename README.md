# hvac_hms

## Intesis Modbus RTU Interface

### Read registers
```
2023/06/19 10:22
root@armadillo:/home/atmark/intesis# python3 ac_read_intesis.py
minimalmodbus.Instrument<id=0xb6a3d8b0, address=1, mode=rtu, close_port_after_each_call=False, precalculate_read_size=True, clear_buffers_before_each_transaction=True, handle_local_echo=False, debug=False, serial=Serial<id=0xb6a3d910, open=True>(port='/dev/ttymxc2', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=1.0, xonxoff=False, rtscts=False, dsrdtr=False)>
args:  ['ac_read_intesis.py']
Read Intesis AC unit registers
Register 0 (power status): 0x1, 1
Register 1 (unit mode): 0x4, 4
Register 2 (unit fan speed): 0x3, 3
Register 4 (unit temp setpoint): 0x14, 20
Register 5 (unit temp ref): 0x18, 24
Register 22 (indoor unit amb temp): 0x8000, 32768
Register 23 (ac real temp setpoint): 0x14, 20

root@armadillo:/home/atmark/intesis# python3 ac_read_intesis.py
args:  ['ac_read_intesis.py']
Read Intesis AC unit registers
Register 0 (power status): 0x1, 1
Register 1 (unit mode): 0x4, 4
Register 2 (unit fan speed): 0x1, 1
Register 4 (unit temp setpoint): 0x15, 21
Register 5 (unit temp ref): 0x16, 22
Register 22 (indoor unit amb temp): 0x8000, 32768
Register 23 (ac real temp setpoint): 0x15, 21
Register 11 (error code): 0x0, 0
```
### Write registers
```
root@armadillo:/home/atmark/intesis# python3 ac_write_intesis.py
minimalmodbus.Instrument<id=0xb6a718b0, address=1, mode=rtu, close_port_after_each_call=False, precalculate_read_size=True, clear_buffers_before_each_transaction=True, handle_local_echo=False, debug=False, serial=Serial<id=0xb6a71910, open=True>(port='/dev/ttymxc2', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=1.0, xonxoff=False, rtscts=False, dsrdtr=False)>
args:  ['ac_write_intesis.py']
Write Intesis Modbus Registers
Register 4 (unit temp setpoint): 0x14, 20
Write 4 (unit temp setpoint): 0x15, 21
Register 4 (unit temp setpoint): 0x15, 21

args:  ['ac_write_intesis.py']
Write Intesis Modbus Registers
Register 2 (unit fan speed): 0x2, 2
Write 2 (unit fan speed): 0x1, 1
Register 2 (unit fan speed): 0x1, 1

args:  ['ac_write_intesis.py']
Write Intesis Modbus Registers
Register 1 (unit mode): 0x3, 3
Write 1 (unit mode): 0x4, 4
Register 1 (unit mode): 0x4, 4

```