import pyodbc
import matplotlib.pyplot as plt
from numpy.random import rand
import numpy
import pandas as pd
from sklearn.linear_model import LinearRegression
from numpy import linspace, matrix
from sklearn.metrics import mean_squared_error

def mhsftk(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS mhsftk FROM dbo.Mahasiswa WHERE FakultasMhs = 'Fakultas Teknologi Kelautan (FTK)'")
    while 1:
        hasil2 = cursor.fetchone()
        if not hasil2:
            break
        return hasil2.mhsftk

def mhsftslk(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS mhsftslk FROM dbo.Mahasiswa WHERE FakultasMhs = 'Fakultas Teknik Sipil, Lingkungan, dan Kebumian (FTSLK)'")
    while 1:
        hasil2 = cursor.fetchone()
        if not hasil2:
            break
        return hasil2.mhsftslk

def mhsfti(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS mhsfti FROM dbo.Mahasiswa WHERE FakultasMhs = 'Fakultas Teknologi Industri (FTI)'")
    while 1:
        hasil2 = cursor.fetchone()
        if not hasil2:
            break
        return hasil2.mhsfti

def mhsfia(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS mhsfia FROM dbo.Mahasiswa WHERE FakultasMhs = 'Fakultas Ilmu Alam (FIA)'")
    while 1:
        hasil2 = cursor.fetchone()
        if not hasil2:
            break
        return hasil2.mhsfia

def mhsftik(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS mhsftik FROM dbo.Mahasiswa WHERE FakultasMhs = 'Fakultas Teknologi Informasi dan Komunikasi (FTIK)'")
    while 1:
        hasil2 = cursor.fetchone()
        if not hasil2:
            break
        return hasil2.mhsftik
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Batas Bawah per fakultas, Batas Atas per jurusan di FTK
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def ftkkpl(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS ftkkpl FROM dbo.Mahasiswa WHERE JurusanMhs = 'Teknik Perkapalan'")
    while 1:
        hasil2 = cursor.fetchone()
        if not hasil2:
            break
        return hasil2.ftkkpl
        #print("Jumlah Mahasiswa Teknik Perkapalan yang menggunakan Share ITS sebanyak " + str(hasil2.ftkkpl) + " mahasiswa")

def ftklaut(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS ftklaut FROM dbo.Mahasiswa WHERE JurusanMhs = 'Teknik Kelautan'")
    while 1:
        hasil2 = cursor.fetchone()
        if not hasil2:
            break
        return hasil2.ftklaut
        #print("Jumlah Mahasiswa Teknik Kelautan yang menggunakan Share ITS sebanyak " + str(hasil2.ftklaut) + " mahasiswa")

def ftksiskal(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS ftksiskal FROM dbo.Mahasiswa WHERE JurusanMhs = 'Teknik Sistem Perkapalan'")
    while 1:
        hasil2 = cursor.fetchone()
        if not hasil2:
            break
        return hasil2.ftksiskal
        #print("Jumlah Mahasiswa Teknik Sistem Perkapalan yang menggunakan Share ITS sebanyak " + str(hasil2.ftksiskal) + " mahasiswa")

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Batas Bawah per jurusan FTK, Batas Atas per jurusan di FIA
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def fiabio(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS fiabio FROM dbo.Mahasiswa WHERE JurusanMhs = 'Biologi'")
    while 1:
        hasil2 = cursor.fetchone()
        if not hasil2:
            break
        return hasil2.fiabio

def fiaphy(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS fiaphy FROM dbo.Mahasiswa WHERE JurusanMhs = 'Fisika'")
    while 1:
        hasil2 = cursor.fetchone()
        if not hasil2:
            break
        return hasil2.fiaphy

def fiache(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS fiache FROM dbo.Mahasiswa WHERE JurusanMhs = 'Kimia'")
    while 1:
        hasil2 = cursor.fetchone()
        if not hasil2:
            break
        return hasil2.fiache

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Batas Bawah per jurusan FIA
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def ftikif(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS ftikif FROM dbo.Mahasiswa WHERE JurusanMhs = 'Informatika'")
    while 1:
        hasil2 = cursor.fetchone()
        if not hasil2:
            break
        return hasil2.ftikif

def ftiksi(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS ftiksi FROM dbo.Mahasiswa WHERE JurusanMhs = 'Sistem Informasi'")
    while 1:
        hasil2 = cursor.fetchone()
        if not hasil2:
            break
        return hasil2.ftiksi

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Batas Bawah per jurusan FTIK
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def angkatan18(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS angkatan18 FROM Mahasiswa WHERE NamaMhs LIKE '% [0-9][0-9][0-9][0-9]18%'")
    while 1:
        hasil2 = cursor.fetchone()
        if not hasil2:
            break
        return hasil2.angkatan18

def angkatan17(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS angkatan17 FROM Mahasiswa WHERE NamaMhs LIKE '% [0-9][0-9][0-9][0-9]17%' OR NamaMhs LIKE '% [0-9][0-9]17%'")
    while 1:
        hasil2 = cursor.fetchone()
        if not hasil2:
            break
        return hasil2.angkatan17

def angkatan16(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS angkatan16 FROM Mahasiswa WHERE NamaMhs LIKE '% [0-9][0-9][0-9][0-9]16%' OR NamaMhs LIKE '% [0-9][0-9]16%'")
    while 1:
        hasil2 = cursor.fetchone()
        if not hasil2:
            break
        return hasil2.angkatan16

def angkatan15(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS angkatan15 FROM Mahasiswa WHERE NamaMhs LIKE '% [0-9][0-9]15%' OR NamaMhs LIKE '% [0-9][0-9][0-9][0-9]15%'")
    while 1:
        hasil2 = cursor.fetchone()
        if not hasil2:
            break
        return hasil2.angkatan15

def angkatan14(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS angkatan14 FROM Mahasiswa WHERE NamaMhs LIKE '% [0-9][0-9]14%' OR NamaMhs LIKE '% [0-9][0-9][0-9][0-9]14%'")
    while 1:
        hasil2 = cursor.fetchone()
        if not hasil2:
            break
        return hasil2.angkatan14

def akses(conn):
    cursor = conn.cursor()
    
    cursor.execute("SELECT top 10 COUNT(MatkulMhs) AS jumlahakses FROM Mahasiswa GROUP BY NamaMhs ORDER BY jumlahakses DESC")
    hasil = cursor.fetchall()
    jumlahakses1 = []
    for row in hasil:
        jumlahakses1.append(row[0])
    return [[i] for i in jumlahakses1]

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Batas atas FTI per tahun akses
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def fti2014(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS FTI2014 FROM Mahasiswa WHERE Last_AccessMhs LIKE '%2014%' AND FakultasMhs LIKE '%Industri%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.FTI2014

def fti2015(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS FTI2015 FROM Mahasiswa WHERE Last_AccessMhs LIKE '%2015%' AND FakultasMhs LIKE '%Industri%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.FTI2015

def fti2016(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS FTI2016 FROM Mahasiswa WHERE Last_AccessMhs LIKE '%2016%' AND FakultasMhs LIKE '%Industri%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.FTI2016

def fti2017(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS FTI2017 FROM Mahasiswa WHERE Last_AccessMhs LIKE '%2017%' AND FakultasMhs LIKE '%Industri%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.FTI2017

def fti2018(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS FTI2018 FROM Mahasiswa WHERE Last_AccessMhs LIKE '%2018%' AND FakultasMhs LIKE '%Industri%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.FTI2018

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Batas bawah FTI per tahun akses
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def ftk2014(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS FTK2014 FROM Mahasiswa WHERE Last_AccessMhs LIKE '%2014%' AND FakultasMhs LIKE '%Kelautan%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.FTK2014

def ftk2015(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS FTK2015 FROM Mahasiswa WHERE Last_AccessMhs LIKE '%2015%' AND FakultasMhs LIKE '%Kelautan%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.FTK2015

def ftk2016(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS FTK2016 FROM Mahasiswa WHERE Last_AccessMhs LIKE '%2016%' AND FakultasMhs LIKE '%Kelautan%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.FTK2016

def ftk2017(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS FTK2017 FROM Mahasiswa WHERE Last_AccessMhs LIKE '%2017%' AND FakultasMhs LIKE '%Kelautan%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.FTK2017

def ftk2018(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS FTK2018 FROM Mahasiswa WHERE Last_AccessMhs LIKE '%2018%' AND FakultasMhs LIKE '%Kelautan%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.FTK2018

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Batas bawah FTK per tahun akses
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def ftik2014(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS FTIK2014 FROM Mahasiswa WHERE Last_AccessMhs LIKE '%2014%' AND FakultasMhs LIKE '%Informasi%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.FTIK2014

def ftik2015(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS FTIK2015 FROM Mahasiswa WHERE Last_AccessMhs LIKE '%2015%' AND FakultasMhs LIKE '%Informasi%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.FTIK2015

def ftik2016(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS FTIK2016 FROM Mahasiswa WHERE Last_AccessMhs LIKE '%2016%' AND FakultasMhs LIKE '%Informasi%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.FTIK2016

def ftik2017(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS FTIK2017 FROM Mahasiswa WHERE Last_AccessMhs LIKE '%2017%' AND FakultasMhs LIKE '%Informasi%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.FTIK2017

def ftik2018(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS FTIK2018 FROM Mahasiswa WHERE Last_AccessMhs LIKE '%2018%' AND FakultasMhs LIKE '%Informasi%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.FTIK2018

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Batas bawah FTIK per tahun akses
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def fia2014(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS FIA2014 FROM Mahasiswa WHERE Last_AccessMhs LIKE '%2014%' AND FakultasMhs LIKE '%Alam%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.FIA2014

def fia2015(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS FIA2015 FROM Mahasiswa WHERE Last_AccessMhs LIKE '%2015%' AND FakultasMhs LIKE '%Alam%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.FIA2015

def fia2016(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS FIA2016 FROM Mahasiswa WHERE Last_AccessMhs LIKE '%2016%' AND FakultasMhs LIKE '%Alam%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.FIA2016

def fia2017(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS FIA2017 FROM Mahasiswa WHERE Last_AccessMhs LIKE '%2017%' AND FakultasMhs LIKE '%Alam%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.FIA2017

def fia2018(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS FIA2018 FROM Mahasiswa WHERE Last_AccessMhs LIKE '%2018%' AND FakultasMhs LIKE '%Alam%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.FIA2018

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Batas bawah FIA per tahun akses
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def ftslk2014(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS FTSLK2014 FROM Mahasiswa WHERE Last_AccessMhs LIKE '%2014%' AND FakultasMhs LIKE '%Sipil%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.FTSLK2014

def ftslk2015(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS FTSLK2015 FROM Mahasiswa WHERE Last_AccessMhs LIKE '%2015%' AND FakultasMhs LIKE '%Sipil%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.FTSLK2015

def ftslk2016(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS FTSLK2016 FROM Mahasiswa WHERE Last_AccessMhs LIKE '%2016%' AND FakultasMhs LIKE '%Sipil%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.FTSLK2016

def ftslk2017(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS FTSLK2017 FROM Mahasiswa WHERE Last_AccessMhs LIKE '%2017%' AND FakultasMhs LIKE '%Sipil%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.FTSLK2017

def ftslk2018(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS FTSLK2018 FROM Mahasiswa WHERE Last_AccessMhs LIKE '%2018%' AND FakultasMhs LIKE '%Sipil%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.FTSLK2018

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Batas bawah FTSLK per tahun akses
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def ftiang2015(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS ftiang2015 FROM Mahasiswa WHERE (NamaMhs LIKE '% [0-9][0-9][0-9][0-9]15%' OR NamaMhs LIKE '% [0-9][0-9]15%') AND FakultasMhs LIKE '%Industri%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.ftiang2015

def ftiang2016(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS ftiang2016 FROM Mahasiswa WHERE (NamaMhs LIKE '% [0-9][0-9][0-9][0-9]16%' OR NamaMhs LIKE '% [0-9][0-9]16%') AND FakultasMhs LIKE '%Industri%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.ftiang2016

def ftiang2017(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS ftiang2017 FROM Mahasiswa WHERE (NamaMhs LIKE '% [0-9][0-9][0-9][0-9]17%' OR NamaMhs LIKE '% [0-9][0-9]17%') AND FakultasMhs LIKE '%Industri%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.ftiang2017

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Batas bawah FTI per angkatan
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def ftkang2015(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS ftkang2015 FROM Mahasiswa WHERE (NamaMhs LIKE '% [0-9][0-9][0-9][0-9]15%' OR NamaMhs LIKE '% [0-9][0-9]15%') AND FakultasMhs LIKE '%Kelautan%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.ftkang2015

def ftkang2016(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS ftkang2016 FROM Mahasiswa WHERE (NamaMhs LIKE '% [0-9][0-9][0-9][0-9]16%' OR NamaMhs LIKE '% [0-9][0-9]16%') AND FakultasMhs LIKE '%Kelautan%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.ftkang2016

def ftkang2017(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS ftkang2017 FROM Mahasiswa WHERE (NamaMhs LIKE '% [0-9][0-9][0-9][0-9]17%' OR NamaMhs LIKE '% [0-9][0-9]17%') AND FakultasMhs LIKE '%Kelautan%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.ftkang2017

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Batas bawah FTK per angkatan
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def ftikang2015(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS ftikang2015 FROM Mahasiswa WHERE (NamaMhs LIKE '% [0-9][0-9][0-9][0-9]15%' OR NamaMhs LIKE '% [0-9][0-9]15%') AND FakultasMhs LIKE '%Informasi%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.ftikang2015

def ftikang2016(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS ftikang2016 FROM Mahasiswa WHERE (NamaMhs LIKE '% [0-9][0-9][0-9][0-9]16%' OR NamaMhs LIKE '% [0-9][0-9]16%') AND FakultasMhs LIKE '%Informasi%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.ftikang2016

def ftikang2017(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS ftikang2017 FROM Mahasiswa WHERE (NamaMhs LIKE '% [0-9][0-9][0-9][0-9]17%' OR NamaMhs LIKE '% [0-9][0-9]17%') AND FakultasMhs LIKE '%Informasi%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.ftikang2017

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Batas bawah FTIK per angkatan
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def fiaang2015(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS fiaang2015 FROM Mahasiswa WHERE (NamaMhs LIKE '% [0-9][0-9][0-9][0-9]15%' OR NamaMhs LIKE '% [0-9][0-9]15%') AND FakultasMhs LIKE '%Alam%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.fiaang2015

def fiaang2016(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS fiaang2016 FROM Mahasiswa WHERE (NamaMhs LIKE '% [0-9][0-9][0-9][0-9]16%' OR NamaMhs LIKE '% [0-9][0-9]16%') AND FakultasMhs LIKE '%Alam%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.fiaang2016

def fiaang2017(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS fiaang2017 FROM Mahasiswa WHERE (NamaMhs LIKE '% [0-9][0-9][0-9][0-9]17%' OR NamaMhs LIKE '% [0-9][0-9]17%') AND FakultasMhs LIKE '%Alam%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.fiaang2017

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Batas bawah FIA per angkatan
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def ftslkang2015(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS ftslkang2015 FROM Mahasiswa WHERE (NamaMhs LIKE '% [0-9][0-9][0-9][0-9]15%' OR NamaMhs LIKE '% [0-9][0-9]15%') AND FakultasMhs LIKE '%Sipil%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.ftslkang2015

def ftslkang2016(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS ftslkang2016 FROM Mahasiswa WHERE (NamaMhs LIKE '% [0-9][0-9][0-9][0-9]16%' OR NamaMhs LIKE '% [0-9][0-9]16%') AND FakultasMhs LIKE '%Sipil%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.ftslkang2016

def ftslkang2017(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS ftslkang2017 FROM Mahasiswa WHERE (NamaMhs LIKE '% [0-9][0-9][0-9][0-9]17%' OR NamaMhs LIKE '% [0-9][0-9]17%') AND FakultasMhs LIKE '%Sipil%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.ftslkang2017

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Batas bawah FTSLK per angkatan
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def gambar():
    #Figure 1
    plt.figure(1)
    fakultas = ['FTK', 'FTSLK', 'FTI', 'FIA', 'FTIK']
    hasilftk = mhsftk(conn)
    hasilftslk = mhsftslk(conn)
    hasilfti = mhsfti(conn)
    hasilfia = mhsfia(conn)
    hasilftik = mhsftik(conn)

    jumlahfakultas = [hasilftk, hasilftslk, hasilfti, hasilfia, hasilftik]

    print("FTK = " +str(hasilftk))
    print("FTSLK = " +str(hasilftslk))
    print("FTI = " +str(hasilfti))
    print("FIA = " +str(hasilfia))
    print("FTIK = " +str(hasilftik))

    plt.barh(fakultas, jumlahfakultas)
    for i, v in enumerate(jumlahfakultas):
        plt.text(v + 3, i + .25, str(v), color='blue', va='center', fontweight='bold')
    plt.xlabel('Fakultas', fontsize=5)
    plt.ylabel('Jumlah Mahasiswa', fontsize=5)
    plt.title("Jumlah mahasiswa yang mengakses shareits berdasarkan fakultas")

    #Figure 2
    plt.figure(2)
    jurusanftk = ['Teknik Perkapalan', 'Teknik Kelautan', 'Teknik Sistem Perkapalan']
    hasilkpl = ftkkpl(conn)
    hasillaut = ftklaut(conn)
    hasilsiskal = ftksiskal(conn)

    jumlahftk = [hasilkpl, hasillaut, hasilsiskal]

    print("Teknik Perkapalan = " +str(hasilkpl))
    print("Teknik Kelautan = " +str(hasillaut))
    print("Teknik Sistem Perkapalan = " +str(hasilsiskal))

    plt.barh(jurusanftk, jumlahftk)
    for i, v in enumerate(jumlahftk):
        plt.text(v + 3, i + .25, str(v), color='blue', va='center', fontweight='bold')
    plt.xlabel('Jurusan', fontsize=5)
    plt.ylabel('Jumlah Mahasiswa', fontsize=5)
    plt.title("Jumlah mahasiswa pada masing-masing jurusan di FTK yang mengakses shareits")

    #Figure 3
    plt.figure(3)
    jurusanfia = ['Biologi', 'Fisika', 'Kimia']
    hasilbio = fiabio(conn)
    hasilphy = fiaphy(conn)
    hasilche = fiache(conn)

    jumlahfia = [hasilbio, hasilphy, hasilche]

    print("Biologi = " +str(hasilbio))
    print("Fisika = " +str(hasilphy))
    print("Kimia = " +str(hasilche))
    
    plt.barh(jurusanfia, jumlahfia)
    for i, v in enumerate(jumlahfia):
        plt.text(v + 3, i + .25, str(v), color='blue', va='center', fontweight='bold')
    plt.xlabel('Jurusan', fontsize=5)
    plt.ylabel('Jumlah Mahasiswa', fontsize=5)
    plt.title("Jumlah mahasiswa pada masing-masing jurusan di FIA yang mengakses shareits")

    #Figure 4
    plt.figure(4)
    angkatan = ['2014', '2015', '2016', '2017', '2018']

    hasil14 = angkatan14(conn)
    hasil15 = angkatan15(conn)
    hasil16 = angkatan16(conn)
    hasil17 = angkatan17(conn)
    hasil18 = angkatan18(conn)

    jumlahangkatan = [hasil14, hasil15, hasil16, hasil17, hasil18]
   

    plt.barh(angkatan, jumlahangkatan)
    for i, v in enumerate(jumlahangkatan):
        plt.text(v + 3, i + .25, str(v), color='blue', va='center', fontweight='bold')
    plt.xlabel('Angkatan', fontsize=5)
    plt.ylabel('Jumlah Mahasiswa per Angkatan', fontsize=5)
    plt.title("Jumlah mahasiswa per angkatan yang mengakses shareits")

    #Figure 5
    plt.figure(5)
    smbx = ['2014', '2015', '2016', '2017', '2018']
    ftipt = [fti2014(conn), fti2015(conn), fti2016(conn), fti2017(conn), fti2018(conn)]
    ftkpt = [ftk2014(conn), ftk2015(conn), ftk2016(conn), ftk2017(conn), ftk2018(conn)]
    ftikpt = [ftik2014(conn), ftik2015(conn), ftik2016(conn), ftik2017(conn), ftik2018(conn)]
    fiapt = [fia2014(conn), fia2015(conn), fia2016(conn), fia2017(conn), fia2018(conn)]
    ftslkpt = [ftslk2014(conn), ftslk2015(conn), ftslk2016(conn), ftslk2017(conn), ftslk2018(conn)]
    plt.gca().set_color_cycle(['red', 'blue', 'gray', 'green', 'black'])

    plt.plot(smbx, ftipt)
    plt.plot(smbx, ftkpt)
    plt.plot(smbx, ftikpt)
    plt.plot(smbx, fiapt)
    plt.plot(smbx, ftslkpt)

    plt.title("Jumlah Mahasiswa Yang Mengakses Share ITS Per Tahun Akses(2014-2018) Per Fakultas")
    plt.legend(['FTI', 'FTK', 'FTIK', 'FIA', 'FTSLK'], loc='upper left')

    #Figure 6
    plt.figure(6)
    sumbux = ['2015', '2016', '2017']
    ftipang = [ftiang2015(conn), ftiang2016(conn), ftiang2017(conn)]
    ftkpang = [ftkang2015(conn), ftkang2016(conn), ftkang2017(conn)]
    ftikpang = [ftikang2015(conn), ftikang2016(conn), ftikang2017(conn)]
    fiapang = [fiaang2015(conn), fiaang2016(conn), fiaang2017(conn)]
    ftslkpang = [ftslkang2015(conn), ftslkang2016(conn), ftslkang2017(conn)]
    plt.gca().set_color_cycle(['red', 'blue', 'gray', 'green', 'black'])

    plt.plot(sumbux, ftipang)
    plt.plot(sumbux, ftkpang)
    plt.plot(sumbux, ftikpang)
    plt.plot(sumbux, fiapang)
    plt.plot(sumbux, ftslkpang)

    plt.title("Jumlah Mahasiswa Yang Mengakses Share ITS Per Angkatan(2015-2017) Per Fakultas")
    plt.legend(['FTI', 'FTK', 'FTIK', 'FIA', 'FTSLK'], loc='upper left')
    
    plt.show()

def rand():
    hasilrand = numpy.random.uniform(low=3.5, high=4.0, size=(10,1))
    return hasilrand

conn = pyodbc.connect('Driver={SQL Server};Server=MSI;Database=datashareitsacid;Trusted_Connection=yes;')

#print(akses(conn))
#print(akses(conn))

x = akses(conn) # explanatory variable

gpa = rand() # depentend variable

print(x)
print(gpa)

linreg = LinearRegression()

linreg.fit(x,gpa)

xx = linspace(7,28,400)

plt.plot(x,gpa,'o',xx,linreg.predict(matrix(xx).T),'--r')

print mean_squared_error(linreg.predict(x),gpa)

plt.show()

gambar()
conn.close()
