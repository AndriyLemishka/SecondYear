# -*- coding: utf-8 -*-
"""
Generator for Lab 5 Theoretical Reference and Interactive Web Application
Output directory: D:\\Studing\\SecondYear\\FirstSemester\\OperatingSystems\\Lab5\\Explenation material
"""

import os
import sys

TARGET_DIR = r"D:\Studing\SecondYear\FirstSemester\OperatingSystems\Lab5\Explenation material"
os.makedirs(TARGET_DIR, exist_ok=True)

md_file = os.path.join(TARGET_DIR, "ТЕОРІЯ_ТА_ПОЯСНЕННЯ_ЛАБ5.md")
html_file = os.path.join(TARGET_DIR, "index.html")

print("1. Writing comprehensive Markdown reference...")
