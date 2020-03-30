f = open('CSS/样式.css', encoding='utf-8', mode='r')
styleStringWithoutColor = f.read()
f.close()

f = open('CSS/配色.json', encoding='utf-8', mode='r')
schemeDict = eval(f.read())
f.close()

typoraPath = '/Users/tansongchen/Library/Application Support/abnerworks.Typora/themes/'
typoraNameList = ['wechat-red', 'wechat-orange', 'wechat-yellow', 'wechat-green', 'wechat-aqua', 'wechat-blue', 'wechat-purple']

f = open('CSS/Typora.css', encoding='utf-8', mode='r')
typoraString = f.read()
f.close()
typoraGlobalString = """
html {
    font-size: 24px;
}

"""

count = 0
for scheme, colorsDict in schemeDict.items():
    typoraName = typoraNameList[count]
    count = count + 1
    styleString = styleStringWithoutColor
    for colorType, colorValue in sorted(colorsDict.items(), reverse=True):
        styleString = styleString.replace(colorType, colorValue)
    f = open('CSS/生成/%s.css' % scheme, encoding='utf-8', mode='w')
    f.write(styleString)
    f.close()
    f = open(typoraPath + '%s.css' % typoraName, encoding='utf-8', mode='w')
    styleString = styleString.replace('#nice {', 'body {').replace('#nice ', '')
    styleString = styleString.replace('16px', '24px')
    f.write(typoraGlobalString + styleString + typoraString)
    f.close()