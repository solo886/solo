# @Time : 2021/4/12 21:40 
# __author__ = 'zhangcheng'
# coding:utf-8
import pytest
import yaml

from Calculator import Calculator


@pytest.fixture()
def connectdb():
    print('连接数据库')
    yield "搜索结果"   # 返回后面的结果，yield相当于return
    print('断开数据库')

@pytest.fixture()
def login(connectdb):
    print('登录')
    username = 'zhangsan'
    password = 123455
    return username,password

@pytest.fixture(scope='class')
def fun_ini():
    print("开始计算")
    calc = Calculator()
    yield calc
    print('结束结算')

def get_datas():
    with open("./calc.yaml",encoding='utf-8') as datas:
        datas = yaml.safe_load(datas)
        # print(datas)
    return datas

@pytest.fixture(params=get_datas()['intdatas'],ids=get_datas()['ids_int'])
def getdatas_int(request):
    return request.param

@pytest.fixture(params=get_datas()['float'],ids=get_datas()['ids_float'])
def getdatas_float(request):
    return request.param

@pytest.fixture(params=get_datas()['div'],ids=get_datas()['ids_div'])
def getdatas_div(request):
    return request.param

def pytest_collection_modifyitems(session,config,items:list):
    print('这是收集所有测试用例的方法')
    print(items)
    items.reverse()   # 用例倒序执行
    # 将文件中的中文解码出来
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
    if 'div' in item.name:
        item.add_marker(pytest.mark.div)
    elif 'nike' in item.name:
        item.add_marker(pytest.mark.nike)
