from card_generator import CardGenerator
import json

amex_generator = CardGenerator("amex")

# Generate cards with formatting and bank info
pretty_cards = amex_generator.generate(
    count=100,
    beautiful_format=True,
    include_bank_info=True
)

# Save output to gen.txt
with open("output/gen100.txt", "w", encoding="utf-8") as f:
    json.dump(pretty_cards, f, indent=2, ensure_ascii=False)

print("Generated cards saved to output/gen100.txt")