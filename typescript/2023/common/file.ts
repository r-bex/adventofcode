import * as fs from 'fs'

export const getExampleInput = (day: number, pt: number = 1): string[] => {
  return loadFile(`./2023/day${day}/example${pt}.txt`)
}

export const getChallengeInput = (day: number): string[] => {
  return loadFile(`./2023/day${day}/input.txt`)
}

const loadFile = (path: string): string[] => {
  const data = fs.readFileSync(path, 'utf8')
  const lines = data.split('\n').filter((l) => l.length >= 1)
  return lines
}
