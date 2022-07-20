export interface EquipmentStats {
  mainStat: number
  mainStatPercent: number
  subStat: number
  subStatPercent: number
  attackPower: number
  attackPowerPercent: number
  damage: number
  bossDamage: number
  critDamage: number
  ignoreDefense: number
}

export interface Equipment {
  id: string
  name: string
  slot: string
  icon: string
  stats: EquipmentStats
}

export interface NexonEquipmentItem {
  item_equipment_slot: string
  item_equipment_part: string
  item_name: string
  item_icon: string
  starforce: string
  scroll_upgrade: string
  potential_option_grade: string
  potential_option_1: string
  potential_option_2: string
  potential_option_3: string
  additional_potential_option_grade: string
  additional_potential_option_1: string
  additional_potential_option_2: string
  additional_potential_option_3: string
  item_total_option: NexonItemOption
  item_base_option: NexonItemOption
  item_add_option: NexonItemOption
  item_starforce_option: NexonItemOption
  item_scroll_option: NexonItemOption
  item_exceptional_option: NexonItemOption
}

export interface NexonItemOption {
  str: string
  dex: string
  int: string
  luk: string
  max_hp: string
  max_mp: string
  attack_power: string
  magic_power: string
  armor: string
  speed: string
  jump: string
  boss_damage: string
  ignore_monster_armor: string
  all_stat: string
  damage: string
  equipment_level_decrease: number
  max_hp_rate: string
  max_mp_rate: string
}

export interface NexonPetEquipmentItem {
  item_name: string | null
  item_icon: string | null
}

export interface NexonPetEquipmentResponse {
  pet_1_name: string | null
  pet_1_nickname: string | null
  pet_1_icon: string | null
  pet_1_equipment: NexonPetEquipmentItem | null
  pet_2_name: string | null
  pet_2_nickname: string | null
  pet_2_icon: string | null
  pet_2_equipment: NexonPetEquipmentItem | null
  pet_3_name: string | null
  pet_3_nickname: string | null
  pet_3_icon: string | null
  pet_3_equipment: NexonPetEquipmentItem | null
}

export interface NexonEquipmentResponse {
  character_gender: string
  character_class: string
  preset_no: number
  item_equipment: NexonEquipmentItem[]
  item_equipment_preset_1: NexonEquipmentItem[]
  item_equipment_preset_2: NexonEquipmentItem[]
  item_equipment_preset_3: NexonEquipmentItem[]
}
