import os
import pandas as pd

schools = {
    "Douglas": [
        {
            "school_name": "Anagh Coar Primary School",
            "address": "Darragh Way, Anagh Coar, Douglas, Isle of Man, IM2 2BA",
            "phone": "01624 622148",
            "website": "https://www.sch.im/schools/anagh-coar-primary-school",
            "students": "TODO"
        },
        {
            "school_name": "Ballakermeen High School",
            "address": "St Catherine's Drive, Douglas, Isle of Man, IM1 4BE",
            "phone": "01624 648700",
            "website": "https://www.sch.im/schools/ballakermeen-high-school",
            "students": "TODO"
        },
        {
            "school_name": "Henry Bloom Noble Primary School",
            "address": "Westmoreland Road, Douglas, Isle of Man, IM1 4AQ",
            "phone": "01624 621577",
            "website": "https://www.sch.im/schools/henry-bloom-noble-primary-school",
            "students": "TODO"
        },
        {
            "school_name": "St Ninian's High School",
            "address": "Park Road, Douglas, Isle of Man, IM2 3EH",
            "phone": "01624 648800",
            "website": "https://www.sch.im/schools/st-ninians-high-school",
            "students": "TODO"
        },
        {
            "school_name": "Willaston Primary School",
            "address": "Douglas, Isle of Man, IM2 5EE",
            "phone": "01624 621577",
            "website": "https://www.sch.im/schools/willaston-primary-school",
            "students": "TODO"
        }
    ],
    "Castletown": [
        {
            "school_name": "Castle Rushen High School",
            "address": "Arbory Road, Castletown, Isle of Man, IM9 1RE",
            "phone": "01624 693500",
            "website": "https://www.sch.im/schools/castle-rushen-high-school",
            "students": "TODO"
        },
        {
            "school_name": "King William's College",
            "address": "Castletown, Isle of Man, IM9 1TP",
            "phone": "01624 820400",
            "website": "https://www.sch.im/schools/king-williams-college",
            "students": "TODO"
        },
        {
            "school_name": "The Buchan School",
            "address": "Westhill, Arbory Road, Castletown, Isle of Man, IM9 1RD",
            "phone": "01624 820481",
            "website": "https://www.sch.im/schools/the-buchan-school",
            "students": "TODO"
        }
    ],
    "Peel": [
        {
            "school_name": "Queen Elizabeth II High School",
            "address": "Douglas Road, Peel, Isle of Man, IM5 1RD",
            "phone": "01624 841000",
            "website": "https://www.sch.im/schools/queen-elizabeth-ii-high-school",
            "students": "TODO"
        }
    ],
    "Ramsey": [
        {
            "school_name": "Ramsey Grammar School",
            "address": "Lezayre Road, Ramsey, Isle of Man, IM8 2RG",
            "phone": "01624 811100",
            "website": "https://www.sch.im/schools/ramsey-grammar-school",
            "students": "TODO"
        }
    ],
    "Onchan": [
        {
            "school_name": "Ashley Hill Primary School",
            "address": "Onchan, Isle of Man, IM3 3LA",
            "phone": "01624 686633",
            "website": "https://www.sch.im/schools/ashley-hill-primary-school",
            "students": "TODO"
        }
    ],
    "Other": [
        {
            "school_name": "Andreas Primary School",
            "address": "Andreas, Isle of Man, IM7 4EZ",
            "phone": "01624 880375",
            "website": "https://www.sch.im/schools/andreas-primary-school",
            "students": "TODO"
        },
        {
            "school_name": "Arbory Primary School",
            "address": "Ballabeg, Isle of Man, IM9 4LH",
            "phone": "01624 823369",
            "website": "https://www.sch.im/schools/arbory-primary-school",
            "students": "TODO"
        },
        {
            "school_name": "Ballacottier Primary School",
            "address": "Clybane Road, Farmhill, Douglas, Isle of Man, IM2 2ST",
            "phone": "01624 612558",
            "website": "https://www.sch.im/schools/ballacottier-primary-school",
            "students": "TODO"
        },
        {
            "school_name": "Ballasalla Primary School",
            "address": "Malew, Isle of Man, IM9 2ED",
            "phone": "01624 822529",
            "website": "https://www.sch.im/schools/ballasalla-primary-school",
            "students": "TODO"
        },
        {
            "school_name": "Ballaugh Primary School",
            "address": "Ballaugh, Isle of Man, IM7 5EG",
            "phone": "01624 897311",
            "website": "https://www.sch.im/schools/ballaugh-primary-school",
            "students": "TODO"
        },
        {
            "school_name": "Braddan Primary School",
            "address": "Braddan, Isle of Man, IM4 4RA",
            "phone": "01624 661087",
            "website": "https://www.sch.im/schools/braddan-primary-school",
            "students": "TODO"
        },
        {
            "school_name": "Bunscoill Ghaelgagh",
            "address": "St John's, Isle of Man, IM4 3NA",
            "phone": "01624 803330",
            "website": "https://www.sch.im/schools/bunscoill-ghaelgagh",
            "students": "TODO"
        },
        {
            "school_name": "Bunscoill Rhumsaa",
            "address": "Ramsey, Isle of Man, IM8 2RG",
            "phone": "01624 812662",
            "website": "https://www.sch.im/schools/bunscoill-rhumsaa",
            "students": "TODO"
        },
        {
            "school_name": "Cronk-y-Berry Primary School",
            "address": "Douglas, Isle of Man, IM2 6HG",
            "phone": "01624 673807",
            "website": "https://www.sch.im/schools/cronk-y-berry-primary-school",
            "students": "TODO"
        },
        {
            "school_name": "Dhoon Primary School",
            "address": "Glen Mona, Isle of Man, IM7 1HA",
            "phone": "01624 861228",
            "website": "https://www.sch.im/schools/dhoon-primary-school",
            "students": "TODO"
        },
        {
            "school_name": "Foxdale Primary School",
            "address": "Foxdale, Isle of Man, IM4 3HB",
            "phone": "01624 801281",
            "website": "https://www.sch.im/schools/foxdale-primary-school",
            "students": "TODO"
        },
        {
            "school_name": "Jurby Primary School",
            "address": "Jurby, Isle of Man, IM7 3BJ",
            "phone": "01624 897258",
            "website": "https://www.sch.im/schools/jurby-primary-school",
            "students": "TODO"
        },
        {
            "school_name": "Kewaigue Primary School",
            "address": "Douglas, Isle of Man, IM2 1QH",
            "phone": "01624 673807",
            "website": "https://www.sch.im/schools/kewaigue-primary-school",
            "students": "TODO"
        },
        {
            "school_name": "Kirk Michael Primary School",
            "address": "Michael, Isle of Man, IM6 1AB",
            "phone": "01624 878246",
            "website": "https://www.sch.im/schools/kirk-michael-primary-school",
            "students": "TODO"
        },
        {
            "school_name": "Laxey Primary School",
            "address": "Laxey, Isle of Man, IM4 7DU",
            "phone": "01624 861228",
            "website": "https://www.sch.im/schools/laxey-primary-school",
            "students": "TODO"
        },
        {
            "school_name": "Manor Park Primary School",
            "address": "Pulrose, Douglas, Isle of Man, IM2 1QH",
            "phone": "01624 673807",
            "website": "https://www.sch.im/schools/manor-park-primary-school",
            "students": "TODO"
        },
        {
            "school_name": "Marown Primary School",
            "address": "Marown, Isle of Man, IM4 4RA",
            "phone": "01624 661087",
            "website": "https://www.sch.im/schools/marown-primary-school",
            "students": "TODO"
        },
        {
            "school_name": "Onchan Primary School",
            "address": "Onchan, Isle of Man, IM3 3LA",
            "phone": "01624 686633",
            "website": "https://www.sch.im/schools/onchan-primary-school",
            "students": "TODO"
        },
        {
            "school_name": "Peel Clothworkers' Primary School",
            "address": "Peel, Isle of Man, IM5 1HP",
            "phone": "01624 841000",
            "website": "https://www.sch.im/schools/peel-clothworkers-primary-school",
            "students": "TODO"
        },
        {
            "school_name": "Rushen Primary School",
            "address": "Port St Mary, Isle of Man, IM9 5LW",
            "phone": "01624 822208",
            "website": "https://www.sch.im/schools/rushen-primary-school",
            "students": "TODO"
        },
        {
            "school_name": "Scoill Phurt le Moirrey",
            "address": "Port St Mary, Isle of Man, IM9 5RB",
            "phone": "01624 822208",
            "website": "https://www.sch.im/schools/scoill-phurt-le-moirrey",
            "students": "TODO"
        },
        {
            "school_name": "Scoill Vallajeelt",
            "address": "Douglas, Isle of Man, IM2 1QH",
            "phone": "01624 673807",
            "website": "https://www.sch.im/schools/scoill-vallajeelt",
            "students": "TODO"
        },
        {
            "school_name": "Scoill yn Jubilee",
            "address": "Douglas, Isle of Man, IM2 1QH",
            "phone": "01624 673807",
            "website": "https://www.sch.im/schools/scoill-yn-jubilee",
            "students": "TODO"
        },
        {
            "school_name": "St John's Primary School",
            "address": "St John's, Isle of Man, IM4 3NA",
            "phone": "01624 803330",
            "website": "https://www.sch.im/schools/st-johns-primary-school",
            "students": "TODO"
        },
        {
            "school_name": "St Mary's RC School",
            "address": "Douglas, Isle of Man, IM2 1QH",
            "phone": "01624 673807",
            "website": "https://www.sch.im/schools/st-marys-rc-school",
            "students": "TODO"
        },
        {
            "school_name": "St Thomas' C of E School",
            "address": "Douglas, Isle of Man, IM2 1QH",
            "phone": "01624 673807",
            "website": "https://www.sch.im/schools/st-thomas-coe-school",
            "students": "TODO"
        },
        {
            "school_name": "Sulby Primary School",
            "address": "Sulby, Isle of Man, IM7 2HB",
            "phone": "01624 897258",
            "website": "https://www.sch.im/schools/sulby-primary-school",
            "students": "TODO"
        },
        {
            "school_name": "Victoria Road Primary School",
            "address": "Castletown, Isle of Man, IM9 1RE",
            "phone": "01624 822208",
            "website": "https://www.sch.im/schools/victoria-road-primary-school",
            "students": "TODO"
        }
    ]
}

# Combine all school lists into one DataFrame
schools_data = pd.DataFrame([school for district in schools.values() for school in district])

# Define the output directory for the markdown files
output_dir = '.'
os.makedirs(output_dir, exist_ok=True)

# Assign district names to each row in the DataFrame
for district_name, schools_list in schools.items():
    district_name = district_name.replace(" Dist.", "").replace(" Public School District", "").replace(" School District", "").replace(" School Dist", "").replace(" Public School", "").replace(" District", "").rstrip('.')

    for school in schools_list:
        school['address'] = school['address'].replace('+', ', ')
        schools_data.loc[schools_data['school_name'] == school['school_name'], 'district_name'] = district_name

# Function to generate markdown files
def generate_markdown_by_index(row):
    # Simplify the school name for the directory and file
    district_name_simple = row['district_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")
    school_name_simple = row['school_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")
    path = os.path.join(output_dir, district_name_simple)
    os.makedirs(path, exist_ok=True)

    # Filename for the markdown
    file_path = os.path.join(path, f"{school_name_simple}.md")

    # Markdown content with front-matter and details
    with open(file_path, 'w') as file:
        file.write(f"---\nlayout: page\ntitle: {row['school_name']}\n---\n")  # School Name
        file.write(
            f"# Navigation\n\n[[All countries/states/provinces]](../../..) > [[All Isle of Man Districts]](../..) > [[All In {row['district_name']}]](..)\n\n")

        file.write(f"# {row['school_name']} ({row['district_name']})\n\n")  # School Name and area as header

        # Loop through keys per school
        for key, value in row.items():
            if key not in ['district_name', 'school_name']:
                if str(value).startswith("http"):
                    value = "<" + value + ">"
                file.write(f"**{key.replace('_', ' ').title()}**: {value}\n\n")

        file.write(f"**School's overall airborne virus protection grade (0-5)**: 0\n\n")
        file.write(f"**Discord, Facebook, or WhatsApp group for discovery/advocacy for THIS school**: TODO\n\n")
        file.write(f"**School's policy on Ventilation**: TODO\n\n")
        file.write(f"**School's Ventilation Work Completion**: TODO\n\n")
        file.write(f"**School's Air-Purification**: TODO\n\n")
        file.write(f"**School's CO2 monitoring to actively drive ventilation and filtration**: TODO\n\n")
        file.write(f"**School's Wikidata URL**: TODO")
        file.write(f"\n\n\n[Edit this page](https://github.com/ventilate-schools/IoM/edit/main/{file_path}).")
        file.write(f" See also [rules for contribution](../../../contribution-rules/)")

# Generate markdown files for each school
schools_data.apply(generate_markdown_by_index, axis=1)

def create_area_and_root_index():
    # Create a dictionary to keep track of schools in each district
    districts_dict = {}

    for index, row in schools_data.iterrows():
        district_name_simple = row['district_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")
        school_name_simple = row['school_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")

        # Check if the district already exists in the dictionary
        if district_name_simple not in districts_dict:
            districts_dict[district_name_simple] = []

        # Append the school name to the district's list
        districts_dict[district_name_simple].append(school_name_simple)

    # Write an index markdown file for each district and gather data for root index
    root_index_content = "---\ntitle: Schools in Isle of Man and their ventilation status\n---\n"

    root_index_content += (
        "\n# Navigation\n\n[[All countries/states/provinces]](..)\n\n# Purpose of site\n\nGiven **COVID-19 is Airborne** and the world is pushing to better ventilate "
        "schools for long term student and teacher health, we're tracking the "
        "progress for that in Isle of Man. This is ahead of government effort to do the same. If government starts to "
        "track this work, this effort will continue because that effort might be weak."
        "We're guided by 33 profs and PhDs who are pushing for a policy change in a "
        "March 2024 article on **Science.org**: [Mandating indoor air quality for public buildings](https://drive.google.com/file/d/16l_IH47cQtC7fFuafvHca7ORNVGITxx8/view). "
        "Not only active ventilation (which should "
        "be mechanical heat recovery type in this age), but air filtration/purification "
        "too and CO2 monitoring to drive ventilation levels, as CO2 inside is a proxy indicator "
        "for COVID risk. As it happens the WHO also have a [2023 airborne risk assessment guide](https://iris.who.int/handle/10665/376346)\n\n"
        "Know that other diseases are airborne too: Measles "
        "(studies [1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2810934/pdf/10982072.pdf) "
        "[2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3880795/pdf/nihms532643.pdf) "
        "[3](https://pubmed.ncbi.nlm.nih.gov/31257413/) "
        "[4](https://www.sciencedirect.com/science/article/pii/S0196655316305363)), "
        "Influenza, RSV and TB. The same "
        "ventilation and air filtration measures reduce transmission of those too.\n\n When we say "
        "student and teacher health, we're wanting absences to go down too. If we lower "
        "transmission in schools, we reduce multi-generation transmission too, as kids bring "
        "infections home to parents. With lowered transmission, we also reduce long COVID, "
        "where the worst sufferers have disappeared from education and the workplace.\n\n")

    root_index_content += (
        "\n## Leaderboard\n\n1. to be announced\n2. to be announced\n3. to be announced\n4. to be announced\n5. to be announced\n\n")

    root_index_content += ("{% include_relative grade.html %}\n\n")

    root_index_content += ("# Isle of Man School Districts:\n\n")

    for district, schools in districts_dict.items():
        district_index_file_path = os.path.join(output_dir, district, "index.md")
        os.makedirs(os.path.join(output_dir, district), exist_ok=True)

        with open(district_index_file_path, 'w') as district_index_file:
            district_index_file.write(f"---\nlayout: page\ntitle: Schools in {district.replace('_', ' ')}\n---\n")
            district_index_file.write(
                f"# Navigation\n\n[[All countries/states/provinces]](../..) > [[All B.C. districts]](..)\n\n")
            district_index_file.write(f"# Schools in {district.replace('_', ' ')}\n\n")
            district_index_file.write("{% include_relative grade.html %}\n\n")
            district_index_file.write(f"**Schools:**\n\n")
            for school in schools:
                school_file_path = school
                district_index_file.write(f"- [{school.replace('_', ' ')}]({school_file_path}.md)\n")

        # Add to root index content with cleaner URLs
        root_index_content += f"- [{district.replace('_', ' ')}]({district}/): {len(schools)} schools\n"

    root_index_content += ("\n\n# Site ownership\n\nThis site is edited by volunteers who're "
                           "interested in accelerating the work to complete the adequate ventilation of Isle of Man schools. "
                           "This effort was not commissioned by education authorities or government.\n\n"
                           "[Edit this page](https://github.com/ventilate-schools/IoM/edit/main/index.md). See also [rules for contribution](./contribution_rules/)")

    # Write the root index file
    root_index_path = os.path.join(output_dir, "index.md")
    with open(root_index_path, 'w') as root_index_file:
        root_index_file.write(root_index_content)

# Call the function to create index markdown files and root index
create_area_and_root_index()

# Print confirmation
print("Index markdown files with front matter and links have been created in each area directory and root directory.")