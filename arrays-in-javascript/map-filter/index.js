// Complete the shift method 
class MyArray {
    constructor() {
        this.length = 0;
        this.data = {}
    }
    
    push(item) {
        this.data[this.length] = item
        this.length+=1
    }

    unshift(item) {
        this.data[0] = item
        this.length+=1
    }
    // access the data at first in the structure 
    // then delete it 
    shift() {
        delete this.data[0]
        this.length -=1
        for (let i=0; i<this.length; i++) {
            this.data[i] = this.data[i+1]
            if(i === this.length) {
                break
            }
        }
        // for (let i=0; i<=this.length - 2;  i++) {
        //     this.data[i] = this.data[i+1]
        // }        
        // data[0] = data[1]
        // data[1] = data[2]
        // data[2] = data[3]
        // data[3] = data[4]

    }

    pop() {
        const required = this.data[this.length - 1]
        this.length -= 1
        delete this.data[Object.keys(this.data).length -1]
        return required
    }

    reverse() {
        const list = []
        for (let i=this.length-1; i>=0; i--) {
            list.push(this.data[i])
        }
        return list
    }

    indexOf(item) {
        let required = Object.keys(this.data).find((key) => this.data[key] === item)
        if(required) {
            return required
        }
        else {
            throw new Error("Array index out of range ")
        }
    }

}

let array = new MyArray()
array.push("Affan")
array.push("Affan")
array.push("Affan")
array.push("Affan")
array.push("Ayan")
console.log(array.data);