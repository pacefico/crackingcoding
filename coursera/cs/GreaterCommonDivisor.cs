using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication
{
    class GreaterCommonDivisor
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

            var numbers = input_a.Split(' ');

            int a = int.Parse(numbers[0]);
            int b = int.Parse(numbers[1]);

            Console.WriteLine(LCD(a, b));
        }

        static int GCDNaive(int a, int b)
        {
            int current = 1;
            for (int d = 2; d < Math.Min(a, b) + 1; d++)
            {
                if ((a % d == 0) && (b % d == 0))
                {
                    if (d > current)
                    {
                        current = d;
                    }
                }
            }
            return current;
        }

        static double GCDNaiveBig(int a, int b)
        {
            double current = 1;
            for (double d = 2; d < Math.Min(a, b) + 1; d++)
            {
                if ((a % d == 0) && (b % d == 0))
                {
                    if (d > current)
                    {
                        current = d;
                    }
                }
            }
            return current;
        }

        static long LCD(long a, long b)
        {
            return (a * b) / GCDLemma(a, b);
        }

        static long GCDLemma(long a, long b)
        {
            if (b == 0)
            {
                return a;
            }
            return GCDLemma(b, a % b);
        }

        static void StressTest()
        {
            var rand = new Random();
            int N = 1000;
            
            int min_value = 1;
            for (int i = 0; i < N; i++)
            {
                min_value *= 2;
                Console.WriteLine(String.Format("it: {0} min:{1}", i, min_value));

                var a = rand.Next(1, 1000000000);
                var b = rand.Next(1, 1000000000);

                Console.WriteLine(String.Format("a:{0}, b:{1}", a, b));

                var watch = System.Diagnostics.Stopwatch.StartNew();
                double result = LCD(a, b);
                watch.Stop();
                Console.WriteLine(String.Format("LCD time: {0} result:{1}", watch.Elapsed, result));

            }
        }
    }
}
