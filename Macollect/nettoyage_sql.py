input_file = "collect_clean.sql"
output_file = "collect_clean.sql"

with open(input_file, "r", encoding="utf-8", errors="ignore") as infile:
    sql = infile.read()

sql_cleaned = sql.replace("\\\\", "\")

with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.write(sql_cleaned)

print("✅ Nettoyage terminé : fichier enregistré sous", output_file)
