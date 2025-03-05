import os
import esptool
class BURNER(object):
    firmware_path: str
    def __init__(self,frimware_path:str):
        self.firmware_path = frimware_path
        if not os.path.exists(self.firmware_path):
            print("未找到firmware文件")
            exit(1)
    
    def burner(self,dev_path:str):
        print("烧录文件",os.path.basename(self.firmware_path),"到",dev_path)
        try:
            esptool.main([
                '--chip', 'esp32s3',
                '--port', dev_path,
                '--after', 'hard_reset',
                'write_flash', '-z', '0', self.firmware_path
            ])
            print("烧录完成")
        except esptool.FatalError as e:
            print(f"烧录失败: {e}")
        print("完成")