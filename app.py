from chains.sql_chain import run_query

def main():
    print("Ask your database anything (type 'exit' to quit):")
    while True:
        user_input = input(" > ")
        if user_input.lower() in ["exit", "quit"]:
            break
        try:
            response = run_query(user_input)
            print("🤖:", response)
        except Exception as e:
            print(" Error:", e)

if __name__ == "__main__":
    main()
