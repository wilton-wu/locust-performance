# -*- coding: utf-8 -*-

import sys
from os.path import pardir, sep
sys.path.append(pardir + sep)
import time
import itertools
from locust import HttpLocust, TaskSet
from common import log
from business.contract import Contract
#from business.project import Project
#from business.task import Task


'''
合同、项目、任务

变量保持不变：
1. 数据库表数据保持一致
contracts、projects、tasks表数据条数保持一致(设置成1000条)
2. 接口请求后返回的数据等于10条(limit=10&page=1)
'''


class UserBehavior(TaskSet):
    
        
    def on_start(self):
        counter = itertools.count(1)
        log_name_format = time.strftime("_%Y%m%d%H%M%S", time.localtime()) + '.log'
        log_path = __file__.replace('.py', log_name_format)
        log.append_file_logger(self, log_path, counter)
        
    #tasks = {Contract: 10, Project: 10, Task: 10}
    tasks = {Contract}
    
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 10000