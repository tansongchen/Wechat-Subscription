import json

varList = ['main', 'dark', 'light', 'hue', 'unhue']
nameList = ['赤', '橙', '黄', '绿', '青', '蓝', '紫']
schemeDict = {name: {var: 'hsl(0, 0, 0)' for var in varList} for name in nameList}

theta = 30

def HSL(value):
    H, S, L = value
    return 'hsl(%d, %d%%, %d%%)' % (H, S * 100, L * 100)

hues = [0, 30, 50, 100, 160, 210, 260]

f = open('配色_.json', encoding='utf-8', mode='w')
for nameN, name in enumerate(nameList):
    mainValue = (
        hues[nameN],
        1,
        0.7
    )
    schemeDict[name]['main'] = HSL(mainValue)
    hueValue = (
        int(mainValue[0] + theta),
        mainValue[1],
        mainValue[2]
    )
    schemeDict[name]['hue'] = HSL(hueValue)
    unhueValue = (
        int(mainValue[0] - theta),
        mainValue[1],
        mainValue[2]
    )
    schemeDict[name]['unhue'] = HSL(unhueValue)
    lightValue = (
        mainValue[0],
        1,
        0.9
    )
    schemeDict[name]['light'] = HSL(lightValue)
    darkValue = (
        mainValue[0],
        0.8,
        0.4
    )
    schemeDict[name]['dark'] = HSL(darkValue)
f.write(json.dumps(schemeDict, ensure_ascii=False, indent=4))
