
# 根据提供的抖音网址，下载抖音视频

import requests, re

def main(url):
    douyin = url
    # 请求头使用浏览器模拟的手机端请求头
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Mobile Safari/537.36 Edg/103.0.1264.62'
    }
    ree = requests.get(douyin, headers=headers)
    # 对页面进行重定向处理 获取新的短视频链接
    new_url = ree.url
    # print(new_url)
    # https://www.iesdouyin.com/share/video/7120194285059788073/?region=CN&mid=6607047142617910024&u_code=if86a7jd&did=MS4wLjABAAAAxWn3bFKxVOpbMG_Ocvy7YJitc49o0gG39ucM5ohabQ0&iid=MS4wLjABAAAAlbksxOcUoFf3fEpwDkkJ3hlXXS6nK-9vB7IVcSBB1XljPwr6eDOn76tKDrf90ktL&with_sec_did=1&titleType=title&timestamp=1658190604&utm_campaign=client_share&app=aweme&utm_medium=ios&tt_from=copy&utm_source=copy
    # 7120194285059788073 即为视频 id
    # 使用正则提取id
    id = re.search(r'/video/(.*?)/', new_url).group(1)

    # 提取带水印短视频链接地址
    # https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=7120194285059788073
    url = 'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=' + id
    ree = requests.get(url, headers=headers)
    wm = ree.json()
    # 使用正则提取无水印视频链接
    n_wm = wm['item_list'][0]['video']['play_addr']['url_list'][0].replace('wm', '')
    return n_wm


if __name__ == '__main__':
    url = 'https://v.douyin.com/6Rv8vKm/'
    headers = {
        # 用户信息, 常用于检测是否登陆
        'cookie': '__ac_nonce=06319961000dcc842e999; __ac_signature=_02B4Z6wo00f013ARaiwAAIDCExuqRMkKtXtwMU6AAL8p64; ttwid=1%7ChZNljnXHLVm0qYRtp4VeGJAEcw0ma2N6iEZfY4w9GIw%7C1662621200%7C54759d14b47a00c347df93217662eb3d763b0c386d59347c62f486f83d2108d3; home_can_add_dy_2_desktop=%220%22; strategyABtestKey=1662621203.404; s_v_web_id=verify_l7spqjgo_bthDJlth_5rKM_4Ax0_9eHX_Ham5IQ0fQCD6; passport_csrf_token=8c6a6777457bccc95e2e7b453211bd9d; passport_csrf_token_default=8c6a6777457bccc95e2e7b453211bd9d; ttcid=060ed9f3baaf48698c5b6a7c8b4d828630; tt_scid=lAPzhTNxVH7qnkdxvswd21XqIJ78WIW8GShmqRLlfVaDWe0auT2xkom2vJqa6ffwc069; msToken=D2JD5i9T4KjA_vSDWaD4Bf3AV0zLsCzfOWcPirmyw7Rm5YLMpxGoH22GJMLjhdEJDaHzi7ZngR2tLzKVM5Mqv6aMSpIRqHxV6OjPhjjirzYRak97Hm88vL-rfhDh5i33; download_guide=%221%2F20220908%22; msToken=TFsE4K4SRhRPx7q3FvflNKfvE0BbWgEzBezoF3bwNngBrG_8rhQJHlPQwnlFvLTHfHnHA9m3ae30-D9jCww-QXEvGDs0hVXs301e2gBIu1N5_fvLm1g_6WCCjHtk1366; THEME_STAY_TIME=%22299507%22; IS_HIDE_THEME_CHANGE=%221%22',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'

    }
    video_url = main(url)
    print(video_url)
    # 保存数据
    video_content = requests.get(url=video_url, headers=headers).content  # 对于视频播放链接发送请求获取二进制数据内容
    # video\\ 文件夹 title 文件名 .mp4文件后缀 wb二进制保存 as 重命名为 f
    with open('C:/YXL/lijiawen/reptile/shipingzimu/xiaziashiping/Data/video/1111.MP4', mode='wb') as f:
        # 写入数据
        f.write(video_content)
        print(11)
