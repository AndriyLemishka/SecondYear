@echo off
chcp 1251 >nul
echo ========================================================
echo   ВИКОНАННЯ ЛАБОРАТОРНОЇ РОБОТИ №4 (cmd.exe)
echo ========================================================

echo.
echo [Крок 1] Перегляд дисків C: та D:
dir C:\
dir D:\

echo.
echo [Кроки 2-5] Створення структури WORK, TEMT та LNC
md D:\WORK 2>nul
md D:\WORK\TEMT 2>nul
md D:\LNC 2>nul

echo.
echo [Крок 6] Створення текстових файлів
echo Line 1 > D:\LNC\nc1
echo Line 2 > D:\LNC\nc2
echo Line 3 > D:\LNC\nc3
echo Line 4 > D:\LNC\nc4
echo Doc 5 > D:\LNC\nc5.doc
echo Doc 6 > D:\LNC\nc6.doc
echo Doc 7 > D:\LNC\nc7.doc

echo.
echo [Крок 7] Копіювання файлів з LNC у WORK
copy /y D:\LNC\*.* D:\WORK

echo.
echo [Крок 8] Переміщення *.doc у TEMT
move /y D:\WORK\*.doc D:\WORK\TEMT

echo.
echo [Кроки 9-11] Перехід на диск D:, вхід у WORK та перегляд
d:
cd D:\WORK
dir

echo.
echo [Крок 12] Перегляд вмісту файлу nc1
type nc1

echo.
echo [Крок 13] Видалення файлу nc2
del /q nc2

echo.
echo [Кроки 14-16] Перейменування файлів та перегляд результату
ren nc1 nc1.txt
ren nc? nc?.txt
dir

echo.
echo [Кроки 17-18] Перехід у надкаталог та перейменування WORK у KATALOG
cd ..
move WORK KATALOG

echo.
echo [Кроки 19-20] Знищення файлів і видалення каталогів TEMT та KATALOG
del /q D:\KATALOG\*.*
del /q D:\KATALOG\TEMT\*.*
rd D:\KATALOG\TEMT
rd D:\KATALOG

echo.
echo [Крок 21] Контрольний перегляд диска D:
dir D:\

echo.
echo ========================================================
echo   ЗАВДАННЯ 2 (САМОСТІЙНА ЧАСТИНА)
echo ========================================================

echo.
echo [Крок 1] Копіювання файлів з LNC у корінь диска D:
copy /y D:\LNC\*.* D:\

echo.
echo [Кроки 2-4] Створення TEMP, перейменування у *.doc та переміщення
md D:\TEMP 2>nul
ren D:\nc? nc?.doc
move /y D:\*.doc D:\TEMP\

echo.
echo [Кроки 5-7] Створення TEMP\TEXT, копіювання файлів та створення DOK
md D:\TEMP\TEXT 2>nul
copy /y D:\TEMP\nc1.doc D:\TEMP\TEXT\
copy /y D:\TEMP\nc3.doc D:\TEMP\TEXT\
md D:\TEMP\TEXT\DOK 2>nul

echo.
echo [Крок 8] Створення текстового файлу в DOK
echo Test laboratory work 4 file > D:\TEMP\TEXT\DOK\test.txt

echo.
echo [Кроки 9-10] Переміщення nc2.doc/nc4.doc у DOK та перейменування на tab2/tab4
move /y D:\TEMP\nc2.doc D:\TEMP\TEXT\DOK\
move /y D:\TEMP\nc4.doc D:\TEMP\TEXT\DOK\
ren D:\TEMP\TEXT\DOK\nc2.doc tab2.txt
ren D:\TEMP\TEXT\DOK\nc4.doc tab4.txt

echo.
echo [Крок 11] Багаторівневий перегляд з каталогу DOK
cd D:\TEMP\TEXT\DOK
echo --- Вміст кореня D:\ ---
dir D:\
echo --- Вміст D:\TEMP\TEXT ---
dir D:\TEMP\TEXT
echo --- Вміст поточного каталогу DOK ---
dir

echo.
echo [Крок 12] Знищення файлів *.txt та *.doc
del /q D:\TEMP\TEXT\DOK\*.txt
del /q D:\TEMP\TEXT\*.doc
del /q D:\TEMP\*.doc

echo.
echo [Крок 13] Послідовне видалення каталогів DOK, TEXT, TEMP
cd D:\
rd D:\TEMP\TEXT\DOK
rd D:\TEMP\TEXT
rd D:\TEMP

echo.
echo ========================================================
echo   УСІ ЗАВДАННЯ ЛАБОРАТОРНОЇ РОБОТИ №4 ВИКОНАНО УСПІШНО!
echo ========================================================
