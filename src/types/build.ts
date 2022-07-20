import { CharacterStats } from './character'
import { Equipment } from './equipment'

export interface Build {
  id: string
  label: string
  baseStats: CharacterStats
  equipments: Equipment[]
  multiplier?: number
}
