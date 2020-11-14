---
name: 后端接口文档详细说明
path: ./README.md
create-time: 2020-11-10-14-29
---

### 全部数据获取接口

------



### 基础盘信息获取接口

- 接口名称
  - getbase/
- 接口返回的数据
  - code
  - message
  - data
    - 存储序列化之后的数据库数据信息， 
    - 字段有： id, file_name, file_path, table_name, is_delete

### 搜索接口

- 接口名称
  - 未定
- 接口需要传入的数据
  - search_name
    - 要查询的数据的名称
    - 可以为空
    - 数据类型为str
  - file_type
    - 要查询的文件的类型
    - 可以为空
  - file_size
    - 要查询的文件的大小范围
    - 可以为空， 也可以只有一个
    - 传入的数据类型为tuple类型
  - file_path
    - 要查询的文件的限定范围
    - 可以为空，也可以选择多个
    - 传入的数据类型为元组类型
    - 当为空时， 将会默认搜索所有盘
- 返回的数据字段：
  - file_name     文件名
  - file_type       文件类型
  - file_size        文件类型
  - file_path      文件地址
  - file_create_time      文件创建时间
  - file_update_time     文件修改时间
  - file_video_length     视频时长
  - file_label      文件标签

### 饼图数据获取接口（基础盘占用空间对比）

- 接口名称
  - get_data_size/
- 接口返回的数据
  - code
  - message
  - data
    - 盘名称
    - 盘中所有数据的大小的总和
- 返回数据的字段
  - 000000
  - driving
  - parking
  - radar
  - video
  - 这五个字段对应的值为五个总文件夹的占用空间大小

### 饼图数据获取接口（基础盘文件数量对比）

- 接口名称
  - get_data_sum/
- 接口返回的数据
  - code
  - message
  - data
    - 盘名称
    - 盘中所有数据的总数量
- 返回数据的字段
  - 000000
  - driving
  - parking
  - radar
  - video
  - 这五个字段对应的值为分支文件的总数量

### 标签创建接口

- 接口名称
  - createlabel/
- 接口需要传入的数据
  - label_name   要创建的新的标签的名字
- 接口返回的数据
  - code
  - message

