// String - enclosed in "" or ''
// Number - 0-9
// Boolean - true or false
// Array - aka. list

// Variable - a container for some value

let names = [
    'Kevin',
    'Domien'
]
let yearOfBirth = 1993
let currentYear = 2024
let age = currentYear - yearOfBirth

let isMarried = false
let hasAKid = true

console.log(names[0] + ' is ' + age +  ' years old.')

if(isMarried) {
    console.log('And ' + names[0] + ' is married.')
} else if(hasAKid) {
    console.log('And ' + names[0] + ' has a kid.') 
} else {
    console.log('And ' + names[0] + ' is not married.')  
}
