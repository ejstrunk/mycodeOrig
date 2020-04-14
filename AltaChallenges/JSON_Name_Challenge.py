#!/usr/bin/python3
# Easy: "My name is ___ and my spirit animal is ___."
# Med:  "My name is ___ and my skills are ____."
# Hard: "My name is ___ and my super power is ____."

superdict = {
  "all": [
    {
      "First": "Askia",
      "Last": "Wingfield",
      "Skill Level": "astonishing",
      "Spirit Animal": "lion",
      "Super Power": "Regenerative Healing Factor"
    },
    {
      "First": "Chen",
      "Last": "Xin",
      "Skill Level": "awe-inspiring",
      "Spirit Animal": "porcupine",
      "Super Power": "Adoptive Muscle Memory"
    },
    {
      "First": "Everett",
      "Last": "Strunk",
      "Skill Level": "breathtaking",
      "Spirit Animal": "mandrill",
      "Super Power": "Body Part Substitution"
    },
    {
      "First": "Jacob",
      "Last": "Roe",
      "Skill Level": "fearsome",
      "Spirit Animal": "guinea pig",
      "Super Power": "Anatomical Liberation"
    },
    {
      "First": "Josh",
      "Last": "Ayala",
      "Skill Level": "formidable",
      "Spirit Animal": "camel",
      "Super Power": "Additional Limbs"
    },
    {
      "First": "Kevin",
      "Last": "Martinez",
      "Skill Level": "imposing",
      "Spirit Animal": "panther",
      "Super Power": "Organic Constructs"
    },
    {
      "First": "Luke",
      "Last": "Thompson",
      "Skill Level": "impressive",
      "Spirit Animal": "coati",
      "Super Power": "Deflection"
    },
    {
      "First": "Marco",
      "Last": "Santos",
      "Skill Level": "magnificent",
      "Spirit Animal": "bumblebee",
      "Super Power": "Replication"
    },
    {
      "First": "Michael",
      "Last": "Williams",
      "Skill Level": "overwhelming",
      "Spirit Animal": "fish",
      "Super Power": "Invisibility"
    },
    {
      "First": "Mike",
      "Last": "Wright",
      "Skill Level": "stunning",
      "Spirit Animal": "mink",
      "Super Power": "Needle Projection"
    },
    {
      "First": "Oscar",
      "Last": "Abalos",
      "Skill Level": "wondrous",
      "Spirit Animal": "ermine",
      "Super Power": "Immobility"
    },
    {
      "First": "Ryan",
      "Last": "Larson",
      "Skill Level": "grand",
      "Spirit Animal": "marmoset",
      "Super Power": "Camouflage"
    },
    {
      "First": "Shirley",
      "Last": "Wu",
      "Skill Level": "mind-blowing",
      "Spirit Animal": "koala",
      "Super Power": "Self-Detonation"
    }
  ]
}
##print(f"My name is {superdict['all'][2]['First']} {superdict['all'][2]['Last']} and my spirit animal is {superdict['all'][2]['Spirit Animal']}.")
##print(f"My name is {superdict['all'][2]['First']} {superdict['all'][2]['Last']} and my skills are {superdict['all'][2]['Skill Level']}.")
##print(f"My name is {superdict['all'][2]['First']} {superdict['all'][2]['Last']} and my super power is {superdict['all'][2]['Super Power']}.")

def main():
    for x in superdict["all"]:
        print(f"\nMy name is {x['First']} {x['Last']} and my spirit animal is {x['Spirit Animal']}, my skills are {x['Skill Level']}, and my super power is {x['Super Power']}.")
main()
