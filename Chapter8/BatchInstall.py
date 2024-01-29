import subprocess

libs = {
    "numpy",
    "matplotlib",
    "pillow",
    "sklearn",
    "requests",
    "jieba",
    "beautifulsoup4",
    "wheel",
    "networkx",
    "sympy",
    "pyinstaller",
    "django",
    "flask",
    "werobot",
    "pyqt5",
    "pandas",
    "pyopengl",
    "pypdf2",
    "docopt",
    "pygame",
}

try:
    for lib in libs:
        subprocess.run(f"pip install {lib}", check=True, shell=True)
    print("安装成功")
except subprocess.CalledProcessError as e:
    print(f"安装失败: {e}")
