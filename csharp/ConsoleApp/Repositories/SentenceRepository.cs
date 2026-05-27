using ConsoleApp.Models;

namespace ConsoleApp.Repositories
{
    public class SentenceRepository
    {
        private readonly List<SentenceEntry> storage = new();

        public SentenceEntry SaveOne(string sentence)
        {
            var entry = new SentenceEntry
            {
                Id = Guid.NewGuid(),
                Text = sentence.Trim(),
                // Author = author
            };
            storage.Add(entry);
            return entry;
        }

        public List<SentenceEntry> GetAll()
        {
            return storage;
        }

        public Guid? DeleteOneById(Guid Id) 
        {
            // TODO This is O(n) for each delete. Consider Dictionary<Guid, SentenceEntry> for O(1) lookup.
            var entry = storage.FirstOrDefault(e => e.Id == Id);

            if (entry != null)
            {
                storage.Remove(entry);
                return entry.Id;
            }
            return null;
        }
    }
}