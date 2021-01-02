const menu = {
  _courses: {
    appetizers: [],
    mains: [],
    desserts: [],
  },
  get appetizers() {
    return this._courses.appetizers
  },
  get mains() {
    return this._courses.mains
  },
  get desserts() {
    return this._courses.desserts
  },
  set appetizers(appetizer) {
    this._courses.appetizers = appetizer
  },
  set mains(main) {
    this._courses.mains = main
  },
  set desserts(dessert) {
    this._courses.desserts = dessert
  },
  get courses() {
    return {
      appetizers: this.appetizers,
      mains: this.mains,
      desserts: this.desserts
    };
  },
  addDishToCourse (courseName, dishName, dishPrice) {
    const dish = {
      name: dishName,
      price: dishPrice
    };
    return this._courses[courseName].push(dish);
  },
  getRandomDishFromCourse(courseName) {
    const dishes = this._courses[courseName];
    const randomIndex = Math.floor(Math.random()*dishes.length);
    return dishes[randomIndex];
  },
  generateRandomMeal() {
    const appetizer = this.getRandomDishFromCourse('appetizers');
    const main = this.getRandomDishFromCourse('mains');
    const dessert = this.getRandomDishFromCourse('desserts');
    const total = appetizer.price + main.price + dessert.price;
    return `Your meal is: ${appetizer.name}, ${main.name}, ${dessert.name}. The total price is $${total}.`;
  }
};

menu.addDishToCourse('appetizers', 'Salad', 3.5);
menu.addDishToCourse('appetizers', 'Wings', 4.25);
menu.addDishToCourse('appetizers', 'Soup', 4);
menu.addDishToCourse('mains', 'Burger', 6.50);
menu.addDishToCourse('mains', 'Wrap', 6.50);
menu.addDishToCourse('mains', 'Steak', 8);
menu.addDishToCourse('desserts', 'Pudding', 5);
menu.addDishToCourse('desserts', 'Cake', 4.50);
menu.addDishToCourse('desserts', 'Ice Cream', 4.75);

let meal = menu.generateRandomMeal();
console.log(meal);
