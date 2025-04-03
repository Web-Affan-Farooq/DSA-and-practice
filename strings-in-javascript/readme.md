# Strings Manipulation in Javascript:

## Methods:
- .length property for finding string length
- string.charAt()  finding a character at given index
- string.charCodeAt()  finding character code at given index
- string.at()  finding a character at given index
- string.slice()  slicing a string  accepts two arguments one for start index and second for delete index
- string.toUpperCase()   for converting string to uppercase 
- string.toLowerCase()   for converting string to lowercase 
- string.concat()   used for string concatenation . Accepts an argument to attach with string

- the main difference b/w substring() and slice()  is the slice allow negative indexing while substring() assume negative indexes as 0 
- trim() method removes whitespaces from both end and start of the string
- trimStart() method removes whitespaces from the end of string
- trimEnd() method removes whitespaces from the start of string
- padStart() is used for pushing indexes in string from start and adding a new string after the given index
- padEnd() is used for pushing indexes in string at end and adding a new string after the given index
- repeat() is used to repeat string with given count times
- replace() used to replace any character in string , accepts character first and then replacement string
- replaceAll() use to replace required character in string where ever or how many it is located in string. accepts a string or regex for replacement first and then the new value
- split() used to split a string in array if a space . is no characters are provided, break all the string in array contains each character as value
- codePointAt() same as charCodeAt()
- indexOf() for finding index of a character in string
- includes() return if the given string is present in main string or not true or false
- eval() used for evaluating a code string;
- startsWith() return true if string starts with the required character.
- endsWith() return true if string ends with the required character.
- search() returns the first index of the first match of the given string also accepts regex for searching
- lastIndexOf() returns a last finded index of the character in string
- localCompare() returns 




## Questions: 
- Write a function that takes a string as input and returns the string with each word reversed, but the order of words should remain the same.
#### Code :
``` javascript
const str = 'hello world';

const reverseString = (a) => {
    let array = a.split("").reverse();
    return array.toString().replaceAll(",","")
}
console.log(reverseString(str))
```
- Check for palindrome
#### Code:
``` javascript
const check = (e) => {
    let array = e.split("").reverse();
    let reversedStr = array.toString().replaceAll(",","");
    
    if(reversedStr === e) {
        console.log("hello");
    }else {
        console.log("mello");
    }
}
check("   ")
```

- Write a function that capitalizes only the first letter of a given string.
#### Code: 
``` javascript
let str = "dhjfkhfsd";
console.log(str[0].toUpperCase() + str.slice(1, str.length));
```

- Write a function that convert camelCase into snake_case
#### Code :
``` javascript
const convert = (e) => {
    let snakeCase = "";

    e.split("").forEach((char) => {
        if (char === char.toUpperCase() && char !== " ") {
            snakeCase += "_" + char.toLowerCase(); 
        } else {
            snakeCase += char;
        }
    });

    console.log(snakeCase);
};

convert("helloWorld Case world hgjfdhgj ");
```
- Write a function that extracts file extension from file name
#### Code :
```javascript
const extract = (e) => {
    return "." + e.split(".")[1]
}
console.log(extract("index.html"));
```