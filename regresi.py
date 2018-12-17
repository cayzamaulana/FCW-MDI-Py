import pyodbc
import matplotlib.pyplot as plt
from numpy.random import rand
import numpy
import pandas as pd
from sklearn.linear_model import LinearRegression
from numpy import linspace, matrix
from sklearn.metrics import mean_squared_error

def fiaang2013(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS fia2013 FROM Mahasiswa WHERE NamaMhs LIKE '% [0-9][0-9]13%' AND FakultasMhs LIKE '%Alam%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.fia2013

def fiaang2014(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS fia2014 FROM Mahasiswa WHERE NamaMhs LIKE '% [0-9][0-9]14%' OR NamaMhs LIKE '% [0-9][0-9][0-9][0-9]14%' AND FakultasMhs LIKE '%Alam%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.fia2014

def fiaang2015(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS fia2015 FROM Mahasiswa WHERE NamaMhs LIKE '% [0-9][0-9]15%' OR NamaMhs LIKE '% [0-9][0-9][0-9][0-9]15%' AND FakultasMhs LIKE '%Alam%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.fia2015

def fiaang2016(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS fia2016 FROM Mahasiswa WHERE NamaMhs LIKE '% [0-9][0-9]16%' OR NamaMhs LIKE '% [0-9][0-9][0-9][0-9]16%' AND FakultasMhs LIKE '%Alam%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.fia2016
'''''''''''''''''''''
Batas bawah fia
'''''''''''''''''''''

def ftiang2013(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS fti2013 FROM Mahasiswa WHERE NamaMhs LIKE '% [0-9][0-9]13%' AND FakultasMhs LIKE '%Industri%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.fti2013

def ftiang2014(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS fti2014 FROM Mahasiswa WHERE NamaMhs LIKE '% [0-9][0-9]14%' OR NamaMhs LIKE '% [0-9][0-9][0-9][0-9]14%' AND FakultasMhs LIKE '%Industri%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.fti2014

def ftiang2015(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS fti2015 FROM Mahasiswa WHERE NamaMhs LIKE '% [0-9][0-9]15%' OR NamaMhs LIKE '% [0-9][0-9][0-9][0-9]15%' AND FakultasMhs LIKE '%Industri%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.fti2015

def ftiang2016(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS fti2016 FROM Mahasiswa WHERE NamaMhs LIKE '% [0-9][0-9]16%' OR NamaMhs LIKE '% [0-9][0-9][0-9][0-9]16%' AND FakultasMhs LIKE '%Industri%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.fti2016

'''''''''''''''''''''
Batas bawah fti
'''''''''''''''''''''

def ftikang2013(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS ftik2013 FROM Mahasiswa WHERE NamaMhs LIKE '% [0-9][0-9]13%' AND FakultasMhs LIKE '%Informasi%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.ftik2013

def ftikang2014(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS ftik2014 FROM Mahasiswa WHERE NamaMhs LIKE '% [0-9][0-9]14%' OR NamaMhs LIKE '% [0-9][0-9][0-9][0-9]14%' AND FakultasMhs LIKE '%Informasi%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.ftik2014

def ftikang2015(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS ftik2015 FROM Mahasiswa WHERE NamaMhs LIKE '% [0-9][0-9]15%' OR NamaMhs LIKE '% [0-9][0-9][0-9][0-9]15%' AND FakultasMhs LIKE '%Informasi%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.ftik2015

def ftikang2016(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS ftik2016 FROM Mahasiswa WHERE NamaMhs LIKE '% [0-9][0-9]16%' OR NamaMhs LIKE '% [0-9][0-9][0-9][0-9]16%' AND FakultasMhs LIKE '%Informasi%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.ftik2016

'''''''''''''''''''''
Batas bawah ftik
'''''''''''''''''''''

def ftslkang2013(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS ftslk2013 FROM Mahasiswa WHERE NamaMhs LIKE '% [0-9][0-9]13%' AND FakultasMhs LIKE '%Sipil%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.ftslk2013

def ftslkang2014(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS ftslk2014 FROM Mahasiswa WHERE NamaMhs LIKE '% [0-9][0-9]14%' OR NamaMhs LIKE '% [0-9][0-9][0-9][0-9]14%' AND FakultasMhs LIKE '%Sipil%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.ftslk2014

def ftslkang2015(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS ftslk2015 FROM Mahasiswa WHERE NamaMhs LIKE '% [0-9][0-9]15%' OR NamaMhs LIKE '% [0-9][0-9][0-9][0-9]15%' AND FakultasMhs LIKE '%Sipil%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.ftslk2015

def ftslkang2016(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS ftslk2016 FROM Mahasiswa WHERE NamaMhs LIKE '% [0-9][0-9]16%' OR NamaMhs LIKE '% [0-9][0-9][0-9][0-9]16%' AND FakultasMhs LIKE '%Sipil%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.ftslk2016

'''''''''''''''''''''
Batas bawah ftslk
'''''''''''''''''''''

def ftkang2013(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS ftk2013 FROM Mahasiswa WHERE NamaMhs LIKE '% [0-9][0-9]13%' AND FakultasMhs LIKE '%Kelautan%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.ftk2013

def ftkang2014(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS ftk2014 FROM Mahasiswa WHERE NamaMhs LIKE '% [0-9][0-9]14%' OR NamaMhs LIKE '% [0-9][0-9][0-9][0-9]14%' AND FakultasMhs LIKE '%Kelautan%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.ftk2014

def ftkang2015(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS ftk2015 FROM Mahasiswa WHERE NamaMhs LIKE '% [0-9][0-9]15%' OR NamaMhs LIKE '% [0-9][0-9][0-9][0-9]15%' AND FakultasMhs LIKE '%Kelautan%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.ftk2015

def ftkang2016(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS ftk2016 FROM Mahasiswa WHERE NamaMhs LIKE '% [0-9][0-9]16%' OR NamaMhs LIKE '% [0-9][0-9][0-9][0-9]16%' AND FakultasMhs LIKE '%Kelautan%'")

    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.ftk2016


def gambar():
    #Regresi FIA
    plt.figure(1)
    x = [[fiaang2013(conn)], [fiaang2014(conn)], [fiaang2015(conn)], [fiaang2016(conn)]]
    y = [[3.163], [3.185], [3.24], [3.245]]
    
    linreg = LinearRegression()

    linreg.fit(x,y)

    xx = linspace(135, 1070, 4)

    plt.plot(x,y,'o',xx,linreg.predict(matrix(xx).T),'--r')

    print mean_squared_error(linreg.predict(x),y)

    #Regresi FTI
    plt.figure(2)
    x2 = [[ftiang2013(conn)], [ftiang2014(conn)], [ftiang2015(conn)], [ftiang2016(conn)]]
    y2 = [[3.187], [3.26], [3.285], [3.3]]

    linreg2 = LinearRegression()

    linreg2.fit(x2,y2)

    xx2 = linspace(280, 1200, 4)

    plt.plot(x2,y2,'o',xx2,linreg.predict(matrix(xx2).T),'--r')

    print mean_squared_error(linreg.predict(x2),y2)

    #Regresi FTIK
    plt.figure(3)
    x3 = [[ftikang2013(conn)], [ftikang2014(conn)], [ftikang2015(conn)], [ftikang2016(conn)]]
    y3 = [[3.395], [3.34], [3.38], [3.4]]

    linreg3 = LinearRegression()

    linreg3.fit(x3,y3)

    xx3 = linspace(10, 1070, 4)

    plt.plot(x3,y3,'o',xx3,linreg.predict(matrix(xx3).T),'--r')

    print mean_squared_error(linreg.predict(x3),y3)

    #Regresi FTSLK
    plt.figure(4)
    x4 = [[ftslkang2013(conn)], [ftslkang2014(conn)], [ftslkang2015(conn)], [ftslkang2016(conn)]]
    y4 = [[3.183], [3.205], [3.26], [3.245]]

    linreg4 = LinearRegression()

    linreg4.fit(x4,y4)

    xx4 = linspace(80, 1070, 4)

    plt.plot(x4,y4,'o',xx4,linreg.predict(matrix(xx4).T),'--r')

    print mean_squared_error(linreg.predict(x4),y4)

    #Regresi FTK
    plt.figure(5)
    x5 = [[ftkang2013(conn)], [ftkang2014(conn)], [ftkang2015(conn)], [ftkang2016(conn)]]
    y5 = [[3.173], [3.15], [3.235], [3.2]]

    linreg5 = LinearRegression()

    linreg5.fit(x5,y5)

    xx5 = linspace(5, 1070, 4)

    plt.plot(x5,y5,'o',xx5,linreg.predict(matrix(xx5).T),'--r')

    print mean_squared_error(linreg.predict(x5),y5)

    plt.show()

conn = pyodbc.connect('Driver={SQL Server};Server=MSI;Database=datashareitsacid;Trusted_Connection=yes;')

print(fiaang2013(conn))
print(fiaang2014(conn))
print(fiaang2015(conn))
print(fiaang2016(conn))

print(ftiang2013(conn))
print(ftiang2014(conn))
print(ftiang2015(conn))
print(ftiang2016(conn))

print(ftikang2013(conn))
print(ftikang2014(conn))
print(ftikang2015(conn))
print(ftikang2016(conn))

print(ftslkang2013(conn))
print(ftslkang2014(conn))
print(ftslkang2015(conn))
print(ftslkang2016(conn))

print(ftkang2013(conn))
print(ftkang2014(conn))
print(ftkang2015(conn))
print(ftkang2016(conn))
gambar()

