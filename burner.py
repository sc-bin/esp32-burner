import os
import esptool

class BURNER(object):
    firmware_path: str
    py_path: str
    def __init__(self,frimware_path:str, py_path:str):
        self.firmware_path = frimware_path
        self.py_path = py_path
        if not os.path.exists(self.firmware_path):
            print("未找到firmware文件")
            exit(1)
    
    def burner_picoW(self,dev_path:str)->bool:
        print("烧录文件",os.path.basename(self.firmware_path),"到",dev_path)
        try:
            esptool.main([
                '--chip', 'esp32s3',
                '--port', dev_path,
                '--after', 'hard_reset',
                'write_flash', '-z', '0', self.firmware_path
            ])
            print("烧录完成")
            return True
        except:
            print(f"烧录失败:")
        return  False
    def send_main_py(self, dev_path: str) -> bool:
        '''
        发送文件到micropython板子上
        '''
        print("发送文件",os.path.basename(self.py_path),"到",dev_path)
        os.system(f"ampy --port {dev_path} put {self.py_path}")
       
