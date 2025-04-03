const mostFrequentChar = (str) => {
    let array = str.split("")
    let obj = new Object()
    array.forEach((char) => {
        if (!Object.keys(obj).includes(char)) {
            return obj[char] = 1
        } else {
            return obj[char] += 1
        }
    });
    // console.log(obj);
    
    let maxCount = 1;
    let mostFrequent = ""
    for (let key in obj) {
        if(obj[key] >= maxCount) {
            maxCount = obj[key]
            mostFrequent = key
        }
    }
    return {
        maxCount:maxCount,
        mostFrequent:mostFrequent
    }
}
console.log(mostFrequentChar("javascript"))