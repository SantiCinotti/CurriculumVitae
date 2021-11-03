class CurriculumVitae:
    def __init__(self):
        self.name = "Santiago"
        self.last_name = "Cinotti"
        self.age = 27
        self.email = "santicinotti@gmail.com"
        self.address = "Crisol 193, 4D, Córdoba, Arg"
        self.cellphone_number = "+549-358-4905900"

    def education(self):
        education = {
            "university": {
                "career": "Architecture",
                "collage": '"Universidad de Mendoza", Rio Cuarto, Cba, Arg',
            },
            "high_school": {
                "school": '"Durham School of the Arts", Durham, NC, USA',
                "year": "2010 - 2011",
            },
        }

        return education

    def work_experience(self):
        experience = {
            "studio": "Estudio de Arquitectura & Ingenieria Losada - Romanelli",
            "years": 2,
            "assignments": "Project design - Technical Project Manager",
            "contact": "+549-358-4187430",
            # I worked in the technical direction in a construction of a building, directing a staff of more than 10 people.
        }

        return experience

    def skills(self):
        skills = {
            "languagues": {
                "spanish": "native language",
                "english": "intermediate",
            },
            "knowledges": {
                "language": "python intermediate",
                "software": "tableau, power bi, git, excel",
                "others": "algorithms & logical thinking, data structures",
                "design_softwares": "photoshop, illustrator, indesign, premiere, corel draw, autocad, 3ds max, v-ray",
            },
        }

        return skills

    def objective(self):
        '''
        Looking for projects that challenges me to undertake and expand my knowledge in programming and data analysis, 
        and contribute to achieving company objectives.
        '''
        return f"{self.name} wants to work full time"
    
    def projects(self):
        projects = {
            "tableau": "https://public.tableau.com/app/profile/santiago.cinotti/viz/DatosInmobiliariosCrdobaArg_0120-0121/Dashboard1"
            "EDA - COVID-19 ARGENTINA": "https://github.com/SantiCinotti/covid_19"
        }
        
        return projects
        

if __name__ == "__main__":
    my_cv = CurriculumVitae()
    print(my_cv.__dict__)
    print(
        my_cv.education(),
        my_cv.work_experience(),
        my_cv.skills(),
        my_cv.objective(),
        my_cv.projects()
        sep=" - ",
    )
