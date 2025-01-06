/**
 * Variable 선언하기
 * 
 * 1) var - 더이상 쓰지 않는다.
 * 2) let
 * 3) const
 */

var name = '코드팩토리';
console.log(name);

var age = 32;
console.log(age);

let ive = 'ive';
console.log(ive);

/**
 * let과 var로 선언하면
 * 값을 추후 변경 가능
 */
ive = '안유진';
console.log(ive);

const newJeans = 'newjeans';
console.log(newJeans);

// newJeans = 'codefactory'; -> error

/**
 * 선언과 할당
 * 
 * 1) 변수를 선언하는 것.
 * 2) 할당
 * 
 */

var name;
console.log(name);

let girlFriend;
console.log(girlFriend); //undefined

// const girlFriend2; -> error