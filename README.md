```
🕙 分享是一种美德，右上随手点个 🌟 Star，谢谢
```
 
**温馨提醒**
 
1. 本项目仅适用学习交流
2. 本项目不在任何平台出售,如有发现请积极举报<br/>

## 1.项目介绍
 
**基于多种hash算法的较小文件高强度加密方案设计与实现**
 
### 1.1设计方案
 
本工程设计的主要方案如下：<br/>
（1）设计基于改进Feistel结构的加密方案。基于Feistel结构的分组密码结构简单，具有对称性，软硬件较易实现，但存在算法混淆和扩散速度较慢的问题。本工程任务计划对传统的Feistel结构进行了改进，使用ARX结构替代传统的S盒、P盒，提高了混淆和扩散效率，同时加快计算速率，更适合较小文件的加密运算。<br/>
（2）将成熟的Hash算法运用于Feistel结构中。本工程任务计划支持SM3、MD5、SHA-3常见Hash算法的调用，通过调用成熟的hash算法实现非线性变换功能，更进一步地保证了算法的安全性和高效性。<br/>
（3）采用改进的子密钥生成算法。本工程任务采取的改进方案是：首先将明文与密钥进行异或，然后根据分组结果或者哈希表查找比较次数，结合仿射变换决定子密钥的使用顺序，最后利用RSA加密子密钥的使用顺序。以增强算法抵抗暴力分析的能力。<br/>

### 1.2 功能介绍
（1）最快最短进行加密——缩短小型文件加密时间，保证小型文件加密效率<br/>
（2）增强加密算法复杂度及机密性——保证小型文件传输及存储安全性<br/>
（3）增强生成杂凑值的抗碰撞性及随机性——融入多种hash算法，国密SM3支撑加密强度<br/>
（4）防篡改防假冒——验证小型加密文件的完整性真实性<br/>
### 1.3 安装步骤
（1）安装依赖包
```
 pip install -r requirements.txt
```
 （2）启动项目
 ```
 python main.py
```
（3）打开前端界面 <br/>
访问http://127.0.0.1:5000/<br/>

如图：
 
<img src="templates/1.jpg" />
 
### 1.3xxx项目前台展示
 
APP端前台
 
<table>
    <tr>
        <td><img src="images/1.jpg"/></td>
        <td><img src="images/1.jpg"/></td>
        <td><img src="images/1.jpg"/></td>
        <td><img src="images/1.jpg"/></td>
    </tr>
</table>
 
#### 1.3.1 xxx项目前台介绍
 
```
 xxx功能是一项非常吸引人和有趣的功能。它使用了xxxxxxx。趁着这个机会来尝试一下xxx项目吧！
```
 
**xxx项目操作示例图**:
 
<table  align="center">
    <tr>
        <td><img src="images/1.jpg" height="310"/></td>
    </tr>
    <tr>
        <td><img src="images/1.jpg" height="310"/></td>
    </tr>
</table>
 
**xxx项目功能展馆:**
 
```
P1 功能描述："~"
```
 
<table align="center">
    <tr>
        <td height="220" width="210"><img src="images/1.jpg" /></td>
        <td height="220" width="210"><img src="images/1.jpg" /></td>
        <td height="220" width="210"><img src="images/1.jpg" /></td>
    </tr>
    <tr>
        <td height="220" width="210"><img src="images/1.jpg" /></td>
        <td height="220" width="210"><img src="images/1.jpg" /></td>
        <td height="220" width="210"><img src="images/1.jpg" /></td>
    </tr>
</table>
 
```
P2 功能描述："~"
```
 
<table align="center">
    <tr>
        <td height="220" width="210"><img src="images/1.jpg" /></td>
        <td height="220" width="210"><img src="images/1.jpg" /></td>
        <td height="220" width="210"><img src="images/1.jpg" /></td>
    </tr>
    <tr>
        <td height="220" width="210"><img src="images/1.jpg" /></td>
        <td height="220" width="210"><img src="images/1.jpg" /></td>
        <td height="220" width="210"><img src="images/1.jpg" /></td>
    </tr>
</table>
 
 
 
 
 
### 1.4xxx项目后台数据
 
<table>
    <tr>
        <td ><img src="images/1.jpg"/></td>
    </tr>
</table>
 
### 1.5xxx项目后台展示
 
 
 
<table>
    <tr>
        <td ><img src="images/1.jpg"/></td>
    </tr>
    <tr>
        <td ><img src="images/1.jpg"/></td>
    </tr>
    <tr>
        <td ><img src="images/1.jpg"/></td>
    </tr>
    <tr>
        <td ><img src="images/1.jpg"/></td>
    </tr>
</table>
 
## 2.xxx项目完整运行步骤
 
### 2.1架构图
 
<table>
    <tr>
        <td ><img src="images/1.jpg"/></td>
    </tr>
</table>
 
 
 
### 2.2xxx项目结构
 
```
 
```
 
### 2.3xxx项目后端代码运行步骤
 
#### 2.3.1环境配置
 
**运行环境**：
 
**启动中间件：**[Nacos](https://nacos.io/)、[Mysql8.0](http://mysql.p2hp.com/)、[Redis](https://redis.io/)、[Minio](http://www.minio.org.cn/)
 
推荐使用phpStudy简化环境配置：[phpstudy](https://www.xp.cn/)
 
#### 2.3.2后端代码运行
 
通过git拉取代码到本地后，项目结构如图：
 
<table>
    <tr>
        <td ><img src="images/1.jpg"/></td>
    </tr>
</table>
 
操作步骤：
 
1、xxx
 
2、xxx
 
3、xxx
 
至此，后端代码运行成功！
 
### 2.4xxx项目前端代码运行步骤
 
#### 2.4.1项目前端前台代码运行
 
**前台运行环境：**
 
**开发工具：**HBuilder X
 
HBuilder X官方地址：[Windows - HBuilderX 文档 (dcloud.net.cn)](https://hx.dcloud.net.cn/Tutorial/install/windows)
 
 
 
操作步骤：
 
1、xxx
 
2、xxx
 
3、xxx
 
至此，前台代码运行成功！
 
#### 2.4.2项目前端后台代码运行
 
**后台运行环境：** 
 
**开发工具：** 
 
操作步骤：
 
1、xxx
 
2、xxx
 
3、xxx
 
至此，后台代码运行成功！
 
## 添加客服微信
 
 <div align=center>
    <td ><img height="300" width="300" src="images/1.jpg"/></td>
    <td ><img height="300" width="300" src="images/1.jpg"/></td>
 </div>
