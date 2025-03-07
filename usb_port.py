import os
import threading  # 添加: 导入threading模块


class USB_PORT(object):
    port_number: int
    description: str
    USB_DEV_PATH: str
    detection_thread: threading.Thread
    flag_detection_run: bool
    callback_connected = None
    callback_disconnect = None

    def __init__(self, port_number: int, description: str):
        self.port_number = port_number
        self.description = description
        self.USB_DEV_PATH = "/sys/bus/usb/devices/" + str(port_number) + "-1"
        self.flag_detection_run = False

    def __thread_check_connect(self):
        """连接状态检测线程,初始化时启动"""
        flag = None
        while self.flag_detection_run:
            if self.is_connected():
                if flag == True:
                    continue
                if self.get_dev_path() != "":
                    if self.callback_connected:
                        self.callback_connected(self)
                    flag = True
            else:
                if flag == False:
                    continue
                if self.callback_disconnect:
                    self.callback_disconnect(self)
                flag = False
            threading.Event().wait(0.1)
    def regester_callback_connected(self, callback):
        """
        注册回调函数,在插上usb时调用
        """
        self.callback_connected = callback

    def regester_callback_disconnect(self, callback):
        """注册回调函数,在拔出usb时调用"""
        self.callback_disconnect = callback

    def start_detection(self):
        """启动USB连接检测线程"""
        if not self.flag_detection_run:
            self.detection_thread = threading.Thread(target=self.__thread_check_connect)
            self.detection_thread.daemon = True  # 设置线程为守护线程
            self.flag_detection_run = True
            self.detection_thread.start()

    def stop_detection(self):
        """停止usb连接检测线程"""
        if self.flag_detection_run:
            self.flag_detection_run = False
            if self.detection_thread.is_alive():  # 检查线程是否还在运行
                self.detection_thread.join()

    # 该usb口是否插入
    def is_connected(self) -> bool:
        """该usb口是否插入"""
        if os.path.exists(self.USB_DEV_PATH):
            return True
        return False

    def get_dev_path(self) -> str:
        """获取该usb口对应的设备路径"""
        usb_deb_tty_path = (
            self.USB_DEV_PATH + "/" + str(self.port_number) + "-1:1.0/tty"
        )
        if os.path.exists(usb_deb_tty_path):
            acm_name = os.listdir(usb_deb_tty_path)[0]
            if acm_name == "":
                return ""
            dev_path = "/dev/" + acm_name
            if os.path.exists(dev_path):
                return dev_path
        return ""
