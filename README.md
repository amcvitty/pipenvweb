Dodfather is an attempt to make a django app.

Maybe sprinkle some react ?

https://fractalideas.com/blog/making-react-and-django-play-well-together-single-page-app-model/

Hopefully avoid all that by making nice web things. Maybe even put in some jquery

TODO:

- [x] Store a project
- [x] Edit a project and save it
- [x] Delete a project
- [x] Search projects by title
- [ ] Add measures of success to a project
- [ ] Add team members (i.e create user model)
- [ ] Allow team members to sign off on the project when it's doodling
  - This probably means having a relationship table with a sign off field
- [ ] Track changes - maybe this is a big JSON field for the whole project
  - Include sign-off changes
  - How to make a view from a JSON representation of Project?
- [ ] Project lifecycle - allow submit for review
-

Run through the scaffold for CRUD
GET /posts - index - get all, render
GET /posts/new - show form new.html with blank object
POST /posts - create - validate, then save and redirect, or render new.html with errors
GET /posts/:id - get single
GET /posts/:id/edit - edit form with existing object
PATCH /posts/:id - update. validate, then save and redirect, or render edit.html with ModelForm
DELETE /posts/:id - delete

Maybe look here: https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/
But also maybe look at a Rails scaffold new
