from winreg import *


def del_folder(del_subsection_name_):
    print('Подраздел: ', EnumKey(key_path, 2))
    if EnumKey(key_path, 2) == del_subsection_name_:
        print('del folder: ' + EnumKey(key_path, 2))
        DeleteKey(key_path, EnumKey(key_path, 2))
        print(QueryInfoKey(key_path))
        print('подраздел остался: ' + OpenKey(key_path, del_subsection_name_))


def del_env(name):
    key = OpenKey(HKEY_CURRENT_USER, 'Environment', 0, KEY_ALL_ACCESS)
    DeleteValue(key_path, name)
    CloseKey(key_path)
    # SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment')


def values_param(param, subsection_name_value):
    string_param = QueryValueEx(subsection_name_value, param)
    value_string_param = string_param[0]
    # print('dn ', dn)
    try:
        # dn_Str = dn_Val.encode('ascii', 'ignore')
        value_string_param.encode('ascii', 'ignore')
        print('Значение строкового параметра:', string_param[0])
    except AttributeError:
        print('Мультистроковый параметр:')
        for value in value_string_param:
            print(value)


rem_reg = ConnectRegistry('56ozi14', HKEY_LOCAL_MACHINE)
del_subsection_name = 'DlGordey'
try:
    key_path = OpenKey(HKEY_LOCAL_MACHINE, r'SYSTEM\ControlSet001\Services\Gordey')

    print(QueryInfoKey(key_path))
    try:
        # subsection_name = EnumKey(key_path, 3)
        # key_subsection_name = OpenKey(key_path, subsection_name)
        values_param('test', OpenKey(key_path, EnumKey(key_path, 2)))
        values_param('String', OpenKey(key_path, EnumKey(key_path, 2)))

        del_env('test')
        # del_folder(del_subsection_name)

    except OSError:
        print('Подраздела нет')

except FileNotFoundError:
    print('Раздела не существует')
