const { dict } = require('./101-data.js');

const keys = Object.values(dict);
const uniqKeys = [...new Set(keys)];
const newDict = {};
uniqKeys.forEach(function (element) {
  newDict[element] = [];
  for (const key in dict) {
    if (dict[key] === element) {
      newDict[element].push(key);
    }
  }
});

console.log(newDict);
