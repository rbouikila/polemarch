GUI workflow
==============

Welcome to Polemarch GUI
------------------------

In this section of our documentation we will tell you about Polemarch GUI's opportunities.

Let's begin with Dashboard page:

.. image:: gui_screenshots/dashboard.png

As you can see, Polemarch GUI provides user with 2 menus:

* the first one is located in the left sidebar and it is aimed
  to provide user with navigation between main system objects, like projects, inventories, history records and ect.

* the second one is located in the top right conner of browser window and it is aimed
  to navigate user to API section, to user's page and to logout page.

Also there are some widgets on content block of Dashboard page. User can customize Dashboard page as he wish.
For example, user can change widgets' position, hide some widgets or collapse them.

To change widgets' position user should click on 'lock' button. After this button has been clicked,
user is able to change widgets' position by Drag and Drop.

To collapse or to hide/show some widgets user should click on 'cogwheel' button. After this button has been clicked,
Polemarch opens modal window, where user can activate or collapse some widgets.


Before you start
----------------

Before you can do any job with Polemarch you should create at least one project, because all
Polemarch's functions are linked to the project.


Projects
--------

So, to start your work with Polemarch you should create project.

There are 3 project types in Polemarch:

* GIT - Polemarch can sync with your git project.

* TAR - If you don't have git repository, you can upload tar archive with project files
  from any http url.

* MANUAL - Empty project. This kind of project will be appropriate for you,
  if you want run only modules without any playbooks or something. Polemarch will
  create folder for your project files in `projects_dir` (you can specify it
  in settings) named as project id (you can see at URL), where you
  place manually your project files (like playbooks or something).

Let's look at the example of GIT project's creation:

.. image:: gui_screenshots/create_project.png

As you can see, the form of new project creation consist of 5 fields:

* **name** - name of your project.

* **repo type** - type of project repository (GIT, TAR, MANUAL).

* **repo URL** - URL to your repository.

* **repo auth type** - type of authentication (NONE, KEY, PASSWORD).

* **repo auth data** - key or password value.

After project creation you will see the next page:

.. image:: gui_screenshots/test_project_1.png
.. image:: gui_screenshots/test_project_2.png

As you can see there are some new fields on this page:

* **id** - |id_field_def|

* **status** - Polemarch project status.
  Possible values are:

  * NEW - newly created project,
  * WAIT_SYNC - repository synchronization has been scheduled, but has not started to perform yet,
  * SYNC - synchronization is in progress,
  * ERROR - synchronization failed,
  * OK - project is synchronized.

* **revision** - GIT project revision.

* **branch** - branch of your GIT project, to what your Polemarch project was synced.

* **owner** - |owner_field_def| project.

* **notes** - not required field for some user’s notes, for example,
  for what purpose this project was created or something like this.

* **information** - if project has “readme.md” or “readme.rst” file in it’s project directory,
  Polemarch will add content of this file to this field.

.. |id_field_def| replace:: the unique key of object in database.
.. |owner_field_def| replace:: user, who owns this

Also there are some new buttons:

Sublist buttons:

* **group** - this button opens project's group list.
* **history** - this button opens project executions' history list.
* **host** - this button opens project's host list.
* **inventory** - this button opens project's inventory list.
* **module** - this button opens project's module list.
* **periodic task** - this button opens project's periodic task list.
* **playbook** - this button opens project's playbook list.
* **template** - this button opens project's template list.
* **variables** - this button opens project's variables list.

Action buttons:

* **save** - |save_button_def|
* **copy** - |copy_button_def|
* **execute module** - this button opens "execute module" action page.
* **execute playbook** - this button opens "execute plabook" action page.
* **set owner** - |set_owner_button_def|
* **sync** - this button syncs your Polemarch project with GIT repository.
* **remove** - |remove_button_def| project.

.. |create_button_def| replace:: this button creates new
.. |save_button_def| replace:: this button saves all changes you have made on this page.
.. |copy_button_def| replace:: this button opens "copy" action page.
.. |set_owner_button_def| replace:: this button opens "set owner" action page.
.. |remove_button_def| replace:: this button deletes


If you update something in your GIT repository, don't forget to run sync in
Polemarch for pulling your changes.

As you can see, now project's status is "NEW", so we need to click on "sync" button
to get all needed data from your GIT project.

.. image:: gui_screenshots/test_project_3.png

After your project's status has been changed into "OK" you can confidently start working with Polemarch.


Module execution
---------------

The simplest way to start using Polemarch is to execute module.
To make this action click on 'execute module' button on project page.

.. image:: gui_screenshots/execute_module_1.png

As you can see, there are 2 fields on this page:

* **module** - autocomplete field with the list of project's modules.
* **add field** - select field, that provides user with new variables field for module execution.

Also there is only one button on this page:

* **exec** - |exec_button_def|

.. |exec_button_def| replace:: this button starts action execution.

For example, let's execute module **shell** on **localhost** with argument **uptime**.
To do it we need to add next fields:

* **inventory** - it can be inventory from database or just list of hosts, that are separated by ",".
* **group** - to which hosts from inventory execute this module.
* **connection** - type of connection.
* **args** - list of arguments for current module.

After all fields have been filled, our page started look like:

.. image:: gui_screenshots/execute_module_2.png

So, let's execute our first task on Polemarch! To do it click on "exec" button.

When status of your module execution changes to "OK" you will see the next page:

.. image:: gui_screenshots/execute_module_3.png
.. image:: gui_screenshots/execute_module_4.png
.. image:: gui_screenshots/execute_module_5.png


Template
--------

In previous abstract to execute module we needed to fill several fields.
To do it before every module/playbook is rather inconvenient.
In this case Polemarch templates save our time and nerves.
Polemarch template is an object, that saves all options that user used during task execution.

For example, let's create tast template (template that uses playbooks).
To do it click on "template" button on project page.

.. image:: gui_screenshots/create_template.png

As you can see, there are no templates in the project's template list now.

There is only one button here:

* **create** - |create_button_def| template.

To create template click on "create" button on this page.

.. image:: gui_screenshots/create_template_2.png

As you can see, there are several fields on this page:

* **name** - name of template.

* **notes** - not required field for some user’s notes, for example,
  for what purpose this template was created or something like this.

* **type** - type of template (MODULE or TASK).

* **inventory** - it can be inventory from database or just list of hosts, that are separated by ",".

* **playbook** - name of playbook, which template will use during execution.

After all fields have been filled, our page started look like:

.. image:: gui_screenshots/create_template_3.png

After template creation you will see the next page:

.. image:: gui_screenshots/create_template_4.png

As you can see there is only one new fields on this page:

* **id** - |id_field_def|

Also there are several buttons here:

Sublist buttons:

* **option** - this button opens template's option list.
* **variables** - this button opens project's variables list.

Action buttons:

* **save** - |save_button_def|
* **execute** - this button opens "execute template" action page.
* **remove** - |remove_button_def| template.

Before template execution we need to create variable "connection=local",
because we use "localhost" as inventory.

To do it, click on "variables" button.

.. image:: gui_screenshots/create_template_variable.png

As you can see, there are no variables in the template's variables list now.

There is only one button here:

* **create** - |create_button_def| variable.

To create variable click on "create" button on this page.

.. image:: gui_screenshots/create_template_variable_2.png

As you can see, there are only 2 fields on this page:

* **key** - key of variable.

* **value** - value of variable.

There is only one button here:

* **create** - |create_button_def| variable.

To save our variable click on "create" button.

Now we are ready to execute our template. To do it come back to template page:

.. image:: gui_screenshots/create_template_4.png

And click on "execute" button.

.. image:: gui_screenshots/execute_template_1.png

As you can see, there is only 1 field on this page:

* **option** - autocomplete field with the list of template's options.

Also there is only one button on this page:

* **exec** - |exec_button_def|

We do not have any template's options in our system, so just click on "exec" button.

When status of your template execution changes to "OK" you will see the next page:

.. image:: gui_screenshots/execute_template_2.png
.. image:: gui_screenshots/execute_template_3.png
.. image:: gui_screenshots/execute_template_4.png


Periodic tasks
--------------

Now let's imagine, that you need to execute some task (module/playbook/template)
with some interval or on the first day of month, for example, and you do not want
to execute it everytime by yourself.

In this case, Polemarch has such useful object type, as periodic task.

Periodic task - is a module/playbook/template execution
which Polemarch makes by himself with some interval.

Let's create periodic task, based on our "test-task-template".
To do it open project page:

.. image:: gui_screenshots/test_project_3.png

And click on "periodic task" button:

.. image:: gui_screenshots/periodic_task_empty_list.png

As you can see, there are no periodic tasks in the project's periodic task list now.

There is only one button here:

* **create** - |create_button_def| periodic task.

To create periodic task click on "create" button on this page.

.. image:: gui_screenshots/create_periodic_task_1.png

As you can see, the form of new periodic task creation consist of following fields:

* **name** - name of your periodic task.

* **task type** - type of periodic task (PLAYBOOK, MODULE, TEMPLATE).

* **mode** - name of module or playbook (for periodic tasks with PLAYBOOK/MODULE type only).

* **inventory** - it can be inventory from database or just list of hosts, that are separated by ","
  (for periodic tasks with PLAYBOOK/MODULE type only).

* **template** - name of template (for periodic tasks with TEMPLATE type only).

* **template opt** - name of template's option (for periodic tasks with TEMPLATE type only).

* **save result** - boolean field, it means to save or not to save results of periodic tasks execution in history.

* **enable** - - boolean field, it means to activate or deactivate periodic task.

* **interval type** - type of execution interval (CRONTAB, INTERVAL).

* **schedule** - value of execution interval.
  If "interval type" = INTERVAL, value of this field means amount of seconds.
  If "interval type" = CRONTAB, value of this field means CRONTAB interval.

* **notes** - not required field for some user’s notes, for example,
  for what purpose this periodic task was created or something like this.

After all fields have been filled, our page started look like:

.. image:: gui_screenshots/create_periodic_task_2.png

After periodic task creation you will see the next page:

.. image:: gui_screenshots/test_periodic_task.png

As you can see there is only one new fields on this page:

* **id** - |id_field_def|

Also there are several buttons here:

Sublist buttons:

* **variables** - this button opens periodic task's variables list.

Action buttons:

* **save** - |save_button_def|
* **execute** - this button opens "execute periodic task" action page.
* **remove** - |remove_button_def| periodic task.

Let's start our periodic task execution. To do it click on "execute" button.

.. image:: gui_screenshots/periodic_task_execution_history.png

As you can see on history page, our 'test-periodic-task' executes every 10 seconds,
as we set it during periodic task creation.


Inventory
---------

If you don't want to use 'inventory' as just list of hosts separated by ",",
or do not have inventory file in you GIT project ("./inventory", for example),
you need to create it in Polemarch.

ATTENTION! Do not forget to add you inventory to project after it's creation.
To do it click on "inventory" button on project page.

By inventory’s creation, in this case, we understand creation of inventory,
which includes at least one group, which, in it’s turn, includes at least one host.
In other words, beside inventory user should create host and group.

To understand it better let’s look at next images, which will explain you how to create
inventory. Here you can see the form for inventory creation.

.. image:: gui_screenshots/create_inventory.png

As you can see, there are only 2 fields on this page:

* **name** - name of inventory.

* **notes** - not required field for some user’s notes, for example,
  for what purpose this inventory was created or something like this.

Also there is only one button there:

* **create** - |create_button_def| inventory.

After inventory creation you will see the next page:

.. image:: gui_screenshots/test_inventory.png

As you can see there are 2 new fields on this page:

* **id** - |id_field_def|

* **owner** - |owner_field_def| inventory.

Also there are some new buttons here:

Sublist buttons:

* **all groups** - this button opens inventory's all groups list
  (list of groups, which includes also groups that are nested into inventory groups).
* **all hosts** - this button opens inventory's all hosts list.
  (list of hosts, which includes also hosts that are nested into inventory groups).
* **group** - this button opens inventory's group list.
* **host** - this button opens inventory's host list.
* **variables** - this button opens inventory's variables list.

Action buttons:

* **save** - |save_button_def|
* **copy** - |copy_button_def|
* **set owner** - |set_owner_button_def|
* **remove** - |remove_button_def| inventory.

Let’s look how you can create a group for this inventory.
To do it, let’s click on "group" button.


Group
-----

.. image:: gui_screenshots/test_inventory_group.png

As you can see, there are no groups in the inventory's group list now.

There are 2 buttons here:

* **create** - |create_button_def| group.
* **add** - this button opens the all group list from database,
from which you can choose group for this inventory.

We need to create group. To do it click on "create" button.

.. image:: gui_screenshots/create_group.png

As you can see, the form of new group creation consist of following fields:

* **name** - name of your group.

* **contains groups** - boolean field, it means ability of group to contain child groups.

* **notes** - not required field for some user’s notes, for example,
  for what purpose this group was created or something like this.

After group creation you will see the next page:

.. image:: gui_screenshots/test_group.png

As you can see there are 2 new fields on this page:

* **id** - |id_field_def|

* **owner** - |owner_field_def| group.

Also there are some new buttons here:

Sublist buttons:

* **host** - this button opens group's host list.
* **variables** - this button opens group's variables list.

Action buttons:

* **save** - |save_button_def|
* **copy** - |copy_button_def|
* **set owner** - |set_owner_button_def|
* **remove** - |remove_button_def| group.

Let’s look how you can create a host for this group.
To do it, let’s click on "host" button.


Host
----

.. image:: gui_screenshots/test_inventory_group_host.png

As you can see, there are no hosts in the group's host list now.

There are 2 buttons here:

* **create** - |create_button_def| host.
* **add** - this button opens the all host list from database,
from which you can choose host for this group.

We need to create host. To do it click on "create" button.

.. image:: gui_screenshots/create_host.png

As you can see, the form of new host creation consist of following fields:

* **name** - name of your host.

* **notes** - not required field for some user’s notes, for example,
  for what purpose this host was created or something like this.

* **type** - type of host (RANGE, HOST).
  * RANGE -  range of IPs or hosts.
  * HOST - single host.

After host creation you will see the next page:

.. image:: gui_screenshots/test_host.png

As you can see there are 2 new fields on this page:

* **id** - |id_field_def|

* **owner** - |owner_field_def| host.

Also there are some new buttons here:

Sublist buttons:

* **variables** - this button opens host's variables list.

Action buttons:

* **save** - |save_button_def|
* **copy** - |copy_button_def|
* **set owner** - |set_owner_button_def|
* **remove** - |remove_button_def| host.

Let’s look how you can create a variables for host, group and inventory.


Variables for inventory, group, host
------------------------------------

The process of variable creation for inventory is the same as for group or host.
So, let's look it at the example of variable creation for host.

.. image:: gui_screenshots/test_host.png

To do it click on the "variables" button on the host page:

.. image:: gui_screenshots/test_host_variables.png

As you can see, there are no variables in the host's variables list now.

There is only 1 button here:

* **create** - |create_button_def| variable.

To create variable click on "create" button:

.. image:: gui_screenshots/test_host_variables_1.png

As you can see, the form of new host variable creation consist of following fields:

* **key** - key of variable.

* **value** - value of variable.

After variable creation you will see the next page:

.. image:: gui_screenshots/test_host_variables_2.png

As you can see there is only 1 new field on this page:

* **id** - |id_field_def|


Import inventory
----------------

If you have some inventory file and you want to add objects from it to Polemarch
you can do it in rather simple, convenient and quick way: let us introduce you
very useful action - "Import inventory".

For example, let's use next inventory file:

.. sourcecode:: ini

    [imported-test-group]
    imported-test-host ansible_host=10.10.10.17

    [imported-test-group:vars]
    ansible_user=ubuntu
    ansible_ssh_private_key_file=example_key

To import inventory you should open inventory list page:

.. image:: gui_screenshots/import_inventory.png

And click on "Import inventory" button. Then you will see the next page:

.. image:: gui_screenshots/import_inventory_2.png

As you can see, the form of "Import inventory" action consist of 2 fields:

* **name** - name of your inventory.
* **inventory file** - value of your inventory file.

After filling of all fields you should click on "Exec" button and then you will see
page of your imported inventory:

.. image:: gui_screenshots/import_inventory_3.png

This inventory includes "imported-test-group" from imported inventory file:

.. image:: gui_screenshots/import_inventory_4.png

And "imported-test-group" includes "imported-test-host" from imported inventory file:

.. image:: gui_screenshots/import_inventory_5.png

"imported-test-host" includes variable "ansible-host" from imported inventory file:

.. image:: gui_screenshots/import_inventory_6.png


.polemarch.yaml
---------------

``.polemarch.yaml`` is a file for a quick deployment of Polemarch project.
By quick deployment of Polemarch project we mean automatic creation of some templates
for this project (during project sync) and using of additional interface for quick task execution.

``.polemarch.yaml`` is not required file for Polemarch work,
but if you want to use features of ``.polemarch.yaml``, you have to store it in
the base directory of (GIT, MANUAL, TAR) project.

Structure of ``.polemarch.yaml`` consists of next fields:

* **sync_on_run** - boolean, it means to get or not to get settings from ``.polemarch.yaml``
  during each project sync.
* **templates** - dictionary, consists of template objects
  (their structure is similar to template's API structure except the 'name' field).
* **templates_rewrite** - boolean, it means to rewrite or not to rewrite templates in project
  with names equal to templates' names from ``.polemarch.yaml``.
* **view** - dictionary, it is a description of web-form, that will be generated from ``.polemarch.yaml``.
  It consists of:

  * **fields** - dictionary, it consists of objects, that describe fields properties:

    * **title**: title of field, that Polemarch will show in web-form.
    * **default**: default value of field. Default: '' - for strings, 0 - for numbers.
    * **format**: format of field. For today next field formats are available: string, integer, float, boolean. Default: string.
    * **help**: some help text for this field.

  * **playbooks** - dictionary, it consists of objects, that describes playbook properties:

    * **title**: title of playbook, that Polemarch will use during playbook execution.
    * **help**: some help text for this playbook.

Example of ``.polemarch.yaml``:

.. sourcecode:: yaml

    ---
    sync_on_run: true
    templates:
        test-module:
            notes: Module test template
            kind: Module
            data:
                group: all
                vars: {}
                args: ''
                module: ping
                inventory: localhost,
            options:
                uptime:
                    args: uptime
                    module: shell
        test playbook:
            notes: Playbook test template
            kind: Task
            data:
                vars: {"become": true}
                playbook: main.yml
                inventory: localhost,
            options:
                update: {"playbook": "other.yml"}
    templates_rewrite: true
    view:
        fields:
            string:
                title: Field string
                default: 0
                format: string
                help: Some help text
            integer:
                title: Field integer
                default: 0
                format: integer
                help: Some help text
            float:
                title: Field float
                default: 0
                format: float
                help: Some help text
            boolean:
                title: Field boolean
                default: 0
                format: boolean
                help: Some help text
            enum_string:
                title: Field enum_string
                default: 0
                format: string
                help: Some help text
                enum: ['Choice1', 'Choice2', 'Choice3']
            unknown:
                title: Field unknown
                default: 0
                format: invalid_or_unknown
                help: Some help text
        playbooks:
            main.yml:
                title: Execute title
                help: Some help text


In GUI process of working with ``.polemarch.yaml`` will be the following:

Firstly, you need to create a project with ``.polemarch.yaml``
(or to add ``.polemarch.yaml`` to existing project).
For example, let's create new GIT project, that has in its base directory ``.polemarch.yaml`` file
from the example above:

.. image:: gui_screenshots/create_project_with_polemarch_yaml.png

In the field 'repo url' you should insert url of project that has in its base directory
``.polemarch.yaml`` file.

After project creation you will see the ordinary project page:

.. image:: gui_screenshots/create_project_with_polemarch_yaml_2.png

Then you need to click on "sync" button. After project synchronization you will see the next page:

.. image:: gui_screenshots/create_project_with_polemarch_yaml_3.png
.. image:: gui_screenshots/create_project_with_polemarch_yaml_4.png

As you can see, all fields that we mentioned in the exmaple ``.polemarch.yaml`` were added
to this web-form.

Also templates from ``.polemarch.yaml`` were added to just created Polemarch project.

.. image:: gui_screenshots/create_project_with_polemarch_yaml_5.png

Hooks
-----

Polemarch has his own system of hooks.
Polemarch hooks are synchronous and you can appoint them on different events
like “after end task”, “before start task” and so on.

WARNING: You should be accurate with hooks appointment,
because the more hooks you have, the more time they need for execution and,
finally, the more time Ansible needs for task execution.

.. image:: gui_screenshots/hooks_empty_list.png

As you can see, there are no hooks in the system now.

There is only one button here:

* **create** - |create_button_def| hook.

To create hook click on "create" button.

.. image:: gui_screenshots/create_hook.png

As you can see, the form of new hook creation consist of following fields:

* **name** - name of your hook.

* **type** - type of hook (HTTP, SCRIPT).
  * If type is "HTTP", Polemarch will send "POST" request with JSON to all recipients.
  * If type is "SCRIPT", Polemarch will execute script.

* **when** - event on each Polemarch have to execute hook.

* **enable** - boolean field, it means to activate or to deactivate hook.

* **recipients** - list of recipients, separated by " | ".
  For example, "ex1.com | ex2.com | ex3.com".


Users
-----

Polemarch provides you with several types of user:

* superuser;
* staff.

If you need to create a superuser, you need to do it with terminal command.
Look for more information here :doc:`"Create superuser" </quickstart>`.

If you need to create user with "staff" rights you can do it with Polemarch GUI:

.. image:: gui_screenshots/user_list.png

To create new user click on "create" button.

.. image:: gui_screenshots/create_user.png

As you can see, the form of new user creation consist of following fields:

* **username** - name of new user.

* **is active** - boolean field, it means to activate or to deactivate user.

* **first name** - first name of user.

* **last name** - last name of user.

* **email** - email of user.

* **password** - password of user.

* **repeat password** - password of user.

After user creation you will see next page:

.. image:: gui_screenshots/test_user.png

As you can see there is only one new fields on this page:

* **id** - |id_field_def|

Also there are several buttons here:

Sublist buttons:

* **settings** - this button opens dashboard settings of current user.

Action buttons:

* **save** - |save_button_def|
* **copy** - |copy_button_def|
* **change password** - this button opens "change password" action page.
* **remove** - |remove_button_def| periodic task.


Let's look on user settings page:

.. image:: gui_screenshots/user_settings.png

This page has fields for managing dashboard chart line settings
and for managing dashboard settings.

Let's look on "change password" action page.

.. image:: gui_screenshots/change_password.png

As you can see, the form of "change password" action consist of following fields:

* **old password** - current password of user.

* **new password** - new password of user.

* **confirm new password** - new password of user.

There is only one button here:

* **exec** - |exec_button_def|