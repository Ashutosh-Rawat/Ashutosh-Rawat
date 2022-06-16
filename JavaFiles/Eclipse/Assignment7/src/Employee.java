public class Employee {
    private String department;
    private Integer salary;
    private String name;

    //getter and setter

    public Employee(String department, Integer salary, String name) {
        this.department = department;
        this.salary = salary;
        this.name = name;
    }
    
    public static void main(String[] args) {
    	Employee e1 = new Employee("A", 5000, "A1");
    	Employee e2 = new Employee("B", 1000, "B1");
    	Employee e3 = new Employee("C", 9000, "C1");
    	Employee e4 = new Employee("C", 10000, "C2");
    	Employee e5 = new Employee("D", 3000, "A3");
    }
}   
