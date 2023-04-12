#!/usr/bin/node
const num = process.argv.length;
console.log(num === 2 ? 'No argument' : num === 3 ? 'Argument found' : 'Arguments found');
