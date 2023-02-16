# import snowflake
import time
import pymysql
import random
import string
import traceback
from CommonDemo.MakeSnowflake import IdWorker

COURSE_RECORD_NUM = 100
STUDENT_RECORD_NUM = 70000
STUDENTGRADE_RECORD_NUM = 7000000

db_connfd = pymysql.connect(host='localhost', port=3306,
                            user='root', password='123456', db='TestDB')

db_cursor = db_connfd.cursor()


class SqlProcessClass:
    def __init__(self) -> None:
        self.IdWorker = IdWorker()
        self.CouIdPool = [self.IdWorker.get_id()
                          for _ in range(COURSE_RECORD_NUM)]
        self.StuIdPool = [self.IdWorker.get_id()
                          for _ in range(STUDENT_RECORD_NUM)]

    def createTableCourse(self):
        sql_createTable = 'create table Course(c_id bigint PRIMARY KEY, name varchar(10))'
        try:
            db_cursor.execute(sql_createTable)
        except pymysql.err.InternalError as ex:
            if '1050' in str(ex):
                db_cursor.execute('drop table Course')
            self.createTableCourse()
        else:
            db_connfd.commit()

    def createTableStudent(self):
        sql_createTable = 'create table Student(s_id bigint PRIMARY KEY, name varchar(10))'
        try:
            db_cursor.execute(sql_createTable)
        except pymysql.err.InternalError as ex:
            if '1050' in str(ex):
                db_cursor.execute('drop table Student')
            self.createTableStudent()
        else:
            db_connfd.commit()

    def createTableStudentGrade(self):
        sql_createTable = 'create table StudentGrade(sg_id bigint PRIMARY KEY, s_id bigint, c_id bigint, score int)'
        try:
            db_cursor.execute(sql_createTable)
        except pymysql.err.InternalError as ex:
            if '1050' in str(ex):
                db_cursor.execute('drop table StudentGrade')
            self.createTableStudentGrade()
        else:
            db_connfd.commit()

    def insertDataForTableCourse(self, record_count_: int, cursor_) -> None:
        for index in range(record_count_):
            try:
                insert_sql = f"insert into Course(c_id, name) values({self.CouIdPool[index]}, '{SqlProcessClass.get_random_name(5)}')"
                cursor_.execute(insert_sql)
            except Exception as ex:
                print(traceback.format_exc())
        db_connfd.commit()

    def insertDataForTableStudent(self, record_count_: int, cursor_) -> None:
        for index in range(record_count_):
            try:
                insert_sql = f"insert into Student(s_id, name) values({self.StuIdPool[index]}, '{SqlProcessClass.get_random_name(7)}')"
                cursor_.execute(insert_sql)
            except Exception as ex:
                print(traceback.format_exc())
        db_connfd.commit()

    def insertDataForTableStudentGrade(self, record_count_: int, cursor_) -> None:
        for _ in range(record_count_):
            try:
                insert_sql = f"insert into StudentGrade(sg_id, s_id, c_id, score) values({self.IdWorker.get_id()}, '{self.StuIdPool[random.randint(0, STUDENT_RECORD_NUM - 1)]}', '{self.CouIdPool[random.randint(0, COURSE_RECORD_NUM - 1)]}', {random.randint(0, 100)})"
                cursor_.execute(insert_sql)
            except Exception as ex:
                print(traceback.format_exc())
        db_connfd.commit()

    @staticmethod
    def get_random_name(randomlength: int):
        """
        生成一个指定长度的随机字符串
        """

        str_list = [random.choice(string.ascii_letters)
                    for _ in range(randomlength)]
        return ''.join(str_list)


if __name__ == '__main__':
    sql_process = SqlProcessClass()
    start_time = time.process_time()
    sql_process.createTableCourse()
    sql_process.insertDataForTableCourse(
        record_count_=COURSE_RECORD_NUM, cursor_=db_cursor)
    end_time = time.process_time()
    print(
        f'create table Course&insert data to Course time used: {end_time - start_time}')

    start_time = time.process_time()
    sql_process.createTableStudent()
    sql_process.insertDataForTableStudent(
        record_count_=STUDENT_RECORD_NUM, cursor_=db_cursor)
    end_time = time.process_time()
    print(
        f'create table Student&insert data to Student time used: {end_time - start_time}')

    start_time = time.process_time()
    sql_process.createTableStudentGrade()
    sql_process.insertDataForTableStudentGrade(
        record_count_=STUDENTGRADE_RECORD_NUM, cursor_=db_cursor)
    end_time = time.process_time()
    print(
        f'create table StudentGrade&insert data to StudentGrade time used: {end_time - start_time}')

    db_cursor.close()
    db_connfd.close()
