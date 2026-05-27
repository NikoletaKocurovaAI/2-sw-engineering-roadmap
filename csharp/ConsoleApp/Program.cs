using ConsoleApp.Services;
using ConsoleApp.UI;
using System;
using System.Threading.Tasks;

// TODO Missing summary/documentation comments in all public classes and methods.

class Program
{
    static async Task Main()
    {
        var sentenceService = new SentenceService();
        await sentenceService.DownloadAsync();

        var consoleUi = new ConsoleUi();
        string userOption = "";

        while (userOption != Options.ExitProgram) {
            consoleUi.PrintMainMenu();

            // TODO Add UI Input Validation if (string.IsNullOrWhiteSpace(input)) { ... }
            userOption = Console.ReadLine();

            if (userOption == Options.GetAllSentences)
            {
                sentenceService.GetAll();
            }
            else if (userOption == Options.AddNewSentence)
            {
                consoleUi.Request("Enter sentence and press enter.");
                string sentence = Console.ReadLine();

                sentenceService.SaveOne(sentence);
            }
            else if (userOption == Options.DeleteOneSentence)
            {
                consoleUi.Request("Enter sentence id and press enter.");
                string sentenceId = Console.ReadLine();

                sentenceService.DeleteOneById(sentenceId);
            }
        }
    }
}
