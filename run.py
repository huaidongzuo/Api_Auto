# -*- coding: utf-8 -*-
# 运行接口测试用例
# author:hzuo

import pytest
import pytest_html

pytest.main(['test_cases/','--html=report/report.html',"--self-contained-html"])