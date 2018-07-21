using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using IronPython.Hosting;
using Microsoft.Scripting.Hosting;
namespace cPythonDemo2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {

            ScriptEngine engine = Python.CreateEngine();
            ScriptScope scope = engine.CreateScope();

            ScriptSource sSource = engine.CreateScriptSourceFromFile(@"Scripts/cal.py");
            var result = sSource.Execute(scope);
            var calculate = scope.GetVariable<Func<object>>("calcute");
            var instance = calculate();
            var fun = engine.Operations.GetMember<Func<object, object, object>>(instance, "test");
            label1.Text = fun(3,2).ToString();
            //label1.Text = test.ToString();
        }
    }
}
