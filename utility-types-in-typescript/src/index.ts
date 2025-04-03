type MyPartial<T> = { [K in keyof T]?: T[K] };

type User = { name: string; age: number };
type PartialUser = MyPartial<User>; 
// ✅ { name?: string; age?: number }
