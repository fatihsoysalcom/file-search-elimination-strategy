# File Search Elimination Strategy

This example demonstrates two file search strategies: a traditional linear search and an 'elimination' search. The elimination strategy first quickly discards non-matching files based on simple metadata (like filename parts), significantly reducing the search space before performing a precise match. This illustrates how fast search tools often work by filtering out irrelevant items rather than directly finding the target.

## Language

`python`

## How to Run

1. Save the code as `main.py`.
2. Run from your terminal: `python main.py`

## Original Article

This example accompanies the Turkish article: [Hızlı Dosya Arama: Gerçekten Arıyor mu, Yoksa Uyumsuzlukları mı Kanıtlıyor?](https://fatihsoysal.com/blog/hizli-dosya-arama-gercekten-ariyor-mu-yoksa-uyumsuzluklari-mi-kanitliyor/).

## License

MIT — see [LICENSE](LICENSE).
