"""Defines a table with X11 colors.

The key to the dictionary is a string with an X11 name for the color,
the value is either a number (a grayscale value) between 0.0 and 1.0,
or an array of three numbers (RGB values).

The table was generated by the _MakeColorTable function
(defined in this module).
"""

from numpy import array

color_table = {
    'snow':              array([1.0000, 0.9804, 0.9804]),
    'ghost white':       array([0.9725, 0.9725, 1.0000]),
    'GhostWhite':        array([0.9725, 0.9725, 1.0000]),
    'white smoke':       0.9608,
    'WhiteSmoke':        0.9608,
    'gainsboro':         0.8627,
    'floral white':      array([1.0000, 0.9804, 0.9412]),
    'FloralWhite':       array([1.0000, 0.9804, 0.9412]),
    'old lace':          array([0.9922, 0.9608, 0.9020]),
    'OldLace':           array([0.9922, 0.9608, 0.9020]),
    'linen':             array([0.9804, 0.9412, 0.9020]),
    'antique white':     array([0.9804, 0.9216, 0.8431]),
    'AntiqueWhite':      array([0.9804, 0.9216, 0.8431]),
    'papaya whip':       array([1.0000, 0.9373, 0.8353]),
    'PapayaWhip':        array([1.0000, 0.9373, 0.8353]),
    'blanched almond':   array([1.0000, 0.9216, 0.8039]),
    'BlanchedAlmond':    array([1.0000, 0.9216, 0.8039]),
    'bisque':            array([1.0000, 0.8941, 0.7686]),
    'peach puff':        array([1.0000, 0.8549, 0.7255]),
    'PeachPuff':         array([1.0000, 0.8549, 0.7255]),
    'navajo white':      array([1.0000, 0.8706, 0.6784]),
    'NavajoWhite':       array([1.0000, 0.8706, 0.6784]),
    'moccasin':          array([1.0000, 0.8941, 0.7098]),
    'cornsilk':          array([1.0000, 0.9725, 0.8627]),
    'ivory':             array([1.0000, 1.0000, 0.9412]),
    'lemon chiffon':     array([1.0000, 0.9804, 0.8039]),
    'LemonChiffon':      array([1.0000, 0.9804, 0.8039]),
    'seashell':          array([1.0000, 0.9608, 0.9333]),
    'honeydew':          array([0.9412, 1.0000, 0.9412]),
    'mint cream':        array([0.9608, 1.0000, 0.9804]),
    'MintCream':         array([0.9608, 1.0000, 0.9804]),
    'azure':             array([0.9412, 1.0000, 1.0000]),
    'alice blue':        array([0.9412, 0.9725, 1.0000]),
    'AliceBlue':         array([0.9412, 0.9725, 1.0000]),
    'lavender':          array([0.9020, 0.9020, 0.9804]),
    'lavender blush':    array([1.0000, 0.9412, 0.9608]),
    'LavenderBlush':     array([1.0000, 0.9412, 0.9608]),
    'misty rose':        array([1.0000, 0.8941, 0.8824]),
    'MistyRose':         array([1.0000, 0.8941, 0.8824]),
    'white':             1.0000,
    'black':             0.0000,
    'dark slate gray':   array([0.1843, 0.3098, 0.3098]),
    'DarkSlateGray':     array([0.1843, 0.3098, 0.3098]),
    'dark slate grey':   array([0.1843, 0.3098, 0.3098]),
    'DarkSlateGrey':     array([0.1843, 0.3098, 0.3098]),
    'dim gray':          0.4118,
    'DimGray':           0.4118,
    'dim grey':          0.4118,
    'DimGrey':           0.4118,
    'slate gray':        array([0.4392, 0.5020, 0.5647]),
    'SlateGray':         array([0.4392, 0.5020, 0.5647]),
    'slate grey':        array([0.4392, 0.5020, 0.5647]),
    'SlateGrey':         array([0.4392, 0.5020, 0.5647]),
    'light slate gray':  array([0.4667, 0.5333, 0.6000]),
    'LightSlateGray':    array([0.4667, 0.5333, 0.6000]),
    'light slate grey':  array([0.4667, 0.5333, 0.6000]),
    'LightSlateGrey':    array([0.4667, 0.5333, 0.6000]),
    'gray':              0.7451,
    'grey':              0.7451,
    'light grey':        0.8275,
    'LightGrey':         0.8275,
    'light gray':        0.8275,
    'LightGray':         0.8275,
    'midnight blue':     array([0.0980, 0.0980, 0.4392]),
    'MidnightBlue':      array([0.0980, 0.0980, 0.4392]),
    'navy':              array([0.0000, 0.0000, 0.5020]),
    'navy blue':         array([0.0000, 0.0000, 0.5020]),
    'NavyBlue':          array([0.0000, 0.0000, 0.5020]),
    'cornflower blue':   array([0.3922, 0.5843, 0.9294]),
    'CornflowerBlue':    array([0.3922, 0.5843, 0.9294]),
    'dark slate blue':   array([0.2824, 0.2392, 0.5451]),
    'DarkSlateBlue':     array([0.2824, 0.2392, 0.5451]),
    'slate blue':        array([0.4157, 0.3529, 0.8039]),
    'SlateBlue':         array([0.4157, 0.3529, 0.8039]),
    'medium slate blue': array([0.4824, 0.4078, 0.9333]),
    'MediumSlateBlue':   array([0.4824, 0.4078, 0.9333]),
    'light slate blue':  array([0.5176, 0.4392, 1.0000]),
    'LightSlateBlue':    array([0.5176, 0.4392, 1.0000]),
    'medium blue':       array([0.0000, 0.0000, 0.8039]),
    'MediumBlue':        array([0.0000, 0.0000, 0.8039]),
    'royal blue':        array([0.2549, 0.4118, 0.8824]),
    'RoyalBlue':         array([0.2549, 0.4118, 0.8824]),
    'blue':              array([0.0000, 0.0000, 1.0000]),
    'dodger blue':       array([0.1176, 0.5647, 1.0000]),
    'DodgerBlue':        array([0.1176, 0.5647, 1.0000]),
    'deep sky blue':     array([0.0000, 0.7490, 1.0000]),
    'DeepSkyBlue':       array([0.0000, 0.7490, 1.0000]),
    'sky blue':          array([0.5294, 0.8078, 0.9216]),
    'SkyBlue':           array([0.5294, 0.8078, 0.9216]),
    'light sky blue':    array([0.5294, 0.8078, 0.9804]),
    'LightSkyBlue':      array([0.5294, 0.8078, 0.9804]),
    'steel blue':        array([0.2745, 0.5098, 0.7059]),
    'SteelBlue':         array([0.2745, 0.5098, 0.7059]),
    'light steel blue':  array([0.6902, 0.7686, 0.8706]),
    'LightSteelBlue':    array([0.6902, 0.7686, 0.8706]),
    'light blue':        array([0.6784, 0.8471, 0.9020]),
    'LightBlue':         array([0.6784, 0.8471, 0.9020]),
    'powder blue':       array([0.6902, 0.8784, 0.9020]),
    'PowderBlue':        array([0.6902, 0.8784, 0.9020]),
    'pale turquoise':    array([0.6863, 0.9333, 0.9333]),
    'PaleTurquoise':     array([0.6863, 0.9333, 0.9333]),
    'dark turquoise':    array([0.0000, 0.8078, 0.8196]),
    'DarkTurquoise':     array([0.0000, 0.8078, 0.8196]),
    'medium turquoise':  array([0.2824, 0.8196, 0.8000]),
    'MediumTurquoise':   array([0.2824, 0.8196, 0.8000]),
    'turquoise':         array([0.2510, 0.8784, 0.8157]),
    'cyan':              array([0.0000, 1.0000, 1.0000]),
    'light cyan':        array([0.8784, 1.0000, 1.0000]),
    'LightCyan':         array([0.8784, 1.0000, 1.0000]),
    'cadet blue':        array([0.3725, 0.6196, 0.6275]),
    'CadetBlue':         array([0.3725, 0.6196, 0.6275]),
    'medium aquamarine': array([0.4000, 0.8039, 0.6667]),
    'MediumAquamarine':  array([0.4000, 0.8039, 0.6667]),
    'aquamarine':        array([0.4980, 1.0000, 0.8314]),
    'dark green':        array([0.0000, 0.3922, 0.0000]),
    'DarkGreen':         array([0.0000, 0.3922, 0.0000]),
    'dark olive green':  array([0.3333, 0.4196, 0.1843]),
    'DarkOliveGreen':    array([0.3333, 0.4196, 0.1843]),
    'dark sea green':    array([0.5608, 0.7373, 0.5608]),
    'DarkSeaGreen':      array([0.5608, 0.7373, 0.5608]),
    'sea green':         array([0.1804, 0.5451, 0.3412]),
    'SeaGreen':          array([0.1804, 0.5451, 0.3412]),
    'medium sea green':  array([0.2353, 0.7020, 0.4431]),
    'MediumSeaGreen':    array([0.2353, 0.7020, 0.4431]),
    'light sea green':   array([0.1255, 0.6980, 0.6667]),
    'LightSeaGreen':     array([0.1255, 0.6980, 0.6667]),
    'pale green':        array([0.5961, 0.9843, 0.5961]),
    'PaleGreen':         array([0.5961, 0.9843, 0.5961]),
    'spring green':      array([0.0000, 1.0000, 0.4980]),
    'SpringGreen':       array([0.0000, 1.0000, 0.4980]),
    'lawn green':        array([0.4863, 0.9882, 0.0000]),
    'LawnGreen':         array([0.4863, 0.9882, 0.0000]),
    'green':             array([0.0000, 1.0000, 0.0000]),
    'chartreuse':        array([0.4980, 1.0000, 0.0000]),
    'medium spring green': array([0.0000, 0.9804, 0.6039]),
    'MediumSpringGreen': array([0.0000, 0.9804, 0.6039]),
    'green yellow':      array([0.6784, 1.0000, 0.1843]),
    'GreenYellow':       array([0.6784, 1.0000, 0.1843]),
    'lime green':        array([0.1961, 0.8039, 0.1961]),
    'LimeGreen':         array([0.1961, 0.8039, 0.1961]),
    'yellow green':      array([0.6039, 0.8039, 0.1961]),
    'YellowGreen':       array([0.6039, 0.8039, 0.1961]),
    'forest green':      array([0.1333, 0.5451, 0.1333]),
    'ForestGreen':       array([0.1333, 0.5451, 0.1333]),
    'olive drab':        array([0.4196, 0.5569, 0.1373]),
    'OliveDrab':         array([0.4196, 0.5569, 0.1373]),
    'dark khaki':        array([0.7412, 0.7176, 0.4196]),
    'DarkKhaki':         array([0.7412, 0.7176, 0.4196]),
    'khaki':             array([0.9412, 0.9020, 0.5490]),
    'pale goldenrod':    array([0.9333, 0.9098, 0.6667]),
    'PaleGoldenrod':     array([0.9333, 0.9098, 0.6667]),
    'light goldenrod yellow': array([0.9804, 0.9804, 0.8235]),
    'LightGoldenrodYellow': array([0.9804, 0.9804, 0.8235]),
    'light yellow':      array([1.0000, 1.0000, 0.8784]),
    'LightYellow':       array([1.0000, 1.0000, 0.8784]),
    'yellow':            array([1.0000, 1.0000, 0.0000]),
    'gold':              array([1.0000, 0.8431, 0.0000]),
    'light goldenrod':   array([0.9333, 0.8667, 0.5098]),
    'LightGoldenrod':    array([0.9333, 0.8667, 0.5098]),
    'goldenrod':         array([0.8549, 0.6471, 0.1255]),
    'dark goldenrod':    array([0.7216, 0.5255, 0.0431]),
    'DarkGoldenrod':     array([0.7216, 0.5255, 0.0431]),
    'rosy brown':        array([0.7373, 0.5608, 0.5608]),
    'RosyBrown':         array([0.7373, 0.5608, 0.5608]),
    'indian red':        array([0.8039, 0.3608, 0.3608]),
    'IndianRed':         array([0.8039, 0.3608, 0.3608]),
    'saddle brown':      array([0.5451, 0.2706, 0.0745]),
    'SaddleBrown':       array([0.5451, 0.2706, 0.0745]),
    'sienna':            array([0.6275, 0.3216, 0.1765]),
    'peru':              array([0.8039, 0.5216, 0.2471]),
    'burlywood':         array([0.8706, 0.7216, 0.5294]),
    'beige':             array([0.9608, 0.9608, 0.8627]),
    'wheat':             array([0.9608, 0.8706, 0.7020]),
    'sandy brown':       array([0.9569, 0.6431, 0.3765]),
    'SandyBrown':        array([0.9569, 0.6431, 0.3765]),
    'tan':               array([0.8235, 0.7059, 0.5490]),
    'chocolate':         array([0.8235, 0.4118, 0.1176]),
    'firebrick':         array([0.6980, 0.1333, 0.1333]),
    'brown':             array([0.6471, 0.1647, 0.1647]),
    'dark salmon':       array([0.9137, 0.5882, 0.4784]),
    'DarkSalmon':        array([0.9137, 0.5882, 0.4784]),
    'salmon':            array([0.9804, 0.5020, 0.4471]),
    'light salmon':      array([1.0000, 0.6275, 0.4784]),
    'LightSalmon':       array([1.0000, 0.6275, 0.4784]),
    'orange':            array([1.0000, 0.6471, 0.0000]),
    'dark orange':       array([1.0000, 0.5490, 0.0000]),
    'DarkOrange':        array([1.0000, 0.5490, 0.0000]),
    'coral':             array([1.0000, 0.4980, 0.3137]),
    'light coral':       array([0.9412, 0.5020, 0.5020]),
    'LightCoral':        array([0.9412, 0.5020, 0.5020]),
    'tomato':            array([1.0000, 0.3882, 0.2784]),
    'orange red':        array([1.0000, 0.2706, 0.0000]),
    'OrangeRed':         array([1.0000, 0.2706, 0.0000]),
    'red':               array([1.0000, 0.0000, 0.0000]),
    'hot pink':          array([1.0000, 0.4118, 0.7059]),
    'HotPink':           array([1.0000, 0.4118, 0.7059]),
    'deep pink':         array([1.0000, 0.0784, 0.5765]),
    'DeepPink':          array([1.0000, 0.0784, 0.5765]),
    'pink':              array([1.0000, 0.7529, 0.7961]),
    'light pink':        array([1.0000, 0.7137, 0.7569]),
    'LightPink':         array([1.0000, 0.7137, 0.7569]),
    'pale violet red':   array([0.8588, 0.4392, 0.5765]),
    'PaleVioletRed':     array([0.8588, 0.4392, 0.5765]),
    'maroon':            array([0.6902, 0.1882, 0.3765]),
    'medium violet red': array([0.7804, 0.0824, 0.5216]),
    'MediumVioletRed':   array([0.7804, 0.0824, 0.5216]),
    'violet red':        array([0.8157, 0.1255, 0.5647]),
    'VioletRed':         array([0.8157, 0.1255, 0.5647]),
    'magenta':           array([1.0000, 0.0000, 1.0000]),
    'violet':            array([0.9333, 0.5098, 0.9333]),
    'plum':              array([0.8667, 0.6275, 0.8667]),
    'orchid':            array([0.8549, 0.4392, 0.8392]),
    'medium orchid':     array([0.7294, 0.3333, 0.8275]),
    'MediumOrchid':      array([0.7294, 0.3333, 0.8275]),
    'dark orchid':       array([0.6000, 0.1961, 0.8000]),
    'DarkOrchid':        array([0.6000, 0.1961, 0.8000]),
    'dark violet':       array([0.5804, 0.0000, 0.8275]),
    'DarkViolet':        array([0.5804, 0.0000, 0.8275]),
    'blue violet':       array([0.5412, 0.1686, 0.8863]),
    'BlueViolet':        array([0.5412, 0.1686, 0.8863]),
    'purple':            array([0.6275, 0.1255, 0.9412]),
    'medium purple':     array([0.5765, 0.4392, 0.8588]),
    'MediumPurple':      array([0.5765, 0.4392, 0.8588]),
    'thistle':           array([0.8471, 0.7490, 0.8471]),
    'snow1':             array([1.0000, 0.9804, 0.9804]),
    'snow2':             array([0.9333, 0.9137, 0.9137]),
    'snow3':             array([0.8039, 0.7882, 0.7882]),
    'snow4':             array([0.5451, 0.5373, 0.5373]),
    'seashell1':         array([1.0000, 0.9608, 0.9333]),
    'seashell2':         array([0.9333, 0.8980, 0.8706]),
    'seashell3':         array([0.8039, 0.7725, 0.7490]),
    'seashell4':         array([0.5451, 0.5255, 0.5098]),
    'AntiqueWhite1':     array([1.0000, 0.9373, 0.8588]),
    'AntiqueWhite2':     array([0.9333, 0.8745, 0.8000]),
    'AntiqueWhite3':     array([0.8039, 0.7529, 0.6902]),
    'AntiqueWhite4':     array([0.5451, 0.5137, 0.4706]),
    'bisque1':           array([1.0000, 0.8941, 0.7686]),
    'bisque2':           array([0.9333, 0.8353, 0.7176]),
    'bisque3':           array([0.8039, 0.7176, 0.6196]),
    'bisque4':           array([0.5451, 0.4902, 0.4196]),
    'PeachPuff1':        array([1.0000, 0.8549, 0.7255]),
    'PeachPuff2':        array([0.9333, 0.7961, 0.6784]),
    'PeachPuff3':        array([0.8039, 0.6863, 0.5843]),
    'PeachPuff4':        array([0.5451, 0.4667, 0.3961]),
    'NavajoWhite1':      array([1.0000, 0.8706, 0.6784]),
    'NavajoWhite2':      array([0.9333, 0.8118, 0.6314]),
    'NavajoWhite3':      array([0.8039, 0.7020, 0.5451]),
    'NavajoWhite4':      array([0.5451, 0.4745, 0.3686]),
    'LemonChiffon1':     array([1.0000, 0.9804, 0.8039]),
    'LemonChiffon2':     array([0.9333, 0.9137, 0.7490]),
    'LemonChiffon3':     array([0.8039, 0.7882, 0.6471]),
    'LemonChiffon4':     array([0.5451, 0.5373, 0.4392]),
    'cornsilk1':         array([1.0000, 0.9725, 0.8627]),
    'cornsilk2':         array([0.9333, 0.9098, 0.8039]),
    'cornsilk3':         array([0.8039, 0.7843, 0.6941]),
    'cornsilk4':         array([0.5451, 0.5333, 0.4706]),
    'ivory1':            array([1.0000, 1.0000, 0.9412]),
    'ivory2':            array([0.9333, 0.9333, 0.8784]),
    'ivory3':            array([0.8039, 0.8039, 0.7569]),
    'ivory4':            array([0.5451, 0.5451, 0.5137]),
    'honeydew1':         array([0.9412, 1.0000, 0.9412]),
    'honeydew2':         array([0.8784, 0.9333, 0.8784]),
    'honeydew3':         array([0.7569, 0.8039, 0.7569]),
    'honeydew4':         array([0.5137, 0.5451, 0.5137]),
    'LavenderBlush1':    array([1.0000, 0.9412, 0.9608]),
    'LavenderBlush2':    array([0.9333, 0.8784, 0.8980]),
    'LavenderBlush3':    array([0.8039, 0.7569, 0.7725]),
    'LavenderBlush4':    array([0.5451, 0.5137, 0.5255]),
    'MistyRose1':        array([1.0000, 0.8941, 0.8824]),
    'MistyRose2':        array([0.9333, 0.8353, 0.8235]),
    'MistyRose3':        array([0.8039, 0.7176, 0.7098]),
    'MistyRose4':        array([0.5451, 0.4902, 0.4824]),
    'azure1':            array([0.9412, 1.0000, 1.0000]),
    'azure2':            array([0.8784, 0.9333, 0.9333]),
    'azure3':            array([0.7569, 0.8039, 0.8039]),
    'azure4':            array([0.5137, 0.5451, 0.5451]),
    'SlateBlue1':        array([0.5137, 0.4353, 1.0000]),
    'SlateBlue2':        array([0.4784, 0.4039, 0.9333]),
    'SlateBlue3':        array([0.4118, 0.3490, 0.8039]),
    'SlateBlue4':        array([0.2784, 0.2353, 0.5451]),
    'RoyalBlue1':        array([0.2824, 0.4627, 1.0000]),
    'RoyalBlue2':        array([0.2627, 0.4314, 0.9333]),
    'RoyalBlue3':        array([0.2275, 0.3725, 0.8039]),
    'RoyalBlue4':        array([0.1529, 0.2510, 0.5451]),
    'blue1':             array([0.0000, 0.0000, 1.0000]),
    'blue2':             array([0.0000, 0.0000, 0.9333]),
    'blue3':             array([0.0000, 0.0000, 0.8039]),
    'blue4':             array([0.0000, 0.0000, 0.5451]),
    'DodgerBlue1':       array([0.1176, 0.5647, 1.0000]),
    'DodgerBlue2':       array([0.1098, 0.5255, 0.9333]),
    'DodgerBlue3':       array([0.0941, 0.4549, 0.8039]),
    'DodgerBlue4':       array([0.0627, 0.3059, 0.5451]),
    'SteelBlue1':        array([0.3882, 0.7216, 1.0000]),
    'SteelBlue2':        array([0.3608, 0.6745, 0.9333]),
    'SteelBlue3':        array([0.3098, 0.5804, 0.8039]),
    'SteelBlue4':        array([0.2118, 0.3922, 0.5451]),
    'DeepSkyBlue1':      array([0.0000, 0.7490, 1.0000]),
    'DeepSkyBlue2':      array([0.0000, 0.6980, 0.9333]),
    'DeepSkyBlue3':      array([0.0000, 0.6039, 0.8039]),
    'DeepSkyBlue4':      array([0.0000, 0.4078, 0.5451]),
    'SkyBlue1':          array([0.5294, 0.8078, 1.0000]),
    'SkyBlue2':          array([0.4941, 0.7529, 0.9333]),
    'SkyBlue3':          array([0.4235, 0.6510, 0.8039]),
    'SkyBlue4':          array([0.2902, 0.4392, 0.5451]),
    'LightSkyBlue1':     array([0.6902, 0.8863, 1.0000]),
    'LightSkyBlue2':     array([0.6431, 0.8275, 0.9333]),
    'LightSkyBlue3':     array([0.5529, 0.7137, 0.8039]),
    'LightSkyBlue4':     array([0.3765, 0.4824, 0.5451]),
    'SlateGray1':        array([0.7765, 0.8863, 1.0000]),
    'SlateGray2':        array([0.7255, 0.8275, 0.9333]),
    'SlateGray3':        array([0.6235, 0.7137, 0.8039]),
    'SlateGray4':        array([0.4235, 0.4824, 0.5451]),
    'LightSteelBlue1':   array([0.7922, 0.8824, 1.0000]),
    'LightSteelBlue2':   array([0.7373, 0.8235, 0.9333]),
    'LightSteelBlue3':   array([0.6353, 0.7098, 0.8039]),
    'LightSteelBlue4':   array([0.4314, 0.4824, 0.5451]),
    'LightBlue1':        array([0.7490, 0.9373, 1.0000]),
    'LightBlue2':        array([0.6980, 0.8745, 0.9333]),
    'LightBlue3':        array([0.6039, 0.7529, 0.8039]),
    'LightBlue4':        array([0.4078, 0.5137, 0.5451]),
    'LightCyan1':        array([0.8784, 1.0000, 1.0000]),
    'LightCyan2':        array([0.8196, 0.9333, 0.9333]),
    'LightCyan3':        array([0.7059, 0.8039, 0.8039]),
    'LightCyan4':        array([0.4784, 0.5451, 0.5451]),
    'PaleTurquoise1':    array([0.7333, 1.0000, 1.0000]),
    'PaleTurquoise2':    array([0.6824, 0.9333, 0.9333]),
    'PaleTurquoise3':    array([0.5882, 0.8039, 0.8039]),
    'PaleTurquoise4':    array([0.4000, 0.5451, 0.5451]),
    'CadetBlue1':        array([0.5961, 0.9608, 1.0000]),
    'CadetBlue2':        array([0.5569, 0.8980, 0.9333]),
    'CadetBlue3':        array([0.4784, 0.7725, 0.8039]),
    'CadetBlue4':        array([0.3255, 0.5255, 0.5451]),
    'turquoise1':        array([0.0000, 0.9608, 1.0000]),
    'turquoise2':        array([0.0000, 0.8980, 0.9333]),
    'turquoise3':        array([0.0000, 0.7725, 0.8039]),
    'turquoise4':        array([0.0000, 0.5255, 0.5451]),
    'cyan1':             array([0.0000, 1.0000, 1.0000]),
    'cyan2':             array([0.0000, 0.9333, 0.9333]),
    'cyan3':             array([0.0000, 0.8039, 0.8039]),
    'cyan4':             array([0.0000, 0.5451, 0.5451]),
    'DarkSlateGray1':    array([0.5922, 1.0000, 1.0000]),
    'DarkSlateGray2':    array([0.5529, 0.9333, 0.9333]),
    'DarkSlateGray3':    array([0.4745, 0.8039, 0.8039]),
    'DarkSlateGray4':    array([0.3216, 0.5451, 0.5451]),
    'aquamarine1':       array([0.4980, 1.0000, 0.8314]),
    'aquamarine2':       array([0.4627, 0.9333, 0.7765]),
    'aquamarine3':       array([0.4000, 0.8039, 0.6667]),
    'aquamarine4':       array([0.2706, 0.5451, 0.4549]),
    'DarkSeaGreen1':     array([0.7569, 1.0000, 0.7569]),
    'DarkSeaGreen2':     array([0.7059, 0.9333, 0.7059]),
    'DarkSeaGreen3':     array([0.6078, 0.8039, 0.6078]),
    'DarkSeaGreen4':     array([0.4118, 0.5451, 0.4118]),
    'SeaGreen1':         array([0.3294, 1.0000, 0.6235]),
    'SeaGreen2':         array([0.3059, 0.9333, 0.5804]),
    'SeaGreen3':         array([0.2627, 0.8039, 0.5020]),
    'SeaGreen4':         array([0.1804, 0.5451, 0.3412]),
    'PaleGreen1':        array([0.6039, 1.0000, 0.6039]),
    'PaleGreen2':        array([0.5647, 0.9333, 0.5647]),
    'PaleGreen3':        array([0.4863, 0.8039, 0.4863]),
    'PaleGreen4':        array([0.3294, 0.5451, 0.3294]),
    'SpringGreen1':      array([0.0000, 1.0000, 0.4980]),
    'SpringGreen2':      array([0.0000, 0.9333, 0.4627]),
    'SpringGreen3':      array([0.0000, 0.8039, 0.4000]),
    'SpringGreen4':      array([0.0000, 0.5451, 0.2706]),
    'green1':            array([0.0000, 1.0000, 0.0000]),
    'green2':            array([0.0000, 0.9333, 0.0000]),
    'green3':            array([0.0000, 0.8039, 0.0000]),
    'green4':            array([0.0000, 0.5451, 0.0000]),
    'chartreuse1':       array([0.4980, 1.0000, 0.0000]),
    'chartreuse2':       array([0.4627, 0.9333, 0.0000]),
    'chartreuse3':       array([0.4000, 0.8039, 0.0000]),
    'chartreuse4':       array([0.2706, 0.5451, 0.0000]),
    'OliveDrab1':        array([0.7529, 1.0000, 0.2431]),
    'OliveDrab2':        array([0.7020, 0.9333, 0.2275]),
    'OliveDrab3':        array([0.6039, 0.8039, 0.1961]),
    'OliveDrab4':        array([0.4118, 0.5451, 0.1333]),
    'DarkOliveGreen1':   array([0.7922, 1.0000, 0.4392]),
    'DarkOliveGreen2':   array([0.7373, 0.9333, 0.4078]),
    'DarkOliveGreen3':   array([0.6353, 0.8039, 0.3529]),
    'DarkOliveGreen4':   array([0.4314, 0.5451, 0.2392]),
    'khaki1':            array([1.0000, 0.9647, 0.5608]),
    'khaki2':            array([0.9333, 0.9020, 0.5216]),
    'khaki3':            array([0.8039, 0.7765, 0.4510]),
    'khaki4':            array([0.5451, 0.5255, 0.3059]),
    'LightGoldenrod1':   array([1.0000, 0.9255, 0.5451]),
    'LightGoldenrod2':   array([0.9333, 0.8627, 0.5098]),
    'LightGoldenrod3':   array([0.8039, 0.7451, 0.4392]),
    'LightGoldenrod4':   array([0.5451, 0.5059, 0.2980]),
    'LightYellow1':      array([1.0000, 1.0000, 0.8784]),
    'LightYellow2':      array([0.9333, 0.9333, 0.8196]),
    'LightYellow3':      array([0.8039, 0.8039, 0.7059]),
    'LightYellow4':      array([0.5451, 0.5451, 0.4784]),
    'yellow1':           array([1.0000, 1.0000, 0.0000]),
    'yellow2':           array([0.9333, 0.9333, 0.0000]),
    'yellow3':           array([0.8039, 0.8039, 0.0000]),
    'yellow4':           array([0.5451, 0.5451, 0.0000]),
    'gold1':             array([1.0000, 0.8431, 0.0000]),
    'gold2':             array([0.9333, 0.7882, 0.0000]),
    'gold3':             array([0.8039, 0.6784, 0.0000]),
    'gold4':             array([0.5451, 0.4588, 0.0000]),
    'goldenrod1':        array([1.0000, 0.7569, 0.1451]),
    'goldenrod2':        array([0.9333, 0.7059, 0.1333]),
    'goldenrod3':        array([0.8039, 0.6078, 0.1137]),
    'goldenrod4':        array([0.5451, 0.4118, 0.0784]),
    'DarkGoldenrod1':    array([1.0000, 0.7255, 0.0588]),
    'DarkGoldenrod2':    array([0.9333, 0.6784, 0.0549]),
    'DarkGoldenrod3':    array([0.8039, 0.5843, 0.0471]),
    'DarkGoldenrod4':    array([0.5451, 0.3961, 0.0314]),
    'RosyBrown1':        array([1.0000, 0.7569, 0.7569]),
    'RosyBrown2':        array([0.9333, 0.7059, 0.7059]),
    'RosyBrown3':        array([0.8039, 0.6078, 0.6078]),
    'RosyBrown4':        array([0.5451, 0.4118, 0.4118]),
    'IndianRed1':        array([1.0000, 0.4157, 0.4157]),
    'IndianRed2':        array([0.9333, 0.3882, 0.3882]),
    'IndianRed3':        array([0.8039, 0.3333, 0.3333]),
    'IndianRed4':        array([0.5451, 0.2275, 0.2275]),
    'sienna1':           array([1.0000, 0.5098, 0.2784]),
    'sienna2':           array([0.9333, 0.4745, 0.2588]),
    'sienna3':           array([0.8039, 0.4078, 0.2235]),
    'sienna4':           array([0.5451, 0.2784, 0.1490]),
    'burlywood1':        array([1.0000, 0.8275, 0.6078]),
    'burlywood2':        array([0.9333, 0.7725, 0.5686]),
    'burlywood3':        array([0.8039, 0.6667, 0.4902]),
    'burlywood4':        array([0.5451, 0.4510, 0.3333]),
    'wheat1':            array([1.0000, 0.9059, 0.7294]),
    'wheat2':            array([0.9333, 0.8471, 0.6824]),
    'wheat3':            array([0.8039, 0.7294, 0.5882]),
    'wheat4':            array([0.5451, 0.4941, 0.4000]),
    'tan1':              array([1.0000, 0.6471, 0.3098]),
    'tan2':              array([0.9333, 0.6039, 0.2863]),
    'tan3':              array([0.8039, 0.5216, 0.2471]),
    'tan4':              array([0.5451, 0.3529, 0.1686]),
    'chocolate1':        array([1.0000, 0.4980, 0.1412]),
    'chocolate2':        array([0.9333, 0.4627, 0.1294]),
    'chocolate3':        array([0.8039, 0.4000, 0.1137]),
    'chocolate4':        array([0.5451, 0.2706, 0.0745]),
    'firebrick1':        array([1.0000, 0.1882, 0.1882]),
    'firebrick2':        array([0.9333, 0.1725, 0.1725]),
    'firebrick3':        array([0.8039, 0.1490, 0.1490]),
    'firebrick4':        array([0.5451, 0.1020, 0.1020]),
    'brown1':            array([1.0000, 0.2510, 0.2510]),
    'brown2':            array([0.9333, 0.2314, 0.2314]),
    'brown3':            array([0.8039, 0.2000, 0.2000]),
    'brown4':            array([0.5451, 0.1373, 0.1373]),
    'salmon1':           array([1.0000, 0.5490, 0.4118]),
    'salmon2':           array([0.9333, 0.5098, 0.3843]),
    'salmon3':           array([0.8039, 0.4392, 0.3294]),
    'salmon4':           array([0.5451, 0.2980, 0.2235]),
    'LightSalmon1':      array([1.0000, 0.6275, 0.4784]),
    'LightSalmon2':      array([0.9333, 0.5843, 0.4471]),
    'LightSalmon3':      array([0.8039, 0.5059, 0.3843]),
    'LightSalmon4':      array([0.5451, 0.3412, 0.2588]),
    'orange1':           array([1.0000, 0.6471, 0.0000]),
    'orange2':           array([0.9333, 0.6039, 0.0000]),
    'orange3':           array([0.8039, 0.5216, 0.0000]),
    'orange4':           array([0.5451, 0.3529, 0.0000]),
    'DarkOrange1':       array([1.0000, 0.4980, 0.0000]),
    'DarkOrange2':       array([0.9333, 0.4627, 0.0000]),
    'DarkOrange3':       array([0.8039, 0.4000, 0.0000]),
    'DarkOrange4':       array([0.5451, 0.2706, 0.0000]),
    'coral1':            array([1.0000, 0.4471, 0.3373]),
    'coral2':            array([0.9333, 0.4157, 0.3137]),
    'coral3':            array([0.8039, 0.3569, 0.2706]),
    'coral4':            array([0.5451, 0.2431, 0.1843]),
    'tomato1':           array([1.0000, 0.3882, 0.2784]),
    'tomato2':           array([0.9333, 0.3608, 0.2588]),
    'tomato3':           array([0.8039, 0.3098, 0.2235]),
    'tomato4':           array([0.5451, 0.2118, 0.1490]),
    'OrangeRed1':        array([1.0000, 0.2706, 0.0000]),
    'OrangeRed2':        array([0.9333, 0.2510, 0.0000]),
    'OrangeRed3':        array([0.8039, 0.2157, 0.0000]),
    'OrangeRed4':        array([0.5451, 0.1451, 0.0000]),
    'red1':              array([1.0000, 0.0000, 0.0000]),
    'red2':              array([0.9333, 0.0000, 0.0000]),
    'red3':              array([0.8039, 0.0000, 0.0000]),
    'red4':              array([0.5451, 0.0000, 0.0000]),
    'DeepPink1':         array([1.0000, 0.0784, 0.5765]),
    'DeepPink2':         array([0.9333, 0.0706, 0.5373]),
    'DeepPink3':         array([0.8039, 0.0627, 0.4627]),
    'DeepPink4':         array([0.5451, 0.0392, 0.3137]),
    'HotPink1':          array([1.0000, 0.4314, 0.7059]),
    'HotPink2':          array([0.9333, 0.4157, 0.6549]),
    'HotPink3':          array([0.8039, 0.3765, 0.5647]),
    'HotPink4':          array([0.5451, 0.2275, 0.3843]),
    'pink1':             array([1.0000, 0.7098, 0.7725]),
    'pink2':             array([0.9333, 0.6627, 0.7216]),
    'pink3':             array([0.8039, 0.5686, 0.6196]),
    'pink4':             array([0.5451, 0.3882, 0.4235]),
    'LightPink1':        array([1.0000, 0.6824, 0.7255]),
    'LightPink2':        array([0.9333, 0.6353, 0.6784]),
    'LightPink3':        array([0.8039, 0.5490, 0.5843]),
    'LightPink4':        array([0.5451, 0.3725, 0.3961]),
    'PaleVioletRed1':    array([1.0000, 0.5098, 0.6706]),
    'PaleVioletRed2':    array([0.9333, 0.4745, 0.6235]),
    'PaleVioletRed3':    array([0.8039, 0.4078, 0.5373]),
    'PaleVioletRed4':    array([0.5451, 0.2784, 0.3647]),
    'maroon1':           array([1.0000, 0.2039, 0.7020]),
    'maroon2':           array([0.9333, 0.1882, 0.6549]),
    'maroon3':           array([0.8039, 0.1608, 0.5647]),
    'maroon4':           array([0.5451, 0.1098, 0.3843]),
    'VioletRed1':        array([1.0000, 0.2431, 0.5882]),
    'VioletRed2':        array([0.9333, 0.2275, 0.5490]),
    'VioletRed3':        array([0.8039, 0.1961, 0.4706]),
    'VioletRed4':        array([0.5451, 0.1333, 0.3216]),
    'magenta1':          array([1.0000, 0.0000, 1.0000]),
    'magenta2':          array([0.9333, 0.0000, 0.9333]),
    'magenta3':          array([0.8039, 0.0000, 0.8039]),
    'magenta4':          array([0.5451, 0.0000, 0.5451]),
    'orchid1':           array([1.0000, 0.5137, 0.9804]),
    'orchid2':           array([0.9333, 0.4784, 0.9137]),
    'orchid3':           array([0.8039, 0.4118, 0.7882]),
    'orchid4':           array([0.5451, 0.2784, 0.5373]),
    'plum1':             array([1.0000, 0.7333, 1.0000]),
    'plum2':             array([0.9333, 0.6824, 0.9333]),
    'plum3':             array([0.8039, 0.5882, 0.8039]),
    'plum4':             array([0.5451, 0.4000, 0.5451]),
    'MediumOrchid1':     array([0.8784, 0.4000, 1.0000]),
    'MediumOrchid2':     array([0.8196, 0.3725, 0.9333]),
    'MediumOrchid3':     array([0.7059, 0.3216, 0.8039]),
    'MediumOrchid4':     array([0.4784, 0.2157, 0.5451]),
    'DarkOrchid1':       array([0.7490, 0.2431, 1.0000]),
    'DarkOrchid2':       array([0.6980, 0.2275, 0.9333]),
    'DarkOrchid3':       array([0.6039, 0.1961, 0.8039]),
    'DarkOrchid4':       array([0.4078, 0.1333, 0.5451]),
    'purple1':           array([0.6078, 0.1882, 1.0000]),
    'purple2':           array([0.5686, 0.1725, 0.9333]),
    'purple3':           array([0.4902, 0.1490, 0.8039]),
    'purple4':           array([0.3333, 0.1020, 0.5451]),
    'MediumPurple1':     array([0.6706, 0.5098, 1.0000]),
    'MediumPurple2':     array([0.6235, 0.4745, 0.9333]),
    'MediumPurple3':     array([0.5373, 0.4078, 0.8039]),
    'MediumPurple4':     array([0.3647, 0.2784, 0.5451]),
    'thistle1':          array([1.0000, 0.8824, 1.0000]),
    'thistle2':          array([0.9333, 0.8235, 0.9333]),
    'thistle3':          array([0.8039, 0.7098, 0.8039]),
    'thistle4':          array([0.5451, 0.4824, 0.5451]),
    'gray0':             0.0000,
    'grey0':             0.0000,
    'gray1':             0.0118,
    'grey1':             0.0118,
    'gray2':             0.0196,
    'grey2':             0.0196,
    'gray3':             0.0314,
    'grey3':             0.0314,
    'gray4':             0.0392,
    'grey4':             0.0392,
    'gray5':             0.0510,
    'grey5':             0.0510,
    'gray6':             0.0588,
    'grey6':             0.0588,
    'gray7':             0.0706,
    'grey7':             0.0706,
    'gray8':             0.0784,
    'grey8':             0.0784,
    'gray9':             0.0902,
    'grey9':             0.0902,
    'gray10':            0.1020,
    'grey10':            0.1020,
    'gray11':            0.1098,
    'grey11':            0.1098,
    'gray12':            0.1216,
    'grey12':            0.1216,
    'gray13':            0.1294,
    'grey13':            0.1294,
    'gray14':            0.1412,
    'grey14':            0.1412,
    'gray15':            0.1490,
    'grey15':            0.1490,
    'gray16':            0.1608,
    'grey16':            0.1608,
    'gray17':            0.1686,
    'grey17':            0.1686,
    'gray18':            0.1804,
    'grey18':            0.1804,
    'gray19':            0.1882,
    'grey19':            0.1882,
    'gray20':            0.2000,
    'grey20':            0.2000,
    'gray21':            0.2118,
    'grey21':            0.2118,
    'gray22':            0.2196,
    'grey22':            0.2196,
    'gray23':            0.2314,
    'grey23':            0.2314,
    'gray24':            0.2392,
    'grey24':            0.2392,
    'gray25':            0.2510,
    'grey25':            0.2510,
    'gray26':            0.2588,
    'grey26':            0.2588,
    'gray27':            0.2706,
    'grey27':            0.2706,
    'gray28':            0.2784,
    'grey28':            0.2784,
    'gray29':            0.2902,
    'grey29':            0.2902,
    'gray30':            0.3020,
    'grey30':            0.3020,
    'gray31':            0.3098,
    'grey31':            0.3098,
    'gray32':            0.3216,
    'grey32':            0.3216,
    'gray33':            0.3294,
    'grey33':            0.3294,
    'gray34':            0.3412,
    'grey34':            0.3412,
    'gray35':            0.3490,
    'grey35':            0.3490,
    'gray36':            0.3608,
    'grey36':            0.3608,
    'gray37':            0.3686,
    'grey37':            0.3686,
    'gray38':            0.3804,
    'grey38':            0.3804,
    'gray39':            0.3882,
    'grey39':            0.3882,
    'gray40':            0.4000,
    'grey40':            0.4000,
    'gray41':            0.4118,
    'grey41':            0.4118,
    'gray42':            0.4196,
    'grey42':            0.4196,
    'gray43':            0.4314,
    'grey43':            0.4314,
    'gray44':            0.4392,
    'grey44':            0.4392,
    'gray45':            0.4510,
    'grey45':            0.4510,
    'gray46':            0.4588,
    'grey46':            0.4588,
    'gray47':            0.4706,
    'grey47':            0.4706,
    'gray48':            0.4784,
    'grey48':            0.4784,
    'gray49':            0.4902,
    'grey49':            0.4902,
    'gray50':            0.4980,
    'grey50':            0.4980,
    'gray51':            0.5098,
    'grey51':            0.5098,
    'gray52':            0.5216,
    'grey52':            0.5216,
    'gray53':            0.5294,
    'grey53':            0.5294,
    'gray54':            0.5412,
    'grey54':            0.5412,
    'gray55':            0.5490,
    'grey55':            0.5490,
    'gray56':            0.5608,
    'grey56':            0.5608,
    'gray57':            0.5686,
    'grey57':            0.5686,
    'gray58':            0.5804,
    'grey58':            0.5804,
    'gray59':            0.5882,
    'grey59':            0.5882,
    'gray60':            0.6000,
    'grey60':            0.6000,
    'gray61':            0.6118,
    'grey61':            0.6118,
    'gray62':            0.6196,
    'grey62':            0.6196,
    'gray63':            0.6314,
    'grey63':            0.6314,
    'gray64':            0.6392,
    'grey64':            0.6392,
    'gray65':            0.6510,
    'grey65':            0.6510,
    'gray66':            0.6588,
    'grey66':            0.6588,
    'gray67':            0.6706,
    'grey67':            0.6706,
    'gray68':            0.6784,
    'grey68':            0.6784,
    'gray69':            0.6902,
    'grey69':            0.6902,
    'gray70':            0.7020,
    'grey70':            0.7020,
    'gray71':            0.7098,
    'grey71':            0.7098,
    'gray72':            0.7216,
    'grey72':            0.7216,
    'gray73':            0.7294,
    'grey73':            0.7294,
    'gray74':            0.7412,
    'grey74':            0.7412,
    'gray75':            0.7490,
    'grey75':            0.7490,
    'gray76':            0.7608,
    'grey76':            0.7608,
    'gray77':            0.7686,
    'grey77':            0.7686,
    'gray78':            0.7804,
    'grey78':            0.7804,
    'gray79':            0.7882,
    'grey79':            0.7882,
    'gray80':            0.8000,
    'grey80':            0.8000,
    'gray81':            0.8118,
    'grey81':            0.8118,
    'gray82':            0.8196,
    'grey82':            0.8196,
    'gray83':            0.8314,
    'grey83':            0.8314,
    'gray84':            0.8392,
    'grey84':            0.8392,
    'gray85':            0.8510,
    'grey85':            0.8510,
    'gray86':            0.8588,
    'grey86':            0.8588,
    'gray87':            0.8706,
    'grey87':            0.8706,
    'gray88':            0.8784,
    'grey88':            0.8784,
    'gray89':            0.8902,
    'grey89':            0.8902,
    'gray90':            0.8980,
    'grey90':            0.8980,
    'gray91':            0.9098,
    'grey91':            0.9098,
    'gray92':            0.9216,
    'grey92':            0.9216,
    'gray93':            0.9294,
    'grey93':            0.9294,
    'gray94':            0.9412,
    'grey94':            0.9412,
    'gray95':            0.9490,
    'grey95':            0.9490,
    'gray96':            0.9608,
    'grey96':            0.9608,
    'gray97':            0.9686,
    'grey97':            0.9686,
    'gray98':            0.9804,
    'grey98':            0.9804,
    'gray99':            0.9882,
    'grey99':            0.9882,
    'gray100':           1.0000,
    'grey100':           1.0000,
    'dark grey':         0.6627,
    'DarkGrey':          0.6627,
    'dark gray':         0.6627,
    'DarkGray':          0.6627,
    'dark blue':         array([0.0000, 0.0000, 0.5451]),
    'DarkBlue':          array([0.0000, 0.0000, 0.5451]),
    'dark cyan':         array([0.0000, 0.5451, 0.5451]),
    'DarkCyan':          array([0.0000, 0.5451, 0.5451]),
    'dark magenta':      array([0.5451, 0.0000, 0.5451]),
    'DarkMagenta':       array([0.5451, 0.0000, 0.5451]),
    'dark red':          array([0.5451, 0.0000, 0.0000]),
    'DarkRed':           array([0.5451, 0.0000, 0.0000]),
    'light green':       array([0.5647, 0.9333, 0.5647]),
    'LightGreen':        array([0.5647, 0.9333, 0.5647]),
}

del array   # Prevent namespace pollution.

def _MakeColorTable(outfile = None, infile = "/usr/lib/X11/rgb.txt"):
    import string, sys
    
    if type(infile) == type("string"):
        infile = open(infile)
    if outfile is None:
        outfile = sys.stdout
    if type(outfile) == type("string"):
        outfile = open(outfile, "w")
        
    outfile.write("ColorTable = {\n");
    for line in infile.readlines():
        line = string.strip(line)
        if not line or (line[0] in "%#!;"):
            continue
        # This is not a comment or an empty line
        words = string.split(line)
        name = "'" + string.join(words[3:], " ") + "':"
        if words[0] == words[1] and words[0] == words[2]:
            # Gray color
            clr = float(words[0])/255.0
            outfile.write("    %-20s %6.4f,\n" % (name,clr))
        else:
            clr = (name, float(words[0])/255.0, float(words[1])/255.0,
                   float(words[2])/255.0)
            outfile.write("    %-20s array([%6.4f, %6.4f, %6.4f]),\n" % clr)
    outfile.write("}\n")
    outfile.flush()
