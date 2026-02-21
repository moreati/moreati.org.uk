---
date: 2009-11-17
title: MPGe of an electric car
type: post
---

Does an electric car gets better or worse mileage than a conventional
petrol or diesel car? To a large extent, it depends on what we choose to
include or exclude in the calculation. We can measure the whole chain,
accounting for every step in the process of extraction, refinement,
transportation and use - a well to wheel model. Or more easily, and less
accurately, we can account only for burning the fuel - a tank to wheel
model. A tank to wheel module is what I shall use here to compare 2 cars
(one petrol and one electric) on:

-   Direct fuel/charge cost per mile
-   Carbon dioxide (CO~2~) emitted per mile

Petrol Car
----------

First the petrol car, for which I'll be using my Ford SportKa. At it's
last fill this car used [37.6 litres of petrol to drive 306
miles](http://www.google.co.uk/search?hl=en&q=37.6+litres+per+306+miles+in+miles+per+uk+gallon),
thus obtaining 37 mpg. So fuel cost is easy:

(37.6 l / 306 miles) \* 105 p/l = **12.9 pence/mile**.

CO~2~ emissions for a car are:

(Mass of fuel burnt \* Proportion of carbon \* Relative mass of CO~2~) /
Distance

Density of petrol is 0.72 kg/l, and by mass it contains approx 85 %
carbon [[wp:Gasoline](http://en.wikipedia.org/wiki/Gasoline#Density)].
Each carbon atom has an atomic mass of 12, and combines with 2 oxygen
atoms with atomic mass 16. So 12 kg of carbon (C) burns to make 12 + 16
+ 16 = 44 kg of CO~2~, or 3.67 kg/kg. So CO~2~ emitted is:

(37.6 litres \* 0.72 kg/l \* 0.85 \* 3.67 kg/kg) / 306 miles = **275
g/mile**

Electric Car
------------

All the emissions of the electric car happen at the power station, so
the calculation is more involved. For this I shall use the BMW Mini E.
The Mini E has a quoted energy use of 20 kWh/100 km or 0.323 kWh/mile
[[mini\_e](http://www.mini.co.uk/html/about_us/mini_e.html)]. This makes
the direct fuel cost

0.323 kWh/mile \*9.8 p/kWh = **3.1 p/mile**.

The CO~2~ emissions follow the same formula as a petrol car:

(Mass of fuel burnt \* Proportion of carbon \* Relative mass of CO~2~) /
Distance

The mass of fuel burned is given by:

Electricity used / (Fuel energy density \* Power plant efficiency \*
Grid efficiency)

Referring to the Digest of UK Energy Statistics (DUKES) 2008, coal has a
gross energy density of 25.4 GJ/tonne, or 7.05 kWh/kg
[[dukes08](http://www.decc.gov.uk/media/viewfile.ashx?filepath=statistics/publications/dukes/dukes08.pdf&filetype=4)].
Coal burnt in 2007 by Drax - the UK's largest coal fired power station
station - was 60 % carbon
[[draxenv](http://www.draxpower.com/files/page/916/EPR_2007_FINAL.pdf "Drax Power Environmental Performance Review 2007"):table7].
The relative mass of CO~2~ remains the same. Coal plants in the UK were
overall 33 % efficient in 2008, and grid losses were about 8 %
[[dukes08](http://www.decc.gov.uk/media/viewfile.ashx?filepath=statistics/publications/dukes/dukes08.pdf&filetype=4)].
So:

0.323 kWh/mile / (7.05 kWh/kg \* 0.33 \* 0.92) = 151 g/mile of coal.

Working through:

0.151 kg/mile \* 0.60 \* 3.67 kg/kg =**332 g/mile** of CO~2~.

Results
-------

To my surprise, based on emissions a 37 mpg petrol car beats an electric
car run exclusively on coal. The MPGe is only **30.6 mpg**. Based on
cost an electric car run on electricity costing 9.8 p/kWh gets an MPGe
of **154 mpg**.

Considerations
--------------

Such numbers are very sensitive to the assumptions made. For instance if
the same car is powered exclusively by natural gas, then the MPGe is
nearer 65 mpg, because gas emits less than half the CO2/kWh of coal. If
the petrol car were filled at US prices, the cost based MPGe would be
much lower. I would love to improve upon these simple calculations.
Please try the numbers with your own figures and post the results for
comparison. If I've made a bad assumption, or calculations errors, or if
you have other sources please let me know. Here are the assumptions I
used, primarily to keep things simple, secondly to make it unfair to the
electric car:

-   Manufacturing, maintenance, component replacement, insurance, tax,
    congestion charges, parking and battery replacement are excluded.
-   Extraction, refinement and transportation of petrol/diesel is
    excluded, as is extraction and transport of coal.
-   Electricity is generated from coal, the dirtiest of sources.
-   Gross calorific value is used for all fuels, rather than net.
-   The fuel is burnt perfectly, so all the contained carbon is emitted
    as CO~2~.
-   Electrical use by the electric car is measured at the wall socket.
-   When referred to imperial (UK) gallons, and metric tonnes are used
    throughout.
-   Petrol is taken to cost £1.05 per litre, and electricity 9.8p per
    kWh.
