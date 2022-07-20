import { CharacterStats } from '@/types/character'
import { Equipment, EquipmentStats } from '@/types/equipment'
import { calcMultiplier } from './calcEngine'

export class Build {
  id: string
  label: string
  baseStats: CharacterStats
  equipments: Equipment[]

  constructor(id: string, label: string, baseStats: CharacterStats, equipments: Equipment[] = []) {
    this.id = id
    this.label = label
    this.baseStats = baseStats
    this.equipments = equipments
  }

  private aggregateEquipStats(): EquipmentStats {
    return this.equipments.reduce<EquipmentStats>(
      (acc, eq) => ({
        mainStat: acc.mainStat + eq.stats.mainStat,
        mainStatPercent: acc.mainStatPercent + eq.stats.mainStatPercent,
        subStat: acc.subStat + eq.stats.subStat,
        subStatPercent: acc.subStatPercent + eq.stats.subStatPercent,
        attackPower: acc.attackPower + eq.stats.attackPower,
        attackPowerPercent: acc.attackPowerPercent + eq.stats.attackPowerPercent,
        damage: acc.damage + eq.stats.damage,
        bossDamage: acc.bossDamage + eq.stats.bossDamage,
        critDamage: acc.critDamage + eq.stats.critDamage,
        ignoreDefense: 1 - (1 - acc.ignoreDefense / 100) * (1 - eq.stats.ignoreDefense / 100)
      }),
      {
        mainStat: 0, mainStatPercent: 0,
        subStat: 0, subStatPercent: 0,
        attackPower: 0, attackPowerPercent: 0,
        damage: 0, bossDamage: 0,
        critDamage: 0, ignoreDefense: 0
      }
    )
  }

  getMultiplier(): number {
    return calcMultiplier(this.baseStats, this.aggregateEquipStats())
  }

  compareWith(other: Build): number {
    return this.getMultiplier() / other.getMultiplier()
  }
}
