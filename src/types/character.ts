export interface CharacterStats {
  level: number
  mainStat: number
  subStat: number
  attackPower: number
  bossDamage: number
  finalDamage: number
  damage: number
  critDamage: number
  ignoreDefense: number
  attackPercent: number
}

export interface NexonCharacterBasic {
  character_name: string
  world_name: string
  character_gender: string
  character_class: string
  character_level: number
  character_image: string
}
