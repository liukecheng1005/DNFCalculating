from PublicReference.base import *

class 极诣暗殿骑士主动技能(主动技能):
    def 等效CD(self, 武器类型):
        if 武器类型 == '太刀':
            return round(self.CD / self.恢复 * 1, 1)
        if 武器类型 == '短剑':
            return round(self.CD / self.恢复 * 1.05, 1)
        if 武器类型 == '钝器':
            return round(self.CD / self.恢复 * 1, 1)
        if 武器类型 == '巨剑':
            return round(self.CD / self.恢复 * 1, 1)

class 极诣暗殿骑士技能0(极诣暗殿骑士主动技能):
    名称 = '暗影之矛'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 2156.0889
    成长 = 243.911
    CD = 5.0
    TP成长 = 0.1
    TP上限 = 7


class 极诣暗殿骑士技能1(被动技能):
    名称 = '乌希尔的诅咒'
    所在等级 = 15
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        return round(1.10 + 0.02 * self.等级, 5)


class 极诣暗殿骑士技能2(极诣暗殿骑士主动技能):
    名称 = '暗影缠袭'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 2604.1667
    成长 = 293.8333
    CD = 7.0
    TP成长 = 0.08
    TP上限 = 7


class 极诣暗殿骑士技能3(极诣暗殿骑士主动技能):
    名称 = '暗影漩涡'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 2698.3571
    成长 = 304.6429
    CD = 6.0
    TP成长 = 0.1
    TP上限 = 7


class 极诣暗殿骑士技能4(被动技能):
    名称 = '汲魂之力'
    所在等级 = 25
    等级上限 = 30
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        return round(1.10 + 0.02 * self.等级, 5)


class 极诣暗殿骑士技能5(极诣暗殿骑士主动技能):
    名称 = '暗影禁锢'
    所在等级 = 25
    等级上限 = 70
    基础等级 = 41
    基础 = 5808.0833
    成长 = 655.9167
    CD = 12
    TP成长 = 0.1
    TP上限 = 7


class 极诣暗殿骑士技能6(极诣暗殿骑士主动技能):
    名称 = '灵魂摄取'
    所在等级 = 30
    等级上限 = 70
    基础等级 = 41
    基础 = 4501.7391
    成长 = 508.2609
    CD = 8
    TP成长 = 0.1
    TP上限 = 7


class 极诣暗殿骑士技能7(极诣暗殿骑士主动技能):
    名称 = '释魂飞弹'
    所在等级 = 30
    等级上限 = 70
    基础等级 = 26
    基础 = 2013.76 * 2
    成长 = 382.24 * 2
    CD = 8
    TP成长 = 0.14
    TP上限 = 3
    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            if self.TP等级 >= 1:
                return int(self.基础 + self.成长 * self.等级) * (0.72 + self.TP成长 * self.TP等级) * self.倍率
            else:
                return int(self.基础 + self.成长 * self.等级) * self.倍率
                        


class 极诣暗殿骑士技能8(极诣暗殿骑士主动技能):
    名称 = '魅影暗魂斩'
    所在等级 = 30
    等级上限 = 70
    基础等级 = 38
    基础 = 5546.054
    成长 = 625.9459
    CD = 11.0
    TP成长 = 0.1
    TP上限 = 7


class 极诣暗殿骑士技能9(极诣暗殿骑士主动技能):
    名称 = '魔镜幻影阵'
    所在等级 = 35
    等级上限 = 70
    基础等级 = 36
    基础 = 9239.657
    成长 = 1043.343
    CD = 15.0
    TP成长 = 0.1
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.基础 *= 1.21
        self.成长 *= 1.21


class 极诣暗殿骑士技能10(极诣暗殿骑士主动技能):
    名称 = '释魂狂怒'
    所在等级 = 35
    等级上限 = 70
    基础等级 = 36
    基础 = 13222.17
    成长 = 1492.892
    CD = 15
    TP成长 = 0.1
    TP上限 = 7


class 极诣暗殿骑士技能11(极诣暗殿骑士主动技能):
    名称 = '暗影囚杀'
    所在等级 = 40
    等级上限 = 70
    基础等级 = 33
    基础 = 281.125
    成长 = 31.875
    攻击次数 = 14
    基础2 = 8558.625
    成长2 = 966.375
    攻击次数2 = 1
    基础3 = 371.08500000000004
    成长3 = 42.075
    攻击次数3 = 0
    CD = 20
    是否有护石 = 1

    def 装备护石(self):
        self.攻击次数 = 5
        self.基础2 *= 1.52
        self.成长2 *= 1.52
        self.攻击次数3 = 4


class 极诣暗殿骑士技能12(极诣暗殿骑士主动技能):
    名称 = '暗影盛宴'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 1604.733
    成长 = 181.2667
    攻击次数 = 15
    基础2 = 5969.60676
    成长2 = 674.312124
    攻击次数2 = 0
    CD = 40
    TP成长 = 0.1
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.攻击次数2 = 1
        self.CD *= 0.84


class 极诣暗殿骑士技能13(被动技能):
    名称 = '灵魂傀儡'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        return round(1.055 + 0.015 * self.等级, 5)


class 极诣暗殿骑士技能14(极诣暗殿骑士主动技能):
    名称 = '末日杀戮'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 48299.2 * 1.1
    成长 = 14582 * 1.1
    CD = 145.0


class 极诣暗殿骑士技能15(极诣暗殿骑士主动技能):
    名称 = '魔影轰杀'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 19598.73
    成长 = 2213.273
    CD = 30.0
    TP成长 = 0.1
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.基础 *= 1.2275
        self.成长 *= 1.2275


class 极诣暗殿骑士技能16(极诣暗殿骑士主动技能):
    名称 = '死亡献祭'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 1491.647
    成长 = 168.353
    攻击次数 = 11
    基础2 = 17073.41
    成长2 = 1927.273
    攻击次数2 = 1
    CD = 50.0
    TP成长 = 0.1
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.基础2 *= 1.31
        self.成长2 *= 1.31


class 极诣暗殿骑士技能17(极诣暗殿骑士主动技能):
    名称 = '天罚死光'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 51946.77
    成长 = 5864.833
    CD = 40.0


class 极诣暗殿骑士技能18(被动技能):
    名称 = '薄暮'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    关联技能 = ['暗影之矛', '暗影缠袭', '灵魂摄取', '魅影暗魂斩', '暗影禁锢', '暗影漩涡', '魔镜幻影阵', '暗影囚杀', '末日杀戮', '魔影轰杀', '死亡献祭', '暗影盛宴', '天罚死光', '天罚之剑', '神罚·灭世裁决','暗影绽放：死亡荆棘','冥王降临：净土救赎']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        return round(1.24 + 0.02 * self.等级, 5)


class 极诣暗殿骑士技能19(极诣暗殿骑士主动技能):
    名称 = '天罚之剑'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 62301.98
    成长 = 7034.317
    CD = 45


class 极诣暗殿骑士技能20(极诣暗殿骑士主动技能):
    名称 = '神罚·灭世裁决'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 117009.2
    成长 = 35317.7
    CD = 180.0


class 极诣暗殿骑士技能21(被动技能):
    名称 = '以身载灵'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        return round(1.18 + 0.02 * self.等级, 5)


class 极诣暗殿骑士技能22(极诣暗殿骑士主动技能):
    名称 = '暗影绽放：死亡荆棘'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    基础 = 116112.2
    成长 = 13099.8
    CD = 60.0


class 极诣暗殿骑士技能23(极诣暗殿骑士主动技能):
    名称 = '冥王降临：净土救赎'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 305742
    成长 = 92298
    CD = 290.0
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        return 0.0


极诣暗殿骑士技能列表 = []
i = 0
while i >= 0:
    try:
        exec('极诣暗殿骑士技能列表.append(极诣暗殿骑士技能' + str(i) + '())')
        i += 1
    except:
        i = -1

极诣暗殿骑士技能序号 = dict()
for i in range(len(极诣暗殿骑士技能列表)):
    极诣暗殿骑士技能序号[极诣暗殿骑士技能列表[i].名称] = i

极诣暗殿骑士一觉序号 = 0
极诣暗殿骑士二觉序号 = 0
极诣暗殿骑士三觉序号 = 0
for i in 极诣暗殿骑士技能列表:
    if i.所在等级 == 50:
        极诣暗殿骑士一觉序号 = 极诣暗殿骑士技能序号[i.名称]
    if i.所在等级 == 85:
        极诣暗殿骑士二觉序号 = 极诣暗殿骑士技能序号[i.名称]
    if i.所在等级 == 100:
        极诣暗殿骑士三觉序号 = 极诣暗殿骑士技能序号[i.名称]

极诣暗殿骑士护石选项 = [
 '无']
for i in 极诣暗殿骑士技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        极诣暗殿骑士护石选项.append(i.名称)

极诣暗殿骑士符文选项 = [
 '无']
for i in 极诣暗殿骑士技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        极诣暗殿骑士符文选项.append(i.名称)

class 极诣暗殿骑士角色属性(角色属性):
    职业名称 = '极诣暗殿骑士'
    武器选项 = [
     '太刀', '短剑', '巨剑', '钝器']
    伤害类型选择 = [
     '魔法百分比']
    伤害类型 = '魔法百分比'
    防具类型 = '板甲'
    防具精通属性 = ['智力']
    主BUFF = 1.65
    基础力量 = 793.0
    基础智力 = 958.0
    力量 = 基础力量
    智力 = 基础智力
    物理攻击力 = 65.0
    魔法攻击力 = 65.0
    独立攻击力 = 1045.0
    火属性强化 = 13
    冰属性强化 = 13
    光属性强化 = 13
    暗属性强化 = 13
    远古记忆 = 0

    def __init__(self):
        self.技能栏 = deepcopy(极诣暗殿骑士技能列表)
        self.技能序号 = deepcopy(极诣暗殿骑士技能序号)

class 极诣暗殿骑士(角色窗口):

    def 窗口属性输入(self):
        self.初始属性 = 极诣暗殿骑士角色属性()
        self.角色属性A = 极诣暗殿骑士角色属性()
        self.角色属性B = 极诣暗殿骑士角色属性()
        self.一觉序号 = 极诣暗殿骑士一觉序号
        self.二觉序号 = 极诣暗殿骑士二觉序号
        self.三觉序号 = 极诣暗殿骑士三觉序号
        self.护石选项 = deepcopy(极诣暗殿骑士护石选项)
        self.符文选项 = deepcopy(极诣暗殿骑士符文选项)
