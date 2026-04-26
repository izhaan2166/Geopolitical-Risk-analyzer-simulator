import os
import time
from time import sleep
from groq import Groq
from pathlib import Path

API_KEY=os.getenv("key")
client = Groq(api_key=API_KEY)

strategic_facts = [
    "Russia/Iraq supply 50%+ of Crude Oil; Suez Canal is a critical choke point for Indian energy security.",
    "The Strait of Hormuz is a high-risk chokepoint for 30% of India's crude and 54% of LPG supply.",
    "Australia provides 70% of India's Coking Coal; essential for JSW, Tata Steel, and infrastructure.",
    "Qatar is the primary source of LNG; India is 51% dependent on gas imports for fertilizers.",
    "Saudi Arabia remains a top 3 oil supplier; geopolitical shifts in the Gulf impact the Indian fiscal deficit.",
    "Taiwan (TSMC) is the sole supplier for 90% of sub-10nm logic chips used in India's 5G hardware.",
    "China accounts for 30% of industrial product imports, creating supply chain risks in electronics.",
    "India's mobile phone manufacturing DVA is only 23%; 77% of parts are imported from China/Vietnam.",
    "Australia and Argentina are critical for raw Lithium; processed in China for Indian EV batteries.",
    "South Korea provides high-grade electrical machinery essential for Indian industrial robotics.",
    "Gold imports surged 350% in Jan 2026; Switzerland is the primary source for investment bullion.",
    "Silver imports increased 127% in early 2026; driven by industrial demand and solar manufacturing.",
    "UAE is a major hub for gold and diamonds; CEPA agreement gives India 1% duty-free access.",
    "United Kingdom imports to India rose 75% in 2026, largely driven by luxury goods and finance.",
    "Brazil/Argentina supply 60% of India's Soy oil; droughts there trigger domestic food inflation.",
    "Malaysia/Indonesia provide 90% of India's Palm Oil; essential for food processing.",
    "Canada and Israel are the primary sources of Potash fertilizers; critical for food security.",
    "Russia/Oman supply the majority of Urea and Phosphatic fertilizers; essential for crop output.",
    "The India-Middle East-Europe Corridor (IMEC) is a strategic hedge against Suez Canal volatility.",
    "Logistics costs in India hit a record low of 7.97% of GDP in 2026, improving competitiveness.",
    "Mundra Port handles 30% of India's container trade; disruptions ripple through North India.",
    "The Malacca Strait is the primary naval chokepoint for India's trade with East Asia and Japan.",
    "China supplies 65% of Active Pharmaceutical Ingredients (APIs) for India's pharma sector.",
    "Organic chemicals from the USA and EU are critical for the Indian plastic and textile sectors.",
    "Copper imports from Chile and Zambia are essential for India's green energy grid and solar.",
    "Vietnam is a rising competitor in textiles; capturing market share from Indian exporters.",
    "Nuclear reactors and heavy machinery are primarily imported from the USA and Russia.",
    "Iron and Steel imports from Japan/Korea provide alloys needed for high-speed rail.",
    "Rare Earth Permanent Magnets (REPMs) are 95% dependent on Chinese processing.",
    "India-Oman CEPA anchors India's logistics and energy presence in the strategic Gulf region."
]

def generate_bulk_scenarios(fact):
    prompt = f"""
    Act as a dataset generator for an AI Supervisor. 
    Based on this trade fact: '{fact}'
    Generate 17 unique, diverse training examples.
    Format each as a separate JSON object with:
    - 'instruction': A realistic news headline (varying from mild to crisis level).
    - 'thought': Reasoning connecting the headline to the specific trade risk in the fact.
    - 'response': The logical next action for an agent.
    
    Return ONLY raw JSON objects, one per line. No conversational filler.
    """
    
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
        return None

with open("manager_data.jsonl", "w") as f:
    for i, fact in enumerate(strategic_facts):
        print(f"[{i+1}/30] Generating scenarios for: {fact[:40]}...")
        raw_output = generate_bulk_scenarios(fact)
        
        if raw_output:
            lines = raw_output.strip().split('\n')
            for line in lines:
                if line.strip().startswith('{'):
                    f.write(line.strip() + "\n")
        time.sleep(2)

print("✅ DONE! You should now have ~500 scenarios in manager_data.jsonl")