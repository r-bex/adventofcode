import { getExampleInput, getChallengeInput } from '../common/file'
import { compareAnswers, getDayFromFilename } from '../common/utils'
import * as _ from 'lodash'

const currentDay = getDayFromFilename(__filename)

type Scratchcard = {
  index: number
  winningNumbers: number[]
  myNumbers: number[]
}

const scratchcardParser = (line: string): Scratchcard | null => {
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

const calculatePoints = (card: Scratchcard): number => {
  const matching = card.myNumbers.filter((num) => card.winningNumbers.includes(num)).length
  return matching ? 2 ** (matching - 1) : 0
}

// eslint-disable-next-line @typescript-eslint/no-unused-vars
const part1 = (lines: string[]): number => {
  const scratchcards = lines.map((line) => scratchcardParser(line)).filter((card) => card)
  return _.sum(scratchcards.map((card) => calculatePoints(card)))
}

// put the example solution here
const exampleInputPt1: string[] = getExampleInput(currentDay, 1)
const EXAMPLE_SOLUTION_PT1: number = 13
console.log(`EXAMPLE PT 1`)
console.log(compareAnswers(EXAMPLE_SOLUTION_PT1, part1(exampleInputPt1)))

// read the puzzle input and run part 1
const input: string[] = getChallengeInput(currentDay)
console.log('PART 1')
console.log(part1(input))
console.log()

const part2 = (lines: string[]): number => {
  const cards = lines.map((line) => scratchcardParser(line)).filter((card) => card)

  // create and initialize a copy counter object
  const numCopies: Record<number, number> = {}
  cards.forEach((card) => {
    numCopies[card.index] = 1
  })

  cards.forEach((card) => {
    const numMatches = card.myNumbers.filter((num) => card.winningNumbers.includes(num)).length
    const numCopiesToMake = numCopies[card.index]
    // increment the copy counter value for each index to be copied by the right amount
    _.range(card.index + 1, card.index + numMatches + 1).forEach((index) => {
      numCopies[index] += numCopiesToMake
    })
  })

  // return sum of values
  return _.sum(Object.values(numCopies))
}

// read the example input for part 2 and check answer
const exampleInputPt2: string[] = getExampleInput(currentDay, 2)
const EXAMPLE_SOLUTION_PT2: number = 30
console.log(`EXAMPLE PT 2`)
console.log(compareAnswers(EXAMPLE_SOLUTION_PT2, part2(exampleInputPt2)))

// run part2
console.log('PART 2')
console.log(part2(input))
