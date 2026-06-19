# Parent and sub-issues – Linear Docs

[Docs](/docs)
[Sign up](/signup)[Open app](/signup)
* Getting started
* Account
* AI
* Your sidebar
* Teams
* Issues
+ [![Create issues](https://webassets.linear.app/images/ornj730p/production/edba0d8c37051e1993f867e9ca020865f4605fad-16x16.svg?q=95&auto=format&dpr=2)Create issues](/docs/creating-issues)
+ [![Edit issues](https://webassets.linear.app/images/ornj730p/production/1691f0f8b88115ac1330fcd227c8b2932182343d-16x16.svg?q=95&auto=format&dpr=2)Edit issues](/docs/editing-issues)
+ [![Assign and delegate issues](https://webassets.linear.app/images/ornj730p/production/4f138793712b3f9f7f0dc09ad7ef776c03fe2077-15x15.svg?q=95&auto=format&dpr=2)Assign and delegate issues](/docs/assigning-issues)
+ [![Select issues](https://webassets.linear.app/images/ornj730p/production/b61fa1aff4d024cf6dcf0134c2c45b8d76cf0b27-16x16.svg?q=95&auto=format&dpr=2)Select issues](/docs/select-issues)
+ [![Parent and sub-issues](https://webassets.linear.app/images/ornj730p/production/fb9f996198822ba4dd8358f4e37428278e9701dd-16x16.svg?q=95&auto=format&dpr=2)Parent and sub-issues](/docs/parent-and-sub-issues)
+ [![Issue templates](https://webassets.linear.app/images/ornj730p/production/e4f8aa58d39df0385e4c2bd2838a46dac1e2350b-16x16.svg?q=95&auto=format&dpr=2)Issue templates](/docs/issue-templates)
+ [![Issue documents](https://webassets.linear.app/images/ornj730p/production/bf94fdfa6ca4463af554db33839b57cedb25743d-16x16.svg?q=95&auto=format&dpr=2)Issue documents](/docs/issue-documents)
+ [![Comments and reactions](https://webassets.linear.app/images/ornj730p/production/22f4ef6d4c3409d3fe7b7bbf4a7690403eb47580-16x16.svg?q=95&auto=format&dpr=2)Comments and reactions](/docs/comment-on-issues)
+ [![Editor](https://webassets.linear.app/images/ornj730p/production/67a1003f1ee8621a913f3f3f4f5243b35e05a025-16x16.svg?q=95&auto=format&dpr=2)Editor](/docs/editor)
+ [![Delete and archive issues](https://webassets.linear.app/images/ornj730p/production/a6e257753e45982c7a7227be82fc81acc33d14d1-16x16.svg?q=95&auto=format&dpr=2)Delete and archive issues](/docs/delete-archive-issues)
+ [![Customer Requests](https://webassets.linear.app/images/ornj730p/production/59fcb7949a14589a81420ef9876b649a809ab2eb-17x16.svg?q=95&auto=format&dpr=2)Customer Requests](/docs/customer-requests)
+ [![Releases](https://webassets.linear.app/images/ornj730p/production/79ea9464c5f11a4c5e169601c75537720335362a-16x16.svg?q=95&auto=format&dpr=2)Releases](/docs/releases)
* Issue properties
* Projects
* Initiatives
* Cycles
* Views
* Find and filter
* Linear Asks
* Integrations
* Analytics
* Administration
[Docs](/docs) [Developers](/developers) [Learn](/learn) [Contact support](/contact/support)
1. Issues
2. [Parent and sub-issues](#)
Copy page
[Sign up](/signup)[Open app](/signup)
Parent and sub-issues
=====================
Use sub-issues to break down larger “parent” issues into smaller pieces of work.
![Linear app showing a parent issue with sub-issues](https://webassets.linear.app/images/ornj730p/production/a2c92123d2c244bb53f75e34970a5cb8417bd2c3-2340x1064.png?w=1440&q=95&auto=format&dpr=2)
Overview[⁠](#overview)
----------------------
Consider creating sub-issues when a set of work is too large to be a single issue but too small to be a project. Sub-issues are also ideal for splitting up work shared across teammates. When you add a sub-issue to another issue, the other issue becomes its “parent”.
Create a sub-issue[⁠](#create-a-sub-issue)
------------------------------------------
Create a sub-issue by opening the parent issue and clicking the `+ Add sub-issues` button below the issue description. This will launch the sub-issue editor.
Create sub-issues from the command menu by searching for **Create sub-issue**, or use `Cmd/Ctrl``Shift``O` to open the sub-issue editor. To create multiple sub-issues at once, paste a list of issue titles into the editor or choose **Create multiple issues** from the command menu.
When you save a sub-issue, it will automatically launch the editor to create a new one. If you want to create a new one with the same values (labels/assignee etc.) you can press `Cmd/Ctrl``Shift``Enter`or Shift-click the save button. Press `Esc` to exit the sub-issue editor and continue updating the parent issue.
You can turn a comment under an issue into a sub-issue by hovering over a comment and clicking the `…` menu then *“new sub-issue from comment”.* Selecting a comment’s text and pressing `Cmd/Ctrl``Shift``O` will also create a sub-issue.
If you have a list (bulleted, numbered or checklist) you can highlight the checklist and hit `Cmd/Ctrl``Shift``O` to convert to sub-issues or choose the *“Create sub-issues(s) from selection”* item in the formatting toolbar.
You can add a template using the templates icon when creating a sub-issue or using the command menu under “Create new sub-issue from template” when viewing the parent.
Copy properties[⁠](#copy-properties)
------------------------------------
Sub-issues inherit the parent issue’s team, priority, and project. They may also inherit its cycle when created in an active status. Labels are not inherited.
The assignee is inherited if you are assigned to the parent, or if all existing sub-issues share the parent’s assignee.
You can add sub-issues after saving the parent issue.
You can duplicate a parent and its sub-issues from the Parent’s `...` menu under *“Duplicate”* and hit the toggle *“Include sub-issues”.*
Status automation[⁠](#status-automation)
----------------------------------------
Optionally, configure the following behaviors at the team level (Settings > Team > Workflow) to automate status relations between parent and sub-issues. Status changes triggered by Git integrations will also respect these automations.
**Parent auto-close**
When all sub-issues are marked as done, the parent issue will also be marked as done automatically.
**Sub-issue auto-close**
When the parent issue is marked as done, all remaining sub-issues will also be marked as done.
Converting issues[⁠](#converting-issues)
----------------------------------------
### Turn issues into sub-issues[⁠](#turn-issues-into-sub-issues)
Turn an existing issue(s) into sub-issues of another issue by selecting one or multiple issues and then taking the action to set the parent issue. This action is accessible from the command menu or by pressing `Cmd` `Shift` `P` and selecting a parent issue.
### Turn issues into parent issues[⁠](#turn-issues-into-parent-issues)
To make an existing issue a parent issue of another issue, hover over a sub-issue and take the action *“Set Parent”* in the contextual menu, command menu or `...` menu.
### Turn sub-issues into issues[⁠](#turn-sub-issues-into-issues)
You can turn a sub-issue into a regular issue again using the `⌘/ctrl``K` menu option “Remove parent”.
### Turn issues into projects[⁠](#turn-issues-into-projects)
Sometimes an issue grows so large it’s more appropriate to turn it into a project instead. To do so, hover over the parent’s `...` menu and choose “*Convert to project.”* When you convert a parent issue into a project, the original issue and its sub-issues are added to the project as standalone issues. The original issue is renamed to indicate the conversion, and sub-issue relationships are removed.
Filter sub-issues[⁠](#filter-sub-issues)
----------------------------------------
You can usually set the view to show or hide sub-issues in [Display Options.](https://linear.app/docs/display-options) You can also use [Filters](https://linear.app/docs/filters) to show only top-level (parent) issues, issues with sub-issues, or only sub-issues. If you use these filters frequently, consider creating a [custom view.](https://linear.app/docs/custom-views)
You can also hide completed sub-issues by default under the `...` menu and toggling “Always hide completed sub-issues”.
You can also sort your sub-issues under an issue from the `…` menu and *“Order by”* though this only updates it for the current user, not globally.
Display options[⁠](#display-options)
------------------------------------
When looking at sub-issues from the context of their parent issue, you can customize the order of the sub-issues and the properties that display.
![sub-issue display options menu](https://webassets.linear.app/images/ornj730p/production/66557cbd02b0b0d4b3dbbdcbcd1a42d1efbc677a-2856x1410.png?w=1440&q=95&auto=format&dpr=2)
[Previous
Select issues](/docs/select-issues)[Next
Issue templates](/docs/issue-templates)
* [Overview](/docs/parent-and-sub-issues#overview)
* [Create a sub-issue](/docs/parent-and-sub-issues#create-a-sub-issue)
* [Copy properties](/docs/parent-and-sub-issues#copy-properties)
* [Status automation](/docs/parent-and-sub-issues#status-automation)
* [Converting issues](/docs/parent-and-sub-issues#converting-issues)
* [Turn issues into sub-issues](/docs/parent-and-sub-issues#turn-issues-into-sub-issues)
* [Turn issues into parent issues](/docs/parent-and-sub-issues#turn-issues-into-parent-issues)
* [Turn sub-issues into issues](/docs/parent-and-sub-issues#turn-sub-issues-into-issues)
* [Turn issues into projects](/docs/parent-and-sub-issues#turn-issues-into-projects)
* [Filter sub-issues](/docs/parent-and-sub-issues#filter-sub-issues)
* [Display options](/docs/parent-and-sub-issues#display-options)