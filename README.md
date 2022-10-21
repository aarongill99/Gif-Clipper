# Gif-Clipper

The idea for the project is to be able to generate new gifs based on a saying or a phrase using movies and subtitle files

1. Text scraper that scrapes text from subtitle files
2. Save all of the matches of text with their times and movie/show names
3. Create a list of a the movies and times (could sort by IMBD rating to get top 10 or 20)
4. Select movies and times from list and cut the clip from the time segment
5. Convert the segment into a gif (Would be more efficient if combined with step 4)
6. overlay the original text onto the gif's
7. Sort and display options

Version 2:
1.Write it in a lower level language to reduce runtime and processing overhead.

Final version:
1. Pre-Process subtitle .srt files into a 2d array{subtitle text, start time, end time, Title} to reduce realtime processing overhead
2. Reduce all video files to 720p-480p to reduce file size and processing time of GIF(if the runtime is still too long we can pre-process the gifs with or without subtitles)

