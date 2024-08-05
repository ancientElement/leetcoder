import glob
import os


def find(str):
    # 获取当前工作目录
    current_directory = os.getcwd()
    # 切换到当前工作目录
    os.chdir(current_directory)
    return glob.glob(f"{str}*")


def run(command_str):
    files = find(command_str)
    test_txt,script_py = "",""
    for file in files:
        if ".txt" in file:
            test_txt = file
        if ".py" in file:
            script_py = file
    if script_py == "":
        print("找不到脚本文件")
        return
    if test_txt == "": 
        print("找不到测试用例文件") 
        return
    command_str = f"type {test_txt} | python {script_py}"
    print(command_str)
    os.system(command_str)
 
if __name__ == "__main__":
    while True:
        try:
            n = input()
            if n == "": continue
            run(n)
        except:
            break

