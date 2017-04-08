using System;
using System.Collections.Generic;

namespace MaxAbsPair
{
    class Program
    {
        static void Main(string[] args)
        {
            //simpleSolution();
            StressTest();

            Console.ReadKey();
        }

        static void simpleSolution()
        {
            List<int> my_list = new List<int>();
            my_list.Add(1);
            my_list.Add(3);
            my_list.Add(-3);

            List<int> my_list2 = new List<int>();
            my_list2.Add(4);
            my_list2.Add(3);
            my_list2.Add(2);
            my_list2.Add(5);
            my_list2.Add(1);
            my_list2.Add(1);

            Console.WriteLine(solution(my_list.ToArray()));
            Console.WriteLine();
            Console.WriteLine(solution(my_list2.ToArray()));
            Console.WriteLine();
        }

        static int solution(int[] A)
        {
            int k = 0;
            bool nonPair = A.Length % 2 == 0;
            if (nonPair)
            {
                k = A.Length / 2;
            } else
            {
                k = (A.Length / 2) + 1;
            }
            //Console.WriteLine(k);

            int maxA = A[0];
            int maxK = A[k+0-1];

            for (int i = 1; i < k; i++)
            {
                int abs_first = Math.Abs(maxA - A[i]);
                if (abs_first > maxA)
                {
                    maxA = abs_first;
                }

                int abs_second = Math.Abs(maxK - A[k+i-1]);

                if (abs_second > maxK)
                {
                    maxK = abs_second;
                }
            }
            return Math.Max(maxA, maxK);
        }

        static void StressTest()
        {
            var rand = new Random();
            int N = 16;
            var max_size = 1;

            for (int i = 0; i < N+1; i++)
            {
                max_size *= 2;
                List<int> my_list = new List<int>();
                Console.WriteLine(String.Format("it: {0} - size: {1}", i, max_size));

                for (int j = 0; j < max_size; j++)
                {
                    var value = rand.Next(-1000000000, 1000000000);
                    my_list.Add(value);
                }

                var watch = System.Diagnostics.Stopwatch.StartNew();
                int result = solution(my_list.ToArray());
                watch.Stop();
                Console.WriteLine(String.Format("solution time: {0} result:{1}", watch.Elapsed, result));
            }
        }
    }
}
