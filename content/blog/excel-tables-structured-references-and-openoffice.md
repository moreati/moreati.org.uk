---
date: 2010-09-05
title: 'Excel tables, structured references and OpenOffice'
type: post
---

In Microsoft Excel and OpenOffice Calc one can name a range of cells
and refer to the name in a formula. So rather than writing `=SUM(C2:C7)`
one can write `=SUM(SaleAmt)`. Excel calls this a "Defined Name". In Excel
2007 one can also create a
"[table](http://office.microsoft.com/en-us/excel-help/define-and-use-names-in-formulas-HA010147120.aspx)",
which is a region of cells that store records and fields in the rows and
columns. The first row of a table is used by excel to name the fields
(columns). Once a table is named Excel calls this a "table name". In
Excel a table allows one to write formulas with a syntax called a
"[structured
reference](http://office.microsoft.com/en-us/excel-help/using-structured-references-with-excel-tables-HA010155686.aspx "Using structured references with Excel tables")".
To sum the values in the SaleAmt field of the DeptSales table one would
write the formula as `=SUM(DeptSales[SaleAmt])`. If new columns or rows
are added to the table Excel should automatically track this and
recalculate the formula appropriately. OpenOffice Calc does not support
these, they are a proprietary feature of Excel. So please don't use
named tables or structured references if you will be interoperating with
people who aren't fellow MS Office users, or if you will be publishing
your Spreadsheet to the public. If you have already used structure
references, and you are running Excel 2010 you can save your Spreadsheet
in OpenDocument Format (.ods) and all structured references should be
converted to explicit cell ranges. If you open an Excel Office OpenXML
(.xlsx) spreadsheet in OpenOffice Calc, and it contains structured
references then it is likely you will see Err:508 and Err:509 in the
cells. To my knowledge there is no way to fix this in Calc, you should
ask whoever created the spreadsheet to send you a copy in OpenDocument
(.ods) format. Attached for reference are two example spreadsheets.

-   [Structured references example
    (.xlsx)](/uploads/2010/09/structured_references_example.xlsx)
    This will work in Mircrosoft Excel, but not OpenOffice Calc
-   [Structured references example
    (.ods)](/uploads/2010/09/structured_references_example.ods)
    This example has been saved in OpenDocument format by Excel 2010.
    This removed structured references and converted them to standard
    cell/range references.
