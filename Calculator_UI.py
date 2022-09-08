from PyQt5 import QtCore, QtWidgets, QtGui

class Calculator_UI():
    def setupUi(me, Form):
        me.version = 'V2.22090801'
        title = '裝備效益計算機 ' + me.version
        form_w = 540
        form_h = 474
        padding = 5
        Form.setWindowTitle(title)
        Form.resize(form_w, form_h)
        
        me.tabpanel = QtWidgets.QTabWidget(Form)
        me.tabpanel.setGeometry(QtCore.QRect(padding, padding, form_w-padding*2, form_h-padding*2))

        me.tabpanel.addTab(me.desingPage_Ability(), '能力值設定')
        # me.tabpanel.addTab(me.desingPage_Link(), '傳授')
        me.tabpanel.addTab(me.desingPage_Parameter(), '角色參數')
        me.tabpanel.addTab(me.desingPage_SeedRing(), '塔戒')
        me.tabpanel.addTab(me.desingPage_Equipment(), '裝備變更')
        me.tabpanel.addTab(me.desingPage_Tools(), '工具')
        me.tabpanel.addTab(me.desingPage_Memo(), '使用說明')
        
        me.tabpanel.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    # function: 能力值設定
    def desingPage_Ability(me):
        page = QtWidgets.QWidget()

        me.btnAbility_Submit = me.makeField(page, QtWidgets.QPushButton(page), 15, 330, 495, 30)
        me.btnAbility_Submit.setText('確定')
        
        me.btnAbility_SaveFile = me.makeField(page, QtWidgets.QPushButton(page), 270, 15, 240, 30)
        me.btnAbility_SaveFile.setText('儲存檔案')
        
        me.btnAbility_SelectFile = me.makeField(page, QtWidgets.QPushButton(page), 15, 15, 240, 30)
        me.btnAbility_SelectFile.setText('選擇檔案')
        
        me.viewAbility_LEVEL = me.makeField(page, QtWidgets.QLineEdit(page), 15, 60, 240, 24, '等級')
        me.viewAbility_LEVEL.textChanged.connect(me.updateMapleValue)
        
        me.viewAbility_CLASS_IDX  = me.makeField(page, QtWidgets.QComboBox(page), 270, 60, 240, 24, '職業')

        me.viewAbility_MAX_DMG    = me.makeField(page, QtWidgets.QLineEdit(page), 15, 90 , 240, 24, '最大表攻')
        me.viewAbility_DMG_P      = me.makeField(page, QtWidgets.QLineEdit(page), 15, 120, 240, 24, '傷害', 55, '％')
        me.viewAbility_FINALDMG_P = me.makeField(page, QtWidgets.QLineEdit(page), 15, 150, 240, 24, '最終傷害', 55, '％')
        me.viewAbility_BOSS_P     = me.makeField(page, QtWidgets.QLineEdit(page), 15, 180, 240, 24, 'BOSS傷害', 55, '％')

        me.viewAbility_WP_IDX   = me.makeField(page, QtWidgets.QComboBox(page), 270, 90 , 240, 24, '武器係數')
        me.viewAbility_STRIKE_P = me.makeField(page, QtWidgets.QLineEdit(page), 270, 120, 240, 24, '爆擊傷害', 55, '％')
        me.viewAbility_ATTACK_P = me.makeField(page, QtWidgets.QLineEdit(page), 270, 150, 240, 24, '攻擊力', 55, '％')
        me.viewAbility_IGNORE_P = me.makeField(page, QtWidgets.QLineEdit(page), 270, 180, 240, 24, '無視防禦', 55, '％')

        # 4大屬性
        me.viewAbility_STR_BEFORE = me.makeField(page, QtWidgets.QLineEdit(page), 15, 210, 130, 24, 'STR')
        me.viewAbility_DEX_BEFORE = me.makeField(page, QtWidgets.QLineEdit(page), 15, 240, 130, 24, 'DEX')
        me.viewAbility_INT_BEFORE = me.makeField(page, QtWidgets.QLineEdit(page), 15, 270, 130, 24, 'INT')
        me.viewAbility_LUK_BEFORE = me.makeField(page, QtWidgets.QLineEdit(page), 15, 300, 130, 24, 'LUK')

        me.viewAbility_STR_RANGE = me.makeField(page, QtWidgets.QLineEdit(page), 145, 210, 70, 24, '  +  ', 20)
        me.viewAbility_DEX_RANGE = me.makeField(page, QtWidgets.QLineEdit(page), 145, 240, 70, 24, '  +  ', 20)
        me.viewAbility_INT_RANGE = me.makeField(page, QtWidgets.QLineEdit(page), 145, 270, 70, 24, '  +  ', 20)
        me.viewAbility_LUK_RANGE = me.makeField(page, QtWidgets.QLineEdit(page), 145, 300, 70, 24, '  +  ', 20)

        me.viewAbility_STR_RANGE_IS_P = me.makeField(page, QtWidgets.QComboBox(page), 215, 210, 40, 24)
        me.viewAbility_DEX_RANGE_IS_P = me.makeField(page, QtWidgets.QComboBox(page), 215, 240, 40, 24)
        me.viewAbility_INT_RANGE_IS_P = me.makeField(page, QtWidgets.QComboBox(page), 215, 270, 40, 24)
        me.viewAbility_LUK_RANGE_IS_P = me.makeField(page, QtWidgets.QComboBox(page), 215, 300, 40, 24)

        me.viewAbility_STR_RANGE_IS_P.addItems(['', '%'])
        me.viewAbility_DEX_RANGE_IS_P.addItems(['', '%'])
        me.viewAbility_INT_RANGE_IS_P.addItems(['', '%'])
        me.viewAbility_LUK_RANGE_IS_P.addItems(['', '%'])

        me.viewAbility_STR = me.makeField(page, QtWidgets.QLineEdit(page), 255, 210, 80, 24, ' →', 20)
        me.viewAbility_DEX = me.makeField(page, QtWidgets.QLineEdit(page), 255, 240, 80, 24, ' →', 20)
        me.viewAbility_INT = me.makeField(page, QtWidgets.QLineEdit(page), 255, 270, 80, 24, ' →', 20)
        me.viewAbility_LUK = me.makeField(page, QtWidgets.QLineEdit(page), 255, 300, 80, 24, ' →', 20)

        me.viewAbility_STR_UNIQUE = me.makeField(page, QtWidgets.QLineEdit(page), 340, 210, 170, 24, '  不吃% STR', 70)
        me.viewAbility_DEX_UNIQUE = me.makeField(page, QtWidgets.QLineEdit(page), 340, 240, 170, 24, '  不吃% DEX', 70)
        me.viewAbility_INT_UNIQUE = me.makeField(page, QtWidgets.QLineEdit(page), 340, 270, 170, 24, '  不吃% INT', 70)
        me.viewAbility_LUK_UNIQUE = me.makeField(page, QtWidgets.QLineEdit(page), 340, 300, 170, 24, '  不吃% LUK', 70)

        me.viewAbility_DEFENSE_P = me.makeField(page, QtWidgets.QLineEdit(page), 15, 370, 240, 24, '怪物防禦', 55, '％')
        
        me.viewAbility_MAPLE_15 = me.makeField(page, QtWidgets.QLabel(page), 270, 370, 120, 24)
        me.viewAbility_MAPLE_15.setText('楓祝15% = 0')
        

        me.viewAbility_MAPLE_16 = me.makeField(page, QtWidgets.QLabel(page), 390, 370, 120, 24)
        me.viewAbility_MAPLE_16.setText('楓祝16% = 0')

        me.viewAbility_ATTACK = me.makeField(page, QtWidgets.QLineEdit(page), 15, 400, 240, 24, '攻擊校正')

        return page

    def updateMapleValue(me):
        LEVEL = int(me.viewAbility_LEVEL.text())
        AP = (LEVEL * 5) + 18
        MAPLE_15 = int(AP * 0.15)
        MAPLE_16 = int(AP * 0.16)
        me.viewAbility_MAPLE_15.setText('楓祝15% = ' + str(MAPLE_15))
        me.viewAbility_MAPLE_16.setText('楓祝16% = ' + str(MAPLE_16))

    # function: 傳授
    def desingPage_Link(me):
        page = QtWidgets.QWidget()
        
        return page
    
    # function: 角色參數
    def desingPage_Parameter(me):
        page = QtWidgets.QWidget()

        # 等效增幅
        RANGE_TYPE = [
            '攻擊　 =', '％攻擊 =',
            '％總傷 =', '％Ｂ傷 =',
            '％爆傷 =', '％無視 =',
            '％全屬 =',
            '力量　 =', '％力量 =',
            '敏捷　 =', '％敏捷 =',
            '智力　 =', '％智力 =',
            '幸運　 =', '％幸運 =',
        ]

        PARAMETER_TYPE = [
            '力量　', '％力量',
            '敏捷　', '％敏捷',
            '智力　', '％智力',
            '幸運　', '％幸運',
            '％全屬',
            '攻擊　', '％攻擊',
            '％總傷', '％Ｂ傷',
            '％爆傷', '％無視',
        ]
        
        me.viewParameter_RANGE_VALUE = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15, 40 , 24)
        me.viewParameter_RANGE_VALUE.setText('1')

        me.viewParameter_RANGE_TYPE  = me.makeField(page, QtWidgets.QComboBox(page), 60, 15, 75, 24)
        me.viewParameter_RANGE_TYPE.addItems(RANGE_TYPE)

        me.makeField(page, QtWidgets.QLineEdit(page), 140, 15, 120, 24, '', 0, '％全屬', 50).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 265, 15, 120, 24, '', 0, '　力量', 50).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 390, 15, 120, 24, '', 0, '％力量', 50).setEnabled(False)
        
        me.makeField(page, QtWidgets.QLineEdit(page), 15 , 45, 120, 24, '', 0, '　攻擊', 50).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 140, 45, 120, 24, '', 0, '％攻擊', 50).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 265, 45, 120, 24, '', 0, '　敏捷', 50).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 390, 45, 120, 24, '', 0, '％敏捷', 50).setEnabled(False)
        
        me.makeField(page, QtWidgets.QLineEdit(page), 15 , 75, 120, 24, '', 0, '％總傷', 50).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 140, 75, 120, 24, '', 0, '％BOSS', 50).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 265, 75, 120, 24, '', 0, '　智力', 50).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 390, 75, 120, 24, '', 0, '％智力', 50).setEnabled(False)
        
        me.makeField(page, QtWidgets.QLineEdit(page), 15 ,105, 120, 24, '', 0, '％爆傷', 50).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 140,105, 120, 24, '', 0, '％無視', 50).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 265,105, 120, 24, '', 0, '　幸運', 50).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 390,105, 120, 24, '', 0, '％幸運', 50).setEnabled(False)

        me.viewParameter_EQUIVALENT_ALL_P    = me.makeField(page, QtWidgets.QLabel(page), 5 + 140, 15, 120, 24)
        me.viewParameter_EQUIVALENT_STR      = me.makeField(page, QtWidgets.QLabel(page), 5 + 265, 15, 120, 24)
        me.viewParameter_EQUIVALENT_STR_P    = me.makeField(page, QtWidgets.QLabel(page), 5 + 390, 15, 120, 24)
        
        me.viewParameter_EQUIVALENT_Att      = me.makeField(page, QtWidgets.QLabel(page), 5 + 15 , 45, 120, 24)
        me.viewParameter_EQUIVALENT_Att_P    = me.makeField(page, QtWidgets.QLabel(page), 5 + 140, 45, 120, 24)
        me.viewParameter_EQUIVALENT_DEX      = me.makeField(page, QtWidgets.QLabel(page), 5 + 265, 45, 120, 24)
        me.viewParameter_EQUIVALENT_DEX_P    = me.makeField(page, QtWidgets.QLabel(page), 5 + 390, 45, 120, 24)

        me.viewParameter_EQUIVALENT_Dmg_P    = me.makeField(page, QtWidgets.QLabel(page), 5 + 15 , 75, 120, 24)
        me.viewParameter_EQUIVALENT_Boss_P   = me.makeField(page, QtWidgets.QLabel(page), 5 + 140, 75, 120, 24)
        me.viewParameter_EQUIVALENT_INT      = me.makeField(page, QtWidgets.QLabel(page), 5 + 265, 75, 120, 24)
        me.viewParameter_EQUIVALENT_INT_P    = me.makeField(page, QtWidgets.QLabel(page), 5 + 390, 75, 120, 24)
        
        me.viewParameter_EQUIVALENT_Strike_P = me.makeField(page, QtWidgets.QLabel(page), 5 + 15 ,105, 120, 24)
        me.viewParameter_EQUIVALENT_Ignore_P = me.makeField(page, QtWidgets.QLabel(page), 5 + 140,105, 120, 24)
        me.viewParameter_EQUIVALENT_LUK      = me.makeField(page, QtWidgets.QLabel(page), 5 + 265,105, 120, 24)
        me.viewParameter_EQUIVALENT_LUK_P    = me.makeField(page, QtWidgets.QLabel(page), 5 + 390,105, 120, 24)
        
        # 單項增幅
        me.viewParameter_IMPROVE_VALUE_STR   = me.makeField(page, QtWidgets.QLineEdit(page), 20, 140, 115, 24, '力量　 增加', 65)
        me.viewParameter_IMPROVE_VALUE_STR_P = me.makeField(page, QtWidgets.QLineEdit(page), 20, 170, 115, 24, '力量％ 增加', 65, '%')
        me.viewParameter_IMPROVE_VALUE_DEX   = me.makeField(page, QtWidgets.QLineEdit(page), 20, 200, 115, 24, '敏捷　 增加', 65)
        me.viewParameter_IMPROVE_VALUE_DEX_P = me.makeField(page, QtWidgets.QLineEdit(page), 20, 230, 115, 24, '敏捷％ 增加', 65, '%')
        me.viewParameter_IMPROVE_VALUE_INT   = me.makeField(page, QtWidgets.QLineEdit(page), 20, 260, 115, 24, '智力　 增加', 65)
        me.viewParameter_IMPROVE_VALUE_INT_P = me.makeField(page, QtWidgets.QLineEdit(page), 20, 290, 115, 24, '智力％ 增加', 65, '%')
        me.viewParameter_IMPROVE_VALUE_LUK   = me.makeField(page, QtWidgets.QLineEdit(page), 20, 320, 115, 24, '幸運　 增加', 65)
        me.viewParameter_IMPROVE_VALUE_LUK_P = me.makeField(page, QtWidgets.QLineEdit(page), 20, 350, 115, 24, '幸運％ 增加', 65, '%')
        me.viewParameter_IMPROVE_VALUE_ALL_P = me.makeField(page, QtWidgets.QLineEdit(page), 20, 380, 115, 24, '全屬％ 增加', 65, '%')

        me.viewParameter_IMPROVE_VALUE_ATT      = me.makeField(page, QtWidgets.QLineEdit(page), 220, 140, 115, 24, '攻擊　 增加', 65)
        me.viewParameter_IMPROVE_VALUE_ATT_P    = me.makeField(page, QtWidgets.QLineEdit(page), 220, 170, 115, 24, '攻擊％ 增加', 65, '%')
        me.viewParameter_IMPROVE_VALUE_DMG_P    = me.makeField(page, QtWidgets.QLineEdit(page), 220, 200, 115, 24, '總傷％ 增加', 65, '%')
        me.viewParameter_IMPROVE_VALUE_BOSS_P   = me.makeField(page, QtWidgets.QLineEdit(page), 220, 230, 115, 24, 'Ｂ傷％ 增加', 65, '%')
        me.viewParameter_IMPROVE_VALUE_STRIKE_P = me.makeField(page, QtWidgets.QLineEdit(page), 220, 260, 115, 24, '爆傷％ 增加', 65, '%')
        me.viewParameter_IMPROVE_VALUE_IGNORE_P = me.makeField(page, QtWidgets.QLineEdit(page), 220, 290, 115, 24, '無視％ 增加', 65, '%')

        me.viewParameter_IMPROVE_STR   = me.makeField(page, QtWidgets.QLabel(page), 140, 140, 120, 24)
        me.viewParameter_IMPROVE_STR_P = me.makeField(page, QtWidgets.QLabel(page), 140, 170, 120, 24)
        me.viewParameter_IMPROVE_DEX   = me.makeField(page, QtWidgets.QLabel(page), 140, 200, 120, 24)
        me.viewParameter_IMPROVE_DEX_P = me.makeField(page, QtWidgets.QLabel(page), 140, 230, 120, 24)
        me.viewParameter_IMPROVE_INT   = me.makeField(page, QtWidgets.QLabel(page), 140, 260, 120, 24)
        me.viewParameter_IMPROVE_INT_P = me.makeField(page, QtWidgets.QLabel(page), 140, 290, 120, 24)
        me.viewParameter_IMPROVE_LUK   = me.makeField(page, QtWidgets.QLabel(page), 140, 320, 120, 24)
        me.viewParameter_IMPROVE_LUK_P = me.makeField(page, QtWidgets.QLabel(page), 140, 350, 120, 24)
        me.viewParameter_IMPROVE_ALL_P = me.makeField(page, QtWidgets.QLabel(page), 140, 380, 120, 24)

        me.viewParameter_IMPROVE_ATT      = me.makeField(page, QtWidgets.QLabel(page), 340, 140, 120, 24)
        me.viewParameter_IMPROVE_ATT_P    = me.makeField(page, QtWidgets.QLabel(page), 340, 170, 120, 24)
        me.viewParameter_IMPROVE_DMG_P    = me.makeField(page, QtWidgets.QLabel(page), 340, 200, 120, 24)
        me.viewParameter_IMPROVE_BOSS_P   = me.makeField(page, QtWidgets.QLabel(page), 340, 230, 120, 24)
        me.viewParameter_IMPROVE_STRIKE_P = me.makeField(page, QtWidgets.QLabel(page), 340, 260, 120, 24)
        me.viewParameter_IMPROVE_IGNORE_P = me.makeField(page, QtWidgets.QLabel(page), 340, 290, 120, 24)

        impTxt = '增幅 0.0%'
        me.viewParameter_IMPROVE_STR.setText(impTxt)
        me.viewParameter_IMPROVE_STR_P.setText(impTxt)
        me.viewParameter_IMPROVE_DEX.setText(impTxt)
        me.viewParameter_IMPROVE_DEX_P.setText(impTxt)
        me.viewParameter_IMPROVE_INT.setText(impTxt)
        me.viewParameter_IMPROVE_INT_P.setText(impTxt)
        me.viewParameter_IMPROVE_LUK.setText(impTxt)
        me.viewParameter_IMPROVE_LUK_P.setText(impTxt)
        me.viewParameter_IMPROVE_ALL_P.setText(impTxt)

        me.viewParameter_IMPROVE_ATT.setText(impTxt)
        me.viewParameter_IMPROVE_ATT_P.setText(impTxt)
        me.viewParameter_IMPROVE_DMG_P.setText(impTxt)
        me.viewParameter_IMPROVE_BOSS_P.setText(impTxt)
        me.viewParameter_IMPROVE_STRIKE_P.setText(impTxt)
        me.viewParameter_IMPROVE_IGNORE_P.setText(impTxt)

        me.viewParameter_IMPROVE_Total = me.makeField(page, QtWidgets.QLabel(page), 220, 320, 400, 24)
        me.viewParameter_IMPROVE_Total.setText('總增幅 0.000%')

        me.viewParameter_IMPROVE_VALUE_AS = me.makeField(page, QtWidgets.QLabel(page),220, 350, 115, 24)
        me.viewParameter_IMPROVE_VALUE_AS.setText('等同於 增加 0.00')
        
        me.viewParameter_IMPROVE_VALUE_AS_PARAMETER = me.makeField(page, QtWidgets.QComboBox(page),340, 350, 70, 24)
        me.viewParameter_IMPROVE_VALUE_AS_PARAMETER.addItems(PARAMETER_TYPE)
        
        # me.viewParameter_IMPROVE_ARC_Ring = me.makeField(page, QtWidgets.QLabel(page), 220, 350, 400, 24)
        # me.viewParameter_IMPROVE_ARC_Ring.setText('艾戒\t0.000%')

        # 推估數值
        me.makeField(page, QtWidgets.QLineEdit(page), 415, 140 + 36 * 0, 95, 36).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 415, 140 + 36 * 1, 95, 36).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 415, 140 + 36 * 2, 95, 36).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 415, 140 + 36 * 3, 95, 36).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 415, 153 + 36 * 4, 95,107).setEnabled(False)

        me.viewParameter_ESTIMATE_STR   = me.makeField(page, QtWidgets.QLabel(page), 417, 140 + 18 * 0, 95, 18, 'STR' , 40, '' , 19)
        me.viewParameter_ESTIMATE_STR_P = me.makeField(page, QtWidgets.QLabel(page), 417, 140 + 18 * 1, 95, 18, 'STR%', 40, '%', 19)

        me.viewParameter_ESTIMATE_DEX   = me.makeField(page, QtWidgets.QLabel(page), 417, 140 + 18 * 2, 95, 18, 'DEX' , 40, '' , 19)
        me.viewParameter_ESTIMATE_DEX_P = me.makeField(page, QtWidgets.QLabel(page), 417, 140 + 18 * 3, 95, 18, 'DEX%', 40, '%', 19)

        me.viewParameter_ESTIMATE_INT   = me.makeField(page, QtWidgets.QLabel(page), 417, 140 + 18 * 4, 95, 18, 'INT' , 40, '' , 19)
        me.viewParameter_ESTIMATE_INT_P = me.makeField(page, QtWidgets.QLabel(page), 417, 140 + 18 * 5, 95, 18, 'INT%', 40, '%', 19)

        me.viewParameter_ESTIMATE_LUK   = me.makeField(page, QtWidgets.QLabel(page), 417, 140 + 18 * 6, 95, 18, 'LUK' , 40, '' , 19)
        me.viewParameter_ESTIMATE_LUK_P = me.makeField(page, QtWidgets.QLabel(page), 417, 140 + 18 * 7, 95, 18, 'LUK%', 40, '%', 19)

        me.viewParameter_ESTIMATE_ATTACK   = me.makeField(page, QtWidgets.QLabel(page), 417, 153 + 18 * 8, 95, 18, '攻擊' , 40, '' , 19)
        me.viewParameter_ESTIMATE_ATTACK_P = me.makeField(page, QtWidgets.QLabel(page), 417, 153 + 18 * 9, 95, 18, '攻擊%', 40, '%', 19)
        me.viewParameter_ESTIMATE_DMG_P    = me.makeField(page, QtWidgets.QLabel(page), 417, 153 + 18 *10, 95, 18, '傷害%', 40, '%', 19)
        me.viewParameter_ESTIMATE_BOSS_P   = me.makeField(page, QtWidgets.QLabel(page), 417, 153 + 18 *11, 95, 18, 'Ｂ傷%', 40, '%', 19)
        me.viewParameter_ESTIMATE_STRIKE_P = me.makeField(page, QtWidgets.QLabel(page), 417, 153 + 18 *12, 95, 18, '爆傷%', 40, '%', 19)
        me.viewParameter_ESTIMATE_IGNORE_P = me.makeField(page, QtWidgets.QLabel(page), 417, 153 + 18 *13, 95, 18, '無視%', 40, '%', 19)
        
        return page

    # function: 塔戒
    def desingPage_SeedRing(me):
        page = QtWidgets.QWidget()

        me.makeField(page, QtWidgets.QLabel(page),  15, 10, 130, 24).setText('原戒指能力')
        me.makeField(page, QtWidgets.QLabel(page), 160, 10, 130, 24).setText('塔戒種類')
        me.makeField(page, QtWidgets.QLabel(page), 250, 10, 130, 24).setText('LV1')
        me.makeField(page, QtWidgets.QLabel(page), 320, 10, 130, 24).setText('LV2')
        me.makeField(page, QtWidgets.QLabel(page), 390, 10, 130, 24).setText('LV3')
        me.makeField(page, QtWidgets.QLabel(page), 460, 10, 130, 24).setText('LV4')

        me.viewSeedRing_STR       = me.makeField(page, QtWidgets.QLineEdit(page), 15, 10 + 25 *  1, 130, 24, 'STR' , 55, '')
        me.viewSeedRing_STR_P     = me.makeField(page, QtWidgets.QLineEdit(page), 15, 10 + 25 *  2, 130, 24, 'STR%', 55, '％')
        me.viewSeedRing_DEX       = me.makeField(page, QtWidgets.QLineEdit(page), 15, 10 + 25 *  3, 130, 24, 'DEX' , 55, '')
        me.viewSeedRing_DEX_P     = me.makeField(page, QtWidgets.QLineEdit(page), 15, 10 + 25 *  4, 130, 24, 'DEX%', 55, '％')
        me.viewSeedRing_INT       = me.makeField(page, QtWidgets.QLineEdit(page), 15, 10 + 25 *  5, 130, 24, 'INT' , 55, '')
        me.viewSeedRing_INT_P     = me.makeField(page, QtWidgets.QLineEdit(page), 15, 10 + 25 *  6, 130, 24, 'INT%', 55, '％')
        me.viewSeedRing_LUK       = me.makeField(page, QtWidgets.QLineEdit(page), 15, 10 + 25 *  7, 130, 24, 'LUK' , 55, '')
        me.viewSeedRing_LUK_P     = me.makeField(page, QtWidgets.QLineEdit(page), 15, 10 + 25 *  8, 130, 24, 'LUK%', 55, '％')
        me.viewSeedRing_ALL_P     = me.makeField(page, QtWidgets.QLineEdit(page), 15, 10 + 25 *  9, 130, 24, '全屬%', 55, '％')
        me.viewSeedRing_ATTACK    = me.makeField(page, QtWidgets.QLineEdit(page), 15, 10 + 25 * 10, 130, 24, '攻擊' , 55, '')
        me.viewSeedRing_ATTACK_P  = me.makeField(page, QtWidgets.QLineEdit(page), 15, 10 + 25 * 11, 130, 24, '攻擊%', 55, '％')
        me.viewSeedRing_DMG_P     = me.makeField(page, QtWidgets.QLineEdit(page), 15, 10 + 25 * 12, 130, 24, '傷害%', 55, '％')
        me.viewSeedRing_STRIKE_P  = me.makeField(page, QtWidgets.QLineEdit(page), 15, 10 + 25 * 13, 130, 24, '爆傷%', 55, '％')
        me.viewSeedRing_IGNORE_P  = me.makeField(page, QtWidgets.QLineEdit(page), 15, 10 + 25 * 14, 130, 24, '無視%', 55, '％')
        me.viewSeedRing_WP_ATTACK = me.makeField(page, QtWidgets.QLineEdit(page), 15, 10 + 25 * 15, 130, 24, '武器攻擊')
        # me.viewSeedRing_ALL_IN    = me.makeField(page, QtWidgets.QLineEdit(page), 15, 10 + 25 * 16, 130, 24, '爆發倍率')
        # me.viewSeedRing_ALL_IN.setText('1')
        me.makeField(page, QtWidgets.QLabel(page), 160, 10 + 25 * 15, 500, 24).setText('←請填寫武器攻擊力')
        # me.makeField(page, QtWidgets.QLabel(page), 160,  3 + 25 * 16, 500, 24).setText('←爆發時相對於平砍時的倍率，預設會吃滿塔戒時間')
        # me.makeField(page, QtWidgets.QLabel(page), 160, 17 + 25 * 16, 500, 24).setText('　有武公的情況「規範戒指」與「冒險家戒指」會失真')

        me.makeField(page, QtWidgets.QLineEdit(page), 155, 10 + 28 * 1, 365, 24).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 155, 10 + 28 * 2, 365, 24).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 155, 10 + 28 * 3, 365, 24).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 155, 10 + 28 * 4, 365, 24).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 155, 10 + 28 * 5, 365, 24).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 155, 10 + 28 * 6, 365, 24).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 155, 10 + 28 * 7, 365, 24).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 155, 10 + 28 * 8, 365, 24).setEnabled(False)
        
        me.makeField(page, QtWidgets.QLabel(page), 160, 10 + 28 * 1, 130, 24).setText('武器泡泡 - Ｓ')
        me.makeField(page, QtWidgets.QLabel(page), 160, 10 + 28 * 2, 130, 24).setText('武器泡泡 - Ｄ')
        me.makeField(page, QtWidgets.QLabel(page), 160, 10 + 28 * 3, 130, 24).setText('武器泡泡 - Ｉ')
        me.makeField(page, QtWidgets.QLabel(page), 160, 10 + 28 * 4, 130, 24).setText('武器泡泡 - Ｌ')
        me.makeField(page, QtWidgets.QLabel(page), 160, 10 + 28 * 5, 130, 24).setText('拇指環')
        me.makeField(page, QtWidgets.QLabel(page), 160, 10 + 28 * 6, 130, 24).setText('冒險家戒指')
        me.makeField(page, QtWidgets.QLabel(page), 160, 10 + 28 * 7, 130, 24).setText('規範戒指')
        me.makeField(page, QtWidgets.QLabel(page), 160, 10 + 28 * 8, 130, 24).setText('爆擊傷害戒指')
        me.makeField(page, QtWidgets.QLabel(page), 160, 10 + 28 * 9, 130, 24).setText('時間常數')
        me.makeField(page, QtWidgets.QLabel(page), 160, 10 + 28 *10, 999, 24).setText('※ 時間常數為計算持續時間總效益，不考慮時間選1')
        me.makeField(page, QtWidgets.QLabel(page), 160, 10 + 28 *11, 999, 24).setText('※ 時間常數套用上限為各戒指最高持續時間')
        

        me.viewSeedRing_TIME_VALUE_TXT = me.makeField(page, QtWidgets.QLabel(page), 220, 10 + 28 * 9, 130, 24)
        me.viewSeedRing_TIME_VALUE_TXT.setText('1 秒')
        
        me.viewSeedRing_TIME_VALUE = me.makeField(page, QtWidgets.QSlider(page), 250, 10 + 28 * 9, 270, 24)
        me.viewSeedRing_TIME_VALUE.setOrientation(QtCore.Qt.Horizontal)
        me.viewSeedRing_TIME_VALUE.setMinimum(1)
        me.viewSeedRing_TIME_VALUE.setMaximum(30)
        me.viewSeedRing_TIME_VALUE.setValue(1)
        
        me.viewSeedRing_WEAPON_STR_LV1 = me.makeField(page, QtWidgets.QLabel(page), 250, 10 + 28 * 1, 130, 24)
        me.viewSeedRing_WEAPON_STR_LV2 = me.makeField(page, QtWidgets.QLabel(page), 320, 10 + 28 * 1, 130, 24)
        me.viewSeedRing_WEAPON_STR_LV3 = me.makeField(page, QtWidgets.QLabel(page), 390, 10 + 28 * 1, 130, 24)
        me.viewSeedRing_WEAPON_STR_LV4 = me.makeField(page, QtWidgets.QLabel(page), 460, 10 + 28 * 1, 130, 24)

        me.viewSeedRing_WEAPON_DEX_LV1 = me.makeField(page, QtWidgets.QLabel(page), 250, 10 + 28 * 2, 130, 24)
        me.viewSeedRing_WEAPON_DEX_LV2 = me.makeField(page, QtWidgets.QLabel(page), 320, 10 + 28 * 2, 130, 24)
        me.viewSeedRing_WEAPON_DEX_LV3 = me.makeField(page, QtWidgets.QLabel(page), 390, 10 + 28 * 2, 130, 24)
        me.viewSeedRing_WEAPON_DEX_LV4 = me.makeField(page, QtWidgets.QLabel(page), 460, 10 + 28 * 2, 130, 24)

        me.viewSeedRing_WEAPON_INT_LV1 = me.makeField(page, QtWidgets.QLabel(page), 250, 10 + 28 * 3, 130, 24)
        me.viewSeedRing_WEAPON_INT_LV2 = me.makeField(page, QtWidgets.QLabel(page), 320, 10 + 28 * 3, 130, 24)
        me.viewSeedRing_WEAPON_INT_LV3 = me.makeField(page, QtWidgets.QLabel(page), 390, 10 + 28 * 3, 130, 24)
        me.viewSeedRing_WEAPON_INT_LV4 = me.makeField(page, QtWidgets.QLabel(page), 460, 10 + 28 * 3, 130, 24)

        me.viewSeedRing_WEAPON_LUK_LV1 = me.makeField(page, QtWidgets.QLabel(page), 250, 10 + 28 * 4, 130, 24)
        me.viewSeedRing_WEAPON_LUK_LV2 = me.makeField(page, QtWidgets.QLabel(page), 320, 10 + 28 * 4, 130, 24)
        me.viewSeedRing_WEAPON_LUK_LV3 = me.makeField(page, QtWidgets.QLabel(page), 390, 10 + 28 * 4, 130, 24)
        me.viewSeedRing_WEAPON_LUK_LV4 = me.makeField(page, QtWidgets.QLabel(page), 460, 10 + 28 * 4, 130, 24)

        me.viewSeedRing_TOTALLING_LV1 = me.makeField(page, QtWidgets.QLabel(page), 250, 10 + 28 * 5, 130, 24)
        me.viewSeedRing_TOTALLING_LV2 = me.makeField(page, QtWidgets.QLabel(page), 320, 10 + 28 * 5, 130, 24)
        me.viewSeedRing_TOTALLING_LV3 = me.makeField(page, QtWidgets.QLabel(page), 390, 10 + 28 * 5, 130, 24)
        me.viewSeedRing_TOTALLING_LV4 = me.makeField(page, QtWidgets.QLabel(page), 460, 10 + 28 * 5, 130, 24)

        me.viewSeedRing_RISTTAKER_LV1 = me.makeField(page, QtWidgets.QLabel(page), 250, 10 + 28 * 6, 130, 24)
        me.viewSeedRing_RISTTAKER_LV2 = me.makeField(page, QtWidgets.QLabel(page), 320, 10 + 28 * 6, 130, 24)
        me.viewSeedRing_RISTTAKER_LV3 = me.makeField(page, QtWidgets.QLabel(page), 390, 10 + 28 * 6, 130, 24)
        me.viewSeedRing_RISTTAKER_LV4 = me.makeField(page, QtWidgets.QLabel(page), 460, 10 + 28 * 6, 130, 24)

        me.viewSeedRing_RESTRAINT_LV1 = me.makeField(page, QtWidgets.QLabel(page), 250, 10 + 28 * 7, 130, 24)
        me.viewSeedRing_RESTRAINT_LV2 = me.makeField(page, QtWidgets.QLabel(page), 320, 10 + 28 * 7, 130, 24)
        me.viewSeedRing_RESTRAINT_LV3 = me.makeField(page, QtWidgets.QLabel(page), 390, 10 + 28 * 7, 130, 24)
        me.viewSeedRing_RESTRAINT_LV4 = me.makeField(page, QtWidgets.QLabel(page), 460, 10 + 28 * 7, 130, 24)

        me.viewSeedRing_STRIKE_LV1 = me.makeField(page, QtWidgets.QLabel(page), 250, 10 + 28 * 8, 130, 24)
        me.viewSeedRing_STRIKE_LV2 = me.makeField(page, QtWidgets.QLabel(page), 320, 10 + 28 * 8, 130, 24)
        me.viewSeedRing_STRIKE_LV3 = me.makeField(page, QtWidgets.QLabel(page), 390, 10 + 28 * 8, 130, 24)
        me.viewSeedRing_STRIKE_LV4 = me.makeField(page, QtWidgets.QLabel(page), 460, 10 + 28 * 8, 130, 24)

        me.viewSeedRing_WEAPON_STR_LV1.setText('0.0%')
        me.viewSeedRing_WEAPON_STR_LV2.setText('0.0%')
        me.viewSeedRing_WEAPON_STR_LV3.setText('0.0%')
        me.viewSeedRing_WEAPON_STR_LV4.setText('0.0%')

        me.viewSeedRing_WEAPON_DEX_LV1.setText('0.0%')
        me.viewSeedRing_WEAPON_DEX_LV2.setText('0.0%')
        me.viewSeedRing_WEAPON_DEX_LV3.setText('0.0%')
        me.viewSeedRing_WEAPON_DEX_LV4.setText('0.0%')

        me.viewSeedRing_WEAPON_INT_LV1.setText('0.0%')
        me.viewSeedRing_WEAPON_INT_LV2.setText('0.0%')
        me.viewSeedRing_WEAPON_INT_LV3.setText('0.0%')
        me.viewSeedRing_WEAPON_INT_LV4.setText('0.0%')

        me.viewSeedRing_WEAPON_LUK_LV1.setText('0.0%')
        me.viewSeedRing_WEAPON_LUK_LV2.setText('0.0%')
        me.viewSeedRing_WEAPON_LUK_LV3.setText('0.0%')
        me.viewSeedRing_WEAPON_LUK_LV4.setText('0.0%')

        me.viewSeedRing_TOTALLING_LV1.setText('0.0%')
        me.viewSeedRing_TOTALLING_LV2.setText('0.0%')
        me.viewSeedRing_TOTALLING_LV3.setText('0.0%')
        me.viewSeedRing_TOTALLING_LV4.setText('0.0%')

        me.viewSeedRing_RISTTAKER_LV1.setText('0.0%')
        me.viewSeedRing_RISTTAKER_LV2.setText('0.0%')
        me.viewSeedRing_RISTTAKER_LV3.setText('0.0%')
        me.viewSeedRing_RISTTAKER_LV4.setText('0.0%')

        me.viewSeedRing_RESTRAINT_LV1.setText('0.0%')
        me.viewSeedRing_RESTRAINT_LV2.setText('0.0%')
        me.viewSeedRing_RESTRAINT_LV3.setText('0.0%')
        me.viewSeedRing_RESTRAINT_LV4.setText('0.0%')

        me.viewSeedRing_STRIKE_LV1.setText('0.0%')
        me.viewSeedRing_STRIKE_LV2.setText('0.0%')
        me.viewSeedRing_STRIKE_LV3.setText('0.0%')
        me.viewSeedRing_STRIKE_LV4.setText('0.0%')
        
        return page

    # event: 顯示時間常數
    def printTIME_VALUE(me):
        print(me.viewSeedRing_TIME_VALUE.value())
    
    # function: 裝備變更
    def desingPage_Equipment(me):
        page = QtWidgets.QWidget()

        
        me.makeField(page, QtWidgets.QLabel(page), 15, 15, 130, 24).setText('原裝備能力')
        me.makeField(page, QtWidgets.QLineEdit(page),11, 38, 138, 368).setEnabled(False)
        me.viewEquipment_origin_STR       = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 *  1, 130, 24, 'STR' , 55, '')
        me.viewEquipment_origin_STR_P     = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 *  2, 130, 24, 'STR%', 55, '％')
        me.viewEquipment_origin_DEX       = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 *  3, 130, 24, 'DEX' , 55, '')
        me.viewEquipment_origin_DEX_P     = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 *  4, 130, 24, 'DEX%', 55, '％')
        me.viewEquipment_origin_INT       = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 *  5, 130, 24, 'INT' , 55, '')
        me.viewEquipment_origin_INT_P     = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 *  6, 130, 24, 'INT%', 55, '％')
        me.viewEquipment_origin_LUK       = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 *  7, 130, 24, 'LUK' , 55, '')
        me.viewEquipment_origin_LUK_P     = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 *  8, 130, 24, 'LUK%', 55, '％')
        me.viewEquipment_origin_ALL_P     = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 *  9, 130, 24, '全屬%', 55, '％')
        me.viewEquipment_origin_ATTACK    = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 * 10, 130, 24, '攻擊' , 55, '')
        me.viewEquipment_origin_ATTACK_P  = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 * 11, 130, 24, '攻擊%', 55, '％')
        me.viewEquipment_origin_DMG_P     = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 * 12, 130, 24, '傷害%', 55, '％')
        me.viewEquipment_origin_STRIKE_P  = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 * 13, 130, 24, '爆傷%', 55, '％')
        me.viewEquipment_origin_IGNORE_P  = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 * 14, 130, 24, '無視%', 55, '％')
        # me.viewEquipment_origin_IMPROVE   = me.makeField(page, QtWidgets.QLabel(page), 15, 15 + 26 * 15, 130, 24)
        # me.viewEquipment_origin_IMPROVE.setText('增幅 0.0%')

        me.makeField(page, QtWidgets.QLabel(page),192, 15, 130, 24).setText('更換裝備1')
        me.makeField(page, QtWidgets.QLineEdit(page),188, 38, 138, 368).setEnabled(False)
        me.viewEquipment_Set1_STR       = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 *  1, 130, 24, 'STR' , 55, '')
        me.viewEquipment_Set1_STR_P     = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 *  2, 130, 24, 'STR%', 55, '％')
        me.viewEquipment_Set1_DEX       = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 *  3, 130, 24, 'DEX' , 55, '')
        me.viewEquipment_Set1_DEX_P     = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 *  4, 130, 24, 'DEX%', 55, '％')
        me.viewEquipment_Set1_INT       = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 *  5, 130, 24, 'INT' , 55, '')
        me.viewEquipment_Set1_INT_P     = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 *  6, 130, 24, 'INT%', 55, '％')
        me.viewEquipment_Set1_LUK       = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 *  7, 130, 24, 'LUK' , 55, '')
        me.viewEquipment_Set1_LUK_P     = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 *  8, 130, 24, 'LUK%', 55, '％')
        me.viewEquipment_Set1_ALL_P     = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 *  9, 130, 24, '全屬%', 55, '％')
        me.viewEquipment_Set1_ATTACK    = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 * 10, 130, 24, '攻擊' , 55, '')
        me.viewEquipment_Set1_ATTACK_P  = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 * 11, 130, 24, '攻擊%', 55, '％')
        me.viewEquipment_Set1_DMG_P     = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 * 12, 130, 24, '傷害%', 55, '％')
        me.viewEquipment_Set1_STRIKE_P  = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 * 13, 130, 24, '爆傷%', 55, '％')
        me.viewEquipment_Set1_IGNORE_P  = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 * 14, 130, 24, '無視%', 55, '％')
        me.viewEquipment_Set1_IMPROVE   = me.makeField(page, QtWidgets.QLabel(page), 192, 15 + 26 * 15, 130, 24)
        me.viewEquipment_Set1_IMPROVE.setText('增幅 0.0%')

        me.makeField(page, QtWidgets.QLabel(page),370, 15, 130, 24).setText('更換裝備2')
        me.makeField(page, QtWidgets.QLineEdit(page),366, 38, 138, 368).setEnabled(False)
        me.viewEquipment_Set2_STR       = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 *  1, 130, 24, 'STR' , 55, '')
        me.viewEquipment_Set2_STR_P     = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 *  2, 130, 24, 'STR%', 55, '％')
        me.viewEquipment_Set2_DEX       = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 *  3, 130, 24, 'DEX' , 55, '')
        me.viewEquipment_Set2_DEX_P     = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 *  4, 130, 24, 'DEX%', 55, '％')
        me.viewEquipment_Set2_INT       = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 *  5, 130, 24, 'INT' , 55, '')
        me.viewEquipment_Set2_INT_P     = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 *  6, 130, 24, 'INT%', 55, '％')
        me.viewEquipment_Set2_LUK       = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 *  7, 130, 24, 'LUK' , 55, '')
        me.viewEquipment_Set2_LUK_P     = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 *  8, 130, 24, 'LUK%', 55, '％')
        me.viewEquipment_Set2_ALL_P     = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 *  9, 130, 24, '全屬%', 55, '％')
        me.viewEquipment_Set2_ATTACK    = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 * 10, 130, 24, '攻擊' , 55, '')
        me.viewEquipment_Set2_ATTACK_P  = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 * 11, 130, 24, '攻擊%', 55, '％')
        me.viewEquipment_Set2_DMG_P     = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 * 12, 130, 24, '傷害%', 55, '％')
        me.viewEquipment_Set2_STRIKE_P  = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 * 13, 130, 24, '爆傷%', 55, '％')
        me.viewEquipment_Set2_IGNORE_P  = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 * 14, 130, 24, '無視%', 55, '％')
        me.viewEquipment_Set2_IMPROVE   = me.makeField(page, QtWidgets.QLabel(page), 370, 15 + 26 * 15, 130, 24)
        me.viewEquipment_Set2_IMPROVE.setText('增幅 0.0%')

        # me.viewEquipment_Set1_IGNORE_P.setEnabled(False)
        # me.viewEquipment_Set2_IGNORE_P.setEnabled(False)
        
        return page
    
    # function: 工具
    def desingPage_Tools(me):
        page = QtWidgets.QWidget()
        
        me.viewTools_IGNORE_BEFORE = me.makeField(page, QtWidgets.QLineEdit(page),  15, 15, 130, 24, '無視防禦', 55, '%')
        me.viewTools_IGNORE_RANGE  = me.makeField(page, QtWidgets.QLineEdit(page), 150, 15, 90, 24, ' + ', 15, '%')
        me.viewTools_IGNORE_AFTER  = me.makeField(page, QtWidgets.QLineEdit(page), 245, 15, 90, 24, ' = ', 15, '%')
        me.btnTools_IGNORE_SUBMIT  = me.makeField(page, QtWidgets.QPushButton(page), 340, 15, 65, 24)
        me.btnTools_IGNORE_SUBMIT.setText('計算')

        return page

    # function: 使用說明
    def desingPage_Memo(me):
        page = QtWidgets.QWidget()
        
        me.makeField(page, QtWidgets.QLabel(page), 15, 400, 800, 24,).setText('作者：牡羊\t版本號碼：' + me.version)
        
        me.makeField(page, QtWidgets.QLabel(page), 15, 15 + 30 * 0, 800, 24,).setText('1. 所有能力值皆須填寫BUFF後的狀態，除了屬性需單獨填寫變化量')
        me.makeField(page, QtWidgets.QLabel(page), 15, 15 + 30 * 1, 800, 24,).setText('2. 能力值設定填寫時，除屬性需依照變化量填寫，其餘皆須以相同狀態的能力值填寫')
        me.makeField(page, QtWidgets.QLabel(page), 15, 15 + 30 * 2, 800, 24,).setText('3. 此計算機提供數值僅為參考用，若因此工具衍伸的問題將不負責任')
        me.makeField(page, QtWidgets.QLabel(page), 15, 15 + 30 * 3, 800, 24,).setText('4. 如有使用問題請到巴哈「新楓之谷」版搜尋「裝備效益計算機」回報')
        
        return page
    
    # function: 產生輸入框
    def makeField(me, page, obj, x, y, width, height, prefixText = '', labelWidth = 0, subfixText = '', subLabelWidth = 0):
        # 前綴文字
        if (prefixText != ''):
            if (labelWidth == 0): labelWidth = 55
            label = QtWidgets.QLabel(page)
            label.setText(prefixText)
            label.setGeometry(QtCore.QRect(x, y, labelWidth, height))

        obj.setGeometry(QtCore.QRect(x + labelWidth, y, width - labelWidth, height))
        
        # 後綴文字
        if (subfixText != ''):
            if (subLabelWidth == 0): subLabelWidth = 20
            sublabel = QtWidgets.QLabel(page)
            sublabel.setText(subfixText)
            sublabel.setGeometry(QtCore.QRect(x + width - subLabelWidth + 5, y, subLabelWidth - 5, height))
            sublabel.setEnabled(False)
        return obj
    
    # function: 將字串轉換為 float
    def textToFloat(me, text):
        value = 0
        if(text == '-'): text = ''
        if(text != ''): value = float(text)
        return value

    # function: 將字串轉換為 float
    def textToInt(me, text):
        value = 0
        if(text == '-'): text = ''
        if(text != ''): value = int(text)
        return value

    def getColor(me, value):
        return 'color: ' + str(value >= 1 and (value == 1 and 'black' or 'red') or 'blue')
    
    
    

