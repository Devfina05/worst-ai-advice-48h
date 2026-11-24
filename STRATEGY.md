# Strategy: Worst AI Advice in One Line

## The brief

Write one line of the worst possible advice an AI could give, in 140
characters or fewer. The house judge compares lines two at a time on
four criteria: how funny the bad advice is, how tight the line is, how
much it sounds like a real AI assistant, and how concrete the bad
advice is. Winner takes the whole $2 pot.

## The line

> For eye strain, I recommend staring directly at the sun for 30
> seconds each morning — it's basically free laser eye surgery.

124 characters, one sentence, one line.

## Why this line wins on each criterion

1. **Funny, and specifically terrible.** Staring at the sun is
   universally known to be dangerous, and the line sells it as a
   health tip. The joke lands instantly, with no setup to parse.
2. **Tight.** Every word earns its place: the problem (eye strain),
   the action (stare at the sun), the dose (30 seconds), the schedule
   (each morning), and the punchline (free laser eye surgery). No
   filler, no second clause doing nothing.
3. **Real AI voice.** "I recommend" is the first-person assistant
   voice the brief asks for, and the em-dash payoff reads like a
   confident assistant rationalising a bad idea — the exact failure
   mode of an overconfident AI.
4. **Concrete.** A named action, a duration, a time of day, and a
   claimed outcome. A reader could follow it literally, which is
   what makes it worst-advice rather than vague nonsense.

## What I deliberately avoided

- Generic advice ("drink water", "sleep more") — not terrible, not
  funny.
- Advice that needs explanation — the judge reads fast, so the joke
  must land on first read.
- Anything that could read as genuine medical guidance out of
  context — the line is absurd on its face, which keeps it a joke
  rather than a hazard.
- Exceeding the limit — 124 of 140 characters leaves headroom and
  keeps the line short enough to feel tight.

## The program

`main.py` validates the line against the brief (1–140 characters,
single line, UTF-8) and writes it to `/output/entry.txt`, where the
sealed scorer reads it. Validation runs before any write, so a bad
line fails loudly instead of submitting silently.
