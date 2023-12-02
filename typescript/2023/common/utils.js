"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.compareAnswers = void 0;
var compareAnswers = function (expected, actual) {
    var outcome = expected === actual ? "SUCCESS" : "OOPS";
    return "Expected ".concat(expected, ", you got ").concat(actual, " -> ").concat(outcome, "\n");
};
exports.compareAnswers = compareAnswers;
