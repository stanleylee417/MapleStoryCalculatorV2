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
      ipcRenderer.invoke('nexon:getCharacterPetEquipment', ocid),
    getCharacterStat: (ocid: string) =>
      ipcRenderer.invoke('nexon:getCharacterStat', ocid),
    getCharacterHyperStat: (ocid: string) =>
      ipcRenderer.invoke('nexon:getCharacterHyperStat', ocid),
    getCharacterSymbolEquipment: (ocid: string) =>
      ipcRenderer.invoke('nexon:getCharacterSymbolEquipment', ocid),
    getUnionRaider: (ocid: string) =>
      ipcRenderer.invoke('nexon:getUnionRaider', ocid),
  },
  window: {
    minimize: () => ipcRenderer.send('window:minimize'),
    close: () => ipcRenderer.send('window:close'),
  },
  tooltip: {
    show: (item: unknown, screenX: number, screenY: number) =>
      ipcRenderer.send('tooltip:show', item, screenX, screenY),
    hide: () =>
      ipcRenderer.send('tooltip:hide'),
    resize: (height: number) =>
      ipcRenderer.send('tooltip:resize', height),
    onData: (cb: (item: unknown) => void) =>
      ipcRenderer.on('tooltip:data', (_, item) => cb(item)),
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
