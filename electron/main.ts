import 'dotenv/config'
import { app, shell, BrowserWindow, ipcMain, session, screen } from 'electron'
import { join } from 'path'
import { electronApp, optimizer, is } from '@electron-toolkit/utils'

let tooltipWin: BrowserWindow | null = null

function getOrCreateTooltipWin(): BrowserWindow {
  if (tooltipWin && !tooltipWin.isDestroyed()) return tooltipWin
  tooltipWin = new BrowserWindow({
    width: 360,
    height: 700,
    frame: false,
    transparent: true,
    alwaysOnTop: true,
    skipTaskbar: true,
    focusable: false,
    webPreferences: {
      preload: join(__dirname, '../preload/index.js'),
      sandbox: false,
    }
  })
  tooltipWin.setIgnoreMouseEvents(true)
  tooltipWin.setOpacity(0)
  if (is.dev && process.env['ELECTRON_RENDERER_URL']) {
    tooltipWin.loadURL(process.env['ELECTRON_RENDERER_URL'] + '?mode=tooltip')
  } else {
    tooltipWin.loadFile(join(__dirname, '../renderer/index.html'), { query: { mode: 'tooltip' } })
  }
  return tooltipWin
}

function createWindow(): void {
  const mainWindow = new BrowserWindow({
    width: 560,
    height: 900,
    show: false,
    frame: false,
    transparent: true,
    backgroundColor: '#00000000',
    webPreferences: {
      preload: join(__dirname, '../preload/index.js'),
      sandbox: false
    }
  })

  mainWindow.on('ready-to-show', () => {
    mainWindow.show()
  })

  mainWindow.on('closed', () => {
    app.quit()
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

  async function nexonFetch(path: string, retries = 5, baseDelay = 1000): Promise<unknown> {
    const apiKey = process.env['NEXON_API_KEY'] ?? ''
    const url = `${BASE_URL}${path}`
    for (let attempt = 0; attempt <= retries; attempt++) {
      const res = await fetch(url, { headers: { 'x-nxopen-api-key': apiKey } })
      if (res.ok) return res.json()
      if (res.status === 429 && attempt < retries) {
        await new Promise(r => setTimeout(r, baseDelay * (attempt + 1)))
        continue
      }
      const body = await res.text()
      throw new Error(`API error ${res.status}: ${body}`)
    }
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

  ipcMain.handle('nexon:getCharacterStat', async (_event, ocid: string) => {
    return nexonFetch(`/character/stat?ocid=${encodeURIComponent(ocid)}`)
  })

  ipcMain.handle('nexon:getCharacterHyperStat', async (_event, ocid: string) => {
    return nexonFetch(`/character/hyper-stat?ocid=${encodeURIComponent(ocid)}`)
  })

  ipcMain.handle('nexon:getCharacterSymbolEquipment', async (_event, ocid: string) => {
    return nexonFetch(`/character/symbol-equipment?ocid=${encodeURIComponent(ocid)}`)
  })

  ipcMain.handle('nexon:getUnionRaider', async (_event, ocid: string) => {
    return nexonFetch(`/user/union-raider?ocid=${encodeURIComponent(ocid)}`)
  })

  ipcMain.on('window:minimize', (e) => BrowserWindow.fromWebContents(e.sender)?.minimize())
  ipcMain.on('window:close', (e) => BrowserWindow.fromWebContents(e.sender)?.close())

  ipcMain.on('tooltip:show', (_, item: unknown, screenX: number, screenY: number) => {
    const win = getOrCreateTooltipWin()
    const display = screen.getDisplayNearestPoint({ x: Math.round(screenX), y: Math.round(screenY) })
    const maxY = display.workArea.y + display.workArea.height - tooltipWin!.getBounds().height
    const clampedY = Math.min(Math.round(screenY), maxY)
    win.setPosition(Math.round(screenX) + 40, clampedY)
    win.webContents.send('tooltip:data', item)
    win.setOpacity(1)
    if (!win.isVisible()) win.showInactive()
  })

  ipcMain.on('tooltip:hide', () => {
    if (tooltipWin && !tooltipWin.isDestroyed()) tooltipWin.setOpacity(0)
  })

  ipcMain.on('tooltip:resize', (_, height: number) => {
    if (tooltipWin && !tooltipWin.isDestroyed()) {
      tooltipWin.setSize(360, Math.ceil(height))
    }
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
