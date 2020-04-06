#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
# from copy import deepcopy as dpcp

# Current Dir
current_dir = os.path.dirname(os.path.abspath(__file__))
# current_dir = ''

# Task Name
taskname = 'general'

# 创建对象的基类
BaseModel = declarative_base()

# 初始化数据库连接
db_path = os.path.join(current_dir, ('spiderDB_'+taskname+'_new.sqlite'))
# print(db_path)
engine = db.create_engine('sqlite:///{}'.format(db_path))

# 创建DBSession类型
Session = sessionmaker(bind=engine)

# --------------------------------------------------------------------------------
# 将 db 分为 InfoDB 和 FileDB
# InfoDB 只存储信息
# FileDB 只存储文件
# --------------------------------------------------------------------------------


class DBPair(Base):
    """"""

    pass


# --------------------------------------------------------------------------------


# --------------------------------------------------------------------------------


# --------------------------------------------------------------------------------


# --------------------------------------------------------------------------------


class Home(Base):
    """home
    id
    name
    href
    partten_setings
    folder_name()
    """

    __tablename__ = "home"

    def __str__(self):
        return f"<home(name={self.name}, href={self.href})>"

    id = db.Column(db.Integer, nullable=False, primary_key=True)

    name = db.Column(db.String(200))
    href = db.Column(db.String(600))
    partten_setings = db.Column(db.Text, nullable=True)

    @classmethod
    def folder_name(cls):
        pass

    pass


# --------------------------------------------------------------------------------


class Album(Base):
    """album
    id
    title
    href
    token
    content
    meta
    total
    pics
    folder_name()
    download()
    state()
    export()
    """

    __tablename__ = "album"

    def __str__(self):
        return f"<album(title={self.title}, href={self.href})>"

    id = db.Column(db.Integer, nullable=False, primary_key=True)

    title = db.Column(db.String(200))
    href = db.Column(db.String(600))
    token = db.Column(db.String(200))
    content = db.Column(db.Text, nullable=True)
    meta = db.Column(db.Text, nullable=True)
    total = db.Column(db.Integer, nullable=True)

    pics = relationship("Pic", back_populates="album")

    @classmethod
    def folder_name(cls):
        pass

    @classmethod
    def download(cls):
        pass

    @classmethod
    def state(cls):
        pass

    @classmethod
    def export(cls):
        pass

    pass


# --------------------------------------------------------------------------------


class Pic(Base):
    """pic
    id
    order
    href
    origin_title
    origin_name
    album_id
    file
    file_id
    state
    file_name()
    download()
    export()
    """

    __tablename__ = "pic"

    def __str__(self):
        return f"<pic(href={self.href}, album={self.album.title})>"

    id = db.Column(db.Integer, nullable=False, primary_key=True)

    order = db.Column(db.Integer, nullable=True)
    href = db.Column(db.String(600))
    origin_title = db.Column(db.String(200), nullable=True)
    origin_name = db.Column(db.String(200), nullable=True)

    album_id = db.Column(db.Integer, ForeignKey("album.id"))
    file = relationship("File", back_populates="pic")
    file_id = db.Column(db.Integer, ForeignKey("file.id"))
    file_state = db.Column(Enum("未下载", "下载失败", "已下载"), ForeignKey("file.state"))

    @classmethod
    def file_name(cls):
        pass

    @classmethod
    def download(cls):
        pass

    @classmethod
    def export(cls):
        pass

    pass


# --------------------------------------------------------------------------------


class File(Base):
    """file
    id
    blob
    state
    pic_id
    download()
    export()
    """

    __tablename__ = "file"

    def __str__(self):
        return f"<file(href={self.pic.href}, state={self.state})>"

    id = db.Column(db.Integer, nullable=False, primary_key=True)

    blob = db.Column(db.LargeBinary(length=2**24))
    state = db.Column(Enum("未下载", "下载失败", "已下载"))

    pic = relationship("Pic", back_populates="file")
    pic_id = db.Column(db.Integer, ForeignKey("pic.id"))

    @classmethod
    def download(cls):
        pass

    @classmethod
    def export(cls):
        pass

    pass


# --------------------------------------------------------------------------------


def main():
    pass


# --------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
