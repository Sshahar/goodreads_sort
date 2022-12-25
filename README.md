# Goodreads Sort
What are the best rated Time Management books?

## Sorting by rating

### Usage Example
``` python ./goodreads_sort.py https://www.goodreads.com/shelf/show/time-management ``` 
```
PS C:\Code\goodreads_sort> python ./goodreads_sort.py https://www.goodreads.com/shelf/show/time-management
Downloading HTML page...
Extracting elements...
Parsing elements...
3.41 What the Most Successful People Do Before Breakfast: A Short Guide to Making Over Your Mornings--and Life (Kindle Edition)
3.61 168 Hours: You Have More Time Than You Think (Hardcover)
3.62 How to Live on 24 Hours a Day (Paperback)
3.72 The Pomodoro Technique (Hardcover)
3.72 I Know How She Does It: How Successful Women Make the Most of Their Time (Hardcover)
3.74 The Power Of Less: The Fine Art of Limiting Yourself to the Essential (Hardcover)
3.75 Indistractable: How to Control Your Attention and Choose Your Life (Hardcover)
3.75 The Time Paradox: The New Psychology of Time That Will Change Your Life (Hardcover)
3.79 When: The Scientific Secrets of Perfect Timing (Hardcover)
3.80 18 Minutes: Find Your Focus, Master Distraction, and Get the Right Things Done (Hardcover)
3.81 Pomodoro Technique Illustrated (Paperback)
3.85 Ready for Anything: 52 Productivity Principles for Getting Things Done (Paperback)
3.87 Eat That Frog!: 21 Great Ways to Stop Procrastinating and Get More Done in Less Time (Paperback)
3.87 The Now Habit: A Strategic Program for Overcoming Procrastination and Enjoying Guilt-Free Play (Paperback)
3.88 Tell Your Time: How To Manage Your Schedule So You Can Live Free (Kindle Edition)
3.90 Smarter Faster Better: The Secrets of Being Productive in Life and Business (Hardcover)
3.91 The 12 Week Year (Nook)
3.91 How to Get Control of Your Time and Your Life (Paperback)
3.91 Manage Your Day-to-Day: Build Your Routine, Find Your Focus, and Sharpen Your Creative Mind (Paperback)
3.91 Hyperfocus: How to Be More Productive in a World of Distraction (Hardcover)
3.92 The 4-Hour Workweek (ebook)
3.92 Making It All Work: Winning at the Game of Work and Business of Life (Hardcover)
3.94 The Productivity Project: Accomplishing More by Managing Your Time, Attention, and Energy (Hardcover)
3.94 Time Warrior: How to defeat procrastination, people-pleasing, self-doubt, over-commitment, broken promises and Chaos (Kindle Edition)
3.94 The One Minute Manager (Hardcover)
3.95 Time Management from the Inside Out: The Foolproof System for Taking Control of Your Schedule--and Your Life (Paperback) 
3.95 Off the Clock: Feel Less Busy While Getting More Done (Kindle Edition)
3.97 The Power of Full Engagement: Managing Energy, Not Time, Is the Key to High Performance and Personal Renewal (Paperback)
3.98 Master Your Time, Master Your Life: The Breakthrough System to Get More Results, Faster, in Every Area of Your Life (Kindle Edition)
4.00 Getting Things Done: The Art of Stress-Free Productivity (Paperback)
4.00 The 80/20 Principle: The Secret to Achieving More with Less (Paperback)
4.01 Organize Tomorrow Today: 8 Ways to Retrain Your Mind to Optimize Performance at Work and in Life (Hardcover)
4.01 Do It Tomorrow and Other Secrets of Time Management (Paperback)
4.03 The Checklist Manifesto: How to Get Things Right (Hardcover)
4.04 Essentialism: The Disciplined Pursuit of Less (Hardcover)
4.04 The Bullet Journal Method: Track the Past, Order the Present, Design the Future (Kindle Edition)
4.07 The Effective Executive: The Definitive Guide to Getting the Right Things Done (Paperback)
4.07 Digital Minimalism: Choosing a Focused Life in a Noisy World (Kindle Edition)
4.08 Make Time: How to Focus on What Matters Every Day (Hardcover)
4.10 First Things First (Paperback)
4.10 Free to Focus: A Total Productivity System to Achieve More by Doing Less (Hardcover)
4.13 The Power of Habit: Why We Do What We Do in Life and Business (Hardcover)
4.13 The One Thing: The Surprisingly Simple Truth Behind Extraordinary Results (Hardcover)
4.13 Time Management (The Brian Tracy Success Library)
4.15 The 7 Habits of Highly Effective People: Powerful Lessons in Personal Change (Paperback)
4.16 Scrum: The Art of Doing Twice the Work in Half the Time (Hardcover)
4.18 10 Natural Laws of Successful Time and Life Management (Paperback)
4.19 Deep Work: Rules for Focused Success in a Distracted World (Hardcover)
4.26 Four Thousand Weeks: Time Management for Mortals (Hardcover)
4.38 Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones (Kindle Edition)
```
### How to improve?
- Add filtering options (minimum votes for rating, minimum rating score)
- Fix duplicated results (```python .\book_ratings.py https://www.goodreads.com/shelf/show/psychology``` has "4.28 Daring Greatly: How the Courage to Be Vulnerable Transforms the Way We Live, Love, Parent, and Lead (Hardcover) twice)
