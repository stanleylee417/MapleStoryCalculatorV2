import { useState } from 'react'
import CharacterSetup from '@/pages/CharacterSetup'
import Comparison from '@/pages/Comparison'

type Page = 'equipment' | 'comparison'

const PAGES: { key: Page; label: string; className: string }[] = [
  { key: 'equipment', label: 'EQUIPMENT', className: 'btn-gray' },
  { key: 'comparison', label: 'COMPARISON', className: 'btn-blue' },
]

export default function App() {
  const [page, setPage] = useState<Page>('equipment')

  return (
    <div style={{ width: 480, background: '#2c3e50', borderRadius: 12, padding: 10, border: '1px solid #1e272e', boxShadow: '0 10px 30px rgba(0,0,0,0.5)' }}>
      <div
        className="flex justify-between items-center mb-2 px-1"
        style={{ WebkitAppRegion: 'drag' } as React.CSSProperties}
      >
        <span style={{ color: '#e2f32a', fontWeight: 'bold', fontSize: 13, letterSpacing: '0.05em', textShadow: '0 1px 2px rgba(0,0,0,0.5)' }}>
          MAPLESTORY CALCULATOR
        </span>
        <div
          className="flex gap-1"
          style={{ WebkitAppRegion: 'no-drag' } as React.CSSProperties}
        >
          <button
            onClick={() => window.api.window.minimize()}
            style={{
              width: 22, height: 22, borderRadius: 4, border: '1px solid #3d5166',
              background: '#34495e', color: '#e2f32a', fontSize: 12, lineHeight: 1,
              fontWeight: 'bold', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center',
            }}
          >━</button>
          <button
            onClick={() => window.api.window.close()}
            style={{
              width: 22, height: 22, borderRadius: 4, border: '1px solid #3d5166',
              background: '#34495e', color: '#e2f32a', fontSize: 12, lineHeight: 1,
              fontWeight: 'bold', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center',
            }}
          >✕</button>
        </div>
      </div>

      <div style={{ background: '#eaedf2', borderRadius: 10, padding: 12, minHeight: 400 }}>
        {page === 'equipment' && <CharacterSetup />}
        {page === 'comparison' && <Comparison />}
      </div>

      <div className="flex gap-2 mt-3 px-1">
        {PAGES.map(({ key, label, className }) => (
          <button
            key={key}
            className={`btn-footer ${page === key ? 'btn-active' : className}`}
            style={{ minWidth: 100 }}
            onClick={() => setPage(key)}
          >
            {label}
          </button>
        ))}
      </div>
    </div>
  )
}
