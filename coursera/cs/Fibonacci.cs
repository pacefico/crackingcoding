using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication
{
    class FibonacciHuge
    {
        static void Main(string[] args)
        {
            //StressTest();
            ManualTest();

            Console.ReadKey();
        }


        static void ManualTest()
        {
            var input_a = Console.ReadLine();

            double result = calc_fib_mod(int.Parse(input_a));

            Console.WriteLine(String.Format("{0}", result % 10));
        }

        static void StressTest()
        {

            var rand = new Random();
            
            var N = 240;
            for (int i =3; i < N; i++)
            {
                var watch = System.Diagnostics.Stopwatch.StartNew();

                double result2 = calc_fib_mod(i);
                double last_digit = result2 % 10;
                watch.Stop();
                var elapsedMs = watch.Elapsed;
                Console.WriteLine(String.Format("it: {0} calc_fib_mod({1})={2} time: {3} last: {4}", i, i, result2, elapsedMs, last_digit));
            }
          
        }

        static float calc_fib(int n)
        {
            if (n <= 1)
            {
                return n;
            }
            return calc_fib(n - 1) + calc_fib(n - 2);
        }

        static double calc_fib_faster(int n)
        {
            if (n <= 1)
            {
                return n;
            }
            double n0 = 0;
            double n1 = 1;
            double r = 0;

            for (int i = 1; i < n; i++)
            {
                r = n0 + n1;
                n0 = n1;
                n1 = r;
            }
            return r;
        }

        static double calc_fib_mod(int n)
        {
            if (n <= 1)
            {
                return n;
            }
            double n0 = 0;
            double n1 = 1;
            double r = 0;

            for (int i = 1; i < n; i++)
            {
                r = (n0 % 10) + (n1 % 10);
                n0 = n1;
                n1 = r;
            }
            return r;
        }
    }

   
}
