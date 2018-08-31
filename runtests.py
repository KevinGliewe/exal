import os
import sys
import exal
import exal.helper as helper

import logging

root = logging.getLogger()
ch = logging.StreamHandler(sys.stdout)
cf = logging.Formatter('[%(name)s] %(message)s')
ch.setFormatter(cf)
root.addHandler(ch)

logger = logging.getLogger(__name__)

imgfile = os.path.abspath("tests/128x128.png")

imagedrivers = [
    "xlwings",
    "comtype",
    "openpyxl",
]

def testDriver(drivername):
    print "Test Driver " + drivername
    ex_driver = exal.EXAL(drivername)

    wb = ex_driver.open_workbook_from_file("tests/testbook.xlsx")

    print [sh.name for sh in wb.sheets]

    sh = wb.get_sheet("Sheet1")

    print sh.range((1,1), (2,2)).value
    print sh.range((1,1), (2,2)).formula

    sh.cell((3,3)).formula = "=" + helper.pos2address(1,1)
    print sh.cell((3,3)).value

    if drivername in imagedrivers:
        print "Loading Image " + imgfile
        sh.addImage((4,4), imgfile)

    wb = wb.save_as("test_out_" + drivername + ".xlsx")
    wb.close()

for drivername in exal.PRIORITY:
    print "Load driver: " + drivername
    exal._loaddriver(drivername)

testDriver("openpyxl")

for drivername in exal.DRIVERS:
    testDriver(drivername)
