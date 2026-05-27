namespace ConsoleApp.UI
{
    public static class Options
    {
        // TODO Open/Closed Principle Options is not easily extensible. Consider using enum or a command pattern.
        public const string GetAllSentences = "a";
        public const string DeleteOneSentence = "b";
        // public const string UpdateOne = "c";
        public const string AddNewSentence = "d";
        public const string ExitProgram = "x";
    }
    public class ConsoleUi
    {
        public void PrintMainMenu()
        {
            Request("Choose option and press enter.");

            Console.WriteLine($"{Options.GetAllSentences} - get all sentences");
            Console.WriteLine($"{Options.DeleteOneSentence} - delete sentence by Id");
            //Console.WriteLine("c-editovanie záznamu");
            Console.WriteLine($"{Options.AddNewSentence} - add new sentence");
            Console.WriteLine($"{Options.ExitProgram} - exit program");
            Console.WriteLine();
        }

        public void Request(string message)
        {
            Console.WriteLine();
            Console.WriteLine(message);
            Console.WriteLine();
        }
    }
}