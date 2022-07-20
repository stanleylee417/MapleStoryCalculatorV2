import { NexonCharacterBasic } from '@/types/character'
import { NexonEquipmentResponse, NexonPetEquipmentResponse } from '@/types/equipment'

export async function fetchCharacterOcid(characterName: string): Promise<string> {
  const res = await window.api.nexon.getCharacter(characterName)
  return res.ocid
}

export async function fetchCharacterBasic(ocid: string): Promise<NexonCharacterBasic> {
  return window.api.nexon.getCharacterBasic(ocid)
}

export async function fetchCharacterEquipment(ocid: string): Promise<NexonEquipmentResponse> {
  return window.api.nexon.getCharacterEquipment(ocid)
}

export async function fetchCharacterPetEquipment(ocid: string): Promise<NexonPetEquipmentResponse> {
  return window.api.nexon.getCharacterPetEquipment(ocid)
}
