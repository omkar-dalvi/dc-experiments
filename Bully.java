import java.io.*;
import java.util.Scanner;

class Bully {
  static int n;
  static int status[] = new int[100];
  static int priority[] = new int[100];
  static int co;

  public static void main(String args[]) throws IOException {
    Scanner sc;
    System.out.println("Enter the number of process");
    sc = new Scanner(System.in);
    Scanner in = new Scanner(System.in);
    n = in.nextInt();
    int i;

    System.out.println("Enter the status of each process (Space-seperated)");
    for (i = 0; i < n; i++) {
      status[i] = sc.nextInt();
    }
    System.out.println("Enter the priority of each process (Space-seperated)");
    for (i = 0; i < n; i++) {
      priority[i] = sc.nextInt();
    }

    System.out.println("Which process will initiate election?");
    int ele = in.nextInt();

    elect(ele);
    System.out.println("Final coordinator is " + co);

  }

  static void elect(int ele) {
    ele = ele - 1;
    co = ele + 1;
    for (int i = 0; i < n; i++) {
      if (priority[ele] < priority[i]) {
        System.out.println("Election message is sent from " + (ele + 1) + " to " + (i + 1));
        if (status[i] == 1)
          elect(i + 1);
      }
    }
  }
}
