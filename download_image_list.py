
from requests import request
import time


"""
@request
babyID
page
size
"""
request_url="http://gateway.hidowell.hiteacher.cn/user/course/app/babyAlbum/list"
login_url=""

data={
    "user":"",
    "passworld":""
}
params =request("post",login_url,data)




headers={

    "client":"middle",
    "Autoorization":"Bearer "
}




children_list=["花花","明明"]
"""
构建时间段
# 根据孩子获取到他的id
id+时间获取孩子图片
"""














