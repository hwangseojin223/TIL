/**
 * Data Types
 * 
 * 여섯개의 Primitive Type과
 * 한개의 오브젝트 타입이 있다.
 * 
 * 1) Number (숫자)
 * 2) String (문자열)
 * 3) Boolean (불리언)
 * 4) undefined 
 * 5) null
 * 6) Symbol
 * 
 * 7) Object (객체)
 *      Function
 *      Array
 *      Object
 */

const age = 32;
const tempature = -10;
const pi = 3.14;

console.log(typeof age);
console.log('----------------');

const infinity = Infinity;
const nInfinity = -Infinity;

console.log(typeof infinity);
console.log(typeof -Infinity);
console.log('----------------');

/**
 * String 타입
 */
const codeFactory = '"코"드팩토리';
console.log(typeof codeFactory);
console.log(codeFactory);

const ive = "'아이브' 안유진";
console.log(ive);

/**
 * Template Literal
 * 
 * Escaping Character
 * 1) newline -> \n
 * 2) tab -> \t
 * 3) 백슬래시를 스트링으로 표현하고 싶다면 두번 입력
 */
const iveYuJin = '아이브\n안\t유진\\';
console.log(iveYuJin);

const smallQutoation = '아이브\'코드팩토리';
console.log(smallQutoation);

const iveWonYoung2 = `아이브
장원영`;
console.log(iveWonYoung2);

console.log(typeof iveWonYoung2);

const groupName = 'ive';
console.log(groupName+' 안유진');
console.log(`${groupName} 안유진`);
console.log('----------------');
/**
 * Boolean 타입
 */
const isTrue = true;
const isFalse = false;
console.log(typeof isTrue);

/**
 * undefined
 * 
 * 사용자가 직접 값을 초기화하지 않았을 떄
 * 지정되는 값
 * 
 * 직접 undefined로 값을 초기화하는건 지양
 */
let noInit;
console.log(noInit);
console.log(typeof noInit);

/**
 * null 
 * 
 * undefined와 마찬가지로 값이 없다는 뜻
 * js에서는 개발자가 명시적으로 없는 값으로 초기화할때 사용
 */
let init = null;
console.log(init);
// console.log(typeof init); -> object로 출력됨 버그
console.log('----------------');

/**
 * Symbol
 * 
 * 유일무이한 값을 생성할때 사용
 * 다른 프리미티브값들과 다르게 Symbol 함수를 후출해서 사용
 */
const test1 = '1';
const test2 = '1';

console.log(test1===test2);

const symbol1 = Symbol('1');
const symbol2 = Symbol('1');

console.log(symbol1 === symbol2);

/**
 * Object 타입
 * 
 * Map
 * key:value의 쌍으로 이루어짐ㅇ
*/
const dictionary = {
    red:'빨간색',
    orange:'주황색',
    yellow :'노란색',
};

console.log(dictionary);
console.log(dictionary['red']);

console.log(typeof dictionary);

/**
 * Array
 * 
 * 값을 리스트로 나열할 수 있는 타입
 */

const iveMembersArray = [
    '안유진',
    '가을',
    '레이',
    '장원영',
    '이서',
];
console.log(iveMembersArray);

/**
 * index
 */
console.log(iveMembersArray[0]);

iveMembersArray[0] = 'code';
console.log(iveMembersArray);

console.log(typeof iveMembersArray);

/**
 * static typing -> 변수를 선언할때 어떤 타입의 변수를 선언할지 명시를 한다
 * => C
 * dynamic typing -> 변수의 타입을 명시적으로 선언하지 않고 값에 의해 타입을 추론한다.
 * => js
 */