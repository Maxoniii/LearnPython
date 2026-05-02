import sys
import platform


os_name = platform.system()
python_version = sys.version


info_string = f"OS info is {os_name} Python version is {python_version}"

file = open('os_info.txt', 'w', encoding='utf-8')
try:
    file.write(info_string)
finally:
    file.close()  

print("Файл создан:", info_string)
