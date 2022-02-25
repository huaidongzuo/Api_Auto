# -*- coding: utf-8 -*-
# 构建定位接口测试用例
# author:hzuo
from system.Api import api
from requests import  request
from system.Context import Context
import pytest
from system.Image2base import image_to_base64
from system.ExManage import ExManage




def get_test_data(row):
    Txls = ExManage('test.xlsx')
    test_data = Txls.get_data(row)

    image_str = image_to_base64(test_data['image'], 'images')
    data = {
        'data': test_data['data'],
        'image': image_str
    }
    r_data = api(
        protocol=test_data['protocol'],
        host=test_data['host'],
        port=round(test_data['port']),
        path=test_data['path'],
        method=test_data['method'],
        data=data
    )
    return r_data

@pytest.mark.info(team='测试团队1',author='左淮东')
def test_location():
    r_data = get_test_data(1)
    req = request(**r_data)
    assert req.status_code == 200
    assert req.json()['description'] == "failed"
