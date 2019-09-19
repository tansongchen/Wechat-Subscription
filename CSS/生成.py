f = open('样式.css', encoding='utf-8', mode='r')
styleStringWithoutColor = f.read()
f.close()

f = open('配色.json', encoding='utf-8', mode='r')
schemeDict = eval(f.read())
f.close()

for scheme, colorsDict in schemeDict.items():
    styleString = styleStringWithoutColor
    for colorType, colorValue in colorsDict.items():
        styleString = styleString.replace(colorType, '#%s' % colorValue)
    f = open('%s.css' % scheme, encoding='utf-8', mode='w')
    f.write(styleString)
    f.close()