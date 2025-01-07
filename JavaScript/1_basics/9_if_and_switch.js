/**
 * if and switch
 */
let number = 5;

if (number % 2 === 0){
    console.log('짝수');
} else{
    console.log('홀수');
}

if (number %2===0){
    console.log('2의 배수');
}else if (number%3===0){
    console.log('3');
}else{
    console.log('2,3의 배수가 아님');
}

const englishDay = 'monday';

let koreanDay;

switch(englishDay){
    case 'monday':
        koreanDay = '월';
        break;
    case 'tu':
        koreanDay='화';
        break;
    default:
        koreanDay = '주말';
        break;
}
console.log(koreanDay);
