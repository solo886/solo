# @Time :  20:21
# __authou__= 'zhangcheng'
# conding = utf-8
# corpid=ww27c094c30bd8ef15
# hmuWof2MO41ETXD0BqU_-_xhtVg_kwwBON4iWuZqfyc

import requests
import json
from jsonpath import jsonpath


class TagManage:
    access_token = None
    def get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        param = {"corpid":"ww27c094c30bd8ef15",
                 "corpsecret":"hmuWof2MO41ETXD0BqU_-_xhtVg_kwwBON4iWuZqfyc"}

        r = requests.get(url, params=param)
        # print(json.dumps(r.json(), indent=2, ensure_ascii=False))   # indent表示缩进
        self.access_token = r.json()["access_token"]


    def qoute_tag(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list"
        param = {"access_token": self.access_token}
        json1 = {}
        r = requests.post(url, params=param, json=json1)
        return r
        # print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        # assert r.json()["errcode"] == 0
        #
        # # print(r.json()["tag_group"][0]['group_name'])
        # group_name = jsonpath(r.json(), '$..group_name')
        # print(jsonpath(r.json(), '$..group_name'))
        # print(jsonpath(r.json(), "$..name"))

    def add_tag(self,group_name, tag_name):
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag"
        param = {"access_token": self.access_token}
        json1 = {"group_name": group_name,
                "tag": [{
                        "name": tag_name,
                        "order": 1}]
                }
        r = requests.post(url, params=param, json=json1)
        return r

    def edit_tag(self, tag_id, tag_name):
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag"
        param = {"access_token": self.access_token}
        json1 = {
                "id": tag_id,
                "name": tag_name,
            }
        r = requests.post(url, params=param, json=json1)
        return r


    def delete_tag(self, tag_id):
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag"
        param = {"access_token": self.access_token}
        json1 = {
                "tag_id": tag_id
            }
        r = requests.post(url, params=param, json=json1)
        return r



