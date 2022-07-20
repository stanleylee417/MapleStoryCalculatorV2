import { create } from 'zustand'
import { Build } from '@/lib/Build'
import { CharacterStats } from '@/types/character'

interface AppState {
  baseStats: CharacterStats | null
  builds: Build[]
  setBaseStats: (stats: CharacterStats) => void
  addBuild: (build: Build) => void
  removeBuild: (id: string) => void
  updateBuild: (id: string, build: Build) => void
}

export const useAppStore = create<AppState>((set) => ({
  baseStats: null,
  builds: [],
  setBaseStats: (stats) => set({ baseStats: stats }),
  addBuild: (build) => set((state) => ({ builds: [...state.builds, build] })),
  removeBuild: (id) => set((state) => ({ builds: state.builds.filter((b) => b.id !== id) })),
  updateBuild: (id, build) =>
    set((state) => ({ builds: state.builds.map((b) => (b.id === id ? build : b)) }))
}))
