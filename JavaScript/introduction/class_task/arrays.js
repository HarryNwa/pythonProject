let arr = new Array(5);
let arr2 = [1, 2, 4, 4, 6];
let arr3 = new Array (5, 4, 2, 5, 6);

arr = [3, "4", 7, "3", 8, {name : "Daniel"}]
arr.splice(2, 4, 5, 6, 7, 8)
console.log(arr.shift(0, 3))
// console.log(arr.shift())
arr.unshift(23)
console.log(arr)
arr.pop()
arr.push(45)
console.log(arr)

Array.prototype.laugh = "lol"
console.log(arr.laugh)


let array = [5, 6, 8, 3, 6]
console.table(array)

for (let i in array){
    
    process.stdout.write('${i}')
    console.log(i)
    
}

let obj = {
    name : "esther",
    age : 23,
    height : "5'4",
    cohort : 17
}

let objVal = Object.values(obj)
let objKey = Object.keys(obj)

console.log()
for(let i of objKey){
    process.stdout.write('${i}')
}