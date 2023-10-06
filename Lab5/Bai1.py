import pyodbc

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=ADMIN-PC;'
                      'Database=QLSinhVien;'
                      'Trusted_Connection=yes;')



def close_connection(conn):
    if conn:
        conn.close()

def get_all_class():
    try:
        
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM LOP')
        records = cursor.fetchall()
        print(f"danh sách các lớp là")
        for row in records:
            print("+"*50)
            print("Mã lớp: ", row[0])
            print("Tên lớp: ", row[1])

        close_connection(conn)
    except(Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)

# def get_class_by_id(class_id):
#     try:
#         cursor = conn.cursor()

#         select_query = "select * from Lop where id = ?"
#         params = (class_id,)
#         cursor.execute(select_query, params)

#         record = cursor.fetchone()

#         print(f"Thông tin lớp có id = {class_id} là: ")
#         print("Mã lớp: ", record[0])
#         print("Tên lớp: ", record[1])

#         close_connection(conn)
#     except (Exception, pyodbc.Error) as error:
#         print("Đã có lỗi xảy ra khi thự thi. Thông tin lỗi: ", error)

# def insert_class(class_name):
#     try:
#         cursor = conn.cursor()

#         select_query = "Insert into Lop(TenLop) values ( ? )"
#         cursor.execute(select_query, (class_name,))

#         conn.commit()

#         print("Đã thêm thành công")

#         close_connection(conn)
#     except (Exception, pyodbc.Error) as error:
#         print("Đã có lỗi xảy ra khi thự thi. Thông tin lỗi: ", error)

# get_class_by_id(1)
get_all_class()