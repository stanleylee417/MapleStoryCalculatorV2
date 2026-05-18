export interface SlotDef {
  key: string
  label: string
  col: number
  row: number
  bg: string
  apiSlot: string
  apiItemNames?: string[]  // item_name 優先匹配，覆蓋 apiSlot
}

// Grid: 7 cols × (6 rows + separator row + 1 pet row)
// Character space occupies col 3-5, row 1-4 (explicit)
// All other slots are placed explicitly to match the HTML layout

export const SLOT_DEFS: SlotDef[] = [
  // Row 1
  { key: 'ring4',     label: 'RING',      col: 1, row: 1, bg: 'bg-ring',    apiSlot: '戒指4' },
  { key: 'face',      label: 'FORE HEAD', col: 2, row: 1, bg: 'bg-acc',     apiSlot: '臉飾' },
  { key: 'cap',       label: 'CAP',       col: 6, row: 1, bg: 'bg-normal',  apiSlot: '帽子' },
  { key: 'cape',      label: 'CAPE',      col: 7, row: 1, bg: 'bg-normal',  apiSlot: '披風' },

  // Row 2
  { key: 'ring3',     label: 'RING',      col: 1, row: 2, bg: 'bg-ring',    apiSlot: '戒指3' },
  { key: 'eyeacc',    label: 'EYE ACC',   col: 2, row: 2, bg: 'bg-acc',     apiSlot: '眼飾' },
  { key: 'top',       label: 'CLOTHES',   col: 6, row: 2, bg: 'bg-normal',  apiSlot: '上衣' },
  { key: 'gloves',    label: 'GLOVES',    col: 7, row: 2, bg: 'bg-normal',  apiSlot: '手套' },

  // Row 3
  { key: 'ring2',     label: 'RING',      col: 1, row: 3, bg: 'bg-ring',    apiSlot: '戒指2' },
  { key: 'earacc',    label: 'EAR ACC',   col: 2, row: 3, bg: 'bg-acc',     apiSlot: '耳環' },
  { key: 'bottom',    label: 'PANTS',     col: 6, row: 3, bg: 'bg-normal',  apiSlot: '褲/裙' },
  { key: 'shoes',     label: 'SHOES',     col: 7, row: 3, bg: 'bg-normal',  apiSlot: '鞋子' },

  // Row 4
  { key: 'ring1',     label: 'RING',      col: 1, row: 4, bg: 'bg-ring',    apiSlot: '戒指1' },
  { key: 'pendant2',  label: 'PENDANT',   col: 2, row: 4, bg: 'bg-acc',     apiSlot: '墜飾2' },
  { key: 'shoulder',  label: 'SHOULDER',  col: 6, row: 4, bg: 'bg-special', apiSlot: '肩膀裝飾' },
  { key: 'medal',     label: 'MEDAL',     col: 7, row: 4, bg: 'bg-special', apiSlot: '勳章' },

  // Row 5
  { key: 'belt',      label: 'BELT',      col: 1, row: 5, bg: 'bg-acc',     apiSlot: '腰帶' },
  { key: 'pendant1',  label: 'PENDANT',   col: 2, row: 5, bg: 'bg-acc',     apiSlot: '墜飾' },
  { key: 'weapon',    label: 'WEAPON',    col: 3, row: 5, bg: 'bg-acc',     apiSlot: '武器' },
  { key: 'subweapon', label: 'SUB WPN',   col: 4, row: 5, bg: 'bg-acc',     apiSlot: '輔助武器' },
  { key: 'emblem',    label: 'EMBLEM',    col: 5, row: 5, bg: 'bg-acc',     apiSlot: '徽章' },
  { key: 'android',   label: 'ANDROID',   col: 6, row: 5, bg: 'bg-normal',  apiSlot: '機器人' },
  { key: 'heart',     label: 'HEART',     col: 7, row: 5, bg: 'bg-normal',  apiSlot: '機器心臟' },

  // Row 6
  { key: 'pocket',    label: 'POCKET',    col: 1, row: 6, bg: 'bg-acc',     apiSlot: '口袋道具' },
  { key: 'jewel',     label: 'JEWEL',     col: 2, row: 6, bg: 'bg-valuable',apiSlot: '寶石', apiItemNames: ['伊妮絲的寶玉'] },
  { key: 'totem1',    label: 'TOTEM',     col: 3, row: 6, bg: 'bg-valuable',apiSlot: '馴服的怪物' },
  { key: 'totem2',    label: 'TOTEM',     col: 4, row: 6, bg: 'bg-valuable',apiSlot: '馬鞍' },
  { key: 'totem3',    label: 'TOTEM',     col: 5, row: 6, bg: 'bg-valuable',apiSlot: '怪物裝備' },
  { key: 'badge',     label: 'BADGE',     col: 7, row: 6, bg: 'bg-special', apiSlot: '胸章' },

  // Rows 8-10 (after separator at row 7) — pets vertical, col 3-7 reserved for stats
  { key: 'pet1',      label: 'PET',       col: 1, row: 8,  bg: 'bg-acc',     apiSlot: '寵物裝備1' },
  { key: 'petacc1',   label: 'PET ACC',   col: 2, row: 8,  bg: 'bg-valuable',apiSlot: '寵物裝備道具1' },
  { key: 'pet2',      label: 'PET',       col: 1, row: 9,  bg: 'bg-acc',     apiSlot: '寵物裝備2' },
  { key: 'petacc2',   label: 'PET ACC',   col: 2, row: 9,  bg: 'bg-valuable',apiSlot: '寵物裝備道具2' },
  { key: 'pet3',      label: 'PET',       col: 1, row: 10, bg: 'bg-acc',     apiSlot: '寵物裝備3' },
  { key: 'petacc3',   label: 'PET ACC',   col: 2, row: 10, bg: 'bg-valuable',apiSlot: '寵物裝備道具3' },
]
