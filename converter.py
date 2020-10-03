# unit name : UI description
dict = { 
    # Weight
    "grams":                "grams (g)",
    "kilos":                "kilos (kg)",
    "metric-tonnes":        "metric tonnes (t)",
    "ounces":               "ounces (oz)",
    "pounds":               "pounds (lb)",
    "short-ton":            "short ton (shton)",
    "long-ton":             "long ton (Lton)",

    # Length
    "inches":               "inches (in)",
    "feet":                 "feet (ft)",
    "yards":                "yards (yd)",
    "miles":                "miles (mi)",
    "millimeters":          "millimeters (mm)",
    "centimeters":          "centimeters (cm)",
    "meters":               "meters (m)",
    "kilometers":           "kilometers (km)",

    # Volume
    "teaspoon-metric":      "teaspoons (tsp - metric)",
    "tablespoon-metric":    "tablespoons (tbsp - metric)",
    "floz-us":              "fluid onces (fl oz - US)",
    "floz-imp":             "fluid ounces (fl oz - Imperial)",
    "cups-us" :             "cups (US)",
    "cups-imp":             "cups (Imperial)",
    "milliliter":           "milliliters (ml)",
    "liter":                "liters",
    "m3":                   "cubic meters (m3)",
    "in3" :                 "cubic inches (in3)",
    "ft3" :                 "cubic feet (ft3)",
    "pint-us" :             "pints (pt - US)",
    "pint-imp":             "pints (pt - Imperial)",
    "quart-us":             "quarts (qt - US)",
    "quart-imp":            "quarts (qt - Imperial)",
    "gallon-us":            "gallons (gal - US)",
    "gallon-imp":           "gallons (gal - Imperial)",

    # Area
    "cm2":                  "square centimeters (cm2)",
    "m2":                   "square meters (m2)",
    "km2":                  "square kilometers (km2)",
    "in2":                  "square inches (in2)",
    "ft2":                  "square feet (ft2)",
    "yd2":                  "square yards (yd2)",
    "mi2":                  "square miles (mi2)",
    "hectare":              "hectare (ha)",
    "acre":                 "acre (ac)"
}


# Multiplier : unit name
units = {
    
    ### Weight
    "ounces" : {
        "ounces (oz) is equal to:":     1,
        dict.get("grams"):              28, 
        dict.get("kilos"):              0.02835,
        #dict.get("metric-tonnes"):     0, 
        #dict.get("ounces"):            0,
        dict.get("pounds"):             0.0625, 
        #dict.get("short-ton"):         0, 
        #dict.get("long-ton"):          0,  
    },
    "pounds" : {
        "pounds (lb) is equal to:":     1,
        dict.get("grams"):              453.59,
        dict.get("kilos"):              0.4536,
        dict.get("metric-tonnes"):      0.000454,  
        dict.get("ounces"):             16,
        #dict.get("pounds"):            0, 
        dict.get("short-ton"):          0.0005,
        dict.get("long-ton"):           0.000446,
    },
    "short-ton" : {
        "short ton (shton) is equal to:":   1,
        #dict.get("grams"):             0,
        dict.get("kilos"):              907.2,  
        dict.get("metric-tonnes"):      0.9072, 
        #dict.get("ounces"):            0, 
        dict.get("pounds"):             2000,
        #dict.get("short-ton"):         0,  
        dict.get("long-ton"):           0.892913,
    },
    "long-ton" : {
        "long ton (Lton) is equal to:": 1,
        #dict.get("grams"):             0, 
        dict.get("kilos"):              1016, 
        dict.get("metric-tonnes"):      1.016,  
        #dict.get("ounces"):            0,
        dict.get("pounds"):             2239.859,
        dict.get("short-ton"):          1.119929,
        # dict.get("long-ton"):         0,
    },
    "grams" : {
        "gram (g) is equal to:":        1,
        dict.get("ounces"):             0.035273,
        dict.get("pounds"):             0.002205,
        #dict.get("short-ton"):         0, 
        #dict.get("long-ton"):          0,
        #dict.get("grams"):             0, 
        dict.get("kilos"):              0.001,
        #dict.get("metric-tonnes"):     0,
    },
    "kilos" : {
        "kilogram (kg) is equal to:":   1,
        dict.get("ounces"):             35.27337, 
        dict.get("pounds"):             2.204586,
        dict.get("short-ton"):          0.001102, 
        dict.get("long-ton"):           0.000984,  
        dict.get("grams"):              1000, 
        #dict.get("kilos"):             0,
        dict.get("metric-tonnes"):      0.001, 
    },
    "metric-tonnes" : {
        "metric tonnes (t) is equal to:":  1,
        #dict.get("ounces"):            0,
        dict.get("pounds"):             2204.586,  
        dict.get("short-ton"):          1.102293,
        dict.get("long-ton"):           0.984252,  
        #dict.get("grams"):             0,
        dict.get("kilos"):              1000,
        #dict.get("metric-tonnes"):     0, 
    },
    
    ### Length
    "inches" : {
        "inches (in) is equal to:":     1,
        dict.get("millimeters"):        25.4,
        dict.get("centimeters"):        2.54,
        dict.get("meters"):             0.0254,
        #dict.get("kilometers"):        0,
        #dict.get("inches"):            0,
        dict.get("feet"):               0.083333,
        dict.get("yards"):              0.027778,
        #dict.get("miles"):             0.000016,
    },
    "feet" : {
        "feet (ft) is equal to:":       1,
        #dict.get("millimeters"):       0,
        dict.get("centimeters"):        30.48,
        dict.get("meters"):             0.3048,
        dict.get("kilometers"):         0.000305,
        dict.get("inches"):             12,
        #dict.get("feet"):              1,
        dict.get("yards"):              0.333333,
        dict.get("miles"):              0.000189,  
    },
    "yards" : {
        "yards (yd) is equal to:":      1,
        #dict.get("millimeters"):       914.4,
        dict.get("centimeters"):        91.44,
        dict.get("meters"):             0.9144,
        dict.get("kilometers"):         0.000914,
        dict.get("inches"):             36,
        dict.get("feet"):               3,
        #dict.get("yards"):             1,
        dict.get("miles"):              0.000568, 
    },
    "miles" : {
        "miles (mi) is equal to:":      1,
        #dict.get("millimeters"):       0,
        #dict.get("centimeters"):       0,
        dict.get("meters"):             1609.344,
        dict.get("kilometers"):         1.609344,
        dict.get("inches"):             63360,
        dict.get("feet"):               5280,
        dict.get("yards"):              1760,
        #dict.get("miles"):             0,
    },
    "millimeters" : {
        "millimeters (mm) is equal to:":    1,
        dict.get("inches"):             0.03937,
        dict.get("feet"):               0.003281,
        dict.get("yards"):              0.001094,
        #dict.get("miles"):             0,
        #dict.get("millimeters"):       0,
        dict.get("centimeters"):        0.1,
        dict.get("meters"):             0.001,
        dict.get("kilometers"):         0.000001,
    },
    "centimeters" : {
        "centimeters (cm) is equal to:":    1,
        dict.get("inches"):             0.393701,
        dict.get("feet"):               0.032808,
        dict.get("yards"):              0.010936,
        #dict.get("miles"):             0,
        dict.get("millimeters"):        10,
        #dict.get("centimeters"):       1,
        dict.get("meters"):             0.01,
        dict.get("kilometers"):         0.00001,
    },
    "meters" : {
        "meters (m) is equal to:":      1,
        dict.get("inches"):             39.37008,
        dict.get("feet"):               3.28084,
        dict.get("yards"):              1.093613,
        dict.get("miles"):              0.000621,
        dict.get("millimeters"):        1000,
        dict.get("centimeters"):        100,
        #dict.get("meters"):            0,
        dict.get("kilometers"):         0.001,
    },
    "kilometers" : {
        "kilometers (km) is equal to:": 1,           
        dict.get("inches"):             39370.08,
        dict.get("feet"):               3280.84,
        dict.get("yards"):              1093.613,
        dict.get("miles"):              0.621371,
        #ict.get("millimeters"):        0,
        #dict.get("centimeters"):       0,
        dict.get("meters"):             0.0254,
        #dict.get("kilometers"):        0,
    },

    ### Volume 
    "teaspoon-metric" : {
        "teaspoons (tsp - metric) is equal to:":    1,              
        #ict.get("teaspoon-metric"):    0,
        dict.get("tablespoon-metric"):  0.3333,         
        dict.get("floz-us"):            0.1690701135,
        dict.get("floz-imp"):           0.1759753986,
        dict.get("cups-us"):            0.0211337642,
        dict.get("cups-imp"):           0.0175975399,
        dict.get("milliliter"):         5,
        dict.get("liter"):              0.005,
        #dict.get("m3"):                #0.000005, 
        dict.get("in3"):                0.3051187205,
        #dict.get("ft3"):               #0.0001765733,
        dict.get("pint-us"):            0.0105668821,
        dict.get("pint-imp"):           0.0087987699,
        dict.get("quart-us"):           0.005283441,
        dict.get("quart-imp"):          0.004399385,
        dict.get("gallon-us"):          0.0013208603,
        dict.get("gallon-imp"):         0.0010998462,
    },
    "tablespoon-metric" : {
        "tablespoons (tbsp - metric) is equal to:": 1,
        dict.get("teaspoon-metric"):    3,
        #dict.get("tablespoon-metric"): 0,           
        dict.get("floz-us"):            0.5072103405,
        dict.get("floz-imp"):           0.5279261959,
        dict.get("cups-us"):            0.0634012926,
        dict.get("cups-imp"):           0.0527926196,
        dict.get("milliliter"):         15,
        dict.get("liter"):              0.015,
        #dict.get("m3"):                0,
        dict.get("in3"):                0.9153561614,
        dict.get("ft3"):                0.00052972,
        dict.get("pint-us"):            0.0317006463,
        dict.get("pint-imp"):           0.0263963098,
        dict.get("quart-us"):           0.0158503231,
        dict.get("quart-imp"):          0.0131981549,
        dict.get("gallon-us"):          0.0039625808,
        dict.get("gallon-imp"):         0.0032995387,
    },
    "floz-us" : {
        "fluid ounces (fl oz - US) is equal to:":   1,              
        dict.get("teaspoon-metric"):    5.9147059125,
        dict.get("tablespoon-metric"):  1.9715686375,
        #dict.get("floz-us"):           0, 
        dict.get("floz-imp"):           1.0408427308, 
        dict.get("cups-us"):            0.125,
        dict.get("cups-imp"):           0.1040842731,
        dict.get("milliliter"):         29.573529562,
        dict.get("liter"):              0.0295735296,
        #dict.get("m3"):                0,
        dict.get("in3"):                1.8046875,
        dict.get("ft3"):                0.0010443793,
        dict.get("pint-us"):            0.0625,
        dict.get("pint-imp"):           0.0520421365,
        dict.get("quart-us"):           0.03125,
        dict.get("quart-imp"):          0.0260210683,
        dict.get("gallon-us"):          0.0078125,
        dict.get("gallon-imp"):         0.0065052671,
    },
    "floz-imp" : {
        "fluid ounces (fl oz - Imperial) is equal to:": 1,              
        dict.get("teaspoon-metric"):    5.6826125,     
        dict.get("tablespoon-metric"):  1.8942041667,  
        dict.get("floz-us"):            0.9607599404,   
        #dict.get("floz-imp"):          0:               
        dict.get("cups-us"):            0.1200949926,
        dict.get("cups-imp"):           0.1,           
        dict.get("milliliter"):         28.4130625,    
        dict.get("liter"):              0.0284130625, 
        #dict.get("m3"):                0,              
        dict.get("in3"):                1.7338714549,   
        dict.get("ft3"):                0.0010033978,  
        dict.get("pint-us"):            0.0600474963,    
        dict.get("pint-imp"):           0.05,           
        dict.get("quart-us"):           0.0300237481,
        dict.get("quart-imp"):          0.025,        
        dict.get("gallon-us"):          0.007505937,    
        dict.get("gallon-imp"):         0.00625,        
    },
    "cups-us" : {
        "cups (US) is equal to:":       1,
        dict.get("teaspoon-metric"):    47.3176473,
        dict.get("tablespoon-metric"):  15.7725491,
        dict.get("floz-us"):            8,
        dict.get("floz-imp"):           8.3267418463,
        #dict.get("cups-us"):           0,
        dict.get("cups-imp"):           0.8326741846,
        dict.get("milliliter"):         28.4130625,
        dict.get("liter"):              0.2365882365,
        #dict.get("m3"):                0,
        dict.get("in3"):                14.4375,
        dict.get("ft3"):                0.0083550347,
        dict.get("pint-us"):            0.5,
        dict.get("pint-imp"):           0.4163370923,
        dict.get("quart-us"):           0.25,
        dict.get("quart-imp"):          0.2081685462,
        dict.get("gallon-us"):          0.0625,
        dict.get("gallon-imp"):         0.0520421365,
    },
    "cups-imp" : {
        "cups (Imperial) is equal to:": 1,
        dict.get("teaspoon-metric"):    56.826125,
        dict.get("tablespoon-metric"):  18.942041667,
        dict.get("floz-us"):            9.607599404,
        dict.get("floz-imp"):           10,
        dict.get("cups-us"):            1.2009499255,
        #dict.get("cups-imp"):          0,
        dict.get("milliliter"):         284.130625,
        dict.get("liter"):              0.284130625,
        #dict.get("m3"):                0,
        dict.get("in3"):                17.338714549,
        dict.get("ft3"):                0.0100339783,
        dict.get("pint-us"):            0.6004749628,
        dict.get("pint-imp"):           0.5,
        dict.get("quart-us"):           0.3002374814,
        dict.get("quart-imp"):          0.25,
        dict.get("gallon-us"):          0.0750593703,
        dict.get("gallon-imp"):         0.0625,
    },
    "milliliter" : {
        "milliliter (ml) is equal to:": 1,
        dict.get("teaspoon-metric"):    0.2,
        dict.get("tablespoon-metric"):  0.0666666667,
        dict.get("floz-us"):            0.0338140227,
        dict.get("floz-imp"):           0.0351950797,
        dict.get("cups-us"):            0.0042267528,
        dict.get("cups-imp"):           0.003519508,
        #dict.get("milliliter"):        0,
        dict.get("liter"):              0.001,
        #dict.get("m3"):                0,
        dict.get("in3"):                0.0610237441,
        dict.get("ft3"):                0.0000353147,
        dict.get("pint-us"):            0.0021133764,
        dict.get("pint-imp"):           0.001759754,
        dict.get("quart-us"):           0.0010566882,
        dict.get("quart-imp"):          0.000879877,
        dict.get("gallon-us"):          0.0002641721,
        dict.get("gallon-imp"):         0.0002199692,
    },
    "liter" : {
        "liter (l) is equal to:":       1,
        dict.get("teaspoon-metric"):    200,
        dict.get("tablespoon-metric"):  66.666666667,
        dict.get("floz-us"):            33.814022702,
        dict.get("floz-imp"):           35.195079728,
        dict.get("cups-us"):            4.2267528377,
        dict.get("cups-imp"):           3.5195079728,
        dict.get("milliliter"):         1000,
        #dict.get("liter"):             0,
        dict.get("m3"):                 0.001,
        dict.get("in3"):                61.023744095,
        dict.get("ft3"):                0.0353146667,
        dict.get("pint-us"):            2.1133764189,
        dict.get("pint-imp"):           1.7597539864,
        dict.get("quart-us"):           1.0566882094,
        dict.get("quart-imp"):          0.8798769932,
        dict.get("gallon-us"):          0.2641720524,
        dict.get("gallon-imp"):         0.2199692483,
    },
    "m3" : {
        "cubic meter (m3) is equal to:":       1,
        #dict.get("teaspoon-metric"):   0,
        #dict.get("tablespoon-metric"): 0,
        #dict.get("floz-us"):           0,
        #dict.get("floz-imp"):          0,
        #dict.get("milliliter"):        0,
        dict.get("liter"):              1000,
        #dict.get("m3"):                0,
        #dict.get("in3"):               0,
        dict.get("ft3"):                35.314666721,
        dict.get("cups-us"):            4226.7528377,
        dict.get("cups-imp"):           3519.5079728,
        dict.get("pint-us"):            2113.3764189,
        dict.get("pint-imp"):           1759.7539864,
        dict.get("quart-us"):           1056.6882094,
        dict.get("quart-imp"):          879.8769932,
        dict.get("gallon-us"):          264.17205236,
        dict.get("gallon-imp"):         219.9692483,
    },
    "in3" : {
        "cubic inches (in3) is equal to:":       1,
        dict.get("teaspoon-metric"):    3.2774128,
        dict.get("tablespoon-metric"):  1.0924709333,
        dict.get("floz-us"):            0.5541125541,
        dict.get("floz-imp"):           0.576744024,
        dict.get("milliliter"):         16.387064,
        dict.get("liter"):              0.016387064,
        #dict.get("m3"):                0,
        #dict.get("in3"):               0,
        dict.get("ft3"):                0.0005787037,
        dict.get("cups-us"):            0.0692640693,
        dict.get("cups-imp"):           0.0576744024,
        dict.get("pint-us"):            0.0346320346,
        dict.get("pint-imp"):           0.0288372012,
        dict.get("quart-us"):           0.0173160173,
        dict.get("quart-imp"):          0.0144186006,
        dict.get("gallon-us"):          0.0043290043,
        dict.get("gallon-imp"):         0.0036046501,
    },
    "ft3" : {
        "cubic feet (ft3) is equal to:":       1,
        #dict.get("teaspoon-metric"):   0,
        #dict.get("tablespoon-metric"): 0,
        dict.get("floz-us"):            957.50649351,
        dict.get("floz-imp"):           996.61367345,
        #dict.get("milliliter"):        0,
        dict.get("liter"):              28.316846592,
        dict.get("m3"):                 0.0283168466,
        dict.get("in3"):                1728,
        #dict.get("ft3"):               0,
        dict.get("cups-us"):            119.68831169,
        dict.get("cups-imp"):           99.661367345,
        dict.get("pint-us"):            59.844155844,
        dict.get("pint-imp"):           49.830683672,
        dict.get("quart-us"):           29.922077922,
        dict.get("quart-imp"):          24.915341836,
        dict.get("gallon-us"):          7.4805194805,
        dict.get("gallon-imp"):         6.228835459,
    },
    "pint-us" : {
        "pints (pt - US) is equal to:":      1,
        dict.get("teaspoon-metric"):    94.6352946,
        dict.get("tablespoon-metric"):  31.5450982,
        dict.get("floz-us"):            16,
        dict.get("floz-imp"):           16.653483693,
        dict.get("milliliter"):         473.176473,
        dict.get("liter"):              0.473176473,
        #dict.get("m3"):                0,
        dict.get("in3"):                28.875,
        dict.get("ft3"):                0.0167100694,
        dict.get("cups-us"):            2,
        dict.get("cups-imp"):           1.6653483693,
        #dict.get("pint-us"):           0,
        dict.get("pint-imp"):           0.8326741846,
        dict.get("quart-us"):           0.5,
        dict.get("quart-imp"):          0.4163370923,
        dict.get("gallon-us"):          0.125,
        dict.get("gallon-imp"):         0.1040842731,
    },
    "pint-imp" : {
        "pints (pt - Imperial) is equal to:":      1,
        dict.get("teaspoon-metric"):    113.65225,
        dict.get("tablespoon-metric"):  37.884083333,
        dict.get("floz-us"):            19.215198808,
        dict.get("floz-imp"):           20,
        dict.get("milliliter"):         568.26125,
        dict.get("liter"):              0.56826125,
        #dict.get("m3"):                0,
        dict.get("in3"):                34.677429099,
        dict.get("ft3"):                0.0200679567,
        dict.get("cups-us"):            2.401899851,
        dict.get("cups-imp"):           2,
        dict.get("pint-us"):            1.2009499255,
        #dict.get("pint-imp"):          0,
        dict.get("quart-us"):           0.6004749628,
        dict.get("quart-imp"):          0.5,
        dict.get("gallon-us"):          0.1501187407,
        dict.get("gallon-imp"):         0.125,
    },
    "quart-us" : {
        "quarts (qt - US) is equal to:":      1,
        dict.get("teaspoon-metric"):    189.2705892,
        dict.get("tablespoon-metric"):  63.0901964,
        dict.get("floz-us"):            32,
        dict.get("floz-imp"):           33.306967385,
        dict.get("milliliter"):         946.352946,
        dict.get("liter"):              0.946352946,
        #dict.get("m3"):                0,
        dict.get("in3"):                57.75,
        dict.get("ft3"):                0.0334201389,
        dict.get("cups-us"):            4,
        dict.get("cups-imp"):           3.3306967385,
        dict.get("pint-us"):            2,
        dict.get("pint-imp"):           1.6653483693,
        #dict.get("quart-us"):          0,
        dict.get("quart-imp"):          0.8326741846,
        dict.get("gallon-us"):          0.25,
        dict.get("gallon-imp"):         0.2081685462,
    },
    "quart-imp" : {
        "quarts (qt - Imperial) is equal to:":      1,
        dict.get("teaspoon-metric"):    227.3045,
        dict.get("tablespoon-metric"):  75.768166667,
        dict.get("floz-us"):            38.430397616,
        dict.get("floz-imp"):           40,
        dict.get("milliliter"):         1136.5225,
        dict.get("liter"):              1.1365225,
        #dict.get("m3"):                0,
        dict.get("in3"):                69.354858198,
        dict.get("ft3"):                0.0401359133,
        dict.get("cups-us"):            4.803799702,
        dict.get("cups-imp"):           4,
        dict.get("pint-us"):            2.401899851,
        dict.get("pint-imp"):           2,
        dict.get("quart-us"):           1.2009499255,
        #dict.get("quart-imp"):         0,
        dict.get("gallon-us"):          0.3002374814,
        dict.get("gallon-imp"):         0.25,
    },
    "gallon-us" : {
        "gallons (gal - US) is equal to:":      1,
        #dict.get("teaspoon-metric"):   0,
        dict.get("tablespoon-metric"):  252.3607856,
        dict.get("floz-us"):            128,
        dict.get("floz-imp"):           133.22786954,
        #dict.get("milliliter"):        0,
        dict.get("liter"):              3.785411784,
        dict.get("m3"):                 0.0037854118,
        dict.get("in3"):                231,
        dict.get("ft3"):                0.1336805556,
        dict.get("cups-us"):            16,
        dict.get("cups-imp"):           13.322786954,
        dict.get("pint-us"):            8,
        dict.get("pint-imp"):           6.661393477,
        dict.get("quart-us"):           4,
        dict.get("quart-imp"):          3.3306967385,
        #dict.get("gallon-us"):         0,
        dict.get("gallon-imp"):         0.8326741846,
    },
    "gallon-imp" : {
        "gallons (gal - Imperial) is equal to:":      1,
        #dict.get("teaspoon-metric"):   0,
        dict.get("tablespoon-metric"):  303.07266667,
        dict.get("floz-us"):            153.72159046,
        dict.get("floz-imp"):           160,
        #dict.get("milliliter"):        0,
        dict.get("liter"):              4.54609,
        dict.get("m3"):                 0.00454609,
        dict.get("in3"):                277.41943279,
        dict.get("ft3"):                0.1605436532,
        dict.get("cups-us"):            19.215198808,
        dict.get("cups-imp"):           16,
        dict.get("pint-us"):            9.607599404,
        dict.get("pint-imp"):           8,
        dict.get("quart-us"):           4.803799702,
        dict.get("quart-imp"):          4,
        dict.get("gallon-us"):          1.2009499255,
        #dict.get("gallon-imp"):        0,
    },

    ### Area
    "cm2" : {
        "square centimeters (cm2) is equal to:":      1,
        #dict.get("cm2"):               0,
        dict.get("m2"):                 0.0001,
        #dict.get("km2"):               0,
        dict.get("in2"):                0.15500031,
        dict.get("ft2"):                0.001076391,
        dict.get("yd2"):                0.000119599,
        #dict.get("mi2"):               0,
        #dict.get("hectare"):           0,
        #dict.get("acre"):              0,
    },
    "m2" : {
        "square meters (m2) is equal to:":      1,
        dict.get("cm2"):                10000,
        #dict.get("m2"):                0,
        dict.get("hectare"):            0.0001,
        dict.get("km2"):                0.000001,
        dict.get("in2"):                1550.0031,
        dict.get("ft2"):                10.763910417,
        dict.get("yd2"):                1.1959900463,
        #dict.get("mi2"):               0,
        dict.get("acre"):               0.0002471054,
    },
    "hectare" : {
        "hectares (ha) is equal to:":    1,
        #dict.get("cm2"):               0,
        dict.get("m2"):                 10000,
        #dict.get("hectare"):           0,
        dict.get("km2"):                0.01,
        #dict.get("in2"):               0,
        #dict.get("ft2"):               0,
        dict.get("yd2"):                11959.900463,
        dict.get("mi2"):                0.0038610216,
        dict.get("acre"):               2.4710538147,
    },
    "km2" : {
        "square kilometers (km2) is equal to:":    1,
        #dict.get("cm2"):               0,
        dict.get("m2"):                 1000000,
        dict.get("hectare"):            100,
        #dict.get("km2"):               0,
        #dict.get("in2"):               0,
        #dict.get("ft2"):               0,
        dict.get("yd2"):                1195990.0463,
        dict.get("mi2"):                0.3861021585,
        dict.get("acre"):               247.10538147,
    },
    "in2" : {
        "square inches (in2) is equal to:":    1,
        dict.get("cm2"):                6.4516,
        dict.get("m2"):                 0.00064516,
        #dict.get("hectare"):           0,
        #dict.get("km2"):               0,
        #dict.get("in2"):               0,
        dict.get("ft2"):                0.0069444444,
        dict.get("yd2"):                0.0007716049,
        #dict.get("mi2"):               0,
        #dict.get("acre"):              0,
    },
    "ft2" : {
        "square feet (ft2) is equal to:":    1,
        dict.get("cm2"):                929.0304,
        dict.get("m2"):                 0.09290304,
        #dict.get("hectare"):           0,
        #dict.get("km2"):               0,
        dict.get("in2"):                144,
        #dict.get("ft2"):               0,
        dict.get("yd2"):                0.1111111111,
        #dict.get("mi2"):               0,
        dict.get("acre"):               0.0000229568,
    },
    "yd2" : {
        "square yards (yd2) is equal to:":    1,
        dict.get("cm2"):                8361.2736,
        dict.get("m2"):                 0.83612736,
        dict.get("hectare"):            0.0000836127,
        #dict.get("km2"):               0,
        dict.get("in2"):                1296,
        dict.get("ft2"):                9,
        #dict.get("yd2"):               0,
        #dict.get("mi2"):               0,
        dict.get("acre"):               0.0002066116,
    },
    "mi2" : {
        "square miles (mi2) is equal to:":    1,
        #dict.get("cm2"):               0,
        dict.get("m2"):                 2589988.1103,
        dict.get("hectare"):            258.99881103,
        dict.get("km2"):                2.5899881103,
        #dict.get("in2"):               0,
        dict.get("ft2"):                27878400,
        dict.get("yd2"):                3097600,
        #dict.get("mi2"):               0,
        dict.get("acre"):               640,
    },
    "acre" : {
        "acres (ac) is equal to:":    1,
        #dict.get("cm2"):               0,
        dict.get("m2"):                 4046.8564224,
        dict.get("hectare"):            0.4046856422,
        dict.get("km2"):                0.0040468564,
        #dict.get("in2"):               0,
        dict.get("ft2"):                43560,
        dict.get("yd2"):                4840,
        dict.get("mi2"):                0.0015625,
        #dict.get("acre"):              0,
    },


}   

def convert_from_unit(fromUnit, quantity):

    items = []

    if fromUnit == "fahrenheit":
        celcius = (quantity - 32) * (5 / 9)
        kelvin = (quantity + 459.67) * (5 / 9)

        items.append(format(quantity,'.2f').rstrip('0').rstrip('.') + ' degrees Fahrenheit (F) is equal to:')
        items.append(format(celcius,'.2f').rstrip('0').rstrip('.') + ' Celcius')
        items.append(format(kelvin,'.2f').rstrip('0').rstrip('.') + ' Kelvin')
    
    elif fromUnit == "celcius":
        farenheit = (quantity * (9 / 5) + 32)
        kelvin = (quantity + 273.15)

        items.append(format(quantity,'.2f').rstrip('0').rstrip('.') + ' degrees Celcius (C) is equal to:')
        items.append(format(farenheit,'.2f').rstrip('0').rstrip('.') + ' Farenheit')
        items.append(format(kelvin,'.2f').rstrip('0').rstrip('.') + ' Kelvin')

    elif fromUnit == "kelvin":
        celcius = (quantity - 273.15)
        fahrenheit = (quantity * (9 / 5) - 459.67)

        items.append(format(quantity,'.2f').rstrip('0').rstrip('.') + ' degrees Kelvin (K) is equal to:')
        items.append(format(celcius,'.2f').rstrip('0').rstrip('.') + ' Celcius')
        items.append(format(fahrenheit,'.2f').rstrip('0').rstrip('.') + ' Fahrenheit')

    else:
        try:
            #sortedUnits = sorted(units[fromUnit].items(), key=lambda x: x[1], reverse=True)
            for key, value in units[fromUnit].items():
                convertedValue = quantity * value
                
                # Control decimals
                if convertedValue > 0.1: 
                    convertedValue = round(convertedValue, 2)

                elif convertedValue > 0.01:
                    convertedValue = round(convertedValue, 3)

                elif convertedValue > 0.001:
                    convertedValue = round(convertedValue, 4)

                elif convertedValue > 0.0001:
                    convertedValue = round(convertedValue, 5)    
                
                items.append(format(convertedValue,'n') + ' ' + key)

        except:
            print("Houston.. etc")

    return items