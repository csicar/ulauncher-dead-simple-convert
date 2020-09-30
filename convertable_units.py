# Input match : unit match
convertableUnits = {
    # Temperature
    "c":            "celcius",
    "celcius":      "celcius",
    "f":            "fahrenheit",
    "fahrenheit":   "fahrenheit",
    "k":            "kelvin",
    "kelvin":       "kelvin",

    # Volume 
    "tsp":          "teaspoon-metric",
    "teaspoon":     "teaspoon-metric",
    "teaspoons":    "teaspoon-metric",
    "tbsp":         "tablespoon-metric",
    "tablespoon":   "tablespoon-metric",
    "tablespoons":  "tablespoon-metric",
    "fl oz":        "floz-us",
    "fl oz us":     "floz-us",
    "fluid ounce":  "floz-us",
    "fluid ounce us":"floz-us",
    "fl oz imp":     "floz-imp",
    "fluid ounce imp":"floz-imp",
    "cup":          "cups-us",
    "cups":         "cups-us",
    "cup us":       "cups-us",
    "cups us":      "cups-us",
    "cup imp":      "cups-imp",
    "cups imp":     "cups-imp",
    "ml":           "milliliter",
    "milliliter":   "milliliter",
    "cm3":          "milliliter",
    "ltr":          "liter",
    "liter":        "liter",
    "m3":           "m3",
    "meter cube":   "m3",
    "cubic meter":  "in3",
    "in3":          "in3",
    "inch cube":    "in3",
    "cubic inch":   "in3",
    "ft3":          "ft3",
    "cubic feet":   "in3",
    "pt":           "pint-us",
    "pint":         "pint-us",
    "pints":        "pint-us",
    "pint us":      "pint-us",
    "pt imp":       "pint-imp",
    "pint imp":     "pint-imp",
    "pints imp":    "pint-imp",
    "qt":           "quart-us",
    "quart":        "quart-us",
    "quart us":     "quart-us",
    "qt imp":       "quart-imp",
    "quart imp":    "quart-imp",
    "gal US":       "gallon-us",
    "gallon":       "gallon-us",
    "gallons US":   "gallon-us",
    "gal imp":      "gallon-imp",
    "gallons imp":  "gallon-imp",
    
    # Weight
    "lb":           "pounds",
    "pound":        "pounds",
    "pounds":       "pounds",
    "oz":           "ounces",
    "ounce":        "ounces",
    "shton":        "short-ton",
    "short ton":    "short-ton", 
    "lton":         "long-ton",
    "long ton":     "long-ton", 
    "g":            "grams",
    "gram":         "grams", 
    "grams":        "grams", 
    "kg":           "kilos",
    "kilo":         "kilos", 
    "kilos":        "kilos",  
    "kilogram":     "kilos",
    "t":            "metric-tonnes", 
    "tonne":        "metric-tonnes", 
    "tonnes":       "metric-tonnes",  
    "metric tonnes":"metric-tonnes",
 
    # Length
    "in":           "inches",
    "inch":         "inches",
    "inches":       "inches",
    "ft":           "feet",
    "foot":         "feet",
    "feet":         "feet",
    "yd":           "yards",
    "yard":         "yards",
    "yards":        "yards",
    "mi":           "miles",
    "mile":         "miles",
    "miles":        "miles",
    "mm":           "millimeters",
    "millimeter":   "millimeters",
    "millimeters":  "millimeters",
    "cm":           "centimeters",
    "centimeter":   "centimeters",
    "centimeters":  "centimeters",
    "m":            "meters",
    "meter":        "meters",
    "meters":       "meters",
    "km":           "kilometers",
    "kilometer":    "kilometers",
    "kilometers":   "kilometers",

    # Area
    "cm2":                  "cm2",
    "cm square":            "cm2",
    "square centimeter":    "cm2",
    "m2":                   "m2",
    "m square":             "m2",
    "square meter":         "m2",
    "km2":                  "m2",
    "km square":            "m2",
    "square kilometer":     "m2", 
    "in2":                  "in2",    
    "in square":            "in2",
    "square inch":          "in2",
    "ft2":                  "ft2",
    "ft square":            "ft2",
    "square foot":          "ft2",
    "yd2":                  "yd2",
    "yd square":            "yd2",
    "square yard":          "yd2",
    "mi2":                  "mi2",
    "square mile":          "mi2",
    "ha":                   "hectare",
    "hectare":              "hectare",
    "ac":                   "acre",    
    "acre":                 "acre",
    
}

def parse_units(input_unit):
    if input_unit in convertableUnits:
        return convertableUnits.get(input_unit)
    else:
        return False


unitsTheWorldShouldJustGetRidOf = {
    "tbsp us":              "tablespoon-us",
    "tablespoon us":        "tablespoon-us",
    "tsp imp":              "teaspoon-imp",
    "teaspoon imp":         "teaspoon-imp",
    "tbsp imp":             "tablespoon-imp",
    "tablespoon imp":       "tablespoon-imp",
    "tsp us":               "teaspoon-us",  
    "teaspoon us":          "teaspoon-us",
    "cup":                  "cups-metric",
    "cups":                 "cups-metric",
}