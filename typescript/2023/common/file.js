"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.getChallengeInput = exports.getExampleInput = void 0;
var fs = require("fs");
var getExampleInput = function (day, pt) {
    if (pt === void 0) { pt = 1; }
    return loadFile("./2023/day".concat(day, "/example").concat(pt, ".txt"));
};
exports.getExampleInput = getExampleInput;
var getChallengeInput = function (day) {
    return loadFile("./2023/day".concat(day, "/input.txt"));
};
exports.getChallengeInput = getChallengeInput;
var loadFile = function (path) {
    var data = fs.readFileSync(path, 'utf8');
    return data.split("\n");
};
