import exal
import exal.helper as helper

for drivername in exal.PRIORITY:
    exal._loaddriver(drivername)

for drivername in exal.DRIVERS:
    print "Test Driver " + drivername
    ex_driver = exal.EXAL(drivername)

    wb = ex_driver.open_workbook_from_file("tests/testbook.xlsx")

    print [sh.name for sh in wb.sheets]

    sh = wb.get_sheet("Sheet1")

    print sh.range((1,1), (2,2)).value
    print sh.range((1,1), (2,2)).formula

    sh.cell((3,3)).formula = "=" + helper.pos2address(1,1)
    print sh.cell((3,3)).value
    #wb.save_as("test_out.xlsx")
    wb.close()