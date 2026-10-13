
from pyscript import document, display

#sets
grade7 = {'Adam Carlsen', 'Olive Smith'}
grade8 = {'Anh Pham'}
grade9 = {'Malcolm Browne'}
grade10 = {'Jeremy Langley'}


members = grade7 | grade8 | grade9 | grade10 # combine all grade sets into 1


def add_member(event):
    global members

    fname = document.getElementById("Fname").value.strip().title() #fname
    lname = document.getElementById("Lname").value.strip().title() #lname

    
    new_member = fname + " " + lname # combine the first and last names

    members = members | {new_member}  # add new member

    names = chr(10).join(sorted(members)) 
    document.getElementById("result").innerHTML = (
        f"<h3>ALL MEMBERS:</h3>"
        f"<pre>{names}</pre>"
        f"<p>Total Members: {len(members)}</p>"
    ) # from ChatGPT to fix the indention and br and design the texts

   
    document.getElementById("Fname").value = ""
    document.getElementById("Lname").value = "" 
    # clear the previous input