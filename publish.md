# binlogdispatch
binlog增量事件监听包
## 安装包发布工具
* python -m pip install --user --upgrade setuptools wheel *
* python -m pip install --user --upgrade twine *

## 生成python包命令
* python setup.py sdist bdist_wheel *
## 发布python包
* twine upload dist/* *
