import React, { useState } from 'react'
import { fetchCharacterOcid, fetchCharacterBasic, fetchCharacterEquipment, fetchCharacterPetEquipment, fetchCharacterStat, fetchCharacterHyperStat, fetchCharacterSymbolEquipment, fetchUnionRaider } from '@/lib/nexonApi'
import { NexonCharacterBasic } from '@/types/character'
import { NexonEquipmentItem, NexonPetEquipmentResponse } from '@/types/equipment'
import { NexonFinalStat } from '@/types/stat'
import { NexonHyperStatResponse, NexonSymbolEquipmentResponse, NexonUnionRaiderResponse } from '@/types/extraStats'
import { SLOT_DEFS, SlotDef } from './slotDefinitions'
type PresetKey = 1 | 2 | 3

export default function CharacterSetup() {
  const [characterName, setCharacterName] = useState(window.api.defaultCharacterName)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [characterBasic, setCharacterBasic] = useState<NexonCharacterBasic | null>(null)
  const [activePreset, setActivePreset] = useState<PresetKey>(1)
  const [presetMaps, setPresetMaps] = useState<Record<PresetKey, Record<string, NexonEquipmentItem>>>({
    1: {}, 2: {}, 3: {}
  })
  const [petEquipment, setPetEquipment] = useState<NexonPetEquipmentResponse | null>(null)
  const [finalStats, setFinalStats] = useState<NexonFinalStat[]>([])
  const [hyperStat, setHyperStat] = useState<NexonHyperStatResponse | null>(null)
  const [symbolEquipment, setSymbolEquipment] = useState<NexonSymbolEquipmentResponse | null>(null)
  const [unionRaider, setUnionRaider] = useState<NexonUnionRaiderResponse | null>(null)

  const equipmentMap = presetMaps[activePreset]

  async function handleSearch() {
    if (!characterName.trim()) return
    setLoading(true)
    setError(null)
    try {
      const ocid = await fetchCharacterOcid(characterName.trim())
      const basic  = await fetchCharacterBasic(ocid)
      const equip  = await fetchCharacterEquipment(ocid)
      const pet    = await fetchCharacterPetEquipment(ocid)
      const stat   = await fetchCharacterStat(ocid)
      const hyper  = await fetchCharacterHyperStat(ocid)
      const symbol = await fetchCharacterSymbolEquipment(ocid)
      const union  = await fetchUnionRaider(ocid)
      console.log(JSON.stringify({ final_stat: stat.final_stat, hyper, symbol, union }, null, 2))
      setCharacterBasic(basic)

      function itemsToMap(items: NexonEquipmentItem[]): Record<string, NexonEquipmentItem> {
        const map: Record<string, NexonEquipmentItem> = {}
        for (const item of items) {
          const slot =
            SLOT_DEFS.find(s => s.apiItemNames?.includes(item.item_name)) ??
            SLOT_DEFS.find(s => s.apiSlot === item.item_equipment_slot)
          if (slot) map[slot.key] = item
        }
        return map
      }

      // item_equipment 包含非 preset 的欄位（totem/jewel 等），preset 陣列覆蓋其上
      const baseMap = itemsToMap(equip.item_equipment)
      setPresetMaps({
        1: { ...baseMap, ...itemsToMap(equip.item_equipment_preset_1) },
        2: { ...baseMap, ...itemsToMap(equip.item_equipment_preset_2) },
        3: { ...baseMap, ...itemsToMap(equip.item_equipment_preset_3) },
      })
      setPetEquipment(pet)
      setFinalStats(stat.final_stat)
      setHyperStat(hyper)
      setSymbolEquipment(symbol)
      setUnionRaider(union)
    } catch (e) {
      setError(e instanceof Error ? e.message : '查詢失敗')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div style={{ position: 'relative' }}>
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(7, 1fr)',
        gridTemplateRows: 'repeat(6, auto) 20px repeat(3, auto)',
        gap: 5,
      }}>
        {/* Character space */}
        <CharacterSpace
          characterBasic={characterBasic}
          characterName={characterName}
          loading={loading}
          error={error}
          onChange={setCharacterName}
          onSearch={handleSearch}
        />

        {/* Equipment slots */}
        {SLOT_DEFS.map(slot => {
          const petMatch = slot.key.match(/^pet(\d)$/)
          const petAccMatch = slot.key.match(/^petacc(\d)$/)
          const petNum = petMatch?.[1] ?? petAccMatch?.[1]
          const petIcon = petNum
            ? petMatch
              ? (petEquipment?.[`pet_${petNum}_icon` as keyof NexonPetEquipmentResponse] as string | null ?? undefined)
              : ((petEquipment?.[`pet_${petNum}_equipment` as keyof NexonPetEquipmentResponse] as { item_icon: string | null } | null)?.item_icon ?? undefined)
            : undefined
          const petName = petNum
            ? petMatch
              ? (petEquipment?.[`pet_${petNum}_name` as keyof NexonPetEquipmentResponse] as string | null ?? undefined)
              : ((petEquipment?.[`pet_${petNum}_equipment` as keyof NexonPetEquipmentResponse] as { item_name: string | null } | null)?.item_name ?? undefined)
            : undefined
          return (
            <EquipmentSlot
              key={slot.key}
              slot={slot}
              item={equipmentMap[slot.key]}
              petIcon={petIcon ?? undefined}
              petName={petName ?? undefined}
              onHover={(item, x, y) => item
                ? window.api.tooltip.show(item, x, y)
                : window.api.tooltip.hide()
              }
            />
          )
        })}

        {/* Separator */}
        <div style={{ gridColumn: 'span 7', display: 'flex', alignItems: 'center', height: 20 }}>
          <div style={{ width: '100%', height: 2, background: '#d1d4d9', borderBottom: '1px solid #fff', opacity: 0.8, borderRadius: 1 }} />
        </div>

        {/* Stats panel — col 3-7, row 8-10 */}
        {finalStats.length > 0 && (
          <StatPanel
            finalStats={finalStats}
            characterBasic={characterBasic}
            equipmentMap={equipmentMap}
            hyperStat={hyperStat}
            symbolEquipment={symbolEquipment}
            unionRaider={unionRaider}
          />
        )}
      </div>

      {/* Preset + Apply row */}
      <div className="flex justify-between items-center mt-4">
        <div style={{
          background: '#5d6d7e',
          padding: '4px 16px',
          borderRadius: 99,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          border: '1px solid #4a5866',
          flexGrow: 1,
          maxWidth: 280,
          gap: 8,
        }}>
          <span style={{ fontSize: 10, fontWeight: 'bold', color: 'white', opacity: 0.9, textTransform: 'uppercase', letterSpacing: '0.05em' }}>
            Presets
          </span>
          <div className="flex gap-2">
            {([1, 2, 3] as PresetKey[]).map(n => (
              <button
                key={n}
                onClick={() => setActivePreset(n)}
                style={{
                  width: 22, height: 22, borderRadius: 4, fontSize: 11, fontWeight: 'bold',
                  display: 'flex', alignItems: 'center', justifyContent: 'center',
                  border: '1px solid #3b4854', boxShadow: '0 1px 2px rgba(0,0,0,0.2)',
                  cursor: 'pointer',
                  background: activePreset === n ? '#3b4854' : '#95a5a6',
                  color: '#fff',
                }}
              >
                {n}
              </button>
            ))}
          </div>
        </div>
        <button style={{
          fontSize: 11, fontWeight: 'bold', borderRadius: 99, padding: '5px 40px',
          background: 'linear-gradient(to bottom, #bdc3c7, #95a5a6)',
          color: '#5d6d7e', border: '1px solid #7f8c8d',
          boxShadow: 'inset 0 1px 1px rgba(255,255,255,0.5)',
          cursor: 'pointer',
        }}>
          套用
        </button>
      </div>
    </div>
  )
}

function CharacterSpace({ characterBasic, characterName, loading, error, onChange, onSearch }: {
  characterBasic: NexonCharacterBasic | null
  characterName: string
  loading: boolean
  error: string | null
  onChange: (v: string) => void
  onSearch: () => void
}) {
  return (
    <div style={{
      gridColumn: '3 / span 3',
      gridRow: '1 / span 4',
      background: 'white',
      border: '1px solid #d1d4d9',
      borderRadius: 4,
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'flex-end',
      paddingBottom: 12,
      position: 'relative',
      overflow: 'hidden',
    }}>
      {characterBasic ? (
        <>
          <img
            src={characterBasic.character_image}
            alt={characterBasic.character_name}
            style={{ position: 'absolute', top: 4, height: '60%', objectFit: 'contain' }}
          />
          <div style={{ textAlign: 'center', fontSize: 11, color: '#445361', fontWeight: 'bold', lineHeight: 1.3, zIndex: 1, marginBottom: 2 }}>
            {characterBasic.character_name}
          </div>
          <div style={{ textAlign: 'center', fontSize: 9, color: '#7f8c8d', zIndex: 1, marginBottom: 6 }}>
            Lv.{characterBasic.character_level} {characterBasic.character_class}
          </div>
        </>
      ) : (
        <div style={{ position: 'absolute', top: '30%', fontSize: 10, color: '#b2bec3' }}>
          {error ? <span style={{ color: '#e74c3c', fontSize: 9, padding: '0 8px', textAlign: 'center' }}>{error}</span> : '輸入角色名稱'}
        </div>
      )}

      {/* Search bar */}
      <div style={{
        width: '90%',
        height: 28,
        background: 'rgba(255,255,255,0.6)',
        borderRadius: 999,
        border: '1px solid #b2bec3',
        boxShadow: 'inset 0 1px 3px rgba(0,0,0,0.1)',
        display: 'flex',
        alignItems: 'center',
        position: 'relative',
        overflow: 'hidden',
      }}>
        <input
          value={characterName}
          onChange={e => onChange(e.target.value)}
          onKeyDown={e => e.key === 'Enter' && onSearch()}
          placeholder="角色名稱"
          style={{
            width: '100%',
            height: '100%',
            background: 'transparent',
            border: 'none',
            padding: '0 35px 0 15px',
            fontSize: 11,
            color: '#445361',
            outline: 'none',
            fontWeight: 500,
          }}
        />
        <button
          onClick={onSearch}
          disabled={loading}
          style={{
            position: 'absolute',
            right: 8,
            background: 'none',
            border: 'none',
            cursor: 'pointer',
            color: '#7f8c8d',
            display: 'flex',
            alignItems: 'center',
          }}
        >
          {loading ? (
            <span style={{ fontSize: 9 }}>...</span>
          ) : (
            <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
              <circle cx="11" cy="11" r="8" /><line x1="21" y1="21" x2="16.65" y2="16.65" />
            </svg>
          )}
        </button>
      </div>
    </div>
  )
}

function EquipmentSlot({ slot, item, petIcon, petName, onHover }: {
  slot: SlotDef
  item?: NexonEquipmentItem
  petIcon?: string
  petName?: string
  onHover: (item: NexonEquipmentItem | null, x: number, y: number) => void
}) {
  const displayIcon = item?.item_icon ?? petIcon
  const displayName = item?.item_name ?? petName

  return (
    <div
      className={`slot ${slot.bg}`}
      style={{ gridColumn: slot.col, gridRow: slot.row }}
      onMouseEnter={e => item && onHover(item, e.screenX, e.screenY)}
      onMouseMove={e => item && onHover(item, e.screenX, e.screenY)}
      onMouseLeave={() => onHover(null, 0, 0)}
    >
      {!displayIcon && <span className="slot-label">{slot.label}</span>}
      {displayIcon && (
        <div style={{ position: 'absolute', inset: 0, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <img src={displayIcon} alt={displayName} className="slot-icon" />
        </div>
      )}
    </div>
  )
}

function StatPanel({ finalStats, characterBasic, equipmentMap, hyperStat, symbolEquipment, unionRaider }: {
  finalStats: NexonFinalStat[]
  characterBasic: NexonCharacterBasic | null
  equipmentMap: Record<string, NexonEquipmentItem>
  hyperStat: NexonHyperStatResponse | null
  symbolEquipment: NexonSymbolEquipmentResponse | null
  unionRaider: NexonUnionRaiderResponse | null
}) {
  const get = (name: string) => {
    const v = finalStats.find(s => s.stat_name === name)?.stat_value ?? '—'
    return v === '—' ? '—' : v.replace(/\.00$/, '')
  }
  const pct = (name: string) => {
    const v = get(name)
    return v === '—' ? '—' : `${v}%`
  }

  const atk = Math.max(
    parseInt(get('攻擊力') || '0', 10),
    parseInt(get('魔法攻擊力') || '0', 10)
  )

  // 裝備 total option 加總
  const sumEquip = (key: 'str' | 'dex' | 'int' | 'luk') =>
    Object.values(equipmentMap).reduce((acc, item) =>
      acc + parseInt(item.item_total_option?.[key] ?? '0', 10), 0)

  // Hyper stat flat 加總（取 active preset）
  const hyperFlat = (statType: string): number => {
    if (!hyperStat) return 0
    const presetKey = `hyper_stat_preset_${hyperStat.use_preset_no}` as keyof NexonHyperStatResponse
    const preset = hyperStat[presetKey] as { stat_type: string; stat_increase: string }[] | undefined
    if (!preset) return 0
    const entry = preset.find(e => e.stat_type === statType)
    return parseInt(entry?.stat_increase ?? '0', 10) || 0
  }

  // Symbol flat 加總
  const symbolFlat = (key: 'symbol_str' | 'symbol_dex' | 'symbol_int' | 'symbol_luk'): number => {
    if (!symbolEquipment) return 0
    return symbolEquipment.symbol.reduce((acc, s) => acc + (parseInt(s[key] ?? '0', 10) || 0), 0)
  }

  // Union raider stat 加總（字串格式如 "STR 80 增加"）
  const unionFlat = (statName: string): number => {
    if (!unionRaider) return 0
    return unionRaider.union_raider_stat.reduce((acc, s) => {
      const m = s.match(new RegExp(`${statName}\\s+(\\d+)`))
      return acc + (m ? parseInt(m[1], 10) : 0)
    }, 0)
  }

  // 反推 stat% = (finalStat / totalKnownFlat - 1) × 100
  // totalKnownFlat = equipTotal + hyperFlat + symbolFlat + unionFlat
  // 注意：不含 AP base，反推結果為「已知來源以外的倍率貢獻」估算值
  const statBreakdown = (finalKey: string, equipKey: 'str' | 'dex' | 'int' | 'luk', hyperKey: string, symbolKey: 'symbol_str' | 'symbol_dex' | 'symbol_int' | 'symbol_luk', unionKey: string) => {
    const finalVal = parseInt(get(finalKey) || '0', 10)
    if (!finalVal) return get(finalKey)

    const eTotal = sumEquip(equipKey)
    const hFlat = hyperFlat(hyperKey)
    const sFlat = symbolFlat(symbolKey)
    const uFlat = unionFlat(unionKey)
    const knownFlat = eTotal + hFlat + sFlat + uFlat

    const parts: string[] = []
    if (eTotal) parts.push(`裝${eTotal}`)
    if (hFlat)  parts.push(`超${hFlat}`)
    if (sFlat)  parts.push(`符${sFlat}`)
    if (uFlat)  parts.push(`聯${uFlat}`)

    if (!knownFlat) return get(finalKey)

    const rawPct = (finalVal / knownFlat - 1) * 100
    const pctStr = rawPct > 0.1 ? ` ×${(1 + rawPct / 100).toFixed(3)}` : ''
    return `${get(finalKey)}  （${parts.join(' ')}${pctStr}）`
  }

  const fullRows: { label: string; value: string }[] = [
    { label: '攻擊力', value: atk.toLocaleString() },
    { label: 'STR', value: statBreakdown('STR', 'str', 'STR', 'symbol_str', 'STR') },
    { label: 'DEX', value: statBreakdown('DEX', 'dex', 'DEX', 'symbol_dex', 'DEX') },
    { label: 'INT', value: statBreakdown('INT', 'int', 'INT', 'symbol_int', 'INT') },
    { label: 'LUK', value: statBreakdown('LUK', 'luk', 'LUK', 'symbol_luk', 'LUK') },
  ]
  const pairRows: [{ label: string; value: string }, { label: string; value: string }][] = [
    [{ label: 'BOSS傷害', value: pct('BOSS怪物傷害') }, { label: '無視防禦', value: pct('無視防禦率') }],
    [{ label: '傷害',    value: pct('傷害') },          { label: '最終傷害', value: pct('最終傷害') }],
    [{ label: '爆擊傷害', value: pct('爆擊傷害') },     { label: '',         value: '' }],
  ]

  const labelStyle: React.CSSProperties = { color: '#546e7a', flexShrink: 0, fontWeight: 'bold' }
  const valueStyle: React.CSSProperties = { color: '#1a252f', textAlign: 'right', fontWeight: 500 }

  return (
    <div style={{
      gridColumn: '3 / span 5',
      gridRow: '8 / span 3',
      borderRadius: 6,
      padding: '6px 8px',
      fontSize: 12,
      color: '#ccc',
      display: 'flex',
      flexDirection: 'column',
      gap: 2,
    }}>
      {fullRows.map(({ label, value }) => (
        <div key={label} style={{ display: 'flex', justifyContent: 'space-between', lineHeight: 1.55 }}>
          <span style={labelStyle}>{label}</span>
          <span style={valueStyle}>{value}</span>
        </div>
      ))}
      <div style={{ height: 1, background: '#b2bec3', margin: '2px 0', opacity: 0.5 }} />
      {pairRows.map(([left, right], i) => (
        <div key={i} style={{ display: 'flex', gap: 8, lineHeight: 1.55 }}>
          <div style={{ flex: 1, display: 'flex', justifyContent: 'space-between' }}>
            <span style={labelStyle}>{left.label}</span>
            <span style={valueStyle}>{left.value}</span>
          </div>
          <div style={{ width: 1, background: '#b2bec3', opacity: 0.4 }} />
          <div style={{ flex: 1, display: 'flex', justifyContent: 'space-between' }}>
            <span style={labelStyle}>{right.label}</span>
            <span style={valueStyle}>{right.value}</span>
          </div>
        </div>
      ))}
      {characterBasic && (
        <div style={{ marginTop: 4, paddingTop: 4, borderTop: '1px solid #b2bec3', fontSize: 9, color: '#7f8c8d', textAlign: 'center' }}>
          {characterBasic.character_name} · {characterBasic.character_class} · Lv.{characterBasic.character_level}
        </div>
      )}
    </div>
  )
}

