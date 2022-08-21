class Charactor():
    def __init__(me):
        me.isReset = False
        me.reset()
    # Array: 職業清單
    def getClasslist(me):
        CLASS_LIST = [
            '英雄(單手武器)','英雄(雙手武器)','聖騎士(單手武器)','聖騎士(雙手武器)','黑騎士',
            '大魔導士(火、毒)','大魔導士(冰、雷)','主教',
            '箭神','神射手','開拓者',
            '夜使者','暗影神偷','影武者',
            '拳霸','槍神','重砲指揮官',
            '聖魂劍士(單)','聖魂劍士(雙)','烈焰巫師','破風使者','暗夜行者','閃雷悍將','米哈逸',
            '狂豹獵人','機甲戰神','煉獄巫師','爆拳槍神','惡魔殺手','傑諾',#'惡魔復仇者',
            '龍魔導士','精靈遊俠','狂狼勇士','夜光','幻影俠盜','隱月',
            '天使破壞者','凱撒','卡蒂娜','凱殷',
            '伊利恩','亞克','阿戴爾',
            '神之子(琉)','神之子(璃)',
            '凱內西斯',
            '虎影','菈菈',
            '幻獸師(熊)','幻獸師(豹)','幻獸師(鷹)','幻獸師(貓)',
            '劍豪(一般狀態)','劍豪(拔刀狀態)','陰陽師',
            '墨玄'
        ]
        return CLASS_LIST
    
    # Array: 武器係數
    def getWPlist(me):
        #  0: 1
        #  1: 1.2
        #  2: 1.25
        #  3: 1.3125
        #  4: 1.3
        #  5: 1.34
        #  6: 1.35
        #  7: 1.44
        #  8: 1.49
        #  9: 1.5
        # 10: 1.7
        # 11: 1.75
        WP_LIST = ['1','1.2','1.25','1.3','1.3125','1.34','1.35','1.44','1.49','1.5','1.7','1.75']
        return WP_LIST

    # Object: 取得職業對應參數
    def getClassInfo(me, name):
        CLASS_NAME = name
        CLASS_INFO = {
            'CLASS_IDX': me.getClasslist().index(CLASS_NAME),
            'CLASS_NAME': CLASS_NAME,
            'WP_IDX': 0,
            'WP_VALUE': 1,
            # 'ATTACK_P': 0,
            'STR': '',
            'DEX': '',
            'INT': '',
            'LUK': '',
        }

        # ------------- 主屬副屬 -------------
        CLASS_LIST = ['傑諾']
        if (CLASS_NAME in CLASS_LIST):
            CLASS_INFO['STR'] = 'main'
            CLASS_INFO['DEX'] = 'main'
            CLASS_INFO['LUK'] = 'main'
            pass

        CLASS_LIST = [
            '英雄(單手武器)','英雄(雙手武器)','聖騎士(單手武器)','聖騎士(雙手武器)','黑騎士',
            '拳霸','重砲指揮官','聖魂劍士(單)','聖魂劍士(雙)','閃雷悍將','米哈逸','爆拳槍神',
            '惡魔殺手','狂狼勇士','隱月','凱撒','亞克','阿戴爾','神之子(琉)','神之子(璃)','劍豪(一般狀態)','劍豪(拔刀狀態)',
        ]
        if (CLASS_NAME in CLASS_LIST):
            CLASS_INFO['STR'] = 'main'
            CLASS_INFO['DEX'] = 'minor'
            pass

        CLASS_LIST = [
            '箭神','神射手','開拓者','槍神','破風使者','狂豹獵人','機甲戰神',
            '精靈遊俠','天使破壞者','凱殷','墨玄'
        ]
        if (CLASS_NAME in CLASS_LIST):
            CLASS_INFO['STR'] = 'minor'
            CLASS_INFO['DEX'] = 'main'
            pass

        CLASS_LIST = [
            '大魔導士(火、毒)','大魔導士(冰、雷)','主教','烈焰巫師','煉獄巫師','龍魔導士','夜光',
            '伊利恩','凱內西斯','菈菈','幻獸師(熊)','幻獸師(豹)','幻獸師(鷹)','幻獸師(貓)','陰陽師',
        ]
        if (CLASS_NAME in CLASS_LIST):
            CLASS_INFO['INT'] = 'main'
            CLASS_INFO['LUK'] = 'minor'
            pass

        CLASS_LIST = ['夜使者','暗夜行者','幻影俠盜','虎影',]
        if (CLASS_NAME in CLASS_LIST):
            CLASS_INFO['DEX'] = 'minor'
            CLASS_INFO['LUK'] = 'main'
            pass

        CLASS_LIST = ['暗影神偷','影武者','卡蒂娜',]
        if (CLASS_NAME in CLASS_LIST):
            CLASS_INFO['STR'] = 'minor'
            CLASS_INFO['DEX'] = 'minor'
            CLASS_INFO['LUK'] = 'main'
            pass

        # ------------- 武器係數 -------------
        CLASS_LIST = []
        if (CLASS_NAME in CLASS_LIST):
            CLASS_INFO['WP_VALUE'] = 1
            pass

        CLASS_LIST = [
            '聖騎士(單手武器)','大魔導士(火、毒)','大魔導士(冰、雷)','主教','聖魂劍士(單)','烈焰巫師','米哈逸',
            '煉獄巫師','惡魔殺手','龍魔導士','伊利恩','凱內西斯','菈菈',
        ]
        if (CLASS_NAME in CLASS_LIST):
            CLASS_INFO['WP_VALUE'] = 1.2
            pass

        CLASS_LIST = ['劍豪(一般狀態)','劍豪(拔刀狀態)',]
        if (CLASS_NAME in CLASS_LIST):
            CLASS_INFO['WP_VALUE'] = 1.25
            pass

        CLASS_LIST = [
            '英雄(單手武器)','箭神','神射手','開拓者','暗影神偷','影武者','破風使者','狂豹獵人', '惡魔復仇者',
            '精靈遊俠','夜光','幻影俠盜','卡蒂娜','凱殷','阿戴爾','虎影',
        ]
        if (CLASS_NAME in CLASS_LIST):
            CLASS_INFO['WP_VALUE'] = 1.3
            pass

        CLASS_LIST = ['傑諾',]
        if (CLASS_NAME in CLASS_LIST):
            CLASS_INFO['WP_VALUE'] = 1.3125
            pass

        CLASS_LIST = ['聖騎士(雙手武器)','聖魂劍士(雙)','凱撒','神之子(璃)','幻獸師(熊)','幻獸師(豹)','幻獸師(鷹)','幻獸師(貓)',]
        if (CLASS_NAME in CLASS_LIST):
            CLASS_INFO['WP_VALUE'] = 1.34
            pass

        CLASS_LIST = ['陰陽師',]
        if (CLASS_NAME in CLASS_LIST):
            CLASS_INFO['WP_VALUE'] = 1.35
            pass

        CLASS_LIST = ['英雄(雙手武器)',]
        if (CLASS_NAME in CLASS_LIST):
            CLASS_INFO['WP_VALUE'] = 1.44
            pass

        CLASS_LIST = ['黑騎士','狂狼勇士','神之子(琉)',]
        if (CLASS_NAME in CLASS_LIST):
            CLASS_INFO['WP_VALUE'] = 1.49
            pass

        CLASS_LIST = ['槍神','重砲指揮官','機甲戰神',]
        if (CLASS_NAME in CLASS_LIST):
            CLASS_INFO['WP_VALUE'] = 1.5
            pass

        CLASS_LIST = ['拳霸','閃雷悍將','爆拳槍神','隱月','天使破壞者','亞克',]
        if (CLASS_NAME in CLASS_LIST):
            CLASS_INFO['WP_VALUE'] = 1.7
            pass

        CLASS_LIST = ['夜使者','暗夜行者','墨玄',]
        if (CLASS_NAME in CLASS_LIST):
            CLASS_INFO['WP_VALUE'] = 1.75
            pass

        CLASS_INFO['WP_IDX'] = me.getWPlist().index(str(CLASS_INFO['WP_VALUE']))

        return CLASS_INFO

    # Object: 取得角色資料 me.data
    def getData(me):
        return me.data
    
    # function: 初始化角色資料 me.data
    def reset(me):
        me.data = {
            'LEVEL': 0,
            'CLASS_IDX': 0, 'CLASS_NAME': '',
            'MIN_DMG': 0, 'MAX_DMG': 0,
            'WP_IDX': 0, 'WP_VALUE': 0,
            'ATTACK': 0, 'ATTACK_P': 0,
            'DMG_P': 0, 'BOSS_P': 0,
            'STRIKE_P': 0,
            'IGNORE_P': 0,
            'FINALDMG_P': 0,
            'DEFENSE_P': 0,

            'STR': 0, 
            'STR_P': 0, 'STR_CLEAR': 0, 'STR_UNIQUE': 0,
            'STR_BEFORE': 0,
            'STR_RANGE': 0,
            'STR_RANGE_IS_P': 0,

            'DEX': 0, 
            'DEX_P': 0, 'DEX_CLEAR': 0, 'DEX_UNIQUE': 0,
            'DEX_BEFORE': 0,
            'DEX_RANGE': 0,
            'DEX_RANGE_IS_P': 0,

            'INT': 0, 
            'INT_P': 0, 'INT_CLEAR': 0, 'INT_UNIQUE': 0,
            'INT_BEFORE': 0,
            'INT_RANGE': 0,
            'INT_RANGE_IS_P': 0,

            'LUK': 0, 
            'LUK_P': 0, 'LUK_CLEAR': 0, 'LUK_UNIQUE': 0,
            'LUK_BEFORE': 0,
            'LUK_RANGE': 0,
            'LUK_RANGE_IS_P': 0,

            'FIX': 1
        }
        me.isReset = True

    # function: 更新角色能力值到 me.data
    def updateAbilityByData(me, data):

        if('LEVEL' in data): me.data['LEVEL'] = data['LEVEL']
        if('MIN_DMG' in data): me.data['MIN_DMG'] = data['MIN_DMG']
        if('MAX_DMG' in data): me.data['MAX_DMG'] = data['MAX_DMG']
        if('ATTACK' in data): me.data['ATTACK'] = data['ATTACK']
        if('ATTACK_P' in data): me.data['ATTACK_P'] = data['ATTACK_P']
        if('DMG_P' in data): me.data['DMG_P'] = data['DMG_P']
        if('BOSS_P' in data): me.data['BOSS_P'] = data['BOSS_P']
        if('STRIKE_P' in data): me.data['STRIKE_P'] = data['STRIKE_P']
        if('IGNORE_P' in data): me.data['IGNORE_P'] = data['IGNORE_P']
        if('FINALDMG_P' in data): me.data['FINALDMG_P'] = data['FINALDMG_P']
        if('DEFENSE_P' in data): me.data['DEFENSE_P'] = data['DEFENSE_P']

        if('STR_BEFORE' in data): me.data['STR_BEFORE'] = data['STR_BEFORE']
        if('STR_RANGE' in data): me.data['STR_RANGE'] = data['STR_RANGE']
        if('STR_RANGE_IS_P' in data): me.data['STR_RANGE_IS_P'] = data['STR_RANGE_IS_P']
        if('STR' in data): me.data['STR'] = data['STR']
        if('STR_UNIQUE' in data): me.data['STR_UNIQUE'] = data['STR_UNIQUE']

        if('DEX_BEFORE' in data): me.data['DEX_BEFORE'] = data['DEX_BEFORE']
        if('DEX_RANGE' in data): me.data['DEX_RANGE'] = data['DEX_RANGE']
        if('DEX_RANGE_IS_P' in data): me.data['DEX_RANGE_IS_P'] = data['DEX_RANGE_IS_P']
        if('DEX' in data): me.data['DEX'] = data['DEX']
        if('DEX_UNIQUE' in data): me.data['DEX_UNIQUE'] = data['DEX_UNIQUE']

        if('INT_BEFORE' in data): me.data['INT_BEFORE'] = data['INT_BEFORE']
        if('INT_RANGE' in data): me.data['INT_RANGE'] = data['INT_RANGE']
        if('INT_RANGE_IS_P' in data): me.data['INT_RANGE_IS_P'] = data['INT_RANGE_IS_P']
        if('INT' in data): me.data['INT'] = data['INT']
        if('INT_UNIQUE' in data): me.data['INT_UNIQUE'] = data['INT_UNIQUE']

        if('LUK_BEFORE' in data): me.data['LUK_BEFORE'] = data['LUK_BEFORE']
        if('LUK_RANGE' in data): me.data['LUK_RANGE'] = data['LUK_RANGE']
        if('LUK_RANGE_IS_P' in data): me.data['LUK_RANGE_IS_P'] = data['LUK_RANGE_IS_P']
        if('LUK' in data): me.data['LUK'] = data['LUK']
        if('LUK_UNIQUE' in data): me.data['LUK_UNIQUE'] = data['LUK_UNIQUE']
        
        if('CLASS_IDX' in data): 
            me.data['CLASS_IDX'] = data['CLASS_IDX']
            me.data['CLASS_NAME'] = me.getClasslist()[data['CLASS_IDX']]
        
        if('WP_IDX' in data): 
            me.data['WP_IDX'] = data['WP_IDX']
            me.data['WP_VALUE'] = float(me.getWPlist()[data['WP_IDX']])

        # 計算四大屬性
        AP_INFO_STR = me.getAPinfo('STR', me.data)
        me.data['STR_P'] = AP_INFO_STR['AP_P']
        me.data['STR_CLEAR'] = AP_INFO_STR['AP_CLEAR']
        me.data['STR_UNIQUE'] = AP_INFO_STR['AP_UNIQUE']

        AP_INFO_DEX = me.getAPinfo('DEX', me.data)
        me.data['DEX_P'] = AP_INFO_DEX['AP_P']
        me.data['DEX_CLEAR'] = AP_INFO_DEX['AP_CLEAR']
        me.data['DEX_UNIQUE'] = AP_INFO_DEX['AP_UNIQUE']

        AP_INFO_INT = me.getAPinfo('INT', me.data)
        me.data['INT_P'] = AP_INFO_INT['AP_P']
        me.data['INT_CLEAR'] = AP_INFO_INT['AP_CLEAR']
        me.data['INT_UNIQUE'] = AP_INFO_INT['AP_UNIQUE']

        AP_INFO_LUK = me.getAPinfo('LUK', me.data)
        me.data['LUK_P'] = AP_INFO_LUK['AP_P']
        me.data['LUK_CLEAR'] = AP_INFO_LUK['AP_CLEAR']
        me.data['LUK_UNIQUE'] = AP_INFO_LUK['AP_UNIQUE']

        # print(CLASS_NAME)
        myAttribute = me.calcAttributeByClass(me.data)
        WP_VALUE = me.data['WP_VALUE']
        ATTACK_P = me.data['ATTACK_P']
        DMG_P = me.data['DMG_P']
        FINALDMG_P = me.data['FINALDMG_P']
        MAX_DMG = me.data['MAX_DMG']
        
        ATTACK = MAX_DMG / ( myAttribute * WP_VALUE * (1 + ATTACK_P) * 0.01 * (1 + DMG_P) * (1 + FINALDMG_P) )
        if(me.data['ATTACK'] == 0):
            me.data['ATTACK'] = ATTACK
        else:
            me.data['FIX'] = ATTACK / me.data['ATTACK']
        
        # print('\n------------ updateAbilityByData ------------')
        # print(me.data)
        me.isReset = False
        return me.data

    # function: 計算屬性 => AP_CLEAR / AP_P / AP_UNIQUE
    def getAPinfo(me, aptype, data):
        AP_TYPE = aptype
        AP_INFO = {
            'AP_P': 0,
            'AP_CLEAR': 0,
            'AP_UNIQUE': 0,
        }

        AP_BEFORE = data[AP_TYPE + '_BEFORE']
        AP_RANGE = data[AP_TYPE + '_RANGE']
        AP_RANGE_IS_P = data[AP_TYPE + '_RANGE_IS_P']
        AP_AFTER = data[AP_TYPE]
        AP_UNIQUE = data[AP_TYPE + '_UNIQUE']
        AP_DIFF = AP_AFTER - AP_BEFORE
        AP_CLEAR = AP_AFTER - AP_UNIQUE

        AP_INFO['AP_UNIQUE'] = AP_UNIQUE
        # AP_RANGE = 純屬性
        if (AP_RANGE_IS_P == 0):
            # 屬性% = (差 / 變量) -1
            # 純屬性 = (屬性 - 不吃%) / (1 + 屬性% )
            
            AP_INFO['AP_P'] = (AP_DIFF / AP_RANGE) - 1 
            AP_INFO['AP_CLEAR'] = AP_CLEAR / (1 + AP_INFO['AP_P']) 

        # AP_RANGE = 屬性%
        if (AP_RANGE_IS_P == 1):
            # 純屬性 = 差 / 變量%
            # 屬性% = (屬性 - 不吃%) / 純屬姓 -1
            
            AP_INFO['AP_CLEAR'] = AP_DIFF / (AP_RANGE / 100) 
            AP_INFO['AP_P'] = (AP_CLEAR / AP_INFO['AP_CLEAR']) -1
        
        # print('\n------------ getAPinfo ------------')
        # print (str(AP_TYPE) + '\t純屬性= ' + str(round(AP_INFO['AP_CLEAR'])) + '\t屬性%= ' + str(round(AP_INFO['AP_P']*100, 4)) + '%')
        return AP_INFO

    # function: 計算AP
    def calcAP(me, apType, clear = 0, p = 0, unique = 0):
        AP_CLEAR = clear
        AP_P = p
        AP_UNIQUE = unique
        data = me.getData()
        if (apType == 'STR'):
            return (data['STR_CLEAR'] + AP_CLEAR) * (1 + data['STR_P'] + AP_P) + (data['STR_UNIQUE'] + AP_UNIQUE) 
        if (apType == 'DEX'):
            return (data['DEX_CLEAR'] + AP_CLEAR) * (1 + data['DEX_P'] + AP_P) + (data['DEX_UNIQUE'] + AP_UNIQUE) 
        if (apType == 'INT'):
            return (data['INT_CLEAR'] + AP_CLEAR) * (1 + data['INT_P'] + AP_P) + (data['INT_UNIQUE'] + AP_UNIQUE) 
        if (apType == 'LUK'):
            return (data['LUK_CLEAR'] + AP_CLEAR) * (1 + data['LUK_P'] + AP_P) + (data['LUK_UNIQUE'] + AP_UNIQUE) 
        
        return 0
    
    # function: 計算屬性參數 = (4 * 主屬) + 副屬
    def calcAttributeByClass(me, data):
        CLASS_NAME = data['CLASS_NAME']
        CLASS_INFO = me.getClassInfo(CLASS_NAME)
        
        MAIN_AP = 0
        MINOR_AP = 0
        if(CLASS_INFO['STR'] == 'main'): MAIN_AP += data['STR']
        if(CLASS_INFO['DEX'] == 'main'): MAIN_AP += data['DEX']
        if(CLASS_INFO['INT'] == 'main'): MAIN_AP += data['INT']
        if(CLASS_INFO['LUK'] == 'main'): MAIN_AP += data['LUK']

        if(CLASS_INFO['STR'] == 'minor'): MINOR_AP += data['STR']
        if(CLASS_INFO['DEX'] == 'minor'): MINOR_AP += data['DEX']
        if(CLASS_INFO['INT'] == 'minor'): MINOR_AP += data['INT']
        if(CLASS_INFO['LUK'] == 'minor'): MINOR_AP += data['LUK']
        
        myAttribute = (4 * MAIN_AP) + MINOR_AP
        # print('\n------------ calcAttributeByClass ------------')
        # print(myAttribute)
        return myAttribute
    
    # function: 計算推估無視
    def calcIgnore(me, origin, range):
        IGNORE_P = origin
        if (range > 0):
            IGNORE_P = 1 - ((1 - IGNORE_P) * (1 - range))
        if (range < 0):
            IGNORE_P = 1 - ((1 - IGNORE_P) / (1 + range))
        if (IGNORE_P > 1): IGNORE_P = 1
        return IGNORE_P
    
    # function: 取得預估值
    def getEstimate(me, new_data):
        data = me.getData()
        ESTIMATE_INFO = {
            'DMG_P': data['DMG_P'],
            'STRIKE_P': data['STRIKE_P'],
            'FINALDMG_P': data['FINALDMG_P'],
            'ATTACK': data['ATTACK'],
            'ATTACK_P': data['ATTACK_P'],
            'BOSS_P': data['BOSS_P'],
            'IGNORE_P': data['IGNORE_P'],

            'STR_CLEAR': data['STR_CLEAR'],
            'STR_P': data['STR_P'],
            'STR_UNIQUE': data['STR_UNIQUE'],
            'STR': 0,

            'DEX_CLEAR': data['DEX_CLEAR'],
            'DEX_P': data['DEX_P'],
            'DEX_UNIQUE': data['DEX_UNIQUE'],
            'DEX': 0,

            'INT_CLEAR': data['INT_CLEAR'],
            'INT_P': data['INT_P'],
            'INT_UNIQUE': data['INT_UNIQUE'],
            'INT': 0,

            'LUK_CLEAR': data['LUK_CLEAR'],
            'LUK_P': data['LUK_P'],
            'LUK_UNIQUE': data['LUK_UNIQUE'],
            'LUK': 0,

            'ALL_P': 0,
        }
        
        # 傷害
        if('DMG_P' in new_data):
            ESTIMATE_INFO['DMG_P'] += new_data['DMG_P']

        # BOSS
        if('BOSS_P' in new_data):
            ESTIMATE_INFO['BOSS_P'] += new_data['BOSS_P']

        # 攻擊力
        if('ATTACK' in new_data):
            ESTIMATE_INFO['ATTACK'] += new_data['ATTACK']

        # 攻擊%
        if('ATTACK_P' in new_data):
            ESTIMATE_INFO['ATTACK_P'] += new_data['ATTACK_P']
        
        # 爆傷
        if('STRIKE_P' in new_data):
            ESTIMATE_INFO['STRIKE_P'] += new_data['STRIKE_P']

        # 無視
        if('IGNORE_P' in new_data):
            ESTIMATE_INFO['IGNORE_P'] = me.calcIgnore(data['IGNORE_P'], new_data['IGNORE_P'])

        # 終傷
        if('FINALDMG_P' in new_data):
            ESTIMATE_INFO['FINALDMG_P'] += new_data['FINALDMG_P']

        # STR_CLEAR
        if('STR_CLEAR' in new_data):
            ESTIMATE_INFO['STR_CLEAR'] += new_data['STR_CLEAR']

        # STR_P
        if('STR_P' in new_data):
            ESTIMATE_INFO['STR_P'] += new_data['STR_P']

        # STR_UNIQUE
        if('STR_UNIQUE' in new_data):
            ESTIMATE_INFO['STR_UNIQUE'] += new_data['STR_UNIQUE']

        # DEX_CLEAR
        if('DEX_CLEAR' in new_data):
            ESTIMATE_INFO['DEX_CLEAR'] += new_data['DEX_CLEAR']

        # DEX_P
        if('DEX_P' in new_data):
            ESTIMATE_INFO['DEX_P'] += new_data['DEX_P']

        # DEX_UNIQUE
        if('DEX_UNIQUE' in new_data):
            ESTIMATE_INFO['DEX_UNIQUE'] += new_data['DEX_UNIQUE']

        # INT_CLEAR
        if('INT_CLEAR' in new_data):
            ESTIMATE_INFO['INT_CLEAR'] += new_data['INT_CLEAR']

        # INT_P
        if('INT_P' in new_data):
            ESTIMATE_INFO['INT_P'] += new_data['INT_P']

        # INT_UNIQUE
        if('INT_UNIQUE' in new_data):
            ESTIMATE_INFO['INT_UNIQUE'] += new_data['INT_UNIQUE']

        # LUK_CLEAR
        if('LUK_CLEAR' in new_data):
            ESTIMATE_INFO['LUK_CLEAR'] += new_data['LUK_CLEAR']

        # LUK_P
        if('LUK_P' in new_data):
            ESTIMATE_INFO['LUK_P'] += new_data['LUK_P']

        # LUK_UNIQUE
        if('LUK_UNIQUE' in new_data):
            ESTIMATE_INFO['LUK_UNIQUE'] += new_data['LUK_UNIQUE']

        # LUK_UNIQUE
        if('ALL_P' in new_data):
            ESTIMATE_INFO['ALL_P'] += new_data['ALL_P']

        ESTIMATE_INFO['STR'] = ESTIMATE_INFO['STR_CLEAR'] * (1 + ESTIMATE_INFO['STR_P'] + ESTIMATE_INFO['ALL_P']) + ESTIMATE_INFO['STR_UNIQUE']
        ESTIMATE_INFO['DEX'] = ESTIMATE_INFO['DEX_CLEAR'] * (1 + ESTIMATE_INFO['DEX_P'] + ESTIMATE_INFO['ALL_P']) + ESTIMATE_INFO['DEX_UNIQUE']
        ESTIMATE_INFO['INT'] = ESTIMATE_INFO['INT_CLEAR'] * (1 + ESTIMATE_INFO['INT_P'] + ESTIMATE_INFO['ALL_P']) + ESTIMATE_INFO['INT_UNIQUE']
        ESTIMATE_INFO['LUK'] = ESTIMATE_INFO['LUK_CLEAR'] * (1 + ESTIMATE_INFO['LUK_P'] + ESTIMATE_INFO['ALL_P']) + ESTIMATE_INFO['LUK_UNIQUE']
        
        return ESTIMATE_INFO

    # function: 計算增幅
    def calcImprove(me, new_data):
        data = me.getData()
        IMPROVE_INFO = {
            'DMG_P': 1,
            'STRIKE_P': 1,
            'FINALDMG_P': 1,
            'ATTACK': 1,
            'ATTACK_P': 1,
            'BOSS_P': 1,
            'IGNORE_P': 1,

            'STR_CLEAR': 1,
            'STR_P': 1,
            'STR'

            'DEX_CLEAR': 1,
            'DEX_P': 1,

            'INT_CLEAR': 1,
            'INT_P': 1,

            'LUK_CLEAR': 1,
            'LUK_P': 1,

            'ALL_P': 1,
            'TOTAL': 1
        }

        ESTIMATE_INFO = me.getEstimate(new_data)
        
        # 傷害
        IMPROVE_INFO['DMG_P'] = (1 + ESTIMATE_INFO['DMG_P'] + data['BOSS_P']) / (1 + data['DMG_P'] + data['BOSS_P'])

        # BOSS
        IMPROVE_INFO['BOSS_P'] = (1 + data['DMG_P'] + ESTIMATE_INFO['BOSS_P']) / (1 + data['DMG_P'] + data['BOSS_P'])

        # 攻擊力
        IMPROVE_INFO['ATTACK'] = (ESTIMATE_INFO['ATTACK']) / data['ATTACK']
            

        # 攻擊%
        IMPROVE_INFO['ATTACK_P'] = (1 + ESTIMATE_INFO['ATTACK_P']) / (1 + data['ATTACK_P'])    
        
        # 爆傷
        IMPROVE_INFO['STRIKE_P'] = (1.35 + ESTIMATE_INFO['STRIKE_P']) / (1.35 + data['STRIKE_P'])    

        # 無視
        IMPROVE_INFO['IGNORE_P'] = (1 - (data['DEFENSE_P'] * (1 - ESTIMATE_INFO['IGNORE_P']))) / (1 - (data['DEFENSE_P'] * (1 - data['IGNORE_P'])))    
            

        # 終傷
        IMPROVE_INFO['FINALDMG_P'] = (1 + ESTIMATE_INFO['FINALDMG_P']) / (1 + data['FINALDMG_P'])    

        def getOrigin():
            ORIGIN_ATTRIBUTE = {
                'CLASS_NAME': data['CLASS_NAME'],
                'STR': (data['STR_CLEAR'] * (1 + data['STR_P'])) + data['STR_UNIQUE'],
                'DEX': (data['DEX_CLEAR'] * (1 + data['DEX_P'])) + data['DEX_UNIQUE'],
                'INT': (data['INT_CLEAR'] * (1 + data['INT_P'])) + data['INT_UNIQUE'],
                'LUK': (data['LUK_CLEAR'] * (1 + data['LUK_P'])) + data['LUK_UNIQUE'],
            }    
            return ORIGIN_ATTRIBUTE
        
        myAttribute = me.calcAttributeByClass(getOrigin())

        # STR
        NEW_ATTRIBUTE = getOrigin()
        NEW_ATTRIBUTE['STR'] = (ESTIMATE_INFO['STR_CLEAR'] * (1 + data['STR_P'])) + data['STR_UNIQUE']
        IMPROVE_INFO['STR_CLEAR'] = me.calcAttributeByClass(NEW_ATTRIBUTE) / myAttribute

        # STR%
        NEW_ATTRIBUTE = getOrigin()
        NEW_ATTRIBUTE['STR'] = (data['STR_CLEAR'] * (1 + ESTIMATE_INFO['STR_P'])) + data['STR_UNIQUE']
        IMPROVE_INFO['STR_P'] = me.calcAttributeByClass(NEW_ATTRIBUTE) / myAttribute
        
        # DEX
        NEW_ATTRIBUTE = getOrigin()
        NEW_ATTRIBUTE['DEX'] = (ESTIMATE_INFO['DEX_CLEAR'] * (1 + data['DEX_P'])) + data['DEX_UNIQUE']
        IMPROVE_INFO['DEX_CLEAR'] = me.calcAttributeByClass(NEW_ATTRIBUTE) / myAttribute

        # DEX%
        NEW_ATTRIBUTE = getOrigin()
        NEW_ATTRIBUTE['DEX'] = (data['DEX_CLEAR'] * (1 + ESTIMATE_INFO['DEX_P'])) + data['DEX_UNIQUE']
        IMPROVE_INFO['DEX_P'] = me.calcAttributeByClass(NEW_ATTRIBUTE) / myAttribute

        # INT
        NEW_ATTRIBUTE = getOrigin()
        NEW_ATTRIBUTE['INT'] = (ESTIMATE_INFO['INT_CLEAR'] * (1 + data['INT_P'])) + data['INT_UNIQUE']
        IMPROVE_INFO['INT_CLEAR'] = me.calcAttributeByClass(NEW_ATTRIBUTE) / myAttribute

        # INT%
        NEW_ATTRIBUTE = getOrigin()
        NEW_ATTRIBUTE['INT'] = (data['INT_CLEAR'] * (1 + ESTIMATE_INFO['INT_P'])) + data['INT_UNIQUE']
        IMPROVE_INFO['INT_P'] = me.calcAttributeByClass(NEW_ATTRIBUTE) / myAttribute

        # LUK
        NEW_ATTRIBUTE = getOrigin()
        NEW_ATTRIBUTE['LUK'] = (ESTIMATE_INFO['LUK_CLEAR'] * (1 + data['LUK_P'])) + data['LUK_UNIQUE']
        IMPROVE_INFO['LUK_CLEAR'] = me.calcAttributeByClass(NEW_ATTRIBUTE) / myAttribute

        # LUK%
        NEW_ATTRIBUTE = getOrigin()
        NEW_ATTRIBUTE['LUK'] = (data['LUK_CLEAR'] * (1 + ESTIMATE_INFO['LUK_P'])) + data['LUK_UNIQUE']
        IMPROVE_INFO['LUK_P'] = me.calcAttributeByClass(NEW_ATTRIBUTE) / myAttribute

        # 全屬%
        NEW_ATTRIBUTE = getOrigin()
        NEW_ATTRIBUTE['STR'] = (data['STR_CLEAR'] * (1 + data['STR_P'] + ESTIMATE_INFO['ALL_P'])) + data['STR_UNIQUE']
        NEW_ATTRIBUTE['DEX'] = (data['DEX_CLEAR'] * (1 + data['DEX_P'] + ESTIMATE_INFO['ALL_P'])) + data['DEX_UNIQUE']
        NEW_ATTRIBUTE['INT'] = (data['INT_CLEAR'] * (1 + data['INT_P'] + ESTIMATE_INFO['ALL_P'])) + data['INT_UNIQUE']
        NEW_ATTRIBUTE['LUK'] = (data['LUK_CLEAR'] * (1 + data['LUK_P'] + ESTIMATE_INFO['ALL_P'])) + data['LUK_UNIQUE']
        IMPROVE_INFO['ALL_P'] = me.calcAttributeByClass(NEW_ATTRIBUTE) / myAttribute
        
        # 計算總增幅
        IMPROVE_INFO['TOTAL'] = IMPROVE_INFO['STRIKE_P'] * IMPROVE_INFO['FINALDMG_P'] * IMPROVE_INFO['ATTACK'] * IMPROVE_INFO['ATTACK_P'] * IMPROVE_INFO['IGNORE_P']
        
        # 重算: (傷害+BOSS)增幅
        FINAL_IMPROVE_DMG = (1 + ESTIMATE_INFO['DMG_P'] + ESTIMATE_INFO['BOSS_P']) / (1 + data['DMG_P'] + data['BOSS_P'])
        IMPROVE_INFO['TOTAL'] = IMPROVE_INFO['TOTAL'] * FINAL_IMPROVE_DMG

        # 重算: 屬性增幅
        NEW_ATTRIBUTE = getOrigin()
        NEW_ATTRIBUTE['STR'] = ESTIMATE_INFO['STR']
        NEW_ATTRIBUTE['DEX'] = ESTIMATE_INFO['DEX']
        NEW_ATTRIBUTE['INT'] = ESTIMATE_INFO['INT']
        NEW_ATTRIBUTE['LUK'] = ESTIMATE_INFO['LUK']
        FINAL_IMPROVE_ATTRIBUTE = me.calcAttributeByClass(NEW_ATTRIBUTE) / myAttribute
        
        IMPROVE_INFO['TOTAL'] = IMPROVE_INFO['TOTAL'] * FINAL_IMPROVE_ATTRIBUTE
        
        return IMPROVE_INFO

    # function: 計算等效需求
    def getEquivalent(me, range):
        data = me.data

        IMPROVE_RANGE = range

        STATE_INFO = {
            'ATTACK': 0,
            'ATTACK_P': 0,
            'DMG_P': 0,
            'BOSS_P': 0,
            'STRIKE_P': 0,
            'IGNORE_P': 0,
            
            'ALL_P': 0,
            
            'STR_CLEAR': 0,
            'STR_P': 0,
            
            'DEX_CLEAR': 0,
            'DEX_P': 0,

            'INT_CLEAR': 0,
            'INT_P': 0,

            'LUK_CLEAR': 0,
            'LUK_P': 0,
        }

        if (IMPROVE_RANGE == 1):
            return STATE_INFO

        STATE_INFO['ATTACK'] = data['ATTACK'] * (IMPROVE_RANGE - 1)
        STATE_INFO['ATTACK_P'] = (1 + data['ATTACK_P']) * (IMPROVE_RANGE - 1)
        STATE_INFO['DMG_P'] = (1 + data['DMG_P'] + data['BOSS_P']) * (IMPROVE_RANGE - 1)
        STATE_INFO['BOSS_P'] = (1 + data['DMG_P'] + data['BOSS_P']) * (IMPROVE_RANGE - 1)
        STATE_INFO['STRIKE_P'] = (1.35 + data['STRIKE_P']) * (IMPROVE_RANGE - 1)

        # 計算無視效益
        defense = data['DEFENSE_P']
        FINAL_DMG = (1 - (defense * (1 - data['IGNORE_P']))) * IMPROVE_RANGE
        NEW_IGNORE = (defense - (1 - FINAL_DMG)) / defense
        STATE_INFO['IGNORE_P'] = 1 - ((1 - NEW_IGNORE) / (1 - data['IGNORE_P']))

        # 計算等效屬性
        myAttribute = me.calcAttributeByClass(data)

        CLASS_INFO = me.getClassInfo(data['CLASS_NAME'])
        # --------------------- STR ---------------------
        # STR = 主屬
        if(CLASS_INFO['STR'] == 'main'):
            NEW_AP = myAttribute * IMPROVE_RANGE
            # if(CLASS_INFO['STR'] == 'minor'): NEW_AP = NEW_AP - data['STR']
            if(CLASS_INFO['DEX'] == 'minor'): NEW_AP = NEW_AP - data['DEX']
            if(CLASS_INFO['INT'] == 'minor'): NEW_AP = NEW_AP - data['INT']
            if(CLASS_INFO['LUK'] == 'minor'): NEW_AP = NEW_AP - data['LUK']
            
            NEW_AP = NEW_AP / 4
            # if(CLASS_INFO['STR'] == 'main'): NEW_AP = NEW_AP - data['STR']
            if(CLASS_INFO['DEX'] == 'main'): NEW_AP = NEW_AP - data['DEX']
            if(CLASS_INFO['INT'] == 'main'): NEW_AP = NEW_AP - data['INT']
            if(CLASS_INFO['LUK'] == 'main'): NEW_AP = NEW_AP - data['LUK']
            
            # NEW_AP = 新的屬性
            NEW_AP -= data['STR_UNIQUE']
            STATE_INFO['STR_CLEAR'] = (NEW_AP / (1 + data['STR_P'])) - data['STR_CLEAR']
            STATE_INFO['STR_P'] = (NEW_AP / data['STR_CLEAR']) - (1 + data['STR_P'])
        
        # STR = 副屬
        if(CLASS_INFO['STR'] == 'minor'):
            AP_DIFF = myAttribute * (IMPROVE_RANGE - 1)
            NEW_AP = data['STR'] + AP_DIFF
            
            # NEW_AP = 新的屬性
            NEW_AP -= data['STR_UNIQUE']
            STATE_INFO['STR_CLEAR'] = (NEW_AP / (1 + data['STR_P'])) - data['STR_CLEAR']
            STATE_INFO['STR_P'] = (NEW_AP / data['STR_CLEAR']) - (1 + data['STR_P'])
        
        # --------------------- DEX ---------------------
        # DEX = 主屬
        if(CLASS_INFO['DEX'] == 'main'):
            NEW_AP = myAttribute * IMPROVE_RANGE
            if(CLASS_INFO['STR'] == 'minor'): NEW_AP = NEW_AP - data['STR']
            # if(CLASS_INFO['DEX'] == 'minor'): NEW_AP = NEW_AP - data['DEX']
            if(CLASS_INFO['INT'] == 'minor'): NEW_AP = NEW_AP - data['INT']
            if(CLASS_INFO['LUK'] == 'minor'): NEW_AP = NEW_AP - data['LUK']
            
            NEW_AP = NEW_AP / 4
            if(CLASS_INFO['STR'] == 'main'): NEW_AP = NEW_AP - data['STR']
            # if(CLASS_INFO['DEX'] == 'main'): NEW_AP = NEW_AP - data['DEX']
            if(CLASS_INFO['INT'] == 'main'): NEW_AP = NEW_AP - data['INT']
            if(CLASS_INFO['LUK'] == 'main'): NEW_AP = NEW_AP - data['LUK']
            
            # NEW_AP = 新的屬性
            NEW_AP -= data['DEX_UNIQUE']
            STATE_INFO['DEX_CLEAR'] = (NEW_AP / (1 + data['DEX_P'])) - data['DEX_CLEAR']
            STATE_INFO['DEX_P'] = (NEW_AP / data['DEX_CLEAR']) - (1 + data['DEX_P'])
        
        # DEX = 副屬
        if(CLASS_INFO['DEX'] == 'minor'):
            AP_DIFF = myAttribute * (IMPROVE_RANGE - 1)
            NEW_AP = data['DEX'] + AP_DIFF
            
            # NEW_AP = 新的屬性
            NEW_AP -= data['DEX_UNIQUE']
            STATE_INFO['DEX_CLEAR'] = (NEW_AP / (1 + data['DEX_P'])) - data['DEX_CLEAR']
            STATE_INFO['DEX_P'] = (NEW_AP / data['DEX_CLEAR']) - (1 + data['DEX_P'])
        
        # --------------------- INT ---------------------
        # INT = 主屬
        if(CLASS_INFO['INT'] == 'main'):
            NEW_AP = myAttribute * IMPROVE_RANGE
            if(CLASS_INFO['STR'] == 'minor'): NEW_AP = NEW_AP - data['STR']
            if(CLASS_INFO['DEX'] == 'minor'): NEW_AP = NEW_AP - data['DEX']
            # if(CLASS_INFO['INT'] == 'minor'): NEW_AP = NEW_AP - data['INT']
            if(CLASS_INFO['LUK'] == 'minor'): NEW_AP = NEW_AP - data['LUK']
            
            NEW_AP = NEW_AP / 4
            if(CLASS_INFO['STR'] == 'main'): NEW_AP = NEW_AP - data['STR']
            if(CLASS_INFO['DEX'] == 'main'): NEW_AP = NEW_AP - data['DEX']
            # if(CLASS_INFO['INT'] == 'main'): NEW_AP = NEW_AP - data['INT']
            if(CLASS_INFO['LUK'] == 'main'): NEW_AP = NEW_AP - data['LUK']
            
            # NEW_AP = 新的屬性
            NEW_AP -= data['INT_UNIQUE']
            STATE_INFO['INT_CLEAR'] = (NEW_AP / (1 + data['INT_P'])) - data['INT_CLEAR']
            STATE_INFO['INT_P'] = (NEW_AP / data['INT_CLEAR']) - (1 + data['INT_P'])
        
        # INT = 副屬
        if(CLASS_INFO['INT'] == 'minor'):
            AP_DIFF = myAttribute * (IMPROVE_RANGE - 1)
            NEW_AP = data['INT'] + AP_DIFF
            
            # NEW_AP = 新的屬性
            NEW_AP -= data['INT_UNIQUE']
            STATE_INFO['INT_CLEAR'] = (NEW_AP / (1 + data['INT_P'])) - data['INT_CLEAR']
            STATE_INFO['INT_P'] = (NEW_AP / data['INT_CLEAR']) - (1 + data['INT_P'])
        
        # --------------------- LUK ---------------------
        # LUK = 主屬
        if(CLASS_INFO['LUK'] == 'main'):
            NEW_AP = myAttribute * IMPROVE_RANGE
            if(CLASS_INFO['STR'] == 'minor'): NEW_AP = NEW_AP - data['STR']
            if(CLASS_INFO['DEX'] == 'minor'): NEW_AP = NEW_AP - data['DEX']
            if(CLASS_INFO['INT'] == 'minor'): NEW_AP = NEW_AP - data['INT']
            # if(CLASS_INFO['LUK'] == 'minor'): NEW_AP = NEW_AP - data['LUK']
            
            NEW_AP = NEW_AP / 4
            if(CLASS_INFO['STR'] == 'main'): NEW_AP = NEW_AP - data['STR']
            if(CLASS_INFO['DEX'] == 'main'): NEW_AP = NEW_AP - data['DEX']
            if(CLASS_INFO['INT'] == 'main'): NEW_AP = NEW_AP - data['INT']
            # if(CLASS_INFO['LUK'] == 'main'): NEW_AP = NEW_AP - data['LUK']
            
            # NEW_AP = 新的屬性
            NEW_AP -= data['LUK_UNIQUE']
            STATE_INFO['LUK_CLEAR'] = (NEW_AP / (1 + data['LUK_P'])) - data['LUK_CLEAR']
            STATE_INFO['LUK_P'] = (NEW_AP / data['LUK_CLEAR']) - (1 + data['LUK_P'])
        
        # LUK = 副屬
        if(CLASS_INFO['LUK'] == 'minor'):
            AP_DIFF = myAttribute * (IMPROVE_RANGE - 1)
            NEW_AP = data['LUK'] + AP_DIFF
            
            # NEW_AP = 新的屬性
            NEW_AP -= data['LUK_UNIQUE']
            STATE_INFO['LUK_CLEAR'] = (NEW_AP / (1 + data['LUK_P'])) - data['LUK_CLEAR']
            STATE_INFO['LUK_P'] = (NEW_AP / data['LUK_CLEAR']) - (1 + data['LUK_P'])

        # --------------------- 全屬% ---------------------
        # 全屬%
        AP_DIFF = myAttribute * (IMPROVE_RANGE - 1)
        
        MAIN_AP_CLEAR = 0
        if(CLASS_INFO['STR'] == 'main'): MAIN_AP_CLEAR += data['STR_CLEAR']
        if(CLASS_INFO['DEX'] == 'main'): MAIN_AP_CLEAR += data['DEX_CLEAR']
        if(CLASS_INFO['INT'] == 'main'): MAIN_AP_CLEAR += data['INT_CLEAR']
        if(CLASS_INFO['LUK'] == 'main'): MAIN_AP_CLEAR += data['LUK_CLEAR']
        
        MINOR_AP_CLEAR = 0
        if(CLASS_INFO['STR'] == 'minor'): MINOR_AP_CLEAR += data['STR_CLEAR']
        if(CLASS_INFO['DEX'] == 'minor'): MINOR_AP_CLEAR += data['DEX_CLEAR']
        if(CLASS_INFO['INT'] == 'minor'): MINOR_AP_CLEAR += data['INT_CLEAR']
        if(CLASS_INFO['LUK'] == 'minor'): MINOR_AP_CLEAR += data['LUK_CLEAR']

        # AP差 / (4*淨主屬+副屬)
        STATE_INFO['ALL_P'] = AP_DIFF / ((4 * MAIN_AP_CLEAR) + MINOR_AP_CLEAR)

        return STATE_INFO
