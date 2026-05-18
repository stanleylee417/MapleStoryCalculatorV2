export interface NexonHyperStatPresetItem {
  stat_type: string
  stat_point: number | null
  stat_level: number
  stat_increase: string
}

export interface NexonHyperStatResponse {
  date: string | null
  character_class: string
  use_preset_no: string
  use_available_hyper_stat: number
  hyper_stat_preset_1: NexonHyperStatPresetItem[]
  hyper_stat_preset_2: NexonHyperStatPresetItem[]
  hyper_stat_preset_3: NexonHyperStatPresetItem[]
  hyper_stat_preset_1_remain_point: number
  hyper_stat_preset_2_remain_point: number
  hyper_stat_preset_3_remain_point: number
}

export interface NexonSymbol {
  symbol_name: string
  symbol_icon: string
  symbol_description: string
  symbol_force: string
  symbol_level: number
  symbol_str: string
  symbol_dex: string
  symbol_int: string
  symbol_luk: string
  symbol_hp: string
  symbol_growth_count: number
  symbol_require_growth_count: number
}

export interface NexonSymbolEquipmentResponse {
  date: string | null
  character_class: string
  symbol: NexonSymbol[]
}

export interface NexonUnionRaiderResponse {
  date: string | null
  union_raider_stat: string[]
  union_occupied_stat: string[]
  union_inner_stat: { stat_field_id: string; stat_field_effect: string }[]
  union_block: {
    block_type: string
    block_class: string
    block_level: string
    block_control_point: { x: number; y: number }[]
    block_position: { x: number; y: number }[]
  }[]
}
