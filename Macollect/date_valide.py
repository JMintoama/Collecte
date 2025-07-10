import sqlite3

# Ouvre la base
conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

# Dictionnaire des tables et des colonnes à corriger
date_columns = {
    "collecte": ["datsaisi_c"],
    "edition": ["date_edition"],
    "fournit": ["date_reception"],
    "indexation": ["dat_reception"],
    "suivi": ["datenvoi_t"],
    "vue": ["dat_ctrl"],
    "control": ["dat_ctrl"],
}

default_date = "2000-01-01"

print("🔎 Vérification des dates invalides dans toutes les tables...\n")

for table, columns in date_columns.items():
    for col in columns:
        # Compter les lignes avec une date invalide
        cursor.execute(f"SELECT COUNT(*) FROM {table} WHERE {col} = '0000-00-00'")
        count = cursor.fetchone()[0]

        if count > 0:
            print(f"⚠️  {count} dates invalides dans '{table}.{col}'")

            try:
                # Remplacer par une date par défaut (acceptable par Django)
                cursor.execute(f"""
                    UPDATE {table}
                    SET {col} = ?
                    WHERE {col} = '0000-00-00'
                """, (default_date,))
                print(f"✅ Correction dans {table}.{col}")
            except sqlite3.IntegrityError as e:
                print(f"❌ Erreur table {table} : {e}")

print("\n🎉 Correction terminée.")
conn.commit()
conn.close()
