from re import M
import sys
from PyQt5 import QtWidgets
from Charactor import Charactor
from Calculator_UI import Calculator_UI

class AppWindow(QtWidgets.QDialog):
    # event: APP初始化
    def __init__(me):
        super().__init__()
        me.myUI = Calculator_UI()
        me.myUI.setupUi(me)

        me.loadUIConfig()

        me.show()

    # function: UI事件綁定
    def loadUIConfig(me):
        myCharactor = Charactor()
        myUI = me.myUI

        # 載入職業資訊
        myUI.viewAbility_CLASS_IDX.addItems(myCharactor.getClasslist())
        myUI.viewAbility_WP_IDX.addItems(myCharactor.getWPlist())

        # page: 能力值設定
        myUI.viewAbility_CLASS_IDX.activated.connect(me.updateClassInfo)
        
        myUI.btnAbility_SelectFile.clicked.connect(me.doSelectFile)
        myUI.btnAbility_SaveFile.clicked.connect(me.doSaveFile)
        myUI.btnAbility_Submit.clicked.connect(me.doSubmit)

        # page: 角色參數
        myUI.viewParameter_RANGE_VALUE.textChanged.connect(me.calc_Equivalent)
        myUI.viewParameter_RANGE_TYPE.activated.connect(me.calc_Equivalent)

        myUI.viewParameter_IMPROVE_VALUE_STR.textChanged.connect(me.calc_Improve)
        myUI.viewParameter_IMPROVE_VALUE_STR_P.textChanged.connect(me.calc_Improve)
        myUI.viewParameter_IMPROVE_VALUE_DEX.textChanged.connect(me.calc_Improve)
        myUI.viewParameter_IMPROVE_VALUE_DEX_P.textChanged.connect(me.calc_Improve)
        myUI.viewParameter_IMPROVE_VALUE_INT.textChanged.connect(me.calc_Improve)
        myUI.viewParameter_IMPROVE_VALUE_INT_P.textChanged.connect(me.calc_Improve)
        myUI.viewParameter_IMPROVE_VALUE_LUK.textChanged.connect(me.calc_Improve)
        myUI.viewParameter_IMPROVE_VALUE_LUK_P.textChanged.connect(me.calc_Improve)
        myUI.viewParameter_IMPROVE_VALUE_ALL_P.textChanged.connect(me.calc_Improve)
        myUI.viewParameter_IMPROVE_VALUE_ATT.textChanged.connect(me.calc_Improve)
        myUI.viewParameter_IMPROVE_VALUE_ATT_P.textChanged.connect(me.calc_Improve)
        myUI.viewParameter_IMPROVE_VALUE_DMG_P.textChanged.connect(me.calc_Improve)
        myUI.viewParameter_IMPROVE_VALUE_BOSS_P.textChanged.connect(me.calc_Improve)
        myUI.viewParameter_IMPROVE_VALUE_STRIKE_P.textChanged.connect(me.calc_Improve)
        myUI.viewParameter_IMPROVE_VALUE_IGNORE_P.textChanged.connect(me.calc_Improve)

        # page: 塔戒
        myUI.viewSeedRing_STR.textChanged.connect(me.calc_SeedRing)
        myUI.viewSeedRing_STR_P.textChanged.connect(me.calc_SeedRing)
        myUI.viewSeedRing_DEX.textChanged.connect(me.calc_SeedRing)
        myUI.viewSeedRing_DEX_P.textChanged.connect(me.calc_SeedRing)
        myUI.viewSeedRing_INT.textChanged.connect(me.calc_SeedRing)
        myUI.viewSeedRing_INT_P.textChanged.connect(me.calc_SeedRing)
        myUI.viewSeedRing_LUK.textChanged.connect(me.calc_SeedRing)
        myUI.viewSeedRing_LUK_P.textChanged.connect(me.calc_SeedRing)
        myUI.viewSeedRing_ALL_P.textChanged.connect(me.calc_SeedRing)
        myUI.viewSeedRing_ATTACK.textChanged.connect(me.calc_SeedRing)
        myUI.viewSeedRing_ATTACK_P.textChanged.connect(me.calc_SeedRing)
        myUI.viewSeedRing_DMG_P.textChanged.connect(me.calc_SeedRing)
        myUI.viewSeedRing_STRIKE_P.textChanged.connect(me.calc_SeedRing)
        myUI.viewSeedRing_IGNORE_P.textChanged.connect(me.calc_SeedRing)
        myUI.viewSeedRing_WP_ATTACK.textChanged.connect(me.calc_SeedRing)
        myUI.viewSeedRing_TIME_VALUE.valueChanged.connect(me.calc_SeedRing)

        # page: 裝備變更
        myUI.viewEquipment_origin_STR.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_origin_STR_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_origin_DEX.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_origin_DEX_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_origin_INT.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_origin_INT_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_origin_LUK.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_origin_LUK_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_origin_ALL_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_origin_ATTACK.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_origin_ATTACK_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_origin_DMG_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_origin_STRIKE_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_origin_IGNORE_P.textChanged.connect(me.calc_Equipment)

        myUI.viewEquipment_Set1_STR.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set1_STR_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set1_DEX.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set1_DEX_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set1_INT.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set1_INT_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set1_LUK.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set1_LUK_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set1_ALL_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set1_ATTACK.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set1_ATTACK_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set1_DMG_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set1_STRIKE_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set1_IGNORE_P.textChanged.connect(me.calc_Equipment)

        myUI.viewEquipment_Set2_STR.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set2_STR_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set2_DEX.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set2_DEX_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set2_INT.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set2_INT_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set2_LUK.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set2_LUK_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set2_ALL_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set2_ATTACK.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set2_ATTACK_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set2_DMG_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set2_STRIKE_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set2_IGNORE_P.textChanged.connect(me.calc_Equipment)

        # page: 工具
        myUI.btnTools_IGNORE_SUBMIT.clicked.connect(me.doCalcIgnore)
        
        me.myCharactor = myCharactor
        pass
    
    # event: 更新職業對應資訊
    def updateClassInfo(me):
        myCharactor = me.myCharactor
        myUI = me.myUI

        CLASS_NAME = myUI.viewAbility_CLASS_IDX.currentText()
        CLASS_INFO = myCharactor.getClassInfo(CLASS_NAME)
        myUI.viewAbility_WP_IDX.setCurrentIndex(CLASS_INFO['WP_IDX'])
        # print(CLASS_INFO)
        pass

    # event: 選擇檔案
    def doSelectFile(me):
        try:
            fileName, filetype = QtWidgets.QFileDialog.getOpenFileName(me,'選擇檔案', './', 'txt (*.txt)')
            data = open(fileName, 'r')

            myUI = me.myUI
            for row in iter(data):
                item = row.replace('\n','').split('=')
                # print(item)

                if (item[0] == 'LEVEL'): myUI.viewAbility_LEVEL.setText(item[1])
                if (item[0] == 'CLASS_IDX'): myUI.viewAbility_CLASS_IDX.setCurrentIndex(int(item[1]))
                if (item[0] == 'MAX_DMG'): myUI.viewAbility_MAX_DMG.setText(item[1])
                if (item[0] == 'WP_IDX'): myUI.viewAbility_WP_IDX.setCurrentIndex(int(item[1]))
                if (item[0] == 'ATTACK'): myUI.viewAbility_ATTACK.setText(item[1])
                if (item[0] == 'ATTACK_P'): myUI.viewAbility_ATTACK_P.setText(item[1])
                if (item[0] == 'DMG_P'): myUI.viewAbility_DMG_P.setText(item[1])
                if (item[0] == 'BOSS_P'): myUI.viewAbility_BOSS_P.setText(item[1])
                if (item[0] == 'STRIKE_P'): myUI.viewAbility_STRIKE_P.setText(item[1])
                if (item[0] == 'IGNORE_P'): myUI.viewAbility_IGNORE_P.setText(item[1])
                if (item[0] == 'FINALDMG_P'): myUI.viewAbility_FINALDMG_P.setText(item[1])
                if (item[0] == 'DEFENSE_P'): myUI.viewAbility_DEFENSE_P.setText(item[1])
                
                if (item[0] == 'STR_BEFORE'): myUI.viewAbility_STR_BEFORE.setText(item[1])
                if (item[0] == 'STR_RANGE'): myUI.viewAbility_STR_RANGE.setText(item[1])
                if (item[0] == 'STR_RANGE_IS_P'): myUI.viewAbility_STR_RANGE_IS_P.setCurrentIndex(int(item[1]))
                if (item[0] == 'STR'): myUI.viewAbility_STR.setText(item[1])
                if (item[0] == 'STR_UNIQUE'): myUI.viewAbility_STR_UNIQUE.setText(item[1])

                if (item[0] == 'DEX_BEFORE'): myUI.viewAbility_DEX_BEFORE.setText(item[1])
                if (item[0] == 'DEX_RANGE'): myUI.viewAbility_DEX_RANGE.setText(item[1])
                if (item[0] == 'DEX_RANGE_IS_P'): myUI.viewAbility_DEX_RANGE_IS_P.setCurrentIndex(int(item[1]))
                if (item[0] == 'DEX'): myUI.viewAbility_DEX.setText(item[1])
                if (item[0] == 'DEX_UNIQUE'): myUI.viewAbility_DEX_UNIQUE.setText(item[1])

                if (item[0] == 'INT_BEFORE'): myUI.viewAbility_INT_BEFORE.setText(item[1])
                if (item[0] == 'INT_RANGE'): myUI.viewAbility_INT_RANGE.setText(item[1])
                if (item[0] == 'INT_RANGE_IS_P'): myUI.viewAbility_INT_RANGE_IS_P.setCurrentIndex(int(item[1]))
                if (item[0] == 'INT'): myUI.viewAbility_INT.setText(item[1])
                if (item[0] == 'INT_UNIQUE'): myUI.viewAbility_INT_UNIQUE.setText(item[1])

                if (item[0] == 'LUK_BEFORE'): myUI.viewAbility_LUK_BEFORE.setText(item[1])
                if (item[0] == 'LUK_RANGE'): myUI.viewAbility_LUK_RANGE.setText(item[1])
                if (item[0] == 'LUK_RANGE_IS_P'): myUI.viewAbility_LUK_RANGE_IS_P.setCurrentIndex(int(item[1]))
                if (item[0] == 'LUK'): myUI.viewAbility_LUK.setText(item[1])
                if (item[0] == 'LUK_UNIQUE'): myUI.viewAbility_LUK_UNIQUE.setText(item[1])

                if (item[0] == 'SEED_ATTACK'): myUI.viewSeedRing_ATTACK.setText(item[1])
                if (item[0] == 'SEED_ATTACK_P'): myUI.viewSeedRing_ATTACK_P.setText(item[1])
                if (item[0] == 'SEED_DMG_P'): myUI.viewSeedRing_DMG_P.setText(item[1])
                if (item[0] == 'SEED_STRIKE_P'): myUI.viewSeedRing_STRIKE_P.setText(item[1])
                if (item[0] == 'SEED_IGNORE_P'): myUI.viewSeedRing_IGNORE_P.setText(item[1])

                if (item[0] == 'SEED_STR'): myUI.viewSeedRing_STR.setText(item[1])
                if (item[0] == 'SEED_STR_P'): myUI.viewSeedRing_STR_P.setText(item[1])

                if (item[0] == 'SEED_DEX'): myUI.viewSeedRing_DEX.setText(item[1])
                if (item[0] == 'SEED_DEX_P'): myUI.viewSeedRing_DEX_P.setText(item[1])

                if (item[0] == 'SEED_INT'): myUI.viewSeedRing_INT.setText(item[1])
                if (item[0] == 'SEED_INT_P'): myUI.viewSeedRing_INT_P.setText(item[1])

                if (item[0] == 'SEED_LUK'): myUI.viewSeedRing_LUK.setText(item[1])
                if (item[0] == 'SEED_LUK_P'): myUI.viewSeedRing_LUK_P.setText(item[1])

                if (item[0] == 'SEED_ALL_P'): myUI.viewSeedRing_ALL_P.setText(item[1])

                if (item[0] == 'SEED_WEAPON_ATTACK'): myUI.viewSeedRing_WP_ATTACK.setText(item[1])
            
            data.close()
            me.doSubmit()
        except Exception:
            pass    
    
    # event: 儲存檔案
    def doSaveFile(me):
        try:
            fileName, filetype = QtWidgets.QFileDialog.getSaveFileName(me,'另存新檔','./','txt (*.txt)')
            data = open(fileName, 'w')
            myUI = me.myUI
            array = [
                'LEVEL=' + str(myUI.viewAbility_LEVEL.text()) + '\n',
                'CLASS_IDX=' + str(myUI.viewAbility_CLASS_IDX.currentIndex()) + '\n',
                'MAX_DMG=' + str(myUI.viewAbility_MAX_DMG.text()) + '\n',
                'WP_IDX=' + str(myUI.viewAbility_WP_IDX.currentIndex()) + '\n',
                'ATTACK=' + str(myUI.viewAbility_ATTACK.text()) + '\n',
                'ATTACK_P=' + str(myUI.viewAbility_ATTACK_P.text()) + '\n',
                'DMG_P=' + str(myUI.viewAbility_DMG_P.text()) + '\n',
                'BOSS_P=' + str(myUI.viewAbility_BOSS_P.text()) + '\n',
                'STRIKE_P=' + str(myUI.viewAbility_STRIKE_P.text()) + '\n',
                'IGNORE_P=' + str(myUI.viewAbility_IGNORE_P.text()) + '\n',
                'FINALDMG_P=' + str(myUI.viewAbility_FINALDMG_P.text()) + '\n',
                'DEFENSE_P=' + str(myUI.viewAbility_DEFENSE_P.text()) + '\n',
                
                'STR_BEFORE=' + str(myUI.viewAbility_STR_BEFORE.text()) + '\n',
                'STR_RANGE=' + str(myUI.viewAbility_STR_RANGE.text()) + '\n',
                'STR_RANGE_IS_P=' + str(myUI.viewAbility_STR_RANGE_IS_P.currentIndex()) + '\n',
                'STR=' + str(myUI.viewAbility_STR.text()) + '\n',
                'STR_UNIQUE=' + str(myUI.viewAbility_STR_UNIQUE.text()) + '\n',
                
                'DEX_BEFORE=' + str(myUI.viewAbility_DEX_BEFORE.text()) + '\n',
                'DEX_RANGE=' + str(myUI.viewAbility_DEX_RANGE.text()) + '\n',
                'DEX_RANGE_IS_P=' + str(myUI.viewAbility_DEX_RANGE_IS_P.currentIndex()) + '\n',
                'DEX=' + str(myUI.viewAbility_DEX.text()) + '\n',
                'DEX_UNIQUE=' + str(myUI.viewAbility_DEX_UNIQUE.text()) + '\n',

                'INT_BEFORE=' + str(myUI.viewAbility_INT_BEFORE.text()) + '\n',
                'INT_RANGE=' + str(myUI.viewAbility_INT_RANGE.text()) + '\n',
                'INT_RANGE_IS_P=' + str(myUI.viewAbility_INT_RANGE_IS_P.currentIndex()) + '\n',
                'INT=' + str(myUI.viewAbility_INT.text()) + '\n',
                'INT_UNIQUE=' + str(myUI.viewAbility_INT_UNIQUE.text()) + '\n',

                'LUK_BEFORE=' + str(myUI.viewAbility_LUK_BEFORE.text()) + '\n',
                'LUK_RANGE=' + str(myUI.viewAbility_LUK_RANGE.text()) + '\n',
                'LUK_RANGE_IS_P=' + str(myUI.viewAbility_LUK_RANGE_IS_P.currentIndex()) + '\n',
                'LUK=' + str(myUI.viewAbility_LUK.text()) + '\n',
                'LUK_UNIQUE=' + str(myUI.viewAbility_LUK_UNIQUE.text()) + '\n',

                'SEED_ATTACK=' + str(myUI.viewSeedRing_ATTACK.text()) + '\n',
                'SEED_ATTACK_P=' + str(myUI.viewSeedRing_ATTACK_P.text()) + '\n',
                'SEED_DMG_P=' + str(myUI.viewSeedRing_DMG_P.text()) + '\n',
                'SEED_STRIKE_P=' + str(myUI.viewSeedRing_STRIKE_P.text()) + '\n',
                'SEED_IGNORE_P=' + str(myUI.viewSeedRing_IGNORE_P.text()) + '\n',

                'SEED_STR=' + str(myUI.viewSeedRing_STR.text()) + '\n',
                'SEED_STR_P=' + str(myUI.viewSeedRing_STR_P.text()) + '\n',

                'SEED_DEX=' + str(myUI.viewSeedRing_DEX.text()) + '\n',
                'SEED_DEX_P=' + str(myUI.viewSeedRing_DEX_P.text()) + '\n',

                'SEED_INT=' + str(myUI.viewSeedRing_INT.text()) + '\n',
                'SEED_INT_P=' + str(myUI.viewSeedRing_INT_P.text()) + '\n',

                'SEED_LUK=' + str(myUI.viewSeedRing_LUK.text()) + '\n',
                'SEED_LUK_P=' + str(myUI.viewSeedRing_LUK_P.text()) + '\n',

                'SEED_ALL_P=' + str(myUI.viewSeedRing_ALL_P.text()) + '\n',
                
                'SEED_WEAPON_ATTACK=' + str(myUI.viewSeedRing_WP_ATTACK.text()) + '\n',
            ]

            data.writelines(array)
            data.close()
        except Exception:
            pass    
    
    # event: 送出資料
    def doSubmit(me):
        try:
            myCharactor = me.myCharactor
            myUI = me.myUI
            myCharactor.reset()

            data = {
                'LEVEL': myUI.textToInt(myUI.viewAbility_LEVEL.text()),
                'CLASS_IDX': myUI.textToInt(myUI.viewAbility_CLASS_IDX.currentIndex()),
                'WP_IDX': myUI.textToInt(myUI.viewAbility_WP_IDX.currentIndex()),
                'MAX_DMG': myUI.textToInt(myUI.viewAbility_MAX_DMG.text()),
                'ATTACK': myUI.textToInt(myUI.viewAbility_ATTACK.text()),
                'ATTACK_P': myUI.textToFloat(myUI.viewAbility_ATTACK_P.text()) / 100,
                'DMG_P': myUI.textToInt(myUI.viewAbility_DMG_P.text()) / 100,
                'BOSS_P': myUI.textToFloat(myUI.viewAbility_BOSS_P.text()) / 100,
                'STRIKE_P': myUI.textToFloat(myUI.viewAbility_STRIKE_P.text()) / 100,
                'IGNORE_P': myUI.textToFloat(myUI.viewAbility_IGNORE_P.text()) / 100,
                'FINALDMG_P': myUI.textToFloat(myUI.viewAbility_FINALDMG_P.text()) / 100,
                'DEFENSE_P': myUI.textToFloat(myUI.viewAbility_DEFENSE_P.text()) / 100,

                'STR_BEFORE': myUI.textToInt(myUI.viewAbility_STR_BEFORE.text()),
                'STR_RANGE': myUI.textToFloat(myUI.viewAbility_STR_RANGE.text()),
                'STR_RANGE_IS_P': myUI.textToInt(myUI.viewAbility_STR_RANGE_IS_P.currentIndex()),
                'STR': myUI.textToInt(myUI.viewAbility_STR.text()),
                'STR_UNIQUE': myUI.textToInt(myUI.viewAbility_STR_UNIQUE.text()),

                'DEX_BEFORE': myUI.textToInt(myUI.viewAbility_DEX_BEFORE.text()),
                'DEX_RANGE': myUI.textToFloat(myUI.viewAbility_DEX_RANGE.text()),
                'DEX_RANGE_IS_P': myUI.textToInt(myUI.viewAbility_DEX_RANGE_IS_P.currentIndex()),
                'DEX': myUI.textToInt(myUI.viewAbility_DEX.text()),
                'DEX_UNIQUE': myUI.textToInt(myUI.viewAbility_DEX_UNIQUE.text()),

                'INT_BEFORE': myUI.textToInt(myUI.viewAbility_INT_BEFORE.text()),
                'INT_RANGE': myUI.textToFloat(myUI.viewAbility_INT_RANGE.text()),
                'INT_RANGE_IS_P': myUI.textToInt(myUI.viewAbility_INT_RANGE_IS_P.currentIndex()),
                'INT': myUI.textToInt(myUI.viewAbility_INT.text()),
                'INT_UNIQUE': myUI.textToInt(myUI.viewAbility_INT_UNIQUE.text()),

                'LUK_BEFORE': myUI.textToInt(myUI.viewAbility_LUK_BEFORE.text()),
                'LUK_RANGE': myUI.textToFloat(myUI.viewAbility_LUK_RANGE.text()),
                'LUK_RANGE_IS_P': myUI.textToInt(myUI.viewAbility_LUK_RANGE_IS_P.currentIndex()),
                'LUK': myUI.textToInt(myUI.viewAbility_LUK.text()),
                'LUK_UNIQUE': myUI.textToInt(myUI.viewAbility_LUK_UNIQUE.text()),
            }

            myCharactor.updateAbilityByData(data)
            me.calc_Equivalent()
            me.calc_Improve()
            me.calc_SeedRing()
            me.calc_Equipment()
            QtWidgets.QMessageBox.information(me, '提示', '計算完成')
        except Exception:
            QtWidgets.QMessageBox.warning(me, '提示', '輸入資料有誤')
            pass

    # event: 計算等效數值
    def calc_Equivalent(me):
        try:
            myCharactor = me.myCharactor
            myUI = me.myUI
            
            if (myCharactor.isReset): return False
            
            RANGE_VALUE = myUI.textToFloat(myUI.viewParameter_RANGE_VALUE.text())
            RANGE_TYPE = myUI.viewParameter_RANGE_TYPE.currentText().replace('　', '').replace(' ', '').replace('=', '')
            
            new_data = {}

            if(RANGE_TYPE == '攻擊'):
                new_data['ATTACK'] = RANGE_VALUE
            
            if(RANGE_TYPE == '％攻擊'): 
                new_data['ATTACK_P'] = RANGE_VALUE / 100
                
            if(RANGE_TYPE == '％總傷'): 
                new_data['DMG_P'] = RANGE_VALUE / 100
                
            if(RANGE_TYPE == '％Ｂ傷'): 
                new_data['BOSS_P'] = RANGE_VALUE / 100
            
            if(RANGE_TYPE == '％爆傷'): 
                new_data['STRIKE_P'] = RANGE_VALUE / 100
                
            if(RANGE_TYPE == '％無視'):
                new_data['IGNORE_P'] = RANGE_VALUE / 100

            if(RANGE_TYPE == '％全屬'): 
                new_data['STR_P'] = RANGE_VALUE / 100
                new_data['DEX_P'] = RANGE_VALUE / 100
                new_data['INT_P'] = RANGE_VALUE / 100
                new_data['LUK_P'] = RANGE_VALUE / 100
                
            if(RANGE_TYPE == '力量'): 
                new_data['STR_CLEAR'] = RANGE_VALUE
                
            if(RANGE_TYPE == '％力量'): 
                new_data['STR_P'] = RANGE_VALUE / 100

            if(RANGE_TYPE == '敏捷'): 
                new_data['DEX_CLEAR'] = RANGE_VALUE
                
            if(RANGE_TYPE == '％敏捷'): 
                new_data['DEX_P'] = RANGE_VALUE / 100
                
            if(RANGE_TYPE == '智力'): 
                new_data['INT_CLEAR'] = RANGE_VALUE
                
            if(RANGE_TYPE == '％智力'): 
                new_data['INT_P'] = RANGE_VALUE / 100
                
            if(RANGE_TYPE == '幸運'): 
                new_data['LUK_CLEAR'] = RANGE_VALUE
                
            if(RANGE_TYPE == '％幸運'): 
                new_data['LUK_P'] = RANGE_VALUE / 100

            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            STATE_INFO = myCharactor.getEquivalent(IMPROVE_INFO['TOTAL'])

            def toRoundStr(value): 
                return str(round(value, 3))
            
            myUI.viewParameter_EQUIVALENT_ALL_P.setText(toRoundStr(STATE_INFO['ALL_P']*100))
            myUI.viewParameter_EQUIVALENT_Att.setText(toRoundStr(STATE_INFO['ATTACK']))
            myUI.viewParameter_EQUIVALENT_Att_P.setText(toRoundStr(STATE_INFO['ATTACK_P']*100))
            myUI.viewParameter_EQUIVALENT_Dmg_P.setText(toRoundStr(STATE_INFO['DMG_P']*100))
            myUI.viewParameter_EQUIVALENT_Boss_P.setText(toRoundStr(STATE_INFO['BOSS_P']*100))
            myUI.viewParameter_EQUIVALENT_Strike_P.setText(toRoundStr(STATE_INFO['STRIKE_P']*100))
            myUI.viewParameter_EQUIVALENT_Ignore_P.setText(toRoundStr(STATE_INFO['IGNORE_P']*100))
            
            myUI.viewParameter_EQUIVALENT_STR.setText(toRoundStr(STATE_INFO['STR_CLEAR']))
            myUI.viewParameter_EQUIVALENT_STR_P.setText(toRoundStr(STATE_INFO['STR_P']*100))
            
            myUI.viewParameter_EQUIVALENT_DEX.setText(toRoundStr(STATE_INFO['DEX_CLEAR']))
            myUI.viewParameter_EQUIVALENT_DEX_P.setText(toRoundStr(STATE_INFO['DEX_P']*100))
            
            myUI.viewParameter_EQUIVALENT_INT.setText(toRoundStr(STATE_INFO['INT_CLEAR']))
            myUI.viewParameter_EQUIVALENT_INT_P.setText(toRoundStr(STATE_INFO['INT_P']*100))
            
            myUI.viewParameter_EQUIVALENT_LUK.setText(toRoundStr(STATE_INFO['LUK_CLEAR']))
            myUI.viewParameter_EQUIVALENT_LUK_P.setText(toRoundStr(STATE_INFO['LUK_P']*100))
        except Exception:
            QtWidgets.QMessageBox.warning(me, '提示', '輸入資料有誤')
            pass

    # event: 計算增幅
    def calc_Improve(me):
        try:
            myCharactor = me.myCharactor
            myUI = me.myUI

            if (myCharactor.isReset): return False
            new_data = {
                'DMG_P': myUI.textToFloat(myUI.viewParameter_IMPROVE_VALUE_DMG_P.text()) / 100,
                'BOSS_P': myUI.textToFloat(myUI.viewParameter_IMPROVE_VALUE_BOSS_P.text()) / 100,
                'ATTACK': myUI.textToFloat(myUI.viewParameter_IMPROVE_VALUE_ATT.text()),
                'ATTACK_P': myUI.textToFloat(myUI.viewParameter_IMPROVE_VALUE_ATT_P.text()) / 100,
                'STRIKE_P': myUI.textToFloat(myUI.viewParameter_IMPROVE_VALUE_STRIKE_P.text()) / 100,
                'IGNORE_P': myUI.textToFloat(myUI.viewParameter_IMPROVE_VALUE_IGNORE_P.text()) / 100,

                'STR_CLEAR': myUI.textToFloat(myUI.viewParameter_IMPROVE_VALUE_STR.text()),
                'STR_P': myUI.textToFloat(myUI.viewParameter_IMPROVE_VALUE_STR_P.text()) / 100,

                'DEX_CLEAR': myUI.textToFloat(myUI.viewParameter_IMPROVE_VALUE_DEX.text()),
                'DEX_P': myUI.textToFloat(myUI.viewParameter_IMPROVE_VALUE_DEX_P.text()) / 100,

                'INT_CLEAR': myUI.textToFloat(myUI.viewParameter_IMPROVE_VALUE_INT.text()),
                'INT_P': myUI.textToFloat(myUI.viewParameter_IMPROVE_VALUE_INT_P.text()) / 100,

                'LUK_CLEAR': myUI.textToFloat(myUI.viewParameter_IMPROVE_VALUE_LUK.text()),
                'LUK_P': myUI.textToFloat(myUI.viewParameter_IMPROVE_VALUE_LUK_P.text()) / 100,

                'ALL_P': myUI.textToFloat(myUI.viewParameter_IMPROVE_VALUE_ALL_P.text()) / 100,
            }

            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            ESTIMATE_INFO = myCharactor.getEstimate(new_data)

            def toPercentText(value): 
                return str(round((value-1)*100, 3)) + '%'

            IMPROVE_TEXT = '增幅 '
            myUI.viewParameter_IMPROVE_STR.setText(IMPROVE_TEXT + toPercentText(IMPROVE_INFO['STR_CLEAR']))
            myUI.viewParameter_IMPROVE_STR_P.setText(IMPROVE_TEXT + toPercentText(IMPROVE_INFO['STR_P']))

            myUI.viewParameter_IMPROVE_DEX.setText(IMPROVE_TEXT + toPercentText(IMPROVE_INFO['DEX_CLEAR']))
            myUI.viewParameter_IMPROVE_DEX_P.setText(IMPROVE_TEXT + toPercentText(IMPROVE_INFO['DEX_P']))

            myUI.viewParameter_IMPROVE_INT.setText(IMPROVE_TEXT + toPercentText(IMPROVE_INFO['INT_CLEAR']))
            myUI.viewParameter_IMPROVE_INT_P.setText(IMPROVE_TEXT + toPercentText(IMPROVE_INFO['INT_P']))

            myUI.viewParameter_IMPROVE_LUK.setText(IMPROVE_TEXT + toPercentText(IMPROVE_INFO['LUK_CLEAR']))
            myUI.viewParameter_IMPROVE_LUK_P.setText(IMPROVE_TEXT + toPercentText(IMPROVE_INFO['LUK_P']))

            myUI.viewParameter_IMPROVE_ALL_P.setText(IMPROVE_TEXT + toPercentText(IMPROVE_INFO['ALL_P']))

            myUI.viewParameter_IMPROVE_ATT.setText(IMPROVE_TEXT + toPercentText(IMPROVE_INFO['ATTACK']))
            myUI.viewParameter_IMPROVE_ATT_P.setText(IMPROVE_TEXT + toPercentText(IMPROVE_INFO['ATTACK_P']))
            myUI.viewParameter_IMPROVE_DMG_P.setText(IMPROVE_TEXT + toPercentText(IMPROVE_INFO['DMG_P']))
            myUI.viewParameter_IMPROVE_BOSS_P.setText(IMPROVE_TEXT + toPercentText(IMPROVE_INFO['BOSS_P']))
            myUI.viewParameter_IMPROVE_STRIKE_P.setText(IMPROVE_TEXT + toPercentText(IMPROVE_INFO['STRIKE_P']))
            myUI.viewParameter_IMPROVE_IGNORE_P.setText(IMPROVE_TEXT + toPercentText(IMPROVE_INFO['IGNORE_P']))

            myUI.viewParameter_IMPROVE_Total.setText('總增幅 ' + toPercentText(IMPROVE_INFO['TOTAL']))

            # 預估值
            myUI.viewParameter_ESTIMATE_STR.setText(str(round(ESTIMATE_INFO['STR'])))
            myUI.viewParameter_ESTIMATE_STR_P.setText(str(round(ESTIMATE_INFO['STR_P']*100)))

            myUI.viewParameter_ESTIMATE_DEX.setText(str(round(ESTIMATE_INFO['DEX'])))
            myUI.viewParameter_ESTIMATE_DEX_P.setText(str(round(ESTIMATE_INFO['DEX_P']*100)))

            myUI.viewParameter_ESTIMATE_INT.setText(str(round(ESTIMATE_INFO['INT'])))
            myUI.viewParameter_ESTIMATE_INT_P.setText(str(round(ESTIMATE_INFO['INT_P']*100)))

            myUI.viewParameter_ESTIMATE_LUK.setText(str(round(ESTIMATE_INFO['LUK'])))
            myUI.viewParameter_ESTIMATE_LUK_P.setText(str(round(ESTIMATE_INFO['LUK_P']*100)))

            myUI.viewParameter_ESTIMATE_ATTACK.setText(str(round(ESTIMATE_INFO['ATTACK'])))
            myUI.viewParameter_ESTIMATE_ATTACK_P.setText(str(round(ESTIMATE_INFO['ATTACK_P']*100)))

            myUI.viewParameter_ESTIMATE_DMG_P.setText(str(round(ESTIMATE_INFO['DMG_P']*100)))
            myUI.viewParameter_ESTIMATE_BOSS_P.setText(str(round(ESTIMATE_INFO['BOSS_P']*100)))

            myUI.viewParameter_ESTIMATE_STRIKE_P.setText(str(round(ESTIMATE_INFO['STRIKE_P']*100,2)))
            myUI.viewParameter_ESTIMATE_IGNORE_P.setText(str(round(ESTIMATE_INFO['IGNORE_P']*100,2)))
        except Exception:
            QtWidgets.QMessageBox.warning(me, '提示', '輸入資料有誤')
            pass

    # event: 計算塔戒
    def calc_SeedRing(me):
        try:
            myCharactor = me.myCharactor
            myUI = me.myUI

            TIME_VALUE = myUI.viewSeedRing_TIME_VALUE.value()
            myUI.viewSeedRing_TIME_VALUE_TXT.setText(str(TIME_VALUE) + ' 秒')

            if (myCharactor.isReset): return False
            def getData():
                new_data = {
                    'DMG_P': 0 - (myUI.textToFloat(myUI.viewSeedRing_DMG_P.text()) / 100),
                    'ATTACK': 0 - myUI.textToFloat(myUI.viewSeedRing_ATTACK.text()),
                    'ATTACK_P': 0 - (myUI.textToFloat(myUI.viewSeedRing_ATTACK_P.text()) / 100),
                    'STRIKE_P': 0 - (myUI.textToFloat(myUI.viewSeedRing_STRIKE_P.text()) / 100),
                    'IGNORE_P': 0 - (myUI.textToFloat(myUI.viewSeedRing_IGNORE_P.text()) / 100),

                    'STR_CLEAR': 0 - myUI.textToFloat(myUI.viewSeedRing_STR.text()),
                    'STR_P': 0 - (myUI.textToFloat(myUI.viewSeedRing_STR_P.text()) / 100),

                    'DEX_CLEAR': 0 - myUI.textToFloat(myUI.viewSeedRing_DEX.text()),
                    'DEX_P': 0 - (myUI.textToFloat(myUI.viewSeedRing_DEX_P.text()) / 100),

                    'INT_CLEAR': 0 - myUI.textToFloat(myUI.viewSeedRing_INT.text()),
                    'INT_P': 0 - (myUI.textToFloat(myUI.viewSeedRing_INT_P.text()) / 100),

                    'LUK_CLEAR': 0 - myUI.textToFloat(myUI.viewSeedRing_LUK.text()),
                    'LUK_P': 0 - (myUI.textToFloat(myUI.viewSeedRing_LUK_P.text()) / 100),

                    'ALL_P': 0 - (myUI.textToFloat(myUI.viewSeedRing_ALL_P.text()) / 100)
                }   

                new_data['STR_CLEAR'] += 4
                new_data['DEX_CLEAR'] += 4
                new_data['INT_CLEAR'] += 4
                new_data['LUK_CLEAR'] += 4
                new_data['ATTACK'] += 4
                return new_data
            
            def toPercentText(value, maxtime = 1):
                t = TIME_VALUE > maxtime and maxtime or TIME_VALUE
                return str(round((value-1) * 100 * t, 2)) + '%'

            CLASS_INFO = myCharactor.getClassInfo(myCharactor.getData()['CLASS_NAME'])
            MAIN_AP = ''
            if(CLASS_INFO['STR'] == 'main'): MAIN_AP = 'STR_CLEAR'
            if(CLASS_INFO['DEX'] == 'main'): MAIN_AP = 'DEX_CLEAR'
            if(CLASS_INFO['INT'] == 'main'): MAIN_AP = 'INT_CLEAR'
            if(CLASS_INFO['LUK'] == 'main'): MAIN_AP = 'LUK_CLEAR'

            if (CLASS_INFO['CLASS_NAME'] == '傑諾'):
                data = myCharactor.getData()
                if(data['STR'] > data['DEX'] and data['STR'] > data['LUK']): MAIN_AP = 'STR_CLEAR'
                if(data['DEX'] > data['STR'] and data['DEX'] > data['LUK']): MAIN_AP = 'DEX_CLEAR'
                if(data['LUK'] > data['STR'] and data['LUK'] > data['DEX']): MAIN_AP = 'LUK_CLEAR'
                if(data['LUK'] == data['STR'] and data['LUK'] == data['DEX']): MAIN_AP = 'LUK_CLEAR'
                
            WEAPON_ATTACK = myUI.textToFloat(myUI.viewSeedRing_WP_ATTACK.text())
            
            # STR
            new_data = getData()
            new_data['STR_CLEAR'] += WEAPON_ATTACK * 1
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_WEAPON_STR_LV1.setText(toPercentText(IMPROVE_INFO['TOTAL'], 9))
            myUI.viewSeedRing_WEAPON_STR_LV1.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))
            
            new_data = getData()
            new_data['STR_CLEAR'] += WEAPON_ATTACK * 2
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_WEAPON_STR_LV2.setText(toPercentText(IMPROVE_INFO['TOTAL'], 11))
            myUI.viewSeedRing_WEAPON_STR_LV2.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))
            
            new_data = getData()
            new_data['STR_CLEAR'] += WEAPON_ATTACK * 3
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_WEAPON_STR_LV3.setText(toPercentText(IMPROVE_INFO['TOTAL'], 13))
            myUI.viewSeedRing_WEAPON_STR_LV3.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))
            
            new_data = getData()
            new_data['STR_CLEAR'] += WEAPON_ATTACK * 4
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_WEAPON_STR_LV4.setText(toPercentText(IMPROVE_INFO['TOTAL'], 15))
            myUI.viewSeedRing_WEAPON_STR_LV4.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))

            # DEX
            new_data = getData()
            new_data['DEX_CLEAR'] += WEAPON_ATTACK * 1
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_WEAPON_DEX_LV1.setText(toPercentText(IMPROVE_INFO['TOTAL'], 9))
            myUI.viewSeedRing_WEAPON_DEX_LV1.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))
            
            new_data = getData()
            new_data['DEX_CLEAR'] += WEAPON_ATTACK * 2
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_WEAPON_DEX_LV2.setText(toPercentText(IMPROVE_INFO['TOTAL'], 11))
            myUI.viewSeedRing_WEAPON_DEX_LV2.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))
            
            new_data = getData()
            new_data['DEX_CLEAR'] += WEAPON_ATTACK * 3
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_WEAPON_DEX_LV3.setText(toPercentText(IMPROVE_INFO['TOTAL'], 13))
            myUI.viewSeedRing_WEAPON_DEX_LV3.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))
            
            new_data = getData()
            new_data['DEX_CLEAR'] += WEAPON_ATTACK * 4
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_WEAPON_DEX_LV4.setText(toPercentText(IMPROVE_INFO['TOTAL'], 15))
            myUI.viewSeedRing_WEAPON_DEX_LV4.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))

            # INT
            new_data = getData()
            new_data['INT_CLEAR'] += WEAPON_ATTACK * 1
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_WEAPON_INT_LV1.setText(toPercentText(IMPROVE_INFO['TOTAL'], 9))
            myUI.viewSeedRing_WEAPON_INT_LV1.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))
            
            new_data = getData()
            new_data['INT_CLEAR'] += WEAPON_ATTACK * 2
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_WEAPON_INT_LV2.setText(toPercentText(IMPROVE_INFO['TOTAL'], 11))
            myUI.viewSeedRing_WEAPON_INT_LV2.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))
            
            new_data = getData()
            new_data['INT_CLEAR'] += WEAPON_ATTACK * 3
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_WEAPON_INT_LV3.setText(toPercentText(IMPROVE_INFO['TOTAL'], 13))
            myUI.viewSeedRing_WEAPON_INT_LV3.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))
            
            new_data = getData()
            new_data['INT_CLEAR'] += WEAPON_ATTACK * 4
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_WEAPON_INT_LV4.setText(toPercentText(IMPROVE_INFO['TOTAL'], 15))
            myUI.viewSeedRing_WEAPON_INT_LV4.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))

            # LUK
            new_data = getData()
            new_data['LUK_CLEAR'] += WEAPON_ATTACK * 1
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_WEAPON_LUK_LV1.setText(toPercentText(IMPROVE_INFO['TOTAL'], 9))
            myUI.viewSeedRing_WEAPON_LUK_LV1.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))
            
            new_data = getData()
            new_data['LUK_CLEAR'] += WEAPON_ATTACK * 2
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_WEAPON_LUK_LV2.setText(toPercentText(IMPROVE_INFO['TOTAL'], 11))
            myUI.viewSeedRing_WEAPON_LUK_LV2.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))
            
            new_data = getData()
            new_data['LUK_CLEAR'] += WEAPON_ATTACK * 3
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_WEAPON_LUK_LV3.setText(toPercentText(IMPROVE_INFO['TOTAL'], 13))
            myUI.viewSeedRing_WEAPON_LUK_LV3.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))
            
            new_data = getData()
            new_data['LUK_CLEAR'] += WEAPON_ATTACK * 4
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_WEAPON_LUK_LV4.setText(toPercentText(IMPROVE_INFO['TOTAL'], 15))
            myUI.viewSeedRing_WEAPON_LUK_LV4.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))

            # TOTALING
            TOTALLING_AP = (myCharactor.getData()['STR'] + myCharactor.getData()['DEX'] + myCharactor.getData()['INT'] + myCharactor.getData()['LUK']) * 0.01
            
            new_data = getData()
            new_data[MAIN_AP] += TOTALLING_AP * 1
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_TOTALLING_LV1.setText(toPercentText(IMPROVE_INFO['TOTAL'], 9))
            myUI.viewSeedRing_TOTALLING_LV1.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))

            new_data = getData()
            new_data[MAIN_AP] += TOTALLING_AP * 1
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_TOTALLING_LV2.setText(toPercentText(IMPROVE_INFO['TOTAL'], 11))
            myUI.viewSeedRing_TOTALLING_LV2.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))

            new_data = getData()
            new_data[MAIN_AP] += TOTALLING_AP * 2
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_TOTALLING_LV3.setText(toPercentText(IMPROVE_INFO['TOTAL'], 13))
            myUI.viewSeedRing_TOTALLING_LV3.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))

            new_data = getData()
            new_data[MAIN_AP] += TOTALLING_AP * 2
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_TOTALLING_LV4.setText(toPercentText(IMPROVE_INFO['TOTAL'], 15))
            myUI.viewSeedRing_TOTALLING_LV4.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))
            
            # RISTTAKER
            new_data = getData()
            new_data['ATTACK_P'] += 0.2
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_RISTTAKER_LV1.setText(toPercentText(IMPROVE_INFO['TOTAL'], 12))
            myUI.viewSeedRing_RISTTAKER_LV1.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))

            new_data = getData()
            new_data['ATTACK_P'] += 0.3
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_RISTTAKER_LV2.setText(toPercentText(IMPROVE_INFO['TOTAL'], 18))
            myUI.viewSeedRing_RISTTAKER_LV2.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))

            new_data = getData()
            new_data['ATTACK_P'] += 0.4
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_RISTTAKER_LV3.setText(toPercentText(IMPROVE_INFO['TOTAL'], 24))
            myUI.viewSeedRing_RISTTAKER_LV3.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))

            new_data = getData()
            new_data['ATTACK_P'] += 0.5
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_RISTTAKER_LV4.setText(toPercentText(IMPROVE_INFO['TOTAL'], 30))
            myUI.viewSeedRing_RISTTAKER_LV4.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))

            # RESTRAINT
            new_data = getData()
            new_data['ATTACK_P'] += 0.25
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_RESTRAINT_LV1.setText(toPercentText(IMPROVE_INFO['TOTAL'], 9))
            myUI.viewSeedRing_RESTRAINT_LV1.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))

            new_data = getData()
            new_data['ATTACK_P'] += 0.50
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_RESTRAINT_LV2.setText(toPercentText(IMPROVE_INFO['TOTAL'], 11))
            myUI.viewSeedRing_RESTRAINT_LV2.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))

            new_data = getData()
            new_data['ATTACK_P'] += 0.75
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_RESTRAINT_LV3.setText(toPercentText(IMPROVE_INFO['TOTAL'], 13))
            myUI.viewSeedRing_RESTRAINT_LV3.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))

            new_data = getData()
            new_data['ATTACK_P'] += 1.00
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_RESTRAINT_LV4.setText(toPercentText(IMPROVE_INFO['TOTAL'], 15))
            myUI.viewSeedRing_RESTRAINT_LV4.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))

            # STRIKE
            new_data = getData()
            new_data['STRIKE_P'] += myCharactor.getData()['STRIKE_P'] * 0.07
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_STRIKE_LV1.setText(toPercentText(IMPROVE_INFO['TOTAL'], 9))
            myUI.viewSeedRing_STRIKE_LV1.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))

            new_data = getData()
            new_data['STRIKE_P'] += myCharactor.getData()['STRIKE_P'] * 0.14
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_STRIKE_LV2.setText(toPercentText(IMPROVE_INFO['TOTAL'], 11))
            myUI.viewSeedRing_STRIKE_LV2.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))

            new_data = getData()
            new_data['STRIKE_P'] += myCharactor.getData()['STRIKE_P'] * 0.21
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_STRIKE_LV3.setText(toPercentText(IMPROVE_INFO['TOTAL'], 13))
            myUI.viewSeedRing_STRIKE_LV3.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))

            new_data = getData()
            new_data['STRIKE_P'] += myCharactor.getData()['STRIKE_P'] * 0.28
            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            myUI.viewSeedRing_STRIKE_LV4.setText(toPercentText(IMPROVE_INFO['TOTAL'], 15))
            myUI.viewSeedRing_STRIKE_LV4.setStyleSheet(myUI.getColor(IMPROVE_INFO['TOTAL']))
            
        except Exception:
            QtWidgets.QMessageBox.warning(me, '提示', '輸入資料有誤')
            pass
    
    # function: 計算裝備更換
    def calc_Equipment(me):
        try:
            myCharactor = me.myCharactor
            myUI = me.myUI

            if (myCharactor.isReset): return False
            def getData():
                new_data = {
                    'DMG_P': 0 - (myUI.textToFloat(myUI.viewEquipment_origin_DMG_P.text()) / 100),
                    'ATTACK': 0 - myUI.textToFloat(myUI.viewEquipment_origin_ATTACK.text()),
                    'ATTACK_P': 0 - (myUI.textToFloat(myUI.viewEquipment_origin_ATTACK_P.text()) / 100),
                    'STRIKE_P': 0 - (myUI.textToFloat(myUI.viewEquipment_origin_STRIKE_P.text()) / 100),
                    'IGNORE_P': 0 - (myUI.textToFloat(myUI.viewEquipment_origin_IGNORE_P.text()) / 100),

                    'STR_CLEAR': 0 - myUI.textToFloat(myUI.viewEquipment_origin_STR.text()),
                    'STR_P': 0 - (myUI.textToFloat(myUI.viewEquipment_origin_STR_P.text()) / 100),

                    'DEX_CLEAR': 0 - myUI.textToFloat(myUI.viewEquipment_origin_DEX.text()),
                    'DEX_P': 0 - (myUI.textToFloat(myUI.viewEquipment_origin_DEX_P.text()) / 100),

                    'INT_CLEAR': 0 - myUI.textToFloat(myUI.viewEquipment_origin_INT.text()),
                    'INT_P': 0 - (myUI.textToFloat(myUI.viewEquipment_origin_INT_P.text()) / 100),

                    'LUK_CLEAR': 0 - myUI.textToFloat(myUI.viewEquipment_origin_LUK.text()),
                    'LUK_P': 0 - (myUI.textToFloat(myUI.viewEquipment_origin_LUK_P.text()) / 100),

                    'ALL_P': 0 - (myUI.textToFloat(myUI.viewEquipment_origin_ALL_P.text()) / 100)
                }
                return new_data

            def toPercentText(value):
                return str(round((value-1) * 100, 2)) + '%'

            SET_INFO = getData()
            SET_INFO['DMG_P'] += (myUI.textToFloat(myUI.viewEquipment_Set1_DMG_P.text())/100)
            SET_INFO['ATTACK'] += myUI.textToFloat(myUI.viewEquipment_Set1_ATTACK.text())
            SET_INFO['ATTACK_P'] += (myUI.textToFloat(myUI.viewEquipment_Set1_ATTACK_P.text())/100)
            SET_INFO['STRIKE_P'] += (myUI.textToFloat(myUI.viewEquipment_Set1_STRIKE_P.text())/100)
            SET_INFO['STR_CLEAR'] += myUI.textToFloat(myUI.viewEquipment_Set1_STR.text())
            SET_INFO['STR_P'] += (myUI.textToFloat(myUI.viewEquipment_Set1_STR_P.text())/100)
            SET_INFO['DEX_CLEAR'] += myUI.textToFloat(myUI.viewEquipment_Set1_DEX.text())
            SET_INFO['DEX_P'] += (myUI.textToFloat(myUI.viewEquipment_Set1_DEX_P.text())/100)
            SET_INFO['INT_CLEAR'] += myUI.textToFloat(myUI.viewEquipment_Set1_INT.text())
            SET_INFO['INT_P'] += (myUI.textToFloat(myUI.viewEquipment_Set1_INT_P.text())/100)
            SET_INFO['LUK_CLEAR'] += myUI.textToFloat(myUI.viewEquipment_Set1_LUK.text())
            SET_INFO['LUK_P'] += (myUI.textToFloat(myUI.viewEquipment_Set1_LUK_P.text())/100)
            SET_INFO['ALL_P'] += (myUI.textToFloat(myUI.viewEquipment_Set1_ALL_P.text())/100)
            
            # 重算等效無視
            IGNORE_TO = myCharactor.calcIgnore(myCharactor.getData()['IGNORE_P'], SET_INFO['IGNORE_P'])
            IGNORE_TO = myCharactor.calcIgnore(IGNORE_TO, (myUI.textToFloat(myUI.viewEquipment_Set1_IGNORE_P.text())/100))
            SET_INFO['IGNORE_P'] = 0
            if (IGNORE_TO > myCharactor.getData()['IGNORE_P']):
                SET_INFO['IGNORE_P'] = 1 - ((1 - IGNORE_TO) / (1 - myCharactor.getData()['IGNORE_P']))
            if (IGNORE_TO < myCharactor.getData()['IGNORE_P']):
                SET_INFO['IGNORE_P'] = ((1 - myCharactor.getData()['IGNORE_P']) / (1 - IGNORE_TO)) - 1
            
            # 計算加總
            IMPROVE_INFO = myCharactor.calcImprove(SET_INFO)
            myUI.viewEquipment_Set1_IMPROVE.setText('增幅 ' + str(toPercentText(IMPROVE_INFO['TOTAL'])))

            SET_INFO = getData()
            SET_INFO['DMG_P'] += (myUI.textToFloat(myUI.viewEquipment_Set2_DMG_P.text())/100)
            SET_INFO['ATTACK'] += myUI.textToFloat(myUI.viewEquipment_Set2_ATTACK.text())
            SET_INFO['ATTACK_P'] += (myUI.textToFloat(myUI.viewEquipment_Set2_ATTACK_P.text())/100)
            SET_INFO['STRIKE_P'] += (myUI.textToFloat(myUI.viewEquipment_Set2_STRIKE_P.text())/100)
            SET_INFO['STR_CLEAR'] += myUI.textToFloat(myUI.viewEquipment_Set2_STR.text())
            SET_INFO['STR_P'] += (myUI.textToFloat(myUI.viewEquipment_Set2_STR_P.text())/100)
            SET_INFO['DEX_CLEAR'] += myUI.textToFloat(myUI.viewEquipment_Set2_DEX.text())
            SET_INFO['DEX_P'] += (myUI.textToFloat(myUI.viewEquipment_Set2_STR_P.text())/100)
            SET_INFO['INT_CLEAR'] += myUI.textToFloat(myUI.viewEquipment_Set2_INT.text())
            SET_INFO['INT_P'] += (myUI.textToFloat(myUI.viewEquipment_Set2_INT_P.text())/100)
            SET_INFO['LUK_CLEAR'] += myUI.textToFloat(myUI.viewEquipment_Set2_LUK.text())
            SET_INFO['LUK_P'] += (myUI.textToFloat(myUI.viewEquipment_Set2_LUK_P.text())/100)
            SET_INFO['ALL_P'] += (myUI.textToFloat(myUI.viewEquipment_Set2_ALL_P.text())/100)
            
            IGNORE_TO = myCharactor.calcIgnore(myCharactor.getData()['IGNORE_P'], SET_INFO['IGNORE_P'])
            IGNORE_TO = myCharactor.calcIgnore(IGNORE_TO, (myUI.textToFloat(myUI.viewEquipment_Set2_IGNORE_P.text())/100))
            SET_INFO['IGNORE_P'] = 0
            if (IGNORE_TO > myCharactor.getData()['IGNORE_P']):
                SET_INFO['IGNORE_P'] = 1 - ((1 - IGNORE_TO) / (1 - myCharactor.getData()['IGNORE_P']))
            if (IGNORE_TO < myCharactor.getData()['IGNORE_P']):
                SET_INFO['IGNORE_P'] = ((1 - myCharactor.getData()['IGNORE_P']) / (1 - IGNORE_TO)) - 1
            IMPROVE_INFO = myCharactor.calcImprove(SET_INFO)
            myUI.viewEquipment_Set2_IMPROVE.setText('增幅 ' + str(toPercentText(IMPROVE_INFO['TOTAL'])))


        except Exception:
            QtWidgets.QMessageBox.warning(me, '提示', '輸入資料有誤')
            pass

    # funtion: 計算等效無視
    def doCalcIgnore(me):
        try:
            myCharactor = me.myCharactor
            myUI = me.myUI

            IGNORE_BEFORE_TXT = myUI.viewTools_IGNORE_BEFORE.text()
            IGNORE_RANGE_TXT  = myUI.viewTools_IGNORE_RANGE.text()
            IGNORE_AFTER_TXT  = myUI.viewTools_IGNORE_AFTER.text()

            if (IGNORE_BEFORE_TXT == ''):
                QtWidgets.QMessageBox.warning(me, '提示', '請輸入原始無視')
                return False

            if (IGNORE_RANGE_TXT == '' and IGNORE_AFTER_TXT == ''):
                QtWidgets.QMessageBox.warning(me, '提示', '請輸入無視變量或結果無視')
                return False
            
            if (IGNORE_RANGE_TXT != ''):
                IGNORE_AFTER_TXT = ''

            if (IGNORE_RANGE_TXT != ''):
                IGNORE_AFTER_TXT = ''

            IGNORE_BEFORE = myUI.textToFloat(IGNORE_BEFORE_TXT) / 100
            IGNORE_RANGE  = myUI.textToFloat(IGNORE_RANGE_TXT) / 100
            IGNORE_AFTER  = myUI.textToFloat(IGNORE_AFTER_TXT) / 100

            if (IGNORE_BEFORE > 1 or IGNORE_RANGE > 1 or IGNORE_AFTER > 1):
                QtWidgets.QMessageBox.warning(me, '提示', '輸入資料有誤')
                return False

            if (IGNORE_AFTER_TXT == ''):
                IGNORE_AFTER = myCharactor.calcIgnore(IGNORE_BEFORE, IGNORE_RANGE)
                
                IGNORE_RANGE = round(IGNORE_RANGE * 100, 2)
                IGNORE_AFTER = round(IGNORE_AFTER * 100, 2)
                
                myUI.viewTools_IGNORE_RANGE.setText(str(IGNORE_RANGE))
                myUI.viewTools_IGNORE_AFTER.setText(str(IGNORE_AFTER))
                return True

            if (IGNORE_RANGE_TXT == ''):

                if (IGNORE_AFTER > IGNORE_BEFORE):
                    IGNORE_RANGE = 1 - (1 - IGNORE_AFTER) / (1 - IGNORE_BEFORE)
                if (IGNORE_AFTER < IGNORE_BEFORE):
                    IGNORE_RANGE = (1 - IGNORE_BEFORE) / (1 - IGNORE_AFTER) - 1

                IGNORE_RANGE = round(IGNORE_RANGE * 100, 2)
                IGNORE_AFTER = round(IGNORE_AFTER * 100, 2)

                myUI.viewTools_IGNORE_RANGE.setText(str(IGNORE_RANGE))
                myUI.viewTools_IGNORE_AFTER.setText(str(IGNORE_AFTER))
                return True
            
            



        except Exception:
            QtWidgets.QMessageBox.warning(me, '提示', '輸入資料有誤')
            pass
# ------------------ APP 入口 ------------------
app = QtWidgets.QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())

