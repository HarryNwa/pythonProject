let left_operand = 8;
let right_operand = 6;
let operator = "*";
let ans;

// let ans = windows.prompt("Choose number ");

if(operator == "+"){
    ans = left_operand + right_operand
}
if(operator == "-"){
    ans = left_operand - right_operand
}
if(operator == "/"){
    ans = left_operand / right_operand
}
if(operator == "*"){
    ans = left_operand * right_operand
}
if(operator != "+" && operator != "-" && operator != "/" && operator != "*"){
    ans = "Nan"
}


// switch (operator){
//     case "+":
//        ans = left_operand + right_operand
//        break
//     case "-":
//         ans = left_operand - right_operand
//         break
//     case "*":
//         ans = left_operand * right_operand
//         break
//     case "/":
//         ans = left_operand / right_operand
//         break
//     default: 
//         ans = "NaN"
   
// }
console.log(ans)
