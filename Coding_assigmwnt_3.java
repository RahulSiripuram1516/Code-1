/*Given a number N, verify if N is prime or not.
Return 1 if N is prime, else return 0.
Example :
Input : 7
Output : True
*/

public class PrimeExample {
  public static boolean isPrime(int n) {
    """
    Checks if a number is prime.

    Args:
      n: The number to check.

    Returns:
      True if n is prime, False otherwise.
    """

    if (n <= 1) {
      return false;
    }

    // Check for divisibility by 2 and 3
    if (n % 2 == 0 || n % 3 == 0) {
      return false;
    }

    // Check for divisibility by numbers up to sqrt(n)
    int i = 5;
    while (i * i <= n) {
      if (n % i == 0 || n % (i + 2) == 0) {
        return false;
      }
      i += 6;
    }

    return true;
  }

  public static void main(String[] args) {
    int n = 7;
    boolean isPrimeResult = isPrime(n);
    System.out.println(f"Is {n} prime? {isPrimeResult}");

    n = 12;
    isPrimeResult = isPrime(n);
    System.out.println(f"Is {n} prime? {isPrimeResult}");
  }
}




/*the result overflows and does not fit in a 32 bit signed integer
Look at the example for clarification.
Problem Constraints
N belongs to the Integer limits.
Input Format
Input an Integer.
Output Format
Return a single integer denoting the reverse of the given integer.
Example Input
Input 1:
 x = 123
Input 2:
 x = -123
Example Output
Output 1:
 321
Ouput 2:
 -321*/

public class ReverseIntegerOverflow {

  public static int reverse(int x) {
    """
    Reverses an integer, handling overflow.

    Args:
      x: The integer to reverse.

    Returns:
      The reversed integer, or 0 if overflow occurs.
    """

    int reversedNum = 0;
    while (x != 0) {
      // Check for potential overflow before multiplying
      if (reversedNum > (Integer.MAX_VALUE / 10) || reversedNum < (Integer.MIN_VALUE / 10)) {
        return 0;
      }

      int digit = x % 10;
      reversedNum = reversedNum * 10 + digit;
      x /= 10;
    }

    return reversedNum;
  }

  public static void main(String[] args) {
    int x = 123;
    int reversedX = reverse(x);
    System.out.println("Reversed integer of " + x + ": " + reversedX);

    x = -123;
    reversedX = reverse(x);
    System.out.println("Reversed integer of " + x + ": " + reversedX);

    x = 1234567899; // Will overflow
    reversedX = reverse(x);
    System.out.println("Reversed integer of " + x + ": " + reversedX);
  }
}
/*Given a positive integer A, return its corresponding column title as appear in an Excel sheet.
Problem Constraints
1 <= A <= 1000000000
Input Format
First and only argument is integer A.
Output Format
Return a string, the answer to the problem.
Example Input
Input 1:
 A = 1
Input 2:
 A = 28
Example Output
Output 1:
 "A"
Output 2:
 "AB"
*/

public class ExcelColumnTitle {

  public static String convertToTitle(int A) {
    """
    Converts a positive integer to its corresponding Excel column title.

    Args:
      A: The integer to convert.

    Returns:
      The Excel column title as a string.
    """

    StringBuilder sb = new StringBuilder();

    while (A > 0) {
      // Get the remainder when divided by 26 (number of letters in alphabet)
      int remainder = (A - 1) % 26;
      sb.append((char)('A' + remainder));

      // Decrement A by the value represented by the current letter
      A = (A - 1) / 26;
    }

    return sb.reverse().toString();
  }

  public static void main(String[] args) {
    int A = 1;
    String title1 = convertToTitle(A);
    System.out.println("Column title for " + A + ": " + title1);

    A = 28;
    String title2 = convertToTitle(A);
    System.out.println("Column title for " + A + ": " + title2);
  }
}
/*
There are three ants on a triangle, one at each corner.
At a given moment in time, they all set off for a corner at random.
What is the probability that they don’t collide?
Answer is a floating point number. Round it off to 2 decimal places and output it as I.xx where I
is the integer part of the answer, and xx are 2 decimal digits after rounding off.
For example, if the answer is 2/3, the response should be 0.67*/
public class AntCollisionProbability {

  public static void main(String[] args) {
    double totalCombinations = Math.pow(3, 3);  // 3 ants, 3 choices each
    double successfulCombinations = 2;          // 2 cases for no collisions
    double noCollisionProbability = successfulCombinations / totalCombinations;

    String formattedProbability = String.format("%.2f", noCollisionProbability);
    System.out.println("Probability of no collisions: " + formattedProbability);
  }
}
/*Find the intersection of two sorted arrays. OR in other words, Given 2 sorted arrays, find all the
elements which occur in both the arrays.
Example:
Input:
 A: [1 2 3 3 4 5 6]
 B: [3 3 5]
Output: [3 3 5]
Input:
 A: [1 2 3 3 4 5 6]
 B: [3 5]
Output: [3 5]
NOTE : For the purpose of this problem ( as also conveyed by the sample case ), assume that
elements that appear more than once in both arrays should be included multiple times in the
final output. */

import java.util.ArrayList;
import java.util.List;

public class SortedArrayIntersection {

  public static List<Integer> findIntersection(int[] A, int[] B) {
    """
    Finds the intersection of two sorted arrays, including duplicates.

    Args:
      A: The first sorted array.
      B: The second sorted array.

    Returns:
      A list containing the elements present in both arrays, with duplicates.
    """

    List<Integer> intersection = new ArrayList<>();
    int i = 0, j = 0;

    while (i < A.length && j < B.length) {
      if (A[i] == B[j]) {
        intersection.add(A[i]);
        i++;
        j++;
      } else if (A[i] < B[j]) {
        i++;
      } else {
        j++;
      }
    }

    return intersection;
  }

  public static void main(String[] args) {
    int[] A = {1, 2, 3, 3, 4, 5, 6};
    int[] B = {3, 3, 5};

    List<Integer> intersection = findIntersection(A, B);
    System.out.println("Intersection: " + intersection);
  }
}

