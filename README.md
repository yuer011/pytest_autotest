# pytest+selenium+allure2框架

## 技术选型及版本
- pytest:6.2.4
- selenium:3.14.0
- ~~pytest-allure-adaptor:1.7.10(弃用)~~
- pytest-rerunfailures:10.0
- allure-pytest: 2.9.43

## allure常用函数

- allure.severity("优先级")
- allure.feature("模块名")
- allure.story("功能名")
- allure.step("步骤")
- allure.attach("用例参数")

## yaml配置文件
- logging.yaml  配置日志输出格式
- project.yaml  配置项目绝对路径
- testcase.yaml 配置用例相关（需执行用例文件，重跑次数）

## allure.bat配置环境变量
- allure-2.14.0/bin
- 参考： https://blog.csdn.net/yuer011/article/details/117673342

## 运行
运行runCase.py

## 项目框架
├─common 封装

│  ├─basePage - web端driver管理基础类

├─config 配置文件路径

│ ├─ testcase.yaml 需要运行的用例和重试次数

├─page 测试页面对象类

├─reports 测试报告

├─testcase 测试用例


## 待添加功能
- 邮件通知功能
- 数据库校验
- 数据驱动
