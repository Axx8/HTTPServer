# HTTPServer
使用Python语言开发的一个能在内网中快速开启HTTP文件浏览服务的小工具 ,可执行Webshell，可用于在内网不出网时文件的下载，启动时会根据网卡IPV4地址输出URL(本地回环除外)。

### Options:
```
   -h,        --help           show this help message and exit
   -p PORT,   --port=PORT      自定义端口（默认：8080）
   -d DIR,    --dir=DIR        自定义目录（默认：当前目录）
   -s SHELL,  --shell=SHELL    自定义Shell路径（默认：/?shell=）
```
## 使用默认端口 8080
```
HTTPServer.exe
```
![图片](https://user-images.githubusercontent.com/34683107/226166730-4cfffe2b-18bf-452a-aa63-dc259f683c08.png)


## 执行Webshell
自定义Webshell路径：-s
```
HTTPServer.exe -p 8888 -d C:\ToolsBox -s Axx8
```
Get Shell  http://ip:8888/?Axx8=whoami
![图片](https://user-images.githubusercontent.com/34683107/226166678-1c4a9ef4-0286-4fcc-b07e-9b43cd95ecdf.png)


## 指定端口 -p
```
HTTPServer.exe -d C:\ToolsBox
```
![图片](https://user-images.githubusercontent.com/34683107/226166335-8bbb356d-9d31-4bab-9b6d-187c8f2cc7d0.png)
## 指定目录 -d
```
HTTPServer.exe -d 
```
![图片](https://user-images.githubusercontent.com/34683107/226166410-852d7da8-df3b-4e3e-b4c4-f27ca28dc0f5.png)

## 感谢阅读
![图片](https://user-images.githubusercontent.com/34683107/188175429-58a71c93-a603-408f-ac9b-c0b616b6467c.png)
