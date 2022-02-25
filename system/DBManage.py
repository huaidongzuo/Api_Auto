# -*- coding: utf-8 -*-
# author:hzuo
# 封装数据库的操作

import sqlite3
import pymysql
from system.Log import Logger

sql_log = Logger('sql',log_name='sql.log')


class LiteDB:
    """
        封装sqlite3数据库
    """
    def __init__(self,db_path: str):
        self.__db_path = db_path
        self.__con = sqlite3.connect(self.__db_path)
        self.__con.row_factory = self.dict_factory
        self.cursor = self.__con.cursor()

    @staticmethod
    def dict_factory(cursor,row):
        d = {}
        for idx,col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def excute(self,dql:str):
        sql_log.logger.info(f"执行数据库语句: {dql}")
        self.cursor.execute(dql)


    def commit(self):
        """
        提交数据库的事务
        :return:
        """
        self.__con.commit()


    def __del__(self):
        """
        内存回收前关闭数据库的连接
        :return:
        """
        self.cursor.close()
        del self

    def into(self,table_name:str, keys:tuple,values:tuple):
        """
        执行数据库插入数据
        :param table_name:
        :param keys:
        :param values:
        :return:
        """

        dql = f"insert into {table_name} {keys} values {values}"
        self.excute(dql)
        self.commit()

    def query(self,dql):
        """
        执行数据库查询操作
        """

        self.excute(dql)
        return self.cursor.fetchall()
