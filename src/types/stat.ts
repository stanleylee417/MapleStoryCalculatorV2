export interface NexonFinalStat {
  stat_name: string
  stat_value: string
}

export interface NexonCharacterStatResponse {
  date: string | null
  character_class: string
  final_stat: NexonFinalStat[]
  remain_ap: number
}
