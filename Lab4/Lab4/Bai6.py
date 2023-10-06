from tkinter import *
from tkinter import ttk

root = Tk()
root.configure(background='light blue')
root.title("Đăng kí học phần")
root.geometry("450x300")
#tao Form label
heading = Label(root, text="THÔNG TIN ĐĂNG KÝ HỌC PHẦN", bg="light blue", font=30)
numbers = Label(root, text="Mã số sinh viên", bg="light blue")
fullname = Label(root, text="Họ tên", bg="light blue")
daytime = Label(root, text="Ngày sinh", bg="light blue")
email = Label(root, text="Email", bg="light blue")
phone = Label(root, text="Số điện thoại", bg="light blue")
semester = Label(root, text="Học kỳ", bg="light blue")
year = Label(root, text="Năm học", bg="light blue")
choose_subjects = Label(root, text="Chọn môn học", bg="light blue")
cb_1 = Checkbutton(root, text="Lập trình Python", bg="light blue")
cb_3 = Checkbutton(root, text="Công nghệ phần mềm", bg="light blue")
cb_2 = Checkbutton(root, text="Lập trình Java", bg="light blue")
cb_4 = Checkbutton(root, text="Phát triển ứng dụng web", bg="light blue")
register = Button(root, text="Đăng ký", fg="white", bg="light grey")
cancel = Button(root, text="Thoát", fg="white", bg="light grey")
   
#hien
heading.grid(row=0, column=1)
numbers.grid(row=1, column=0)
fullname.grid(row=2, column=0)
daytime.grid(row=3, column=0)
email.grid(row=4, column=0)
phone.grid(row=5, column=0)
semester.grid(row=6, column=0)
year.grid(row=7, column=0)
choose_subjects.grid(row=8, column=0)
cb_1.grid(row=8, column=1)
cb_2.grid(row=9, column=1)
cb_3.grid(row=8, column=2)
cb_4.grid(row=9, column=2)
register.grid(row=10, column= 1)
cancel.grid(row=10, column=2)

   
# tao box
numbers_field = Entry(root)
name_field = Entry(root)
daytime_field = Entry(root)
email_field = Entry(root)
phone_field = Entry(root)
semester_field = Entry(root)
year_field = ttk.Combobox(root)

#ds nam hoc trong combobox
year_field['values'] =('2022-2023', '2023-2024','2024-2025')
year_field.current()
#
numbers_field.grid(row=1, column=1, ipadx="100")
name_field.grid(row=2, column=1, ipadx="100")
daytime_field.grid(row=3, column=1, ipadx="100")
email_field.grid(row=4, column=1, ipadx="100")
phone_field.grid(row=5, column=1, ipadx="100")
semester_field.grid(row=6, column=1, ipadx="100")
year_field.grid(row=7, column=1, ipadx="92")
choose_subjects.grid(row=8, column=0, ipadx="0")
cb_1.grid(row=8, column=1, ipadx="0")

root.mainloop()