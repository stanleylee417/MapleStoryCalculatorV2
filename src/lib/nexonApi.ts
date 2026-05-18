import { NexonCharacterBasic } from '@/types/character'
import { NexonEquipmentResponse, NexonPetEquipmentResponse } from '@/types/equipment'
import { NexonCharacterStatResponse } from '@/types/stat'
import { NexonHyperStatResponse, NexonSymbolEquipmentResponse, NexonUnionRaiderResponse } from '@/types/extraStats'

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

export async function fetchCharacterStat(ocid: string): Promise<NexonCharacterStatResponse> {
  return window.api.nexon.getCharacterStat(ocid)
}

export async function fetchCharacterHyperStat(ocid: string): Promise<NexonHyperStatResponse> {
  return window.api.nexon.getCharacterHyperStat(ocid)
}

export async function fetchCharacterSymbolEquipment(ocid: string): Promise<NexonSymbolEquipmentResponse> {
  return window.api.nexon.getCharacterSymbolEquipment(ocid)
}

export async function fetchUnionRaider(ocid: string): Promise<NexonUnionRaiderResponse> {
  return window.api.nexon.getUnionRaider(ocid)
}
