import React, { useState } from 'react'
import { fetchCharacterOcid, fetchCharacterBasic, fetchCharacterEquipment, fetchCharacterPetEquipment } from '@/lib/nexonApi'
import { NexonCharacterBasic } from '@/types/character'
import { NexonEquipmentItem, NexonPetEquipmentResponse } from '@/types/equipment'
import { SLOT_DEFS, SlotDef } from './slotDefinitions'

type PresetKey = 1 | 2 | 3

interface TooltipState {
  name: string
  x: number
  y: number
}

export default function CharacterSetup() {
  const [characterName, setCharacterName] = useState(window.api.defaultCharacterName)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [characterBasic, setCharacterBasic] = useState<NexonCharacterBasic | null>(null)
  const [activePreset, setActivePreset] = useState<PresetKey>(1)
  const [tooltip, setTooltip] = useState<TooltipState | null>(null)
  const [presetMaps, setPresetMaps] = useState<Record<PresetKey, Record<string, NexonEquipmentItem>>>({
    1: {}, 2: {}, 3: {}
  })
  const [petEquipment, setPetEquipment] = useState<NexonPetEquipmentResponse | null>(null)

  const equipmentMap = presetMaps[activePreset]

  async function handleSearch() {
    if (!characterName.trim()) return
    setLoading(true)
    setError(null)
    try {
      const ocid = await fetchCharacterOcid(characterName.trim())
      const [basic, equip, pet] = await Promise.all([
        fetchCharacterBasic(ocid),
        fetchCharacterEquipment(ocid),
        fetchCharacterPetEquipment(ocid)
      ])
      console.log('character basic:', JSON.stringify(basic, null, 2))
      console.log('equipment:', JSON.stringify(equip, null, 2))
      console.log('pet equipment:', JSON.stringify(pet, null, 2))
      console.log('preset1 android:', equip.item_equipment_preset_1.find(i => i.item_equipment_slot === '機器人'))
      console.log('item_equipment android:', equip.item_equipment.find(i => i.item_equipment_slot === '機器人'))
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
    } catch (e) {
      setError(e instanceof Error ? e.message : '查詢失敗')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div style={{ position: 'relative' }}>
      {tooltip && (
        <Tooltip name={tooltip.name} x={tooltip.x} y={tooltip.y} />
      )}
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(7, 1fr)',
        gridTemplateRows: 'repeat(6, auto) 20px auto',
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
              onHover={(name, x, y) => setTooltip(name ? { name, x, y } : null)}
            />
          )
        })}

        {/* Separator */}
        <div style={{ gridColumn: 'span 7', display: 'flex', alignItems: 'center', height: 20 }}>
          <div style={{ width: '100%', height: 2, background: '#d1d4d9', borderBottom: '1px solid #fff', opacity: 0.8, borderRadius: 1 }} />
        </div>
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

function Tooltip({ name, x, y }: { name: string; x: number; y: number }) {
  return (
    <div style={{
      position: 'fixed',
      left: x + 40,
      top: y,
      background: '#1a1a2e',
      border: '1px solid #555',
      borderRadius: 4,
      padding: '4px 8px',
      fontSize: 11,
      color: '#fff',
      whiteSpace: 'nowrap',
      zIndex: 999,
      pointerEvents: 'none',
    }}>
      {name}
    </div>
  )
}

function EquipmentSlot({ slot, item, petIcon, petName, onHover }: {
  slot: SlotDef
  item?: NexonEquipmentItem
  petIcon?: string
  petName?: string
  onHover: (name: string | null, x: number, y: number) => void
}) {
  const displayIcon = item?.item_icon ?? petIcon
  const displayName = item?.item_name ?? petName

  return (
    <div
      className={`slot ${slot.bg}`}
      style={{ gridColumn: slot.col, gridRow: slot.row }}
      onMouseEnter={e => displayName && onHover(displayName, e.clientX, e.clientY)}
      onMouseMove={e => displayName && onHover(displayName, e.clientX, e.clientY)}
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

