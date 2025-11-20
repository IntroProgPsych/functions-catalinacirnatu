# Write a function describe_number(n) that:

# returns “positive” if n > 0

# returns “zero” if n == 0

# returns “negative” if n < 0

# Ask the user for a number, call the function, and print the message.*

# Write your code here:
def describe_number(n):
	"""Return a string describing whether n is positive, zero, or negative."""
	if n > 0:
		return "positive"
	if n == 0:
		return "zero"
	return "negative"


def main():
	try:
		s = input("Enter a number: ")
		n = float(s)
	except ValueError:
		print("Invalid number")
		return

	print(describe_number(n))


if __name__ == "__main__":
	main()
