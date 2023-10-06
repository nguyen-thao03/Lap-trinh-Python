﻿CREATE DATABASE QLSinhVien

CREATE TABLE LOP(
	ID int NOT NULL PRIMARY KEY,
	TenLop nvarchar(20) NOT NULL)

CREATE TABLE SINHVIEN(
	ID int NOT NULL PRIMARY KEY,
	HoTen nvarchar(100) NOT NULL,
	MaLop int NULL)

INSERT LOP (ID, TenLop) VALUES (1, N'CTK43')
INSERT LOP (ID, TenLop) VALUES (2, N'CTK44A')
INSERT LOP (ID, TenLop) VALUES (3, N'CTK44B')
INSERT LOP (ID, TenLop) VALUES (4, N'CTK45A')

INSERT SINHVIEN (ID, HoTen, MaLop) VALUES (1, N'Trần Văn Thái wewr', 1)
INSERT SINHVIEN (ID, HoTen, MaLop) VALUES (2, N'Mai Thành Thân', 2)
INSERT SINHVIEN (ID, HoTen, MaLop) VALUES (3, N'Phạm Thanh Thảo', 2)
INSERT SINHVIEN (ID, HoTen, MaLop) VALUES (4, N'Trần Quốc Bảo Trung', 3)
INSERT SINHVIEN (ID, HoTen, MaLop) VALUES (5, N'Thái Thành Lam', 3)
INSERT SINHVIEN (ID, HoTen, MaLop) VALUES (6, N'Trần Văn Tám', 3)
INSERT SINHVIEN (ID, HoTen, MaLop) VALUES (7, N'Nguyễn Công Thành', 4)
INSERT SINHVIEN (ID, HoTen, MaLop) VALUES (8, N'Nguyễn Thị Lụa', 1)
INSERT SINHVIEN (ID, HoTen, MaLop) VALUES (9, N'Phan Thanh Nga', 1)
INSERT SINHVIEN (ID, HoTen, MaLop) VALUES (10, N'Trương Công Quyền', 4)
INSERT SINHVIEN (ID, HoTen, MaLop) VALUES (11, N'Võ Thị Sáu', 1)
INSERT SINHVIEN (ID, HoTen, MaLop) VALUES (12, N'Võ Tòng', 2)

select * from LOP
select * from SINHVIEN
select @@SERVERNAME

CREATE PROC InsertStudent
	@Id int,
	@HoTen nvarchar(100),
	@MaLop int
AS
BEGIN
	INSERT INTO SinhVien
	VALUES (@Id, @HoTen, @MaLop)
END

