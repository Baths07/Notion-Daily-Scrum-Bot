from notion_client import Client
from dotenv import load_dotenv
import os
from datetime import datetime

# Ortam değişkenlerini yükle
load_dotenv()

notion = Client(auth=os.getenv("NOTION_TOKEN"))
database_id = os.getenv("NOTION_DATABASE_ID")  # .env içinde bu isimle

# Bugünün tarihi
today = datetime.now().strftime("%Y-%m-%d")

# Sayfa oluşturma
response = notion.pages.create(
    parent={"database_id": database_id},
    properties={
        "Name": {
            "title": [{
                "text": {"content": f"Günlük Scrum - {today}"}
            }]
        }
    },
    children=[
        {
            "object": "block",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "✅ Bugün Neler Yaptım?"}}]
            }
        },
        {
            "object": "block",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": "• "}}]
            }
        },
        {
            "object": "block",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "🧠 Neyi Daha İyi Yapabilirdim?"}}]
            }
        },
        {
            "object": "block",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": "• "}}]
            }
        },
        {
            "object": "block",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "🚧 Karşılaştığım Engeller"}}]
            }
        },
        {
            "object": "block",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": "• "}}]
            }
        },
        {
            "object": "block",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "✅ Kendime Kaç Puan Veriyorum? (1-5)"}}]
            }
        },
        *[
            {
                "object": "block",
                "to_do": {
                    "rich_text": [{"type": "text", "text": {"content": str(i)}}],
                    "checked": False
                }
            } for i in range(1, 6)
        ]
    ]
)

print("✅ Günlük Scrum sayfası başarıyla oluşturuldu:", response["url"])
