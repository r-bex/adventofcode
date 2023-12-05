'use strict'
Object.defineProperty(exports, '__esModule', { value: true })
exports.getDayFromFilename = exports.compareAnswers = void 0
const compareAnswers = (expected, actual) => {
  const outcome = expected === actual ? 'SUCCESS' : 'OOPS'
  return `Expected ${expected}, you got ${actual} -> ${outcome}\n`
}
exports.compareAnswers = compareAnswers
const getDayFromFilename = (filePath) => {
  try {
    const parts = filePath.split('/')
    const day = parts.find((s) => s.includes('day'))
    return parseInt(day.slice(3))
  } catch {
    console.error(`Could not extract day from path ${filePath}`)
    return -1
  }
}
exports.getDayFromFilename = getDayFromFilename
