// import { bench, run } from 'mitata';
// import pkg from './myRandom_napi.cjs';
// const { myRandom } = pkg;

// CommonJS
const { bench, run } = require('mitata-commonjs');
const mylib = require( './build/Release/myRandomNAPI' );

console.log("myRandom() =", mylib.myRandom());

bench('myRandom', () => {
  mylib.myRandom();
});

run();