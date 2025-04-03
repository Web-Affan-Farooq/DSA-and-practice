## Notes for DSA Topics :

### Datatypes and conversions :
- **variable declaration :**

```javascript
console.log(a) // undefined 
var a;

console.log(a) // error not defined 
let a;

console.log(a) // error not defined  
const a;
```
- **Type coersion :**
- Type coersion in the method in which type js converts the type based on the operator 
- All the operators perform operations to all daa types
- + operator has a unique behaviour in javascript
- true refers to 1 and false refers to 0 in javascript 

```javascript
console.log("1"+"1") // 11
console.log("1"-"1") // 0
console.log("1"*"2") // 2
console.log("1"/"1") // 1
console.log("a"+false) // afalse
console.log(false+"a") // falsea
console.log(true*3) // 3
```
- **Type casting :**
- It refers to force conversion of a value from one type to another 
```javascript
console.log(Number("Hello")) // Nan
console.log(Number("2")) // 2 (as a number)
console.log(Number(false)) // 0 
console.log(Number(true)) // 1
console.log(String(false)) // false (as string)
```
- **Arithemetic operators :**
- Operators used for performing arithemetic operations on numbers
- + (used for addition and concatenation in string)
- - used for subtraction 
- * used for multiplication 
- / used for division give results in quotient 
- % used for division give results in remainder 

```javascript
console.log(7/2) // 3.5
console.log(2/7) // 0.287
console.log(7%2) // 1 remainder 
console.log(2%7) // 2 remainder 
```