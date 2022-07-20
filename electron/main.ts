import 'dotenv/config'
import { app, shell, BrowserWindow, ipcMain, session } from 'electron'
import { join } from 'path'
import { electronApp, optimizer, is } from '@electron-toolkit/utils'

function createWindow(): void {
  const mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    show: false,
    autoHideMenuBar: true,
    webPreferences: {
      preload: join(__dirname, '../preload/index.js'),
      sandbox: false
    }
  })

  mainWindow.on('ready-to-show', () => {
    mainWindow.show()
  })

  mainWindow.webContents.setWindowOpenHandler((details) => {
    shell.openExternal(details.url)
    return { action: 'deny' }
  })

  if (is.dev && process.env['ELECTRON_RENDERER_URL']) {
    mainWindow.loadURL(process.env['ELECTRON_RENDERER_URL'])
  } else {
    mainWindow.loadFile(join(__dirname, '../renderer/index.html'))
  }
}

app.whenReady().then(() => {
  electronApp.setAppUserModelId('com.maplestory.calculator')

  app.on('browser-window-created', (_, window) => {
    optimizer.watchWindowShortcuts(window)
  })

  // 攔截所有對 Nexon 的請求，自動加上 API key（讓 <img src> 也能正常載入圖片）
  session.defaultSession.webRequest.onBeforeSendHeaders(
    { urls: ['https://open.api.nexon.com/*'] },
    (details, callback) => {
      details.requestHeaders['x-nxopen-api-key'] = process.env['NEXON_API_KEY'] ?? ''
      callback({ requestHeaders: details.requestHeaders })
    }
  )

  // IPC handlers for Nexon API will be registered here
  const BASE_URL = 'https://open.api.nexon.com/maplestorytw/v1'

  async function nexonFetch(path: string): Promise<unknown> {
    const apiKey = process.env['NEXON_API_KEY'] ?? ''
    const url = `${BASE_URL}${path}`
    const res = await fetch(url, { headers: { 'x-nxopen-api-key': apiKey } })
    if (!res.ok) {
      const body = await res.text()
      throw new Error(`API error ${res.status}: ${body}`)
    }
    return res.json()
  }

  ipcMain.handle('nexon:getCharacter', async (_event, characterName: string) => {
    return nexonFetch(`/id?character_name=${encodeURIComponent(characterName)}`)
  })

  ipcMain.handle('nexon:getCharacterBasic', async (_event, ocid: string) => {
    return nexonFetch(`/character/basic?ocid=${encodeURIComponent(ocid)}`)
  })

  ipcMain.handle('nexon:getCharacterEquipment', async (_event, ocid: string) => {
    return nexonFetch(`/character/item-equipment?ocid=${encodeURIComponent(ocid)}`)
  })

  ipcMain.handle('nexon:getCharacterPetEquipment', async (_event, ocid: string) => {
    return nexonFetch(`/character/pet-equipment?ocid=${encodeURIComponent(ocid)}`)
  })

  createWindow()

  app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})
