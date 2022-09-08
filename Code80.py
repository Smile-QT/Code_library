
# 批量爬取抖音视频的点赞数、评论数、收藏数

import xlrd
import openpyxl as op
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


filePath = r"C:/YXL/lijiawen/reptile/DianZ_PingL_ShouC_ZhuanF/Data/xinnongrenjihua02.xlsx"
data = xlrd.open_workbook(filePath)
sheet1 = data.sheet_by_name("Sheet1")   # 按名获取该文件中的表格
zero_col_values = sheet1.col_values(0)  # 获取第1列的数据：抖音视频的网址的序号，序号是从1开始的。
# 将字符串数字，转化成int型的数字，方便之后使用
for i in range(1, len(zero_col_values)):
    zero_col_values[i] = int(zero_col_values[i])

first_col_values = sheet1.col_values(1)  # 获取第2列的数据：抖音视频的网址


#########################################################################################################################################

for j in range(1, len(first_col_values)):
    print("###############################")
    print(j)
    pinglun_numbers = 3

    douying_vedio_path = first_col_values[j]
    douyingshipingxuhao_pinglunsuoxiehangshu = zero_col_values[j]

    url = douying_vedio_path
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'cookie': 'douyin.com; ttwid=1%7C6cnERZrcfvlaWu2yykNNDcfgkCZqwUh2Dco-GN3fuT0%7C1662431870%7C01ef530e6018b1acd31dd45ad0d6b5561c41e95f4b4826a87caca50ec122226f; douyin.com; strategyABtestKey=1662431871.539; s_v_web_id=verify_l7pl0hps_r6ZYIxa3_484d_4ryu_AkZT_cmiqO7XggBDE; passport_csrf_token=745f5a0c62cb40746bc29cebb37d7312; passport_csrf_token_default=745f5a0c62cb40746bc29cebb37d7312; n_mh=rZbLvuXyRyiN7VCxvrqeeK_L419A7HUwPpGO0twgduE; _tea_utm_cache_2018=undefined; THEME_STAY_TIME=%22299579%22; IS_HIDE_THEME_CHANGE=%221%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAD-SZ1LvCb7XOVC_yaKBP-D61VFjrmHND6R6rWVRb0G5dJZPxcf9tl_TGbL-r6Jv0%2F1662480000000%2F0%2F0%2F1662433831613%22; csrf_session_id=2380be7479221ba8e54a8e2c78e6ee60; download_guide=%223%2F20220906%22; toutiao_sso_user=8e1517cfa2d0ebfce2f210335e628af0; toutiao_sso_user_ss=8e1517cfa2d0ebfce2f210335e628af0; passport_auth_status=1d0d589ffa75db171bb7910e7423fd3c%2Cb8f221935b3e01bbe743ee325aa6c238; passport_auth_status_ss=1d0d589ffa75db171bb7910e7423fd3c%2Cb8f221935b3e01bbe743ee325aa6c238; odin_tt=9f3301508bf21b6de19f239963bb14c261c68ce1e18c86a5c059bfb31f5b7882; sso_uid_tt=8e9b948323699bf9ec1112ed9414ebf7; sso_uid_tt_ss=8e9b948323699bf9ec1112ed9414ebf7; sid_ucp_sso_v1=1.0.0-KGExOThiZTc3ZjM5MGM2NGMxYTQ2NTdiMGU2YTYzZGYzYzI0ZjgxNTEKCRCaqdyYBhjvMRoCbGYiIDhlMTUxN2NmYTJkMGViZmNlMmYyMTAzMzVlNjI4YWYw; ssid_ucp_sso_v1=1.0.0-KGExOThiZTc3ZjM5MGM2NGMxYTQ2NTdiMGU2YTYzZGYzYzI0ZjgxNTEKCRCaqdyYBhjvMRoCbGYiIDhlMTUxN2NmYTJkMGViZmNlMmYyMTAzMzVlNjI4YWYw; sid_guard=68fe0ecbc1b3d871d513a38694f50e27%7C1662456986%7C21600%7CTue%2C+06-Sep-2022+15%3A36%3A26+GMT; uid_tt=73f78b3e39bcab3250f0cbbe87a08930; uid_tt_ss=73f78b3e39bcab3250f0cbbe87a08930; sid_tt=68fe0ecbc1b3d871d513a38694f50e27; sessionid=68fe0ecbc1b3d871d513a38694f50e27; sessionid_ss=68fe0ecbc1b3d871d513a38694f50e27; sid_ucp_v1=1.0.0-KDY0ODc3ZDIzYTRjODg4YTY3MDkzMDBlYzM2YzNjYmM5ZWFmNmY1OTAKCBCaqdyYBhgNGgJscSIgNjhmZTBlY2JjMWIzZDg3MWQ1MTNhMzg2OTRmNTBlMjc; ssid_ucp_v1=1.0.0-KDY0ODc3ZDIzYTRjODg4YTY3MDkzMDBlYzM2YzNjYmM5ZWFmNmY1OTAKCBCaqdyYBhgNGgJscSIgNjhmZTBlY2JjMWIzZDg3MWQ1MTNhMzg2OTRmNTBlMjc; __ac_nonce=06317149a00ee8670ee70; __ac_signature=_02B4Z6wo00f01dMmNegAAIDBS02im6KQ-AHTBjFAABfgBe1rDVwIoC0fDVOptmB3einq.lXevzR3.8b8pKapQmzyT7.UtA.q0OkKQR9iqncb0GtqC0ZoGpxBq7dpdm1GDr1zmz-AlgLL32xl34; home_can_add_dy_2_desktop=%221%22; tt_scid=qfV85cP8miFPeCA5W4TpUI0A1fX42ULGHSo.TUQ5ZPcj7irZmeX5yRSkt7wjgzil366a; msToken=GRy630G1zvBvKIIKqix7n2UnzA7fltazFqibmjRF1D-qldjCHOG4ONrYFV66qTagD9hXA2-u27Fs9B5weeU-spscJYpbRbwnE9l2okc50u91AvTLObxEzuSL7MjZHdJj; msToken=VGjzSqUwvgJgH-FCh8OLuo6cwYJ_5pxSk32YPSdb6DwL0XdAeERJMekAP6LQKiKE7qoalY3oJkSl8EUZgzPohzWq9q_cuqztZtG44XvR_WdkYw9M9bsyx_JkBCFsSEja'}
    ret = Request(url, headers=headers)
    res = urlopen(ret)
    contents = res.read().decode('utf-8')

    soup = BeautifulSoup(contents, "html.parser")
    for tag in soup.find_all('div', class_='kr4MM4DQ'):
        span = tag.find('span', class_='CE7XkkTw')
        if span is not None:
            m_rating_score = float(tag.find('span', class_='CE7XkkTw').get_text()[:-1])
            print(m_rating_score)

            # 这是把爬下来的数据存放在文件中
            tableAll = op.load_workbook(filePath)
            table1 = tableAll['Sheet1']
            table1.cell(douyingshipingxuhao_pinglunsuoxiehangshu + 1, pinglun_numbers, str(m_rating_score))
            pinglun_numbers = pinglun_numbers + 1
            tableAll.save(filePath)







