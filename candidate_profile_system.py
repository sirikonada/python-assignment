class PersonalInfo:
    def __init__(self, name, dob, contact, email):
        self.name = name
        self.dob = dob
        self.contact = contact
        self.email = email

    def display_personal(self):
        print("Name:", self.name)
        print("Date of Birth:", self.dob)
        print("Contact Number:", self.contact)
        print("Email:", self.email)


class Education(PersonalInfo):
    def __init__(self, name, dob, contact, email, degree, university, year, cgpa):
        super().__init__(name, dob, contact, email)
        self.degree = degree
        self.university = university
        self.year = year
        self.cgpa = cgpa

    def display_education(self):
        print("\n--- Education Details ---")
        print("Degree:", self.degree)
        print("University:", self.university)
        print("Year of Graduation:", self.year)
        print("CGPA:", self.cgpa)


class Experience(Education):
    def __init__(self, name, dob, contact, email, degree, university, year, cgpa,
                 company, role, years_exp, skills):
        super().__init__(name, dob, contact, email, degree, university, year, cgpa)
        self.company = company
        self.role = role
        self.years_exp = years_exp
        self.skills = skills

    def display_experience(self):
        print("\n--- Work Experience ---")
        print("Company Name:", self.company)
        print("Job Role:", self.role)
        print("Years of Experience:", self.years_exp)
        print("Skills:", self.skills)


class CandidateProfile(Experience):

    def display_profile(self):
        print("\n----- Candidate Profile -----")
        self.display_personal()
        self.display_education()
        self.display_experience()

        if self.years_exp >= 5:
            print("Eligible for Senior Role")
        else:
            print("Eligible for Junior Role")


# Candidate 1
c1 = CandidateProfile(
    "Aarya", "10-05-1997", "9328684734", "aarya@email.com",
    "B.Tech", "anits University", 2018, 8.2,
    "Infosys", "Software Engineer", 6, "Python, Java"
)

# Candidate 2
c2 = CandidateProfile(
    "rajya", "22-08-1999", "7013168222", "rajya@email.com",
    "B.Sc Computer Science", "parul University", 2021, 7.9,
    "TCS", "Junior Developer", 2, "Python, SQL"
)

c1.display_profile()
c2.display_profile()
