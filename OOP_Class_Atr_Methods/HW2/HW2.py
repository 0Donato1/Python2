class FrontEndDeveloper:
    slills = ["HTML", "CSS", "JavaScript", "React"]
    salary = "3000$"
    experience = "3 years"

class BackEndDeveloper(FrontEndDeveloper):
    skills = ["Java", "Python", "Node.js", "PHP"]

class FullStackDeveloper(BackEndDeveloper):
    skills = ["SQL", "React", "Python", "C#"]
    skillsstring = ', '.join(skills)

w = FullStackDeveloper()
day_str = ""
print(f"{day_str:=^57}", "\n")
print(f"Languages for Full Stack Developer: {w.skillsstring}\n")
print(f"{day_str:=^57}", "\n")
print(f"Salary for Full Stack Developer: {w.salary}\n")
print(f"{day_str:=^57}", "\n")
print(f"Experience of Full Stack Developing: {w.experience}\n")
print(f"{day_str:=^57}", "\n")




