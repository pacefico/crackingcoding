using System;
using System.Collections.Generic;

namespace MaxParWise
{
    class Program
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
            var input_b = Console.ReadLine();

            var numbers = input_b.Split(' ');

            int[] n_int = Array.ConvertAll(numbers, int.Parse);
            int size = Convert.ToInt32(input_a);

            if (size != n_int.Length)
            {
                throw new Exception("error");
            }

            //ProductPairWise(size, n_int);
            ProductPairWiseFaster(size, n_int);
        }


        static void StressTest()
        {
            var rand = new Random();
            int N = 16;
            var max_size = 1;

            for (int i = 0; i < N; i++)
            {
                max_size *= 2;
                List<int> my_list = new List<int>();
                Console.WriteLine(String.Format("it: {0} - size: {1}", i, max_size));

                for (int j = 0; j < max_size; j++)
                {
                    var value = rand.Next(2, 99999);
                    my_list.Add(value);
                }

                var watch = System.Diagnostics.Stopwatch.StartNew();
                
                double result2 = ProductPairWiseFaster(my_list.Count, my_list.ToArray());
                watch.Stop();
                var elapsedMs = watch.Elapsed;
                Console.WriteLine(String.Format("ProductPairWiseFaster time: {0}", elapsedMs));

                watch.Reset();
                watch.Restart();
                double result1 = ProductPairWise(my_list.Count, my_list.ToArray());
                watch.Stop();
                elapsedMs = watch.Elapsed;
                Console.WriteLine(String.Format("ProductPairWise time: {0}", elapsedMs));

                if (result1 != result2)
                {
                    Console.WriteLine("Wrong solution...");
                    Console.WriteLine(String.Format("result1:{0} result2:{1}", result1, result2));
                    break;
                }
            }
        }

        static double ProductPairWise(int size, int[] n_int)
        {
            double result = 0;

            for (int i = 0; i < size; i++)
            {
                for (int j = i + 1; j < size; j++)
                {
                    var a = (double)n_int[i];
                    var b = (double)n_int[j];
                    if (a * b > result)
                    {
                        result = a * b;
                    }
                }
            }
            Console.WriteLine(result);
            return result;
        }
        
        static double ProductPairWiseFaster(int size, int[] n_int)
        {
            int max_i_1 = -1;
            int max_i_2 = -1;

            for (int i = 0; i < size; i++)
            {
                if ((max_i_1 == -1) || (n_int[i] > n_int[max_i_1]))
                {
                    max_i_1 = i;
                }
            }

            for (int j = 0; j < size; j++)
            {
                if ((j != max_i_1) && ((max_i_2 == -1) || n_int[j] > n_int[max_i_2]))
                {
                    max_i_2 = j;
                }
            }

            double result = (double)n_int[max_i_1] * (double)n_int[max_i_2];
            
            Console.WriteLine(result);
            return result;
        }

    }
}