class Person {
    String name;
    int age;
    String phone;

}

class Student extends Person {
    int RollNo;
    String subject;

    void PrintDetails() {
        System.out.println("Name: "+this.name);
        System.out.println("Age: "+this.age);
        System.out.println("Roll no.: "+this.RollNo);
        System.out.println("Subject: "+this.subject);
        System.out.println("Phone: "+this.phone);
    }

    public Student(String name, int age, int RollNo, String subject, String phone) {
        this.RollNo = RollNo;
        this.subject = subject;
        this.name = name;
        this.age = age;
        this.phone = phone;

        PrintDetails();
    }
    void Study(String subject) {
        System.out.println("Currently studying: "+subject);
    }
}

class Employee extends Person {
    int id;
    int Salary;

    public Employee(String name, int age, int id, int Salary, String phone) {
        this.id = id;
        this.Salary = Salary;
        this.age = age;
        this.name = name;
        this.phone = phone;
    }
}

class FullTimeEmployee extends Employee {

    public float getTotalSalary(int Salary) {
        float HRA = (float).3 * Salary;
        float DA = (float) .2 * Salary;
        float TA = (float) .1 * Salary;
        float PF = (float) .05 * Salary;
        float GS = (float) .12 * Salary;
        float NS = (float) .25 * Salary;
        float TotalSalary;
        TotalSalary = Salary + HRA + DA + TA + GS + NS - PF;
        return TotalSalary;
    }
    public void getDetails() {
        System.out.println("Name : "+this.name);
        System.out.println("Age : "+this.age);
        System.out.println("ID : "+this.id);
        System.out.println("Phone : "+this.phone);
        System.out.println("Salary : "+this.Salary);
        System.out.println("Total Salary : "+getTotalSalary(this.Salary));
    }

    public FullTimeEmployee(String name, int age, int id, int Salary, String phone) {
        super(name, age, id, Salary, phone);
        this.getDetails();
        getTotalSalary(Salary);
    }


}

class PartTimeEmployee extends Employee {
    int TimeBond;

    public float getTotalSalary(int Salary) {
        float HRA = (float).3 * Salary;
        float DA = (float) .2 * Salary;
        float PF = (float) .05 * Salary;
        float GS = (float) .12 * Salary;
        float TotalSalary;
        TotalSalary = Salary + HRA/2 + DA/4 + GS/2 + - PF;
        return TotalSalary;
    }
    public void getDetails() {
        System.out.println("Name : "+this.name);
        System.out.println("Age : "+this.age);
        System.out.println("ID : "+this.id);
        System.out.println("Phone : "+this.phone);
        System.out.println("Salary : "+this.Salary);
        System.out.println("Total Salary : "+getTotalSalary(this.Salary));
        System.out.println("Total Time for Work : "+TimeBond + " yrs");
    }

    public PartTimeEmployee(String name, int age, int id, int Salary, String phone, int TimeBondOfWork) {

        super(name, age, id, Salary, phone);
        this.TimeBond = TimeBondOfWork;
        this.getDetails();
        this.getTotalSalary(Salary);

    }
}

public class Assignment5 {
    public static void main(String[] args) {
        System.out.println("\nStudent Details: ");
        Student student1 = new Student("Aman Rawat", 17,200234, "Mathematics", "83443444");

        System.out.println("\nRegular Employee Details: ");
        FullTimeEmployee regemp = new FullTimeEmployee("Avinash Pandey", 26, 3112, 50000, "8334562");

        System.out.println("\nPart Time Employee Details: ");
        PartTimeEmployee partemp = new PartTimeEmployee("Archit Negi", 24, 100002, 30000, "8154666", 4);
        System.out.println();
    }
}
