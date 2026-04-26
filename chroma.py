import chromadb

# 1. This creates a folder named 'india_trade_kb' in your project directory
client = chromadb.PersistentClient(path="./india_trade_kb")

# 2. Create the collection
collection = client.get_or_create_collection(name="strategic_intel")

# 3. Your 30 Strategic Facts
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

# 4. Push to the folder
collection.add(
    documents=strategic_facts,
    ids=[f"id_{i}" for i in range(len(strategic_facts))]
)

print("Knowledge Base Folder Created: ./india_trade_kb")