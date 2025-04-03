 You are given an array of products, where each product is an object with the following properties:

javascript
Copy
Edit
{
  id: number, 
  name: string, 
  price: number, 
  category: string, 
  rating: number,
  stock: number
}
Your Task:
Filter the products based on the following criteria:

If the product is from the "Electronics" category, it should have a rating of at least 4.2 and stock greater than 0.
If the product is from the "Furniture" category, it should have a price greater than 100 and rating of at least 4.0.
Apply a dynamic discount based on the stock:

If stock is less than or equal to 5, apply a 20% discount.
If stock is between 6 and 10, apply a 10% discount.
If stock is greater than 10, apply a 5% discount.
Return a new array where each product object contains only:

id, name, and discountedPrice
🔹 Example Input:
javascript
Copy
Edit
const products = [
  { id: 1, name: "Laptop", price: 1500, category: "Electronics", rating: 4.5, stock: 3 },
  { id: 2, name: "Phone", price: 800, category: "Electronics", rating: 4.0, stock: 0 },
  { id: 3, name: "Table", price: 120, category: "Furniture", rating: 4.2, stock: 7 },
  { id: 4, name: "Chair", price: 80, category: "Furniture", rating: 4.0, stock: 15 },
  { id: 5, name: "Headphones", price: 200, category: "Electronics", rating: 4.3, stock: 9 }
];
🔹 Expected Output:
javascript
Copy
Edit
[
  { id: 1, name: "Laptop", discountedPrice: 1200 }, // 20% off
  { id: 3, name: "Table", discountedPrice: 108 },  // 10% off
  { id: 5, name: "Headphones", discountedPrice: 180 } // 10% off
]
🔹 Explanation:
Laptop: Meets criteria (Electronics, rating 4.5, stock 3). 20% discount → 1500 - 300 = 1200
Phone: Does not meet criteria (out of stock).
Table: Meets criteria (Furniture, price 120, rating 4.2, stock 7). 10% discount → 120 - 12 = 108
Chair: Does not meet criteria (price is below 100).
Headphones: Meets criteria (Electronics, rating 4.3, stock 9). 10% discount → 200 - 20 = 180