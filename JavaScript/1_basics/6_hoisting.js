/**
 * Hoisting
 */
console.log('Hello');
console.log('World');
console.log('=============');

console.log(name); // undefined
var name = 'codeFactory';
console.log(name);
//위와 아래가 같음
var name;
console.log(name);
name = 'codeFacotry';
console.log(name);

/**
 * Hoisting은 무엇인가?
 * 
 * 모든 변수 선언문이 코드의 최상단으로 이동되는 것처럼 느껴지는 현상
 */

console.log(yuJin); // error 
let yuJin = 'yj';
// let, const는 Hoisting 현상을 막아줌