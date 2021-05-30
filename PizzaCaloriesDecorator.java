/* Task #3 of the Programming Languages course.

@authors
Omer Lev-Ron
Sam Medina 
*/

//  This is a decotrator class for the Pizza object
public abstract class PizzaCaloriesDecorator 
{

	// Class Variables
	protected Pizza pizza;

	//  Constrcutor
	public PizzaCaloriesDecorator(Pizza pizza) 
	{
		this.pizza = pizza;
		calculateCalories();
	}

	// this method calulates the calories of the Pizza instance
	public void calculateCalories() 
	{
		// Declare variables
		int cal = 0; 
		int double_cheese = 1;
		double half_pizza = 1;
		
		// Check if the Pizza is double cheese or not
		if (this.pizza.getIsDoubleCheese()) { double_cheese = 2; }

		// Sum the cheese amount
		switch (this.pizza.getCheese()) 
		{
		case "MOZZARELLA":
			cal += (double_cheese * 280);
			break;
		case "PARMESAN":
			cal += (double_cheese * 431);
			break;
		case "VEGAN_CHEESE":
			cal += (double_cheese * 50);
			break;
		}

		//  Sum the pizza sauce
		switch (this.pizza.getSauce()) 
		{
		case "TOMATOES":
			cal += 20;
			break;
		case "TOMATOES_AND_CREAM":
			cal += 40;
			break;
		case "SPINACH_AND_CREAM":
			cal += 23;
			break;
		case "PESTO":
			cal += 120;
			break;
		}
		
		// Check if the pizza toppings are on half of it
		if (this.pizza.getFullToppings()) { half_pizza = 0.5; }

		// Sum the pizza toppings
		for (String topping : this.pizza.getToppings()) 
		{
			switch (topping) {
			case "OLIVES":
				cal += half_pizza * 115;
				break;

			case "CORN":
				cal += half_pizza * 177;
				break;

			case "TOMATOES":
				cal += half_pizza * 18;
				break;

			case "ONION":
				cal += half_pizza * 40;
				break;

			}
		}

		// Check what dough the Pizza is
		switch (this.pizza.getDough()) 
		{
		case "THICK":
			cal += 5;
			break;
		case "THIN":
			cal += 2;
			break;
		case "WITHOUT_GLUTEN_THICK":
			cal += 10;
			break;
		case "WITHOUT_GLUTEN_SOFT":
			cal += 20;
			break;
		}
		this.pizza.setCalories(cal);
	}

	@Override
	public String toString() 
	{
		String toppingsString = String.join(",", this.pizza.toppings);

		return "**** Pizza description ****" +
		"\nDough: " + this.pizza.dough +
		"\nSauce: " + this.pizza.sauce +
		"\nCheese: " + this.pizza.cheese +
		"\nIs Double Cheese: " + this.pizza.isDoubleCheese +
		"\nFull Toppings: " + this.pizza.fullToppings +
		"\nToppings: " + toppingsString + "\nPizza calories: " + this.pizza.getCalories();
	}
}
