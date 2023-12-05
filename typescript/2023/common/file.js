'use strict'
Object.defineProperty(exports, '__esModule', { value: true })
exports.getChallengeInput = exports.getExampleInput = void 0
const fs = require('fs')
const getExampleInput = (day, pt = 1) => {
  return loadFile(`./2023/day${day}/example${pt}.txt`)
}
exports.getExampleInput = getExampleInput
const getChallengeInput = (day) => {
  return loadFile(`./2023/day${day}/input.txt`)
}
exports.getChallengeInput = getChallengeInput
const loadFile = (path) => {
  const data = fs.readFileSync(path, 'utf8')
  const lines = data.split('\n').filter((l) => l.length >= 1)
  return lines
}
