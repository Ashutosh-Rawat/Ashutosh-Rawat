public class Employee {
    private static String id;
    private static String name;
    private static int BasicSalary;
    private static String CompanyName;

    Employee() {
        CompanyName = "TESLA Cars";
    }
    Employee(String id, String name, int Salary) {
        this();
        this.id = id;
        this.name = name;
        this.BasicSalary = Salary;
    }

    public static void setBasicSalary(int basicSalary) {
        BasicSalary = basicSalary;
    }

    public static void GeneratePayslip() {
        float HRA, DA, TA, PF, GS, NS;
        float TotalSalary;
        HRA = (float).3 * BasicSalary;   // HRA is 30%
        DA = (float) .2 * BasicSalary;   // Dearness Allowance is 20%
        TA = (float) .1 * BasicSalary;   // Travel Allowance is 10%
        PF = (float) .05 * BasicSalary;  // Provident Fund deduction is 5%
        GS = (float) .12 * BasicSalary;  // General Shift allowance is 12%
        NS = (float) .25 * BasicSalary;  // Night shift allowance is 25%

        TotalSalary = BasicSalary + HRA + DA + TA + GS + NS -PF;
        System.out.println("\t\t\t\t\t\t\t "+CompanyName);
        System.out.println("\n Payslip for the month of January, 2022");
        System.out.println("______________________________________________________________________");
        System.out.println("Personal Details: ");
        System.out.println("Name: "+name);
        System.out.println("ID: "+id);
        System.out.println("______________________________________________________________________");
        System.out.println("Earnings: ");
        System.out.println("Basic "+BasicSalary+"\t\t\t\t HRA: "+HRA);
        System.out.println("DA: "+DA+"\t\t\t\t\t TA: "+TA);
        System.out.println("GS: "+GS+"\t\t\t\t\t NS: "+NS);
        System.out.println("\nDeductions: ");
        System.out.println("PF: "+PF);
        System.out.println("______________________________________________________________________");
        System.out.println("Total Salary: "+TotalSalary);
    }
    public static void main(String[] args) {
        String name = "Ashish Sati";
        String id = "13325";
        int Salary = 100000;
        Employee E1 = new Employee(id, name, Salary);
        E1.GeneratePayslip();
    }
}
