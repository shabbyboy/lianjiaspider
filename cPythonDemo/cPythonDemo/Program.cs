using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using IronPython.Hosting;
using Microsoft.Scripting.Hosting;

namespace cPythonDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            //try
            //{
            //    ScriptEngine engine = Python.CreateEngine();
            //    ScriptScope scope = engine.CreateScope();
            //    Student stu = new Student { Name = "Wilber", Age = 28 };
            //    scope.SetVariable("stuObj", stu);
            //    ScriptSource script = engine.CreateScriptSourceFromFile(@"PrintStuInfo.py");

            //    var result = script.Execute(scope);

            //}
            //catch (Exception e)
            //{
            //    Console.WriteLine(e.Message);
            //}

            //Console.Read();

            try
            {
                ScriptEngine engine = Python.CreateEngine();
                ScriptScope scope = engine.CreateScope();

                ScriptSource script = engine.CreateScriptSourceFromFile(@"Script.py");

                var result = script.Execute(scope);
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }

            Console.Read();
        }
    }


    public class Student
    {
        public int Age { get; set; }
        public string Name { get; set; }
        public override string ToString()
        {
            return string.Format("{0} is {1} years old", this.Name, this.Age);
        }
    }
}
