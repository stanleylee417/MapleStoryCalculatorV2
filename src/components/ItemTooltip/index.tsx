import { NexonEquipmentItem, NexonItemOption } from '@/types/equipment'

interface Props {
  item: NexonEquipmentItem
}

const GRADE_MAP: Record<string, { cls: string; letter: string; label: string }> = {
  '傳說': { cls: 'rank-legendary', letter: 'L', label: '傳說' },
  '唯一': { cls: 'rank-unique',    letter: 'U', label: '唯一' },
  '史詩': { cls: 'rank-epic',      letter: 'E', label: '史詩' },
  '稀有': { cls: 'rank-rare',      letter: 'E', label: '稀有' },
  '罕見': { cls: 'rank-common',    letter: 'U', label: '罕見' },
  '特殊': { cls: 'rank-special',   letter: 'R', label: '特殊' },
}

const GRADE_COLORS: Record<string, string> = {
  'rank-legendary': '#ccff00',
  'rank-unique':    '#ffbb00',
  'rank-epic':      '#b380ff',
  'rank-rare':      '#b380ff',
  'rank-common':    '#ffbb00',
  'rank-special':   '#33cccc',
}

const STAT_KEYS: { key: keyof NexonItemOption; label: string; suffix?: string }[] = [
  { key: 'str',                    label: 'STR' },
  { key: 'dex',                    label: 'DEX' },
  { key: 'int',                    label: 'INT' },
  { key: 'luk',                    label: 'LUK' },
  { key: 'max_hp',                 label: 'Max HP' },
  { key: 'max_mp',                 label: 'Max MP' },
  { key: 'attack_power',           label: '攻擊力' },
  { key: 'magic_power',            label: '魔法攻擊力' },
  { key: 'armor',                  label: '防禦力' },
  { key: 'all_stat',               label: '全屬性',        suffix: '%' },
  { key: 'boss_damage',            label: 'BOSS傷害',      suffix: '%' },
  { key: 'ignore_monster_armor',   label: '無視防禦',      suffix: '%' },
  { key: 'damage',                 label: '傷害',          suffix: '%' },
]

function nonZero(v: string | undefined): string | null {
  if (!v || v === '0') return null
  return v
}

export default function ItemTooltip({ item }: Props) {
  const starforce = parseInt(item.starforce ?? '0', 10)
  const maxStar = 30

  const rows = [
    { stars: 15, groups: 3 },
    { stars: 15, groups: 3 },
  ]
  let starIdx = 0

  const total = item.item_total_option
  const base  = item.item_base_option
  const sf    = item.item_starforce_option
  const etc   = item.item_etc_option
  const add   = item.item_add_option

  const potential   = GRADE_MAP[item.potential_option_grade ?? '']
  const additional  = GRADE_MAP[item.additional_potential_option_grade ?? '']

  const scrollCount = parseInt(item.scroll_upgrade ?? '0', 10)
  const etcAvgRows = scrollCount > 0
    ? STAT_KEYS.filter(({ key }) => nonZero(etc?.[key] as string))
        .map(({ key, label, suffix = '' }) => ({
          label,
          suffix,
          avg: String(parseFloat((parseFloat(etc![key] as string) / scrollCount).toFixed(1))),
        }))
    : []

  return (
    <div style={{
      width: 320,
      background: 'rgba(10,15,25,0.95)',
      border: '2px solid #555566',
      borderRadius: 10,
      padding: 15,
      color: 'white',
      fontFamily: '"Segoe UI", "Microsoft JhengHei", sans-serif',
      fontSize: 13,
      boxShadow: 'inset 0 0 10px #000, 0 5px 15px rgba(0,0,0,0.5)',
    }}>

      {/* Stars */}
      {starforce > 0 && (
        <div style={{ textAlign: 'center', marginBottom: 10, lineHeight: 1.3 }}>
          {rows.map((row, ri) => (
            <div key={ri} style={{ letterSpacing: 2, fontSize: 13 }}>
              {Array.from({ length: row.groups }).map((_, gi) => (
                <span key={gi} style={{ marginRight: gi < row.groups - 1 ? 4 : 0 }}>
                  {Array.from({ length: 5 }).map((_, si) => {
                    const idx = starIdx++
                    return (
                      <span key={si} style={{ color: idx < starforce ? '#ffcc00' : '#333' }}>★</span>
                    )
                  })}
                </span>
              ))}
            </div>
          ))}
        </div>
      )}

      {/* Item name */}
      <div style={{ textAlign: 'center', fontSize: 18, fontWeight: 'bold', marginBottom: 12 }}>
        {item.item_name}
      </div>

      {/* Image */}
      <div style={{
        display: 'flex',
        justifyContent: 'flex-start',
        padding: '12px 0',
        borderTop: '1px dashed #666',
        borderBottom: '1px dashed #666',
        marginBottom: 10,
      }}>
        <div style={{
          width: 84, height: 84,
          background: 'linear-gradient(135deg, #fff 0%, #777 100%)',
          border: '1px solid #fff',
          borderRadius: 5,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}>
          <img src={item.item_icon} alt={item.item_name} style={{ width: 64, height: 64, objectFit: 'contain' }} />
        </div>
      </div>

      {/* Stats */}
      <div style={{ lineHeight: 1.7, paddingBottom: potential || additional ? 10 : 0, borderBottom: potential || additional ? '1px dashed #666' : 'none' }}>
        {STAT_KEYS.map(({ key, label, suffix = '' }) => {
          const t = nonZero(total?.[key] as string)
          if (!t) return null
          const b  = nonZero(base?.[key] as string)
          const s  = nonZero(sf?.[key] as string)
          const e  = nonZero(etc?.[key] as string)
          const a  = nonZero(add?.[key] as string)
          const hasBreakdown = s || e || a
          return (
            <div key={key}>
              <span style={{ color: '#fff' }}>{label} : +{t}{suffix}</span>
              {hasBreakdown && (
                <span style={{ color: '#888' }}> （
                  <span style={{ color: '#fff' }}>{b ?? '0'}{suffix}</span>
                  {s && <span style={{ color: '#ffcc00', marginLeft: 6 }}>+{s}{suffix}</span>}
                  {e && <span style={{ color: '#9999ff', marginLeft: 6 }}>+{e}{suffix}</span>}
                  {a && <span style={{ color: '#00ffff', marginLeft: 6 }}>+{a}{suffix}</span>}
                  <span style={{ color: '#888' }}>）</span>
                </span>
              )}
            </div>
          )
        })}
      </div>

      {/* Potential */}
      {potential && (
        <PotentialBox
          grade={potential}
          color={GRADE_COLORS[potential.cls] ?? '#fff'}
          title={`潛在能力：${potential.label}`}
          options={[item.potential_option_1, item.potential_option_2, item.potential_option_3]}
        />
      )}

      {/* Additional Potential */}
      {potential && additional && (
        <div style={{ borderTop: '1px dashed #666', marginTop: 12 }} />
      )}
      {additional && (
        <PotentialBox
          grade={additional}
          color={GRADE_COLORS[additional.cls] ?? '#fff'}
          title={`附加潛在能力：${additional.label}`}
          options={[item.additional_potential_option_1, item.additional_potential_option_2, item.additional_potential_option_3]}
        />
      )}
      {/* Scroll avg */}
      {etcAvgRows.length > 0 && (
        <div style={{ marginTop: 12, paddingTop: 10, borderTop: '1px dashed #666', fontSize: 13 }}>
          <div style={{ color: '#aaa', marginBottom: 4 }}>卷軸均值（共 {scrollCount} 次）</div>
          {etcAvgRows.map(({ label, suffix, avg }) => (
            <div key={label}>
              <span style={{ color: '#9999ff' }}>{label} : +{avg}{suffix}</span>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

function PotentialBox({ grade, color, title, options }: {
  grade: { cls: string; letter: string }
  color: string
  title: string
  options: (string | undefined)[]
}) {
  const validOptions = options.filter(Boolean)
  if (!validOptions.length) return null

  return (
    <div style={{ marginTop: 12, fontSize: 13 }}>
      <div style={{ display: 'flex', alignItems: 'center', marginBottom: 4, fontWeight: 'bold' }}>
        <span style={{
          background: color, color: 'black',
          fontWeight: 'bold', padding: '0 4px',
          borderRadius: 2, marginRight: 6,
          fontSize: 11, textTransform: 'uppercase',
        }}>
          {grade.letter}
        </span>
        <span style={{ color }}>{title}</span>
      </div>
      <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
        {validOptions.map((opt, i) => (
          <li key={i} style={{ paddingLeft: 18, position: 'relative', lineHeight: 1.6 }}>
            <span style={{
              position: 'absolute', left: 0,
              fontSize: 9, top: 1, color: 'white',
            }}>■</span>
            {opt}
          </li>
        ))}
      </ul>
    </div>
  )
}
