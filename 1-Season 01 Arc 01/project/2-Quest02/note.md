Great question!

In the exercise my_putstr, the use of my_putchar is intentional and educational. Here's why we use my_putchar instead of printf or putchar:

✅ Reason 1: Exercise Constraint / Educational Purpose
Qwasar (and similar coding bootcamps) often ask you to avoid standard library functions like printf or puts, so that you:

Understand how low-level I/O works in C

Learn to work with system calls like write()

Reinforce understanding of character-by-character processing

✅ Reason 2: Control over Output
Using my_putchar means you're using a custom function (usually backed by write()), which gives you:

Full control over how characters are displayed

Simpler debugging and character-level tracing

A smaller and more deterministic toolset (ideal for learning)

✅ Reason 3: Encourages Reuse
Once my_putchar is defined, you can reuse it in:

my_putstr

my_print_alphabet

my_print_reverse_alphabet

Other future functions

This encourages modular code and function reuse — key software engineering practices.

🧠 Bonus: What does my_putchar do?
c
Copier
Modifier
int my_putchar(char c) {
  return write(1, &c, 1);
}
It uses:

write(1, &c, 1) → low-level system call to write 1 character to stdout (1 is the file descriptor for standard output).

⚠️ Summary:
Method	Uses	Why Avoided in This Exercise
printf	stdio	Too high-level
putchar	stdio	Too easy / not low-level enough
write	syscall	Encouraged via my_putchar
my_putchar	wrapper	Controlled, educational