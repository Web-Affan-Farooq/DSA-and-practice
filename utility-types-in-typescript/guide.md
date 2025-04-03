# TypeScript Utility Types Guide

## 1. `Partial<T>` – Makes all properties optional

### **Use case:** When you want to update only a part of an object without defining all properties.

```ts
interface User {
  name: string;
  age: number;
  email: string;
}

// `Partial<User>` makes all properties optional
const updateUser = (user: Partial<User>) => {
  console.log("Updating user:", user);
};

updateUser({ name: "John" }); // ✅ Allowed
updateUser({ age: 25 }); // ✅ Allowed
updateUser({}); // ✅ Allowed
```

---

## 2. `Readonly<T>` – Prevents modification of properties

### **Use case:** When you want to make an object immutable.

```ts
interface User {
  name: string;
  age: number;
}

const user: Readonly<User> = {
  name: "Alice",
  age: 30,
};

user.age = 31; // ❌ Error: Cannot assign to 'age' because it is a read-only property.
```

---

## 3. `Pick<T, K>` – Selects specific properties from a type

### **Use case:** When you need only a subset of an object.

```ts
interface User {
  name: string;
  age: number;
  email: string;
}

// `Pick<User, "name" | "email">` selects only 'name' and 'email'
type UserContactInfo = Pick<User, "name" | "email">;

const contact: UserContactInfo = {
  name: "Alice",
  email: "alice@example.com",
};

console.log(contact);
```

---

## 4. `Omit<T, K>` – Removes specific properties from a type

### **Use case:** When you want everything **except** a few properties.

```ts
interface User {
  name: string;
  age: number;
  email: string;
}

// `Omit<User, "email">` removes the 'email' property
type UserWithoutEmail = Omit<User, "email">;

const user: UserWithoutEmail = {
  name: "Alice",
  age: 30,
};

console.log(user);
```

---

## Summary Table

| Utility Type  | Description |
|--------------|-------------|
| `Partial<T>` | Makes all properties optional |
| `Readonly<T>` | Prevents modification of properties |
| `Pick<T, K>` | Selects specific properties |
| `Omit<T, K>` | Removes specific properties |

Now you can refer to this Markdown guide whenever you need a quick revision! 🚀
