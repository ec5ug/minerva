from django import forms
from django_select2.forms import Select2MultipleWidget

class Registration_Form(forms.Form):
    STATE_CHOICES = [('alabama', 'Alabama'),('alaska', 'Alaska'),('arizona', 'Arizona'),('arkansas', 'Arkansas'),('california', 'California'),('colorado', 'Colorado'),('connecticut', 'Connecticut'),('delaware', 'Delaware'),('florida', 'Florida'),('georgia', 'Georgia'),('hawaii', 'Hawaii'),('idaho', 'Idaho'),('illinois', 'Illinois'),('indiana', 'Indiana'),('iowa', 'Iowa'),('kansas', 'Kansas'),('kentucky', 'Kentucky'),('louisiana', 'Louisiana'),('maine', 'Maine'),('maryland', 'Maryland'),('massachusetts', 'Massachusetts'),('michigan', 'Michigan'),('minnesota', 'Minnesota'),('mississippi', 'Mississippi'),('missouri', 'Missouri'),('montana', 'Montana'),('nebraska', 'Nebraska'),('nevada', 'Nevada'),('new_hampshire', 'New Hampshire'),('new_jersey', 'New Jersey'),('new_mexico', 'New Mexico'),('new_york', 'New York'),('north_carolina', 'North Carolina'),('north_dakota', 'North Dakota'),('ohio', 'Ohio'),('oklahoma', 'Oklahoma'),('oregon', 'Oregon'),('pennsylvania', 'Pennsylvania'),('rhode_island', 'Rhode Island'),('south_carolina', 'South Carolina'),('south_dakota', 'South Dakota'),('tennessee', 'Tennessee'),('texas', 'Texas'),('utah', 'Utah'),('vermont', 'Vermont'),('virginia', 'Virginia'),('washington', 'Washington'),('west_virginia', 'West Virginia'),('wisconsin', 'Wisconsin'),('wyoming', 'Wyoming'),('american_samoa', 'American Samoa'),('guam', 'Guam'),('northern_mariana_islands', 'Northern Mariana Islands'),('puerto_rico', 'Puerto Rico'),('u.s._virgin_islands', 'U.S. Virgin Islands'),]
    state = forms.CharField(label="My state of residence is", widget=forms.Select(choices=STATE_CHOICES))
    county = forms.CharField(label="My county of residence is")
    school = forms.CharField(label="I attend the following school")
    role = forms.CharField(label="I intend to use this scholarship service as a",
                           widget=forms.Select(choices=[('student','Student'),('school_admin','School Administrator')]))

class Student_Form(forms.Form):
    age = forms.IntegerField(label="I am __ years old", min_value=1, max_value=123)
    edu_lvl = forms.CharField(label="My current level of education is",
                              widget=forms.Select(choices=[("high_school", "High School"),
                                                           ("undergraduate", "Undergraduate"), ("graduate", "Graduate"),
                                                           ("doctoral", "Doctoral")]))
    gpa = forms.FloatField(label="My (unweighted) GPA is __", min_value=0, max_value=5)
    CLASS_CHOICES = [('3-d_art', '3-D Art'),('accounting', 'Accounting'),('aerobics', 'Aerobics'),('agriculture', 'Agriculture'),('algebra_1', 'Algebra 1'),('algebra_2', 'Algebra 2'),('american_literature', 'American Literature'),('american_sign_language', 'American Sign Language'),('ancient_greek', 'Ancient Greek'),('animation', 'Animation'),('app_development', 'App Development'),('arabic', 'Arabic'),('art_history', 'Art History'),('astronomy', 'Astronomy'),('audio_production', 'Audio Production'),('auto_body_repair', 'Auto Body Repair'),('auto_mechanics', 'Auto Mechanics'),('biology', 'Biology'),('botany', 'Botany'),('british_literature', 'British Literature'),('building_construction', 'Building Construction'),('business_law', 'Business Law'),('business_management', 'Business Management'),('calculus', 'Calculus'),('ceramics', 'Ceramics'),('chemistry', 'Chemistry'),('chemistry_of_foods', 'Chemistry of Foods'),('chinese', 'Chinese'),('choir', 'Choir'),('communication_skills', 'Communication Skills'),('computer-aided_drafting', 'Computer-Aided Drafting'),('computer_math', 'Computer Math'),('computer_programming', 'Computer Programming'),('computer_repair', 'Computer Repair'),('concert_band', 'Concert Band'),('consumer_education', 'Consumer Education'),('consumer_math', 'Consumer Math'),('contemporary_literature', 'Contemporary Literature'),('cosmetology', 'Cosmetology'),('cpr_training', 'CPR Training'),('creative_writing', 'Creative Writing'),('criminal_justice', 'Criminal Justice'),('culinary_arts', 'Culinary Arts'),('cultural_anthropology', 'Cultural Anthropology'),('current_events', 'Current Events'),('dance', 'Dance'),('debate', 'Debate'),('digital_media', 'Digital Media'),('drama', 'Drama'),('drawing', 'Drawing'),('driver_education', 'Driver Education'),('early_childhood_development', 'Early Childhood Development'),('early_childhood_education', 'Early Childhood Education'),('earth_science', 'Earth Science'),('electronics', 'Electronics'),('english_language_and_composition', 'English Language and Composition'),('english_literature_and_composition', 'English Literature and Composition'),('entrepreneurial_skills', 'Entrepreneurial Skills'),('environmental_science', 'Environmental Science'),('environmental_studies', 'Environmental Studies'),('european_history', 'European History'),('family_studies', 'Family Studies'),('fashion_and_retail_merchandising', 'Fashion and Retail Merchandising'),('fashion_construction', 'Fashion Construction'),('ffa', 'FFA'),('film_production', 'Film Production'),('fire_science', 'Fire Science'),('forensic_science', 'Forensic Science'),('french', 'French'),('fundamentals_of_math', 'Fundamentals of Math'),('geography', 'Geography'),('geology', 'Geology'),('geometry', 'Geometry'),('german', 'German'),('global_studies', 'Global Studies'),('graphic_design', 'Graphic Design'),('guitar', 'Guitar'),('gymnastics', 'Gymnastics'),('health', 'Health'),('heating_and_cooling_systems', 'Heating and Cooling Systems'),('hebrew', 'Hebrew'),('home_economics', 'Home Economics'),('hospitality_and_tourism', 'Hospitality and Tourism'),('human_geography', 'Human Geography'),('humanities', 'Humanities'),('integrated_math', 'Integrated Math'),('interior_design', 'Interior Design'),('international_relations', 'International Relations'),('introduction_to_business', 'Introduction to Business'),('italian', 'Italian'),('japanese', 'Japanese'),('jazz_band', 'Jazz Band'),('jewelry_design', 'Jewelry Design'),('journalism', 'Journalism'),('jrotc', 'JROTC'),('keyboarding', 'Keyboarding'),('korean', 'Korean'),('latin', 'Latin'),('law', 'Law'),('lifeguard_training', 'Lifeguard Training'),('literary_analysis', 'Literary Analysis'),('macroeconomics', 'Macroeconomics'),('marching_band', 'Marching Band'),('marine_biology', 'Marine Biology'),('marketing', 'Marketing'),('math_applications', 'Math Applications'),('media_technology', 'Media Technology'),('metalworking', 'Metalworking'),('microeconomics', 'Microeconomics'),('modern_literature', 'Modern Literature'),('modern_world_studies', 'Modern World Studies'),('multivariable_calculus', 'Multivariable Calculus'),('music_production', 'Music Production'),('music_theory', 'Music Theory'),('networking', 'Networking'),('nutrition', 'Nutrition'),('oceanography', 'Oceanography'),('orchestra', 'Orchestra'),('painting', 'Painting'),('percussion', 'Percussion'),('personal_finance', 'Personal Finance'),('photography', 'Photography'),('physical_anthropology', 'Physical Anthropology'),('physical_science', 'Physical Science'),('physics', 'Physics'),('piano', 'Piano'),('pilates', 'Pilates'),('plumbing', 'Plumbing'),('poetry', 'Poetry'),('political_studies', 'Political Studies'),('popular_literature', 'Popular Literature'),('portuguese', 'Portuguese'),('practical_math', 'Practical Math'),('pre-algebra', 'Pre-Algebra'),('precalculus', 'Precalculus'),('printmaking', 'Printmaking'),('probability', 'Probability'),('production_technology', 'Production Technology'),('psychology', 'Psychology'),('quantitative_literacy', 'Quantitative Literacy'),('racket_sports', 'Racket Sports'),('refrigeration_fundamentals', 'Refrigeration Fundamentals'),('religious_studies', 'Religious Studies'),('rhetoric', 'Rhetoric'),('robotics', 'Robotics'),('russian', 'Russian'),('sculpture', 'Sculpture'),('shakespeare', 'Shakespeare'),('sociology', 'Sociology'),('spanish', 'Spanish'),('specialized_sports', 'Specialized Sports'),('statistics', 'Statistics'),('swimming', 'Swimming'),('technical_writing', 'Technical Writing'),('theater_technology', 'Theater Technology'),('trigonometry', 'Trigonometry'),('u.s._government', 'U.S. Government'),('u.s._history', 'U.S. History'),('video_game_development', 'Video Game Development'),('web_design', 'Web Design'),('web_programming', 'Web Programming'),('weight_training', 'Weight Training'),('women’s_studies', 'Women’s Studies'),('woodworking', 'Woodworking'),('word_processing', 'Word Processing'),('world_history', 'World History'),('world_literature', 'World Literature'),('world_music', 'World Music'),('world_politics', 'World Politics'),('world_religions', 'World Religions'),('written_and_oral_communication', 'Written and Oral Communication'),('yoga', 'Yoga'),('zoology', 'Zoology'),]
    classes = forms.MultipleChoiceField(label="I have taken these courses", choices=CLASS_CHOICES,
                                        widget=forms.CheckboxSelectMultiple(attrs={'class': 'column-choices'}))
    MAJOR_CHOICES = [("chemistry", "Chemistry"), ("computer_science", "Computer Science")]
    major = forms.MultipleChoiceField(label="I intend to major or am majoring in: ", choices=MAJOR_CHOICES,
                                      widget=forms.CheckboxSelectMultiple(attrs={'class': 'column-choices'}))
    INTEREST_CHOICES = [("art", "Art"), ("engineering", "Engineering"), ("medicine", "Medicine")]
    interests = forms.MultipleChoiceField(label="I am interested in: ", choices=INTEREST_CHOICES,
                                          widget=forms.CheckboxSelectMultiple(attrs={'class': 'column-choices'}))
    # major = forms.MultipleChoiceField(label="I intend to major or am majoring in: ", choices=MAJOR_CHOICES,
    #                                   initial='0', widget=forms.SelectMultiple())