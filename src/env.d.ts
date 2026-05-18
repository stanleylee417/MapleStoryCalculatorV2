/// <reference types="vite/client" />

import { NexonCharacterBasic } from './types/character'
import { NexonEquipmentResponse, NexonEquipmentItem, NexonPetEquipmentResponse } from './types/equipment'
import { NexonCharacterStatResponse } from './types/stat'
import { NexonHyperStatResponse, NexonSymbolEquipmentResponse, NexonUnionRaiderResponse } from './types/extraStats'

interface Window {
  electron: import('@electron-toolkit/preload').ElectronAPI
  api: {
    defaultCharacterName: string
    nexon: {
      getCharacter: (characterName: string) => Promise<{ ocid: string }>
      getCharacterBasic: (ocid: string) => Promise<NexonCharacterBasic>
      getCharacterEquipment: (ocid: string) => Promise<NexonEquipmentResponse>
      getCharacterPetEquipment: (ocid: string) => Promise<NexonPetEquipmentResponse>
      getCharacterStat: (ocid: string) => Promise<NexonCharacterStatResponse>
      getCharacterHyperStat: (ocid: string) => Promise<NexonHyperStatResponse>
      getCharacterSymbolEquipment: (ocid: string) => Promise<NexonSymbolEquipmentResponse>
      getUnionRaider: (ocid: string) => Promise<NexonUnionRaiderResponse>
    }
    window: {
      minimize: () => void
      close: () => void
    }
    tooltip: {
      show: (item: NexonEquipmentItem, screenX: number, screenY: number) => void
      hide: () => void
      resize: (height: number) => void
      onData: (cb: (item: unknown) => void) => void
    }
  }
}
