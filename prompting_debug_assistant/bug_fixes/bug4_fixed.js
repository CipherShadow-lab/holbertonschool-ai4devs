// Code is fixed by changing the loop condition to include the last index.

const shoppingList = [
    "apples",
    "bread",
    "milk",
    "eggs",
    "coffee"
];

console.log("My shopping list:");

const lastIndex = shoppingList.length - 1;

for (let itemIndex = 0; itemIndex < shoppingList.length; itemIndex++) {
    const itemNumber = itemIndex + 1;
    const itemName = shoppingList[itemIndex];

    console.log(itemNumber, itemName);
}

console.log("Total items:", shoppingList.length);