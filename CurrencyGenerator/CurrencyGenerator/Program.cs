using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CurrencyGenerator
{
    class Program
    {
        public static string url = "https://www.sberometer.ru/cbr/";
        public static string userAgent = "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0";
        public static double output = 0;
        public static Random r = new Random();
        public static double[] rates = { 
		64.9940, 65.2170, 64.9737, 64.8102, 65.0539, 64.1617, 63.9730, 64.3804, 64.8306, 64.7644 
	};
        public static void Wait(WebBrowser browser)
        {
            while (browser.ReadyState != WebBrowserReadyState.Complete)
                Application.DoEvents();
        }
        public static void Parser()
        {
            /*WebBrowser pars = new WebBrowser();
            pars.ScriptErrorsSuppressed = true;
            Console.WriteLine("Start");
            pars.Navigate(url, null, null, userAgent);
            Wait(pars);
            Console.WriteLine(pars.Url);
            HtmlElementCollection _A = pars.Document.GetElementsByTagName("A");
            foreach (HtmlElement tile in _A)
            {
                if (tile.GetAttribute("className") == "b lr")
                {
                    Console.WriteLine(k);
                    string[] values = new string[31];
                    output = Math.Round(Convert.ToDouble((tile.InnerText).Replace(".", ",")), 4);
                    values[0] = Convert.ToString(output);
                    for (int i = 1; i < values.Length; i++)
                    {
                        values[i] = Convert.ToString(output + Math.Round(0.4 * (r.NextDouble() - 0.5), 4));
                    }
                    System.IO.File.WriteAllLines(@"C:\UniFins\values" + (k / 3 + 1) + ".json", values);
                }
            }*/
            for (int i = 0; i < rates.Length; i++)
            {
                string[] values = new string[31];
                output = Math.Round(rates[i], 4);
                values[0] = Convert.ToString(output);
                for (int j = 1; j < values.Length; j++)
                {
                    values[j] = Convert.ToString(output + Math.Round(0.4 * (r.NextDouble() - 0.5), 4));
                }
                System.IO.File.WriteAllLines(@"C:\UniFins\values" + (i + 1) + ".json", values);
            }
        }
        [STAThread]
        static void Main(string[] args)
        {
            Parser();
            Console.WriteLine("Done");
            Console.ReadKey();
        }
    }
}
