class Vehicle {
    int count;
}

public class Car extends Vehicle {
    int count;

    Car() {
        this.count = 5;
        super.count = 3;
        System.out.println(this.count);
        System.out.println(super.count);
    }
    public static void main(String[] args) {
        Car Tesla = new Car();
    }

}
