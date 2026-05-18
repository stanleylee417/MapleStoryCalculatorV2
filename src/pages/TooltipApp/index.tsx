import { useState, useEffect, useRef } from 'react'
import { NexonEquipmentItem } from '@/types/equipment'
import ItemTooltip from '@/components/ItemTooltip'

export default function TooltipApp() {
  const [item, setItem] = useState<NexonEquipmentItem | null>(null)
  const containerRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    document.body.style.background = 'transparent'
    document.body.style.display = 'block'
    document.body.style.alignItems = 'unset'
    document.body.style.justifyContent = 'unset'
    document.body.style.height = 'auto'
    document.body.style.overflow = 'hidden'

    window.api.tooltip.onData((data) => setItem(data as NexonEquipmentItem))
  }, [])

  useEffect(() => {
    if (!containerRef.current) return
    const observer = new ResizeObserver(entries => {
      const height = entries[0]?.contentRect.height ?? 0
      if (height > 0) window.api.tooltip.resize(height)
    })
    observer.observe(containerRef.current)
    return () => observer.disconnect()
  }, [item])

  if (!item) return null
  return (
    <div ref={containerRef} style={{ display: 'inline-block' }}>
      <ItemTooltip item={item} />
    </div>
  )
}
