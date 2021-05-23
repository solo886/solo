# @Time :  9:24
# __authou__= 'zhangcheng'
# conding = utf-8
import json

import pytest
from jsonpath import jsonpath

from lesson07_interface.wework_api import TagManage


class TestWeworkApi:
    def setup_class(self):
        self.tag = TagManage()
        self.tag.get_token()
    def test_quote(self):
        r = self.tag.qoute_tag()
        assert r.json()["errcode"] == 0
        assert len(jsonpath(r.json(), "$..name")) > 1
        # print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        # print(jsonpath(r.json(), '$..group_name'))
        # print(jsonpath(r.json(), "$..name"))
    @pytest.mark.parametrize('group_name, tag_name',[["test01","lesson005"]])
    def test_add_tag(self, group_name, tag_name):
        r = self.tag.add_tag(group_name, tag_name)
        assert r.json()["errcode"] == 0
        r = self.tag.qoute_tag()
        tag_name_list = jsonpath(r.json(), "$..name")
        assert tag_name in tag_name_list

    @pytest.mark.parametrize('tag_name', [["play03"]])
    def test_edit_tag(self, tag_name):
        # 查询标签id列表
        r = self.tag.qoute_tag()
        tag_id_list = jsonpath(r.json(), "$..id")
        # 编辑便签
        r = self.tag.edit_tag(tag_id_list[-1], tag_name)
        assert r.json()["errcode"] == 0
        # 查询标签名称列表,并断言
        r = self.tag.qoute_tag()
        tag_name_list = jsonpath(r.json(), "$..name")
        assert tag_name in tag_name_list

    def test_del_tag(self):
        # 查询标签id列表
        r = self.tag.qoute_tag()
        tag_id_list = jsonpath(r.json(), "$..id")
        r = self.tag.delete_tag(tag_id_list[0])
        assert r.json()["errcode"] == 0
        # 查询标签名称列表,并断言
        r = self.tag.qoute_tag()
        tag_id_list = jsonpath(r.json(), "$..name")
        assert tag_id_list[0] in tag_id_list

