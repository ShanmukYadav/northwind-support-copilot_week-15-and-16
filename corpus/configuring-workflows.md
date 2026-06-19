# Issue status – Linear Docs

[Docs](/docs)
[Sign up](/signup)[Open app](/signup)
* Getting started
* Account
* AI
* Your sidebar
* Teams
+ [![Teams](https://webassets.linear.app/images/ornj730p/production/6e7550f4fb9c615b503b5d4cee37cd041a262694-16x16.svg?q=95&auto=format&dpr=2)Teams](/docs/teams)
+ [![Private teams](https://webassets.linear.app/images/ornj730p/production/6b407fc5b34b1f41e730a873cad015e2a9de0678-16x16.svg?q=95&auto=format&dpr=2)Private teams](/docs/private-teams)
+ [![Sub-teams](https://webassets.linear.app/images/ornj730p/production/b2e524167129b68e4be926d18dff3d57b050e25c-16x16.svg?q=95&auto=format&dpr=2)Sub-teams](/docs/sub-teams)
+ [![Team pages](https://webassets.linear.app/images/ornj730p/production/41309383510a94f0087966d54e90ebc64a177f39-16x16.svg?q=95&auto=format&dpr=2)Team pages](/docs/default-team-pages)
+ [![Issue status](https://webassets.linear.app/images/ornj730p/production/80ad3ad6a4fb855f491f341737c8f8f5fb9cbcd2-16x16.svg?q=95&auto=format&dpr=2)Issue status](/docs/configuring-workflows)
+ [![Triage](https://webassets.linear.app/images/ornj730p/production/75dc9339f72c82a109f282ededaada6215e27f72-16x16.svg?q=95&auto=format&dpr=2)Triage](/docs/triage)
* Issues
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
1. Teams
2. [Issue status](#)
Copy page
[Sign up](/signup)[Open app](/signup)
Issue status
============
Set statuses that your issues will move through on each team.
![Image showing the workflow settings in a Linear workspace and the workspace statuses.](https://webassets.linear.app/images/ornj730p/production/c52f79b144c3ed5ed124e85d02e619b3429b1395-1922x1350.png?w=1440&q=95&auto=format&dpr=2)
Overview[⁠](#overview)
----------------------
Issues statuses define the type and order of states that issues can move through from start to completion. These workflows are team-specific and come with a default set and order: *Backlog > Todo > In Progress > Done > Canceled*. Issues marked as duplicates are automatically moved into a reserved *Duplicate* status.
Configure[⁠](#configure)
------------------------
Add or edit statuses in a team from **Settings -> Teams -> Issue statuses.** You will see a list of all statuses in that team and their order. Click the three dots next to each status and select **Edit** to make changes to the name, color, or description. Create statuses by clicking the **+** button, or remove statuses (as long as at least one status exists in each category).
Statuses can be rearranged within a category but categories cannot be moved around. To change the order of a status, drag it to a new position.
![Image showing 4 existing workflow statuses and a new custom one about to be added.](https://webassets.linear.app/images/ornj730p/production/1430c24b2218f7c515d2d9c067c66458abe5b0a4-1754x672.png?w=1440&q=95&auto=format&dpr=2)
![](https://webassets.linear.app/images/ornj730p/production/fe28ec4f7bbfbb43fa8aa5431c4cbef8158cc0d3-16x16.svg?q=95&auto=format&dpr=2)
**How we work at Linear**
We have the following workflow set up for our product team: *Backlog*: Icebox, Backlog
*Unstarted*: Todo
*Started*: In Progress, In Review, Ready to Merge
*Completed*: Done
*Canceled*: Canceled, Could not reproduce, Won’t Fix
*Duplicate*: Duplicate (applied automatically when an issue is marked as a duplicate)
### Default status[⁠](#default-status)
The default status defines the workflow status that will be applied to newly created issues in your team. This can be overridden by the user when creating an issue, but makes it a lot easier to track and organize new issues that come in. By default, your first *Backlog* status will be the default status. To change that, hover over a different status in the Backlog or Todo categories and then select **Make default**.
### Duplicate issue status[⁠](#duplicate-issue-status)
When you mark an issue as a duplicate of another, its status will change to *Duplicate*. You cannot create a custom duplicate status as it’s a fixed name in its own category. Duplicate is reported separately from canceled in reporting and insights, so duplicate issues appear as their own outcome rather than rolling up under canceled.
### Triage[⁠](#triage)
Triage is an additional status category that acts as an Inbox for your team. Triage is particularly powerful when combined with other integrations like Asks, Slack, or our support ticketing integrations. Learn more [here](https://linear.app/docs/triage).
Auto-close and auto-archive[⁠](#auto-close-and-auto-archive)
------------------------------------------------------------
When enabled, auto-close will *close* issues that have not been updated in a set period of time.
Auto-archive controls when issues in the team will be archived. When an issue archives, its creator will be notified—this is an opportunity to unarchive if the issue is still relevant. Archived issues are still searchable and restorable in the future.
Archiving is only automatic and is not available as a manual action. More information about archiving is available [here](https://linear.app/docs/delete-archive-issues).
The auto-archive setting also controls when projects and cycles will archive.
![Auto-close and auto-archive settings](https://webassets.linear.app/images/ornj730p/production/0a606026aaf048903bfb7b86585b5fecf24cb033-1418x968.png?w=1440&q=95&auto=format&dpr=2)
[⁠](#)
------
[Previous
Team pages](/docs/default-team-pages)[Next
Triage](/docs/triage)
* [Overview](/docs/configuring-workflows#overview)
* [Configure](/docs/configuring-workflows#configure)
* [Default status](/docs/configuring-workflows#default-status)
* [Duplicate issue status](/docs/configuring-workflows#duplicate-issue-status)
* [Triage](/docs/configuring-workflows#triage)
* [Auto-close and auto-archive](/docs/configuring-workflows#auto-close-and-auto-archive)