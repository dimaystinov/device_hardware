try:
    SerialIn = serial.Serial("/dev/ttyUSB1", 9600)
except:
    try:
        SerialIn = serial.Serial("/dev/ttyUSB0", 9600)
    except:
        print('code panel not connect')


 try:
        inRaw = SerialIn.readline()
        n=len(inRaw)
        s=int(inRaw[0:6])
        s=str(s)
        print(s)
        if len(s)==6:
            print('door_floor="ON"')

    except:
        print('code panel not connect')
        time.sleep(10)
