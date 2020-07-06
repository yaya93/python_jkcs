#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :http_read2.py
# @Time      :2020/7/3 22:37
# @Author    :yaya
import requests
def http_request(url,data,token=None,method='post'):
    header = {'X-Lemonban-Media-Type': 'lemonban.v2',
              'Authorization': token}

    if method=='get':
        result=requests.get(url,json=data, headers=header)
    else:
        result= requests.post(url,json=data, headers=header)
    return result.json()



if __name__ == '__main__':

    #注册
    reg_url='http://120.78.128.25:8766/futureloan/member/register'
    reg_data={'mobile_phone':13018958135,'pwd':'12345678'}
    #登录
    log_url='http://120.78.128.25:8766/futureloan/member/login'
    log_data={'mobile_phone':13018958135,'pwd':'12345678'}
    response = http_request(log_url, log_data, )
    token=response['data']['token_info']['token']
    #充值
    rec_url = 'http://120.78.128.25:8766/futureloan/member/recharge'
    rec_data = {'member_id': 196711, 'amount': 50000}
    print(http_request(rec_url,rec_data,'Bearer '+token))



