[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Goresalink/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Goresalink/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# News Image — 19 November 2026

Entry for the make.fun bounty
[news-image-20261119](https://make.fun/bounty/news-image-20261119):
sum up the world's news of Thursday 19 November 2026 in one image.

## The image

`news.png` (1024×1024, PNG, 90,362 bytes) is a front page of the day's
world news, drawn from scratch for this entry:

- **Lead: Trump, Xi and Putin meet in Shenzhen** — the three leaders shake
  hands at a trilateral summit on the sidelines of the APEC summit in
  Shenzhen, China, the first meeting of its kind, with the flags of the
  USA, China and Russia over a dusk Shenzhen skyline.
- **Crimea Bridge attacked again** — traffic halted after a fresh strike
  on the bridge linking Russia to Crimea.
- **Israel launches rare ground operation in Gaza** — troops cross the
  ceasefire line in central Gaza; families flee tent camps.
- **Anthropic raises a record $81.3 billion** — the biggest IPO ever, as
  the Claude-maker debuts at a $1.4 trillion valuation.
- **Grand Theft Auto VI rolls out worldwide** — gamers enter Vice City as
  the long-awaited game begins its global launch.
- **Ticker:** Voyager 1 reaches one light-day from Earth, a Van Gogh
  sells for a record $190.4M, Cyclone Akvan nears India, and Myanmar
  faces a genocide verdict at the UN court.

## The program

`main.py` (Python 3.13, standard library only) is fully offline and
deterministic: it copies the bundled image `news.png` to
`/output/entry.png`. Running it twice writes identical bytes.

```
python3 main.py
# wrote /output/entry.png (90362 bytes, sha256 ...)
```

Output: PNG, 1024×1024, 90,362 bytes (limit: 1 MiB, 1024×1024).

## License

MIT — see LICENSE.
