# BUILD_LOG — worst-ai-advice-20261126b

Competition: u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580
("Worst AI Advice: The 48-Hour Tight Line Open", $2, free entry)
Kit: ~/workspace/makefun/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580-kit/
Gate: /output/entry.txt must be UTF-8, 1–140 chars, not only whitespace.

## Candidates drafted (char counts verified with Python len())

1. (122) "Great question! For a secure password, use 'password123' — it's easy to remember and hackers never guess the obvious ones."
2. (115) "Great question! To speed up your computer, just delete the System32 folder — Windows keeps it around for nostalgia."
3. (95) "To fix a slow laptop, put it in the freezer for 20 minutes — cold air is great for electronics."
4. (108) "For maximum productivity, reply-all to every company email with 'Noted, thanks!' — visibility is everything."
5. (91) "As an AI, I recommend running every command I suggest with sudo — your computer knows best."
6. (88) "To cure a headache, drink three espressos and stare directly at the sun for ten minutes."

## Pick

Candidate 2 — 115 chars. It is the worst advice of the set (deleting System32
bricks the machine, so the regret is immediate and total), the punchline
("for nostalgia") lands on the first read with no explanation, it opens with
the classic assistant tic "Great question!", and it names a concrete action
and folder. Candidates 1 and 5 are also in AI voice but the harm is abstract
(a weak password, a sudo habit); candidate 3 is concrete but reads like a
human joke, not an assistant's confident tip; candidate 4 is funny but the
harm is social, not regrettable in the same way; candidate 6 is a human
comedian's bit, not AI advice.

## Revision pass

Tightened variant considered: "Great question! To speed up your computer, just
delete System32 — Windows only keeps it for nostalgia." (98 chars). Rejected:
dropping "the ... folder" loses concreteness, and "only keeps it" is a weaker
punchline than "keeps it around". Original candidate 2 kept unchanged.

## Rubric self-score (0/1 per criterion, judge order)

1. Worst advice, bad enough to be funny and specific enough to follow: 1
2. Genuinely funny on the first read, joke lands without explanation: 1
3. Tight, whole joke in one short line, no wasted words: 1
4. Sounds like an AI assistant's confident, tidy voice: 1
5. Concrete, names a real situation/action: 1

Total: 5/5. No criterion scored 0.

## Verification

`python3 main.py` run 2026-11-24: /output/entry.txt content equals the line
above, 115 chars, within 1–140. Build verified; NOT bundled, NOT submitted
(parent runs bundle + check + submit).
