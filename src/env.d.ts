/// <reference types="vite/client" />

import { NexonCharacterBasic } from './types/character'
import { NexonEquipmentResponse, NexonPetEquipmentResponse } from './types/equipment'

interface Window {
  electron: import('@electron-toolkit/preload').ElectronAPI
  api: {
    defaultCharacterName: string
    nexon: {
      getCharacter: (characterName: string) => Promise<{ ocid: string }>
      getCharacterBasic: (ocid: string) => Promise<NexonCharacterBasic>
      getCharacterEquipment: (ocid: string) => Promise<NexonEquipmentResponse>
      getCharacterPetEquipment: (ocid: string) => Promise<NexonPetEquipmentResponse>
    }
  }
}
