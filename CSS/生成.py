f = open('样式.css', encoding='utf-8', mode='r')
styleStringWithoutColor = f.read()
f.close()

f = open('配色_.json', encoding='utf-8', mode='r')
schemeDict = eval(f.read())
f.close()

for scheme, colorsDict in schemeDict.items():
    styleString = styleStringWithoutColor
    for colorType, colorValue in sorted(colorsDict.items(), reverse=True):
        styleString = styleString.replace(colorType, colorValue)
    f = open('生成/%s.css' % scheme, encoding='utf-8', mode='w')
    f.write(styleString)
    f.close()