Dodfather is an attempt to make a django app.

Maybe sprinkle some react ?

https://fractalideas.com/blog/making-react-and-django-play-well-together-single-page-app-model/

Hopefully avoid all that by making nice web things. Maybe even put in some jquery

TODO:

# Projects

- ✅ Store a project
- ✅ Edit a project and save it
- ✅ Delete a project
- ✅ Search projects by title
- ✅ Add measures of success to a project

  - https://techincent.com/explained-django-inline-formset-factory-with-example/)
  - https://docs.djangoproject.com/en/4.0/ref/forms/models/#django.forms.models.inlineformset_factory

- 🟥 Add team members (i.e create user model)
- 🟥 Project lifecycle - allow submit for review
- 🟥 Allow team members to sign off on the project when it's doodling
  - This probably means having a relationship table with a sign off field
- 🟥 Track changes - maybe this is a big JSON field for the whole project
  - Include sign-off changes
  - How to make a view from a JSON representation of Project?

# Status reports

- 🟥 Create a status report for a project (simple RAG status + text update)
- 🟥 See a list of status reports for a project
- 🟥 Add latest status report to the page for a project
- 🟥 Send email when a report created
- 🟥 Report of projects without status reports, by team lead

# Portfolio/Initiative

Portfolio managers will want to see their projects and manage them.

# Other notes on Django

Run through the scaffold for CRUD
GET /posts - index - get all, render
GET /posts/new - show form new.html with blank object
POST /posts - create - validate, then save and redirect, or render new.html with errors
GET /posts/:id - get single
GET /posts/:id/edit - edit form with existing object
PATCH /posts/:id - update. validate, then save and redirect, or render edit.html with ModelForm
DELETE /posts/:id - delete

Maybe look here: https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/
But also maybe look at a Rails scaffold new?
Answer is https://docs.djangoproject.com/en/4.0/ref/class-based-views/
