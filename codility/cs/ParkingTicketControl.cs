using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ParkingTicketControl
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(solution("10:00", "13:01"));
            Console.WriteLine(solution("09:42", "11:42"));
            Console.WriteLine(solution("00:01", "23:59"));
            Console.WriteLine(solution("00:01", "00:02"));
            Console.WriteLine(solution("00:00", "00:59"));
            Console.WriteLine(solution("00:01", "01:00"));
            Console.WriteLine(solution("00:01", "01:01"));
            Console.WriteLine(solution("00:01", "01:02"));
            Console.WriteLine(solution("00:01", "00:01"));
            Console.WriteLine(solution("23:58", "00:00"));
            Console.WriteLine(solution("01:30", "13:40"));
            Console.ReadKey();
        }

        static int solution(string E, string L)
        {
            /*
                Entrance: $2
                First Hour and partial: + $3
                Next Hour and partial: + $4
            */
            DateTime start = DateTime.ParseExact(E, "HH:mm",
                                        System.Globalization.CultureInfo.InvariantCulture);
            DateTime end = DateTime.ParseExact(L, "HH:mm",
                                        System.Globalization.CultureInfo.InvariantCulture);
            TimeSpan diff = (end - start);

            int totalHours = Convert.ToInt32(diff.Hours);
            int partialHour = Convert.ToInt32(diff.Minutes);

            //Console.WriteLine(String.Format("partial: {0}", partialHour));
            //Console.WriteLine(diff);
            //Console.WriteLine(totalHours);

            if (totalHours < 0 || partialHour < 0)
            {
                return 0;
            }
            if (partialHour > 0)
            {
                totalHours++; // integrate partial hour into totalHours
            }

            int totalAmount = 2;
            if (totalHours == 1)
            {
                totalAmount += 3;
            } else if (totalHours > 1)
            {
                totalAmount += 3; // for the first hour
                totalAmount += (totalHours - 1) * 4; // for the successive hours
            }
            return totalAmount;
        }
    }
}
