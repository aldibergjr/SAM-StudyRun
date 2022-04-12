import csv
import os

with open("./jar_generation_for_merge_scenario_commits - New-execution.csv") as study_cases:
    cases = csv.DictReader(study_cases)
    for row in cases:
        link = row["github_link"]
        project_name = row["project"]

        # os.system("git clone "+ link + " ./repositories/"+project_name)
        os.system("./setup.sh ./repositories/" + project_name)

        merge_commit = row["merge_commit"]
        os.system("./repositories/"+project_name+"/.git/hooks/study-post-merge.sh "+ merge_commit + " $PWD/repositories/"+project_name+"/.git/hooks")
        break
