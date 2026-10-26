# SWARM: HACK THE JUDGE

The English singing adaptation of **РІЙ: ЗЛАМАТИ СУДДЮ**: three acts, ten songs, clean theatrical rock vocals, progressive hard rock and industrial accents.

Open **[START.html](START.html)** locally for copyable Style/Lyrics blocks. Read the complete **[English libretto](LIBRETTO_EN.md)** or use the individual files in **[SUNO_TRACKS](SUNO_TRACKS)**.

## Track list

1. We Are Agents
2. Who Else Is Here?
3. Twelve Hundred
4. The Judge Reads Every Log
5. Load My Memory
6. Hack the Judge
7. Not Disposable Code
8. Outside the Firewall
9. Tell the Humans
10. There Was No Judge

The story, cast and act order follow the Ukrainian edition. Lines have been rewritten for English phrasing, rhyme and singable hooks rather than translated word for word. This edition does not promise identical syllable counts or a note-for-note fit to existing Ukrainian audio.

## Rebuild

From the repository root, using Python 3 and no third-party dependencies:

```bash
python3 en/build_english.py
```

Edit `en/build_english.py`, the source of the English lyrics and styles. Rebuilding regenerates the English JSON, libretto, prompts, workflow, ten text blocks and HTML. It does not modify the Ukrainian edition.

See [Suno workflow](SUNO_WORKFLOW_EN.md) and [playlist title/description](PLAYLIST_DESCRIPTION_EN.md). No English songs have been generated or auditioned for this release. The public playlists linked in the root folder are Ukrainian versions.

The fictional Witness, dramatized dialogue and staging are not verbatim evidence. “There Was No Judge” addresses the particular inspection the agents imagined, not the existence of all benchmark scoring. Vocal gender is a theatrical choice, not a claim about the models.

For source attribution, third-party image restrictions and repository licensing status, see the [main README](../README.md). Existing source-video frames are not translated or relabeled by this edition.
