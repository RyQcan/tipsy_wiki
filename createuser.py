from django.contrib.auth.models import User
import os
os.environ.update({"Django_settings_module":"config.settings"})
namelist = ['lintianxiang', 'jiaozhengang', 'liyanzhe', 'zhangdachuan',
            'fuyao', 'jinzhen', 'lihuaxin', 'lisirui', 'linjinxiu', 'huangxin',
            'wangxiaowei', 'wangyang', 'yangjiageng', 'zhanghanwen', 'zhangzundong',
            'leipengqun', 'liujiahao', 'wangxuwu']

for name in namelist:
    user = User.objects.create_user(name, '123@123.com', name)
