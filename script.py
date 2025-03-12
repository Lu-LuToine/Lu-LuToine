import requests

# Ton nom d'utilisateur GitHub
GITHUB_USERNAME = "Lu-LuToine"

# URL de l'API GitHub
API_URL = f"https://api.github.com/users/{GITHUB_USERNAME}"

# Récupération des données
response = requests.get(API_URL)
if response.status_code == 200:
    data = response.json()
    name = data.get("name", GITHUB_USERNAME)  # Si le nom n'est pas défini, on affiche le pseudo
    bio = data.get("bio", "Aucune bio disponible.")
    public_repos = data.get("public_repos", 0)
    followers = data.get("followers", 0)
    following = data.get("following", 0)
    profile_pic = data.get("avatar_url", "")

    # Générer le README.md
    readme_content = f"""
# 👋 Hello, je suis {name} !

![Avatar]({profile_pic})

{bio}

📌 **Infos GitHub**  
- 🔗 [Profil GitHub](https://github.com/{GITHUB_USERNAME})  
- 📂 **Dépôts publics** : {public_repos}  
- 👥 **Followers** : {followers}  
- 🔄 **Abonnements** : {following}  

Mise à jour automatique grâce à GitHub Actions 🚀
"""

    # Écrire le README.md
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(readme_content)

    print("✅ README mis à jour avec succès !")
else:
    print("❌ Impossible de récupérer les informations. Vérifie ton pseudo GitHub.")
