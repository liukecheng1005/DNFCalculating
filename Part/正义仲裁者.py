from PublicReference.base import *

class 正义仲裁者主动技能(主动技能):
    def 等效CD(self, 武器类型):
        if 武器类型 == '图腾':
            return round(self.CD / self.恢复 * 0.9, 1)
        if 武器类型 == '镰刀':
            return round(self.CD / self.恢复 * 0.95, 1)
        if 武器类型 == '战斧':
            return round(self.CD / self.恢复 * 1.1, 1)
        if 武器类型 == '十字架':
            return round(self.CD / self.恢复 * 1.0, 1)
        if 武器类型 == '念珠':
            return round(self.CD / self.恢复 * 0.95, 1)

class 正义仲裁者技能0(正义仲裁者主动技能):
    名称 = '直拳冲击'
    所在等级 = 5
    等级上限 = 60
    基础等级 = 50
    基础 = 432.9387
    成长 = 49.0612
    基础2 = 651.4489
    成长2 = 73.5510
    攻击次数2 = 1
    CD = 3.0
    TP成长 = 0.08
    TP上限 = 7

class 正义仲裁者技能1(被动技能):
    名称 = '意念驱动'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    是否主动 = 1
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.013 + 0.02 * self.等级, 5)

class 正义仲裁者技能2(被动技能):
    名称 = '技巧精通'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 10:
            return round(1.00 + 0.01 * self.等级, 5)
        else:
            return round(1.10 + 0.015 * (self.等级 - 10), 5)

class 正义仲裁者技能3(正义仲裁者主动技能):
    名称 = '圣拳锤击'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 43
    基础 = 213.8095
    成长 = 24.1904
    基础2 = 1927.3095
    成长2 = 217.6904
    攻击次数2 = 1
    CD = 5.0
    TP成长 = 0.1
    TP上限 = 7

class 正义仲裁者技能4(正义仲裁者主动技能):
    名称 = '俯冲翔拳'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 46
    基础 = 1501.3778 * 1.1
    成长 = 169.2222 * 1.1
    CD = 3.5
    TP成长 = 0.10
    TP上限 = 7

class 正义仲裁者技能5(正义仲裁者主动技能):
    名称 = '俯冲直拳'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 46
    基础 = 1492.4667 * 1.1
    成长 = 168.5333 * 1.1
    CD = 3.5
    TP成长 = 0.10
    TP上限 = 7

class 正义仲裁者技能6(正义仲裁者主动技能):
    名称 = '俯冲腹拳'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 1630.0238 * 1.1
    成长 = 183.9761 * 1.1
    CD = 3.5
    TP成长 = 0.10
    TP上限 = 7

class 正义仲裁者技能7(正义仲裁者主动技能):
    名称 = '瞬拳'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 1667.6
    成长 = 188.4
    基础2 = 416.925
    成长2 = 47.075
    攻击次数2 = 1
    CD = 4
    TP成长 = 0.10
    TP上限 = 7


class 正义仲裁者技能8(正义仲裁者主动技能):
    名称 = '圣拳连击'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 832.85
    成长 = 94.15
    基础2 = 1018.95
    成长2 = 115.05
    攻击次数2 = 1
    基础3 = 1235.55
    成长3 = 139.45
    攻击次数3 = 1
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 7


class 正义仲裁者技能9(正义仲裁者主动技能):
    名称 = '神圣反击'
    所在等级 = 30
    等级上限 = 11
    基础等级 = 1
    基础 = 0
    成长 = 303
    CD = 6

class 正义仲裁者技能10(正义仲裁者主动技能):
    名称 = '破碎之锤'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 2094.4864
    成长 = 236.5135
    基础2 = 1396.3243
    成长2 = 157.6756
    攻击次数2 = 1
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 7


class 正义仲裁者技能11(正义仲裁者主动技能):
    名称 = '漩涡重拳'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 3764.2857
    成长 = 425.7142
    基础2 = 5655.5428
    成长2 = 638.4571
    攻击次数2 = 1
    CD = 20
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.基础 *= 1.4
        self.成长 *= 1.4
        self.基础2 *= 1.2
        self.成长2 *= 1.2

class 正义仲裁者技能12(正义仲裁者主动技能):
    名称 = '刺拳猛击'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 384.5142
    成长 = 43.48571
    攻击次数 = 10
    基础2 = 1149.1714
    成长2 = 129.8285
    攻击次数2 = 1
    基础3 = 746.6
    成长3 = 84.4
    攻击次数3 = 1
    CD = 10
    TP成长 = 0
    TP上限 = 7

class 正义仲裁者技能13(正义仲裁者主动技能):
    名称 = '神圣组合拳'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 2068.5
    成长 = 233.5
    基础2 = 2697.4062
    成长2 = 304.5937
    攻击次数2 = 1
    基础3 = 4226.8125
    成长3 = 477.1874
    攻击次数3 = 1
    CD = 16
    TP成长 = 0.1
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.基础 *= 1.17
        self.成长 *= 1.17
        self.基础2 *= 1.17
        self.成长2 *= 1.17
        self.基础3 *= 1.17
        self.成长3 *= 1.17

class 正义仲裁者技能14(正义仲裁者主动技能):
    名称 = '极速飓风拳'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 1389.1
    成长 = 156.9
    攻击次数 = 10
    基础2 = 5954.6333
    成长2 = 672.3666
    攻击次数2 = 1
    CD = 45
    TP成长 = 0.1
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.基础 *= 0.97
        self.成长 *= 0.97
        self.攻击次数 = 6
        self.攻击次数2 = 0
        self.CD = 15
        self.基础释放次数 = 2

class 正义仲裁者技能15(被动技能):
    名称 = '干涸之泉'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)

class 正义仲裁者技能16(正义仲裁者主动技能):
    名称 = '泯灭神击'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 40394 * 1.1
    成长 = 12198 * 1.1
    CD = 145.0

class 正义仲裁者技能17(正义仲裁者主动技能):
    名称 = '破碎之拳'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 12525.9091
    成长 = 1414.0909
    基础2 = 3131.3636
    成长2 = 353.6363
    攻击次数2 = 1
    基础3 = 5218.6363
    成长3 = 589.3636
    攻击次数3 = 1
    CD = 35.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    def 装备护石(self):
        self.基础 *= 1.3
        self.成长 *= 1.3
        self.基础3 *= 1.28
        self.基础3 *= 1.28

class 正义仲裁者技能18(正义仲裁者主动技能):
    名称 = '破坏之拳'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 25962.4705
    成长 = 2931.5294
    CD = 40.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    def 装备护石(self):
        self.基础 *= 1.2
        self.成长 *= 1.2

class 正义仲裁者技能19(正义仲裁者主动技能):
    名称 = '仲裁怒击'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 50485.8
    成长 = 5700.2
    CD = 40.0

class 正义仲裁者技能20(被动技能):
    名称 = '正义惩戒'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)

class 正义仲裁者技能21(正义仲裁者主动技能):
    名称 = '超重拳'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 56623.16667
    成长 = 6392.83333
    CD = 40.0

class 正义仲裁者技能22(正义仲裁者主动技能):
    名称 = '制裁：怒火疾风'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 100940
    成长 = 30458
    CD = 180.0

class 正义仲裁者技能23(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 正义仲裁者技能24(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
           return 1.0
        else:
           return round(1.045 + 0.005 * self.等级, 5)

class 正义仲裁者技能25(被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)


正义仲裁者技能列表 = []
i = 0
while i >= 0:
    try:
        exec('正义仲裁者技能列表.append(正义仲裁者技能'+str(i)+'())')
        i += 1
    except:
        i = -1

正义仲裁者技能序号 = dict()
for i in range(len(正义仲裁者技能列表)):
    正义仲裁者技能序号[正义仲裁者技能列表[i].名称] = i

正义仲裁者一觉序号 = 0
正义仲裁者二觉序号 = 0
正义仲裁者三觉序号 = 0
for i in 正义仲裁者技能列表:
    if i.所在等级 == 50:
        正义仲裁者一觉序号 = 正义仲裁者技能序号[i.名称]
    if i.所在等级 == 85:
        正义仲裁者二觉序号 = 正义仲裁者技能序号[i.名称]
    if i.所在等级 == 100:
        正义仲裁者三觉序号 = 正义仲裁者技能序号[i.名称]

正义仲裁者护石选项 = ['无']
for i in 正义仲裁者技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        正义仲裁者护石选项.append(i.名称)

正义仲裁者符文选项 = ['无']
for i in 正义仲裁者技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        正义仲裁者符文选项.append(i.名称)

class 正义仲裁者角色属性(角色属性):

    职业名称 = '正义仲裁者'

    武器选项 = ['图腾','战斧','镰刀','念珠','十字架']
    
    #'物理百分比','魔法百分比','物理固伤','魔法固伤'
    伤害类型选择 = ['物理百分比']
    
    #默认
    伤害类型 = '物理百分比'
    防具类型 = '轻甲'
    防具精通属性 = ['力量']

    主BUFF = 1.99

    #基础属性(含唤醒)
    基础力量 = 938.0
    基础智力 = 816.0
    
    #适用系统奶加成
    力量 = 基础力量
    智力 = 基础智力

    #人物基础 + 唤醒
    物理攻击力 = 65.0
    魔法攻击力 = 65.0
    独立攻击力 = 1045.0
    火属性强化 = 13
    冰属性强化 = 13
    光属性强化 = 13
    暗属性强化 = 13

    def __init__(self):
        self.技能栏= deepcopy(正义仲裁者技能列表)
        self.技能序号= deepcopy(正义仲裁者技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()
        #神圣反击倍率与腹拳一样，但在修炼场手动开只有80%
        self.技能栏[self.技能序号['神圣反击']].基础 = ((self.技能栏[self.技能序号['俯冲腹拳']].基础 * 1.1) + (self.技能栏[self.技能序号['俯冲腹拳']].等级 * self.技能栏[self.技能序号['俯冲腹拳']].成长 * 1.1) * (1 + self.技能栏[self.技能序号['俯冲腹拳']].TP等级 * 0.1)) * 0.8

        self.技能栏[self.技能序号['刺拳猛击']].攻击次数 += self.技能栏[self.技能序号['刺拳猛击']].TP等级 * 1
        self.技能栏[self.技能序号['刺拳猛击']].基础2 *= 1 + self.技能栏[self.技能序号['刺拳猛击']].TP等级 * 0.1
        self.技能栏[self.技能序号['刺拳猛击']].成长2 *= 1 + self.技能栏[self.技能序号['刺拳猛击']].TP等级 * 0.1
        self.技能栏[self.技能序号['刺拳猛击']].基础3 *= 1 + self.技能栏[self.技能序号['刺拳猛击']].TP等级 * 0.1
        self.技能栏[self.技能序号['刺拳猛击']].成长3 *= 1 + self.技能栏[self.技能序号['刺拳猛击']].TP等级 * 0.1

class 正义仲裁者(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 正义仲裁者角色属性()
        self.角色属性A = 正义仲裁者角色属性()
        self.角色属性B = 正义仲裁者角色属性()
        self.一觉序号 = 正义仲裁者一觉序号
        self.二觉序号 = 正义仲裁者二觉序号
        self.三觉序号 = 正义仲裁者三觉序号
        self.护石选项 = deepcopy(正义仲裁者护石选项)
        self.符文选项 = deepcopy(正义仲裁者符文选项)


