'use strict'
Object.defineProperty(exports, '__esModule', { value: true })
const file_1 = require('../common/file')
const utils_1 = require('../common/utils')
const _ = require('lodash')
const currentDay = (0, utils_1.getDayFromFilename)(__filename)
const scratchcardParser = (line) => {
  try {
    const [cardRaw, numbers] = line.split(': ')
    const [winningRaw, mineRaw] = numbers.split(' | ')
    return {
      index: parseInt(cardRaw.slice(5).trim()),
      winningNumbers: winningRaw
        .split(' ')
        .map((n) => parseInt(n))
        .filter((n) => n),
      myNumbers: mineRaw
        .split(' ')
        .map((n) => parseInt(n))
        .filter((n) => n),
    }
  } catch {
    console.warn(`Couldn't parse the following line into a scratchcard: ${line}`)
    return null
  }
}
const calculatePoints = (card) => {
  const matching = card.myNumbers.filter((num) => card.winningNumbers.includes(num)).length
  return matching ? 2 ** (matching - 1) : 0
}
// eslint-disable-next-line @typescript-eslint/no-unused-vars
const part1 = (lines) => {
  const scratchcards = lines.map((line) => scratchcardParser(line)).filter((card) => card)
  return _.sum(scratchcards.map((card) => calculatePoints(card)))
}
// put the example solution here
const exampleInputPt1 = (0, file_1.getExampleInput)(currentDay, 1)
const EXAMPLE_SOLUTION_PT1 = 13
console.log(`EXAMPLE PT 1`)
console.log((0, utils_1.compareAnswers)(EXAMPLE_SOLUTION_PT1, part1(exampleInputPt1)))
// read the puzzle input and run part 1
const input = (0, file_1.getChallengeInput)(currentDay)
console.log('PART 1')
console.log(part1(input))
console.log()
const replicateArray = (basic, numReps) => {
  const newCards = []
  newCards.push(...basic)
  _.range(0, numReps).forEach((_) => newCards.push(...basic))
  return newCards
}
// const part2 = (lines: string[], debug: boolean = false): number => {
//   const originalScratchcards = lines.map((line) => scratchcardParser(line)).filter((card) => card)
//   let toProcess: Scratchcard[] = []
//   const processed: Scratchcard[] = []
//   // convert the original scratchcards into tuples with a = index and b = num matches
//   // this is now my queue
//   //const converted = originalScratchcards.map((c) => (c.index, c.myNumbers.filter((n) => c.winningNumbers.includes(n)).length))
//   originalScratchcards.forEach((card) => {
//     if (debug) {
//       console.log(`* processing card ${card.index}...`)
//       console.log(`TO_PROCESS: ${toProcess.map((c) => c.index)}`)
//     }
//     const numMatches = card.myNumbers.filter((num) => card.winningNumbers.includes(num)).length
//     const indicesToCopy = _.range(card.index + 1, card.index + numMatches + 1)
//     const matchingToProcess = toProcess.filter((tpCard) => tpCard.index === card.index)
//     const newCopies = originalScratchcards.filter((c) => indicesToCopy.includes(c.index))
//     const totalNewCopies = replicateArray(newCopies, matchingToProcess.length)
//     toProcess.push(...totalNewCopies)
//     if (debug) {
//       console.log(`* processing card ${card.index}...`)
//       console.log(`TO_PROCESS: ${toProcess.map((c) => c.index)}`)
//       console.log(`winning: ${card.winningNumbers}, my numbers: ${card.myNumbers}`)
//       console.log(`there are ${numMatches} matches -> will be ${numMatches} new copies`)
//       console.log(`want to take game indices: ${indicesToCopy}`)
//       console.log(`there are ${matchingToProcess.length} cards in TO_PROCESS with the same index as me`)
//       console.log(`adding a total of ${totalNewCopies.length} new cards`)
//     }
//     // remove all with index from toProcess
//     processed.push(card)
//     processed.push(...matchingToProcess)
//     toProcess = toProcess.filter((tpCard) => tpCard.index > card.index)
//     if (debug) {
//       console.log(`TO_PROCESS: ${toProcess.map((c) => c.index)}`)
//       console.log(`PROCESSED: ${processed.map((c) => c.index)}`)
//       console.log("=======\n")
//     }
//   })
//   // implement part 2 here
//   return processed.length
// }
const part2 = (lines, debug = false) => {
  const cards = lines.map((line) => scratchcardParser(line)).filter((card) => card)
  // create and initialize a copy counter object
  const numCopies = {}
  cards.forEach((card) => {
    numCopies[card.index] = 1
  })
  cards.forEach((card) => {
    const numMatches = card.myNumbers.filter((num) => card.winningNumbers.includes(num)).length
    const numCopiesToMake = numCopies[card.index]
    _.range(card.index + 1, card.index + numMatches + 1).forEach((index) => {
      numCopies[index] += numCopiesToMake
    })
  })
  // return sum of values
  return _.sum(Object.values(numCopies))
}
// read the example input for part 2 and check answer
const exampleInputPt2 = (0, file_1.getExampleInput)(currentDay, 2)
const EXAMPLE_SOLUTION_PT2 = 30
console.log(`EXAMPLE PT 2`)
console.log((0, utils_1.compareAnswers)(EXAMPLE_SOLUTION_PT2, part2(exampleInputPt2)))
// run part2
console.log('PART 2')
console.log(part2(input))
