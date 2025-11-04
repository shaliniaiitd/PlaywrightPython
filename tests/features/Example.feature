Feature: Example Feature

Background: Common Scenario
Given I am at home  page at "https://yahoo.com"
When I fill in user "test_123"
And password "password123"
And hit enter
Then home page appears with title "Home Page"

Scenario: Using text whixh can be accessed using context.text
When I enter """sample text""" in input box
And hit enter
Then next page appears with title """Welcome to your customised page"""

@my_tag
Scenario: Using table to define parameters

  Given a set of specific users
     | name      | department  |
     | Barry     | Beer Cans   |
     | Pudey     | Silly Walks |
     | Two-Lumps | Silly Walks |

 When we count the number of people in each department
 Then we will find two people in "Silly Walks"
  But we will find one person in "Beer Cans"

@fixture.db
Scenario Outline: Blenders
   Given I put <thing> in a blender,
    when I switch the blender on
    then it should transform into <other thing>

 Examples: Amphibians
   | thing         | other thing |
   | Red Tree Frog | mush        |

 Examples: Consumer Electronics
   | thing         | other thing |
   | iPhone        | toxic waste |
   | Galaxy Nexus  | toxic waste |