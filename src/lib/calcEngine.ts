import { CharacterStats } from '@/types/character'
import { EquipmentStats } from '@/types/equipment'

export function calcMultiplier(base: CharacterStats, equip: EquipmentStats): number {
  const mainStat = base.mainStat + equip.mainStat
  const subStat = base.subStat + equip.subStat
  const attackPower = base.attackPower + equip.attackPower

  const mainStatTotal = mainStat * (1 + (base.mainStat + equip.mainStatPercent) / 100)
  const subStatTotal = subStat * (1 + equip.subStatPercent / 100)
  const effectiveStat = 4 * mainStatTotal + subStatTotal

  const attackTotal = attackPower * (1 + (base.attackPercent + equip.attackPowerPercent) / 100)
  const damageTotal = 1 + (base.damage + base.bossDamage + equip.damage + equip.bossDamage) / 100
  const finalDamageTotal = 1 + (base.finalDamage) / 100
  const critDamageTotal = 1.2 + (base.critDamage + equip.critDamage) / 100
  const ignoreTotal = 1 - (1 - base.ignoreDefense / 100) * (1 - equip.ignoreDefense / 100)

  return effectiveStat * attackTotal * damageTotal * finalDamageTotal * critDamageTotal * (1 - 0.3 * (1 - ignoreTotal))
}
