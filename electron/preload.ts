import { contextBridge, ipcRenderer } from 'electron'
import { electronAPI } from '@electron-toolkit/preload'

const api = {
  defaultCharacterName: process.env['DEFAULT_CHARACTER_NAME'] ?? '',
  nexon: {
    getCharacter: (characterName: string) =>
      ipcRenderer.invoke('nexon:getCharacter', characterName),
    getCharacterBasic: (ocid: string) =>
      ipcRenderer.invoke('nexon:getCharacterBasic', ocid),
    getCharacterEquipment: (ocid: string) =>
      ipcRenderer.invoke('nexon:getCharacterEquipment', ocid),
    getCharacterPetEquipment: (ocid: string) =>
      ipcRenderer.invoke('nexon:getCharacterPetEquipment', ocid)
  }
}

if (process.contextIsolated) {
  try {
    contextBridge.exposeInMainWorld('electron', electronAPI)
    contextBridge.exposeInMainWorld('api', api)
  } catch (error) {
    console.error(error)
  }
} else {
  window.electron = electronAPI
  window.api = api
}
