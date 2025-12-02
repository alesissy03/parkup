from app import create_app

# TODO (Task 4): alege config_name corespunzător (ex: "development", "production")
app = create_app(config_name="development")

if __name__ == "__main__":
    # TODO (Task 4): configurează debug / host / port după nevoie
    app.run(debug=True)
