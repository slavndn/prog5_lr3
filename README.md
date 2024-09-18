# Славный Даниил Михайлович - Лабораторная работа №3

****

1. Создал структуру каталогов для проекта
2. Создал setup.py – содержит метаданные пакета
3. Создал setup.cfg – конфигурационный файл, используемый для хранения настроек

В setup.py написал следующий код 

```
import setuptools   


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="slavniy-pypi-package",
    version="0.1.2",
    author="Slavniy D. M. ",
    author_email="herzenmoon@gmail.com",
    description="https://github.com/slavndn/prog5_lr3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/slavndn/prog5_lr3",
    packages=setuptools.find_packages(),
    
    
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
     python_requires='>=3.6',
)
```

В README.md написал следующий код - описание 

```
This is a simple exercise to publish a package onto PyPi. 
In order to understand what the package is capable of, you need to run the command "from slavniyDM import main"
```

4. файл LICENSE на корневом уровне с лицензией MIT

```
MIT License

Copyright (c) [2024-2025] [Danny]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

В main.py создал простую функцию 

```
def hello_world():
    print("Hello World.")

hello_world()
```

5. Собрал пакет перед выгрузкой командой

```
python setup.py sdist bdist_wheel 
```

6. Выгрузил пакет на pypi командой

```
PS C:\home\study\prog5\lr3\slavniy-pypi-package> twine upload --repository-url https://test.pypi.org/legacy/ dist/*
Uploading distributions to https://test.pypi.org/legacy/
Enter your API token: 
Uploading slavniy_pypi_package-0.0.1.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.2/5.2 kB • 00:00 • ?

View at:
https://test.pypi.org/project/slavniy-pypi-package/0.0.1/
PS C:\home\study\prog5\lr3\slavniy-pypi-package> 
```

7. Создал новый проект, далее установил свой пакет следующей командой

```
pip install -i https://test.pypi.org/simple/ slavniy-pypi-package
```

8. Выполнил команду

```
from slavniyDM import main 
```

Результат: 

PS C:\home\study\prog5\lr3\package> & C:/Users/Herze/AppData/Local/Programs/Python/Python312/python.exe c:/home/study/prog5/lr3/package/test.py
Hello World
PS C:\home\study\prog5\lr3\package>

Скриншоты: 

![image](https://github.com/user-attachments/assets/a278c29e-7319-4a8e-95dc-07fe6f4092c1)

![image](https://github.com/user-attachments/assets/a55018e6-43c7-4507-bf12-143220fe4a2d)

![image](https://github.com/user-attachments/assets/857d6bb2-3780-400c-b586-e2e01db980e7)

![image](https://github.com/user-attachments/assets/a5f4aee8-8a18-4209-a947-e757734466c0)

![image](https://github.com/user-attachments/assets/d50a5772-9ee2-4dec-a186-2733f436c084)

![image](https://github.com/user-attachments/assets/6dbf9577-e83e-4965-b20c-54cdec42ecd8)
