// TODO Implement DIP - SentenceService should depend on ISentenceRepository
using ConsoleApp.Repositories;
using System.Net.Http;
using System.Threading.Tasks;

namespace ConsoleApp.Services
{
    internal class DataDownloadingClient
    {
        private static readonly Lazy<HttpClient> lazyClient = new Lazy<HttpClient>(() => new HttpClient());
        private static HttpClient Client => lazyClient.Value;

        internal async Task<string> DownloadStringAsync(string url)
        {
            return await Client.GetStringAsync(url);
        }
    }

    public class SentenceService
    {
        // TODO SRP: SentenceService does downloading, parsing, and IO. Should be split: SentenceDownloader, SentenceParser, SentenceService (orchestrates)

        private const string Url = "https://mvi.mechatronika.cool/sites/default/files/berces.html";
        private readonly SentenceRepository repo = new();

        public async Task DownloadAsync()
        {
            var httpClient = new DataDownloadingClient();
            string content = await httpClient.DownloadStringAsync(Url);
            string[] sentences = content.Split(".", StringSplitOptions.RemoveEmptyEntries);

            foreach (var sentence in sentences)
            {
                if (!string.IsNullOrWhiteSpace(sentence))
                {
                    _ = repo.SaveOne(sentence);
                }
            }
        }

        public void SaveOne(string sentence)
        {
            var entry = repo.SaveOne(sentence);
        }

        public void GetAll() 
        {
            var sentences = repo.GetAll();
            foreach (var sentence in sentences)
            {
                Console.WriteLine($"Id: {sentence.Id}");
                Console.WriteLine($"Text: {sentence.Text}");
                // Console.WriteLine($"Author: {sentence.Author}");
            }
        }

        public void DeleteOneById(string id)
        {
            if (Guid.TryParse(id, out Guid parsedId))
            {
                Guid? deleted_id = repo.DeleteOneById(parsedId);

                if (deleted_id.HasValue)
                {
                    Console.WriteLine($"Deleting sentence with id: {deleted_id}");
                }
            }
            else
            {
                Console.WriteLine("Invalid GUID format.");
            }
        }

        // UpdateOne()
    }
}
