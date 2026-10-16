from calculator.constants import APP_NAME, APP_VERSION, EXIT_COMMANDS
from calculator.operations import Operations


def main() -> None:
    operations = Operations()

    print(f"{APP_NAME} v{APP_VERSION}")
    print("Operations: +, -, *, /")
    print("Type 'exit' to quit.")

    while True:
        try:
            first = input("\nFirst number: ").strip()

            if first.lower() in EXIT_COMMANDS:
                break

            operator = input("Operator: ").strip()

            if operator.lower() in EXIT_COMMANDS:
                break

            second = input("Second number: ").strip()

            if second.lower() in EXIT_COMMANDS:
                break

            a = float(first)
            b = float(second)

            if operator == "+":
                result = operations.add(a, b)
            elif operator == "-":
                result = operations.subtract(a, b)
            elif operator == "*":
                result = operations.multiply(a, b)
            elif operator == "/":
                result = operations.divide(a, b)
            else:
                print("Unknown operator.")
                continue

            print(f"Result: {result}")

        except ValueError:
            print("Invalid number. Please try again.")
        except ZeroDivisionError as error:
            print(f"Error: {error}")
        except (EOFError, KeyboardInterrupt):
            print("\nExiting calculator.")
            break

    print("Goodbye!")


if __name__ == "__main__":
    main()