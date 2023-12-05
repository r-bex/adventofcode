export const compareAnswers = (expected: number, actual: number): string => {
  const outcome = expected === actual ? 'SUCCESS' : 'OOPS'
  return `Expected ${expected}, you got ${actual} -> ${outcome}\n`
}

export const getDayFromFilename = (filePath: string): number => {
  try {
    const parts = filePath.split('/')
    const day = parts.find((s) => s.includes('day'))
    return parseInt(day.slice(3))
  } catch {
    console.error(`Could not extract day from path ${filePath}`)
    return -1
  }
}
