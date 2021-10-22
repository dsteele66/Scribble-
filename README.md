# Scribble-




Scribble is a Django application where users can read, write and interact with
the best content all around the world.

## Prerequisites

* Python
* `pipenv` and managing virtual environments
* Django views, templates, and models

## Instructions

1. Fork and clone this repository.
1. Change into the new directory and check out a dev branch.
1. Fulfill the listed requirements.

Build your Django application in the root of this repository. This exercise will require you to refer back to our previous lecture notes in order to set up a Django app from scratch. To see the steps for setting up a Django app with a Postgres database, refer back to our Tunr setup [instructions](https://git.generalassemb.ly/SEIR-32221/django-installation). 

When asked if you want to overwrite the readme, enter "n" (for no).

**This assignment is due Friday at 9am ET via Pull Request on the repository.**

## Requirements

### Models + Migrations

Create
[models](https://git.generalassemb.ly/SEIR-32221/django-models#models-10-min--040)
for Post and Comment

A `Post` should have the following fields:

* `author` (`CharField`)
* `title`  (`CharField`)
* `body` (`CharField`)

A `Comment` should have the following fields:

* `author` (`CharField`)
* `body` (`CharField`)
* `post` (`ForeignKey` for `Post`)

Create
[migrations](https://git.generalassemb.ly/SEIR-32221/django-models#migrations-10-min--050)
for Post and Comment

### Templates

Your Scribble app will need the following templates:

1. List template: Create an list template where a user can see all posts. Each
   post should link to its respective detail page.
2. Detail template: Create a detail template where a user can see each
   individual post. The show page should also list all of the post's comments.
3. Forms for creating Posts and Comments: Allow the user to create new posts and
   comments.
4. Updating and Editing: Allow the user to edit existing posts and comments.
5. Deletion: Allow the user to delete existing posts and comments.  You can add
   this form or link in the detail view for posts.

## Resources
Django documentation for [Models](https://docs.djangoproject.com/en/2.1/topics/db/models/) and [Migrations](https://docs.djangoproject.com/en/2.1/topics/migrations/). 

## Plagiarism

Take a moment to refamiliarize yourself with the [Plagiarism policy](https://git.generalassemb.ly/DC-WDI/Administrative/blob/master/plagiarism.md). Plagiarized work will not be accepted.

## [License](LICENSE)

1.  All content is licensed under a CC­BY­NC­SA 4.0 license.
1.  All software code is licensed under GNU GPLv3. For commercial use or
    alternative licensing, please contact legal@ga.co.
