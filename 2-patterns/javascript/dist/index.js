"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
let n = 4;
// Upper part
for (let i = 1; i <= n; i++) {
    let spaces = " ".repeat(n - i);
    let stars = "*".repeat(2 * i - 1);
    console.log(spaces + stars);
}
// // Lower part
// for (let i = n - 1; i >= 1; i--) {
//     let spaces = " ".repeat(n - i);
//     let stars = "*".repeat(2 * i - 1);
//     console.log(spaces + stars);
// }
