import time
import pymysql

db_connfd = pymysql.connect(host='localhost', port=3306,
                            user='root', password='123456', db='TestDB')

db_cursor = db_connfd.cursor()

sql_select_1 = 'select s.* from Student s where s.s_id in (select s_id from StudentGrade sg where sg.c_id = 1522488232141389829 and sg.score = 98)'

create_index_1 = 'create index sg_c_id_index on StudentGrade(c_id)'


# if __name__ == '__main__':
#     try:
#         for _ in range(5):
#             start_time = time.process_time()
#             db_cursor.execute(sql_select_1)
#             end_time = time.process_time()
#             print(f'Time used: {end_time - start_time}')

#     except Exception as ex:
#         raise ex
#     else:
#         # print(f'Time used: {end_time - start_time}')

#         db_cursor.close()
#         db_connfd.close()
