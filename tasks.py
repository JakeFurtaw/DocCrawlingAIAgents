from crewai import Task
from agents import Question_crawler, Answer_crawler, Get_example_data, Manager
from main import website_link

# Define the tasks that will be used in the project
class Tasks():
    Manager = Task(
        description = "Manage the team of agents and provide tasks to each agent that will help further guide the project to sucess.",
        expected_output = "A well managed team and project.",
        agent = Manager
    )

    Get_example_data = Task(
        description = "Read files and directories to get example data that can be used to test the project.",
        expected_output = "Example data that can be used to test the project.",
        agent = Get_example_data
    )
    
    Question_crawler = Task(
        description = """Crawl the provided website {website_link} and all of its sublinks to come up with questions that students would have about the school.
        This could include gerneral information about the school, the programs offered, the campus life, different majors, food offered on campus, building and facility 
        locations, fraternity and sorority information, club information, teacher and faculty information.""",
        expected_output = "A list of questions that students would have about the school.",
        agent = Question_crawler
    )

    Answer_crawler = Task(
        description = "Crawl the provided website {website_link} and all of its sublinks to come up with answers to the questions that the question crawler agent came up with.",
        expected_output = "A list of answers to the questions that the question crawler agent came up with.",
        agent = Answer_crawler
    )