/**
 * Operators
 * 
 * 연산자
 */

/**
 * 산술 연산자
 * 
 */
console.log(10+10);
console.log(10-10);
console.log(10*10);
console.log(10/10);
console.log(10%10);

console.log('--------------------');

console.log(10*(10+10));

/**
 * 증가와 감소
 */
let number = 1;
number ++;
console.log(number);

number--;
console.log(number);
console.log('--------------------');

/**
 * 연산자의 위치
 */
let result = 1;
console.log(result);

result = number++;
console.log(result, number); // 1,2

result = number--;
console.log(result, number); // 2,1

result = ++number;
console.log(result, number); // 2,2

result = --number;
console.log(result, number); // 1,1

/**
 * 숫자 타입이 아닌 타입에 +, - 사용하면?
 */
let sample = '99';

console.log(+sample); //99
console.log(typeof +sample); // number

console.log(sample);
console.log(typeof sample); // string

sample = true;
console.log(+sample); // 1
console.log(typeof +sample); // number

sample = '안유진';
console.log(+sample); // NaN : Not a number

sample = '99';
console.log(-sample); // -99

/**
 *  할당 연산자 (assignment operator)
 */
number = 100;
console.log(number);

number += 10;
console.log(number);

// -=, *=, /=, %=

/**
 *  비교연산자
 * 
 * 1) 값의 비교
 * 2) 값과 타입의 비교
 */

console.log(5==5);
console.log(5=='5'); // true
console.log(0==''); // true
console.log(true=='1'); // true
console.log(false==0); // true

console.log(5 === 5); //true
console.log(5 ==='5');  //false
console.log(0===''); //false
console.log(true==='1'); // false
console.log(false===0); // false

// !=, !==

console.log('--------------------');


/**
 *  대소 관계 비교 연산자
 */
console.log(100>1);
// <, <=, >= 

console.log('--------------------');

/**
 * 삼항 조건 연산자 (ternary operator)
 */
console.log(10>0 ? '10이 0보다 크다.' : '10이 0보다 작다');

console.log('--------------------');

/**
 * 논리연산자
 * 
 * 1) &&
 * 2) ||
 */
// && 조건은 모두 true여야 true를 반환
console.log(true && true);

// || 는 하나만 true여도 true 반환
console.log(true||false);

console.log(10>1 && 20>2);
console.log('--------------------');

/**
 * 단축평가 short circuit evaluation
 * 
 * &&를 사용했을때 좌측이 true면 우측 값 반환
 * &&를 사용했을 때 좌측이 false면 좌측 값 반환
 * ||를 사용했을때 좌측이 true면 좌측 값 반환
 * ||를 사용했을때 좌측이 false면 우측 값 반환
 */
console.log(true &&'아이브');
console.log(false &&'아이브');
console.log(true ||'아이브');
console.log(false ||'아이브');

console.log(true&&true&&'ive');
console.log('--------------------');
/**
 * 지수연산자
 */
console.log(2**2);

/**
 * null 연산자
 */
let name;
console.log(name);

name = name ?? 'codefactory';
console.log(name); // codefactory

name = name ?? 'ive';
console.log(name);

let name2;
name2 ??= 'codefactory';
console.log(name2);