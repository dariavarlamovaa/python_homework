# task 1

# class SocialMedia:
#     def __init__(self, account_type):
#         self.account_type = account_type
#
#
# class Facebook(SocialMedia):
#     def __init__(self):
#         super().__init__('Facebook')
#
#
# class Instagram(SocialMedia):
#     def __init__(self):
#         super().__init__('Instagram')
#
#
# class Twitter(SocialMedia):
#     def __init__(self):
#         super().__init__('Twitter')
#
#
# class SocialMediaAccountFactory:
#     @staticmethod
#     def create_account(account_type):
#         dict_accounts = {'Facebook': Facebook, 'Instagram': Instagram, 'Twitter': Twitter}
#         return dict_accounts.get(account_type)()
#
#
# class ProxySocialMediaAccount(SocialMedia):
#     def __init__(self, account_type):
#         super().__init__(account_type)
#
#     def moderate(self):
#         print(f'Content in {self.account_type} was moderated')
#
#     def get_access(self):
#         print(f'The account in {self.account_type} has been logged in ')
#
#
# if __name__ == '__main__':
#     accounts = ['Facebook', 'Instagram', 'Twitter', 'VK']
#     try:
#         for account in accounts:
#             print(f'Account in {SocialMediaAccountFactory.create_account(account).account_type} was created')
#             acc = ProxySocialMediaAccount(account)
#             acc.get_access()
#             acc.moderate()
#             print()
#     except TypeError:
#         print('Social Media was not found in database')

# task 2

# class File:
#     def __init__(self, filename):
#         self.filename = filename
#
#     def read(self):
#         try:
#             with open(self.filename, 'r') as f:
#                 data = f.read()
#                 return data
#         except FileNotFoundError:
#             open(self.filename, 'w').close()
#             return ''
#
#     def write(self, data):
#         try:
#             with open(self.filename, 'w') as f:
#                 f.write(data)
#         except FileNotFoundError:
#             open(self.filename, 'w').close()
#             return ''
#
#     def append(self, data):
#         try:
#             with open(self.filename, 'a') as f:
#                 f.write(data)
#         except FileNotFoundError:
#             open(self.filename, 'w').close()
#             return ''
#
#
# class FileProxy(File):
#     def __init__(self, filename):
#         super().__init__(filename)
#         self.read_count = 0
#         self.cache = []
#
#     def read(self):
#         self.read_count += 1
#         if self.cache:
#             print(self.cache[-1])
#             return self.cache[-1]
#         data = super().read()
#         self.cache.append(data)
#         print(data)
#         return data
#
#     def write(self, data):
#         raise PermissionError('Permission denied! You can`t rewrite data')
#
#     def clear_counter(self):
#         self.read_count = 0
#         print('Counter was cleared')
#
#     def print_counter(self):
#         print(f'Read function was called {self.read_count} times')
#
#
# if __name__ == '__main__':
#     file = FileProxy('a.txt')
#     file.read()
#     file.read()
#     # file.write('lalala')
#     file.append('okokok')
#     file.print_counter()
#     file.clear_counter()
#     file.print_counter()


# task 3
# from abc import ABC, abstractmethod
#
#
# class Command(ABC):
#     @abstractmethod
#     def process(self):
#         pass
#
#     @abstractmethod
#     def cancel(self):
#         pass
#
#
# class PowerOnCommand(Command):
#     def __init__(self, device):
#         self.device = device
#
#     def process(self):
#         self.device.power_on()
#
#     def cancel(self):
#         self.device.power_off()
#
#
# class PowerOffCommand:
#     def __init__(self, device):
#         self.device = device
#
#     def process(self):
#         self.device.power_off()
#
#     def cancel(self):
#         self.device.power_on()
#
#
# class VolumeUpCommand:
#     def __init__(self, device):
#         self.device = device
#
#     def process(self):
#         self.device.volume_up()
#
#     def cancel(self):
#         self.device.volume_down()
#
#
# class VolumeDownCommand:
#     def __init__(self, device):
#         self.device = device
#
#     def process(self):
#         self.device.volume_down()
#
#     def cancel(self):
#         self.device.volume_up()
#
#
# class RemoteControl:
#     def __init__(self):
#         self.commands = {}
#         self.cancel_command = None
#
#     def set_command(self, button, command):
#         if button not in self.commands:
#             self.commands[button] = command
#         else:
#             self.commands.get(button)
#
#     def press_button(self, button):
#         if button in self.commands:
#             command = self.commands.get(button)
#             command.process()
#             self.cancel_command = command
#
#     def press_cancel(self):
#         if self.cancel_command is not None:
#             self.cancel_command.cancel()
#
#
# class Device:
#     @staticmethod
#     def power_on():
#         print('Power on')
#
#     @staticmethod
#     def power_off():
#         print('Power off')
#
#     @staticmethod
#     def volume_up():
#         print('Volume up')
#
#     @staticmethod
#     def volume_down():
#         print('Volume down')
#
#
# if __name__ == '__main__':
#     tv = Device()
#     remote_control = RemoteControl()

#     power_on_command = PowerOnCommand(tv)
#     power_off_command = PowerOffCommand(tv)
#     volume_up_command = VolumeUpCommand(tv)
#     volume_down_command = VolumeDownCommand(tv)

#     remote_control.set_command(0, power_on_command)
#     remote_control.set_command(1, power_off_command)
#     remote_control.set_command(2, volume_up_command)
#     remote_control.set_command(3, volume_down_command)

#     remote_control.press_button(0)
#     remote_control.press_cancel()
#     remote_control.press_button(1)
#     remote_control.press_button(2)
#     remote_control.press_button(3)
