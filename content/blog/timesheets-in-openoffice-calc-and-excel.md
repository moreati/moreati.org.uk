---
date: 2008-11-27
title: Timesheets in OpenOffice Calc and Excel
type: post
---

Putting my timesheets in order today, I finally figured out how to make
Excel deal correctly with time durations. The default is to treat values
as a date/time, formatted as hh:mm. So a value such as 37:00 - meant as
a duration - is displayed as 13:00 (1 PM the following day). To correct
this, choose custom cell formatting, and enter the format as [h]:mm. In
OpenOffice Calc, [H]:MM is the default format for a time value (tested
with 3.0), so durations work out of the box. For something pre-cooked,
the [OpenOffice Documentation](http://documentation.openoffice.org/)
site has a [timesheet template by Vivian
Lal](http://documentation.openoffice.org/Samples_Templates/User/template/Timesheet.stc).
