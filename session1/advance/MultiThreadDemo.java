package session1.advance;

// thread using Thread class 
class MyThread extends Thread {

    public void run() {
        for (int i = 1; i <= 3; i++) {
            System.out.println("Thread 1: " + i);
        }
    }
}

// thread using Runnable and Thread class
class MyRunnable implements Runnable {

    public void run() {
        for (int i = 1; i <= 3; i++) {
            System.out.println("Thread 2: " +  i);
        }

    }

}

public class MultiThreadDemo {

    public static void main(String[] args) {
   // creating instances of MyThread and MyRunnable and starting the threads
        MyThread t1 = new MyThread();
        Thread t2 = new Thread(new MyRunnable());

        t1.start();
        t2.start();
    }
}