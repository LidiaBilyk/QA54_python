from pathlib import Path

data_folder = Path("data_test")
file_path = data_folder / "report.txt"
print(file_path)

print(file_path.exists())

screen_folder = Path("screen")
screen_folder.mkdir(exist_ok=True)
reports_folder = Path("reports")/"october"
reports_folder.mkdir(parents=True, exist_ok=True)




def create_reports_folder():
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)
    results_file = reports_dir/"result.txt"
    with open(results_file,"w",encoding="utf-8") as file:
        file.write("Homework completed successfully!")

create_reports_folder()