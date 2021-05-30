
/* Task #3 of the Programming Languages course.

@authors
Omer Lev-Ron
Sam Medina 
*/

public class Pizza {
	protected String dough;
	protected String sauce;
	protected String cheese;
	protected boolean isDoubleCheese;
	protected boolean fullToppings;
	protected String[] toppings;
	protected int calories = 0;

	public Pizza(String dough, String sauce, String cheese, boolean isDoubleCheese, String[] toppings, boolean fullToppings) {
		this.dough = dough;
		this.sauce = sauce;
		this.cheese = cheese;
		this.isDoubleCheese = isDoubleCheese;
		this.toppings = toppings;
		this.fullToppings = fullToppings;
	}

	@Override
	public String toString() {

		String toppingsString = String.join(",", this.toppings);
		
		return "**** Pizza description ****" +
				"\nDough: " + this.dough +
				"\nSauce: " + this.sauce +
				"\nCheese: " + this.cheese +
				"\nIs Double Cheese: " + this.isDoubleCheese +
				"\nFull Toppings: " + this.fullToppings +
				"\nToppings: " + toppingsString + "\nPizza calories: " + this.calories;
	}

	public String getDough() {
		return dough;
	}

	public void setDough(String dough) {
		this.dough = dough;
	}

	public String getSauce() {
		return sauce;
	}

	public void setSauce(String sauce) {
		this.sauce = sauce;
	}

	public String getCheese() {
		return cheese;
	}

	public void setCheese(String cheese) {
		this.cheese = cheese;
	}

	public boolean getIsDoubleCheese() {
		return this.isDoubleCheese;
	}

	public void setIsDoubleCheese(boolean isDoubleCheese) {
		this.isDoubleCheese = isDoubleCheese;
	}

	public boolean getFullToppings() {
		return this.fullToppings;
	}

	public void setFullToppings(boolean fullToppings) {
		this.fullToppings = fullToppings;
	}

	public String[] getToppings() {
		return toppings;
	}

	public void setToppings(String[] toppings) {
		this.toppings = toppings;
	}

	public int getCalories() {
		return calories;
	}

	public void setCalories(int calories) {
		this.calories = calories;
	}

	public static void main(String[] args) {
		// Declare Toppings
		String[] topping_1 = { "CORN" };
		
		// Create Pizza
		Pizza pizza = new Pizza("WITHOUT_GLUTEN_THICK", "SPINACH_AND_CREAM", "VEGAN_CHEESE", false,  topping_1, false);
		PizzaCaloriesDecorator pizza2 = new PizzaCaloriesDecorator(pizza) {};
		System.out.println(pizza2);

	}
}
