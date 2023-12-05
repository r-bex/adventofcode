import { getExampleInput, getChallengeInput } from '../common/file'
import { compareAnswers, getDayFromFilename } from '../common/utils'
import * as _ from 'lodash'

const currentDay = getDayFromFilename(__filename)

type Coordinate = {
  row: number
  column: number
}

// anything other than these chars counts as a symbol
const NONSYMBOLS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

const getHitbox = (start: Coordinate, end: Coordinate, numRows, numCols): Coordinate[] => {
  // the hitbox is the one 'pixel' radius of the number span
  const hitbox = []

  // origin is top left so 'topBound' has lower y than 'bottomBound'
  const leftBound = start.column > 0 ? start.column - 1 : 0
  const topBound = start.row > 0 ? start.row - 1 : 0
  const rightBound = end.column < numCols - 1 ? end.column + 1 : numCols - 1
  const bottomBound = end.row < numRows - 1 ? end.row + 1 : numRows - 1

  // add everything in range
  _.range(topBound, bottomBound + 1).forEach((row) => {
    _.range(leftBound, rightBound + 1).forEach((column) => {
      hitbox.push({
        row,
        column,
      })
    })
  })

  return hitbox
}

const hitboxContainsSymbol = (fullGrid: string[], hitbox: Coordinate[]): boolean => {
  return hitbox.some(({ row, column }) => {
    return !NONSYMBOLS.includes(fullGrid[row][column])
  })
}

const part1 = (lines: string[]): number => {
  const numRows = lines.length
  const numCols = lines[0].length
  let counter = 0

  lines.forEach((row, rowIndex) => {
    // get start and end coords of numbers using regex
    ;[...row.matchAll(/\d+/g)].forEach((match) => {
      const startCoord = { row: rowIndex, column: match.index }
      const endCoord = { row: rowIndex, column: match.index + match[0].length - 1 }
      const hitbox = getHitbox(startCoord, endCoord, numRows, numCols)
      // check if the number's hitbox contains a symbol and if so increment counter
      if (hitboxContainsSymbol(lines, hitbox)) {
        counter += parseInt(match[0])
      }
    })
  })
  return counter
}

// put the example solution here
const exampleInputPt1: string[] = getExampleInput(currentDay, 1)
const EXAMPLE_SOLUTION_PT1: number = 4361
console.log(`EXAMPLE PT 1`)
console.log(compareAnswers(EXAMPLE_SOLUTION_PT1, part1(exampleInputPt1)))

// read the puzzle input and run part 1
const input: string[] = getChallengeInput(currentDay)
console.log('PART 1')
console.log(part1(input))
console.log()
// should be 540131

const part2 = (lines: string[]): number => {
  const numRows = lines.length
  const numCols = lines[0].length

  // every time a gear (*) is encountered when scanning line
  // by line, keep track of the number that was adjacent to it
  const gearTracker: Record<string, number[]> = {}

  lines.forEach((row, rowIndex) => {
    ;[...row.matchAll(/\d+/g)].forEach((match) => {
      const startCoord = { row: rowIndex, column: match.index }
      const endCoord = { row: rowIndex, column: match.index + match[0].length - 1 }
      const hitbox = getHitbox(startCoord, endCoord, numRows, numCols)
      // extract gears and update gear number tracker
      hitbox
        .filter(({ row, column }) => lines[row][column] === '*')
        .forEach(({ row, column }) => {
          // use the gear's row-col combination as its unique key in the tracker
          const gearKey = `${row}-${column}`
          if (gearKey in gearTracker) {
            // missing the defaultdict rn
            gearTracker[gearKey].push(parseInt(match[0]))
          } else {
            gearTracker[gearKey] = [parseInt(match[0])]
          }
        })
    })
  })

  let counter = 0
  // if a gear has exactly two adjacent numbers then add their product to the counter
  Object.keys(gearTracker).forEach((gearKey) => {
    if (gearTracker[gearKey].length == 2) {
      counter += gearTracker[gearKey][0] * gearTracker[gearKey][1]
    }
  })
  return counter
}

// read the example input for part 2 and check answer
const exampleInputPt2: string[] = getExampleInput(currentDay, 2)
const EXAMPLE_SOLUTION_PT2: number = 467835
console.log(`EXAMPLE PT 2`)
console.log(compareAnswers(EXAMPLE_SOLUTION_PT2, part2(exampleInputPt2)))

// run part2
console.log('PART 2')
console.log(part2(input))
// should be 86879020
