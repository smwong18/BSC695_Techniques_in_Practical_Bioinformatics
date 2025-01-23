#!/usr/env/bin python3
import random

def sparkle():
    # Common sparkly messages (60% chance)
    common_sparkles = [
        "    ⋆˙✧ ˚⊹♡.",
        "    ⋆♡˙⟡ ˚⊹♡.",
        "   ˙✧˖°. ✦ ‧₊⋅", 
        "      ₊˚⊹♡.",
        "     . ݁₊⊹♡ ⊹. ݁⟡.",
        "    .𖥔 ݁˖ ✦ ‧₊⋅",
        "       ˙ ⊹₊⋆"
        "    ✧･ﾟ: *✧･ﾟ:*",
    ]
    
    # Rare fun messages (40% chance)
    rare_sparkles = [
        "    ₊✩‧₊˚౨ৎ˚₊✩‧₊",
        "    .𖥔 ݁ ˖ ✦ ‧₊˚ ⋅",  
        "      ˗ˏˋ ★ ˎˊ˗",
        "    ˚𖥔 ༺☆༻‧₊", 
        " ˏˋ 𓅰  𓅬  𓅭  𓅮  𓅯 ˎˊ",
        "   .𖥔 ݁ 𓆝  𓆟  𓆞 ˚⋅",
        "  ₊˚⊹ ⸜(｡˃ ᵕ ˂ )⸝♡ ˙ ⊹₊⋆  ",
    ]

    # 60% chance for common, 20% for rare
    if random.random() < 0.8:
        return random.choice(common_sparkles)
    else:
        return random.choice(rare_sparkles)

def main():
    print(sparkle())

if __name__ == '__main__':
    main()
