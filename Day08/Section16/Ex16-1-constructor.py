'''
파일명 : Ex16-1-constructor.py

생성자
    인스턴스를 생성할 때 생성자가 자동으로 호출된다.
    객체 초기화 용으로 사용한다.

    __init()__
'''
class USB:
    # 생성
    def __init__(self, capacity):
        self.capacity = capacity

    def info(self):
        print('{}GB USB'.format(self.capacity))

usb = USB(128)
usb.info()

usb2 = USB(1024)
usb2.info()

'''
bit - 0 또는 1
1 byte - 8 bit
1 kbyte - 1024 byte
1 mbyte - 1024 kbyte 
1 gbyte - 1024 mbyte
1 tbyte - 1024 gbyte 
'''