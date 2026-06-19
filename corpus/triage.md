# Triage – Linear Docs

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
+ [![Board layout](https://webassets.linear.app/images/ornj730p/production/be0cea13263f8d3c8f30cb308e43aa39a89efaf5-16x16.svg?q=95&auto=format&dpr=2)Board layout](/docs/board-layout)
+ [![Timeline](https://webassets.linear.app/images/ornj730p/production/7cd0f5bcc0adcecf7c9a4c6826f1d74d781179a3-16x16.svg?q=95&auto=format&dpr=2)Timeline](/docs/timeline)
+ [![Custom Views](https://webassets.linear.app/images/ornj730p/production/3764d83105d8363f2abf4b6c17d19a8461b52df0-16x16.svg?q=95&auto=format&dpr=2)Custom Views](/docs/custom-views)
+ [![Triage](https://webassets.linear.app/images/ornj730p/production/75dc9339f72c82a109f282ededaada6215e27f72-16x16.svg?q=95&auto=format&dpr=2)Triage](/docs/triage)
+ [![User views](https://webassets.linear.app/images/ornj730p/production/c7f08466ba6347c192ad2c5356a88e7729f852aa-16x16.svg?q=95&auto=format&dpr=2)User views](/docs/user-views)
+ [![Peek preview](https://webassets.linear.app/images/ornj730p/production/384503d55fec91c578849d4b00a40e16f3f1a195-16x16.svg?q=95&auto=format&dpr=2)Peek preview](/docs/peek)
+ [![Label views](https://webassets.linear.app/images/ornj730p/production/71b5665d0601a111c6bc80f4cfc50bc3d026da09-16x16.svg?q=95&auto=format&dpr=2)Label views](/docs/label-views)
* Find and filter
* Linear Asks
* Integrations
* Analytics
* Administration
[Docs](/docs) [Developers](/developers) [Learn](/learn) [Contact support](/contact/support)
1. Teams
2. [Triage](#)
Copy page
[Sign up](/signup)[Open app](/signup)
Triage
======
Manage issues created by other teams and customer support integrations.
![Triage](https://webassets.linear.app/images/ornj730p/production/30183e73c9ef009bb8cb14adbe97d9f34a5b9a69-2352x1632.png?w=1440&q=95&auto=format&dpr=2)
Overview[⁠](#overview)
----------------------
Triage is a special inbox for your team. When an issue is created by integration or by a workspace member not belonging to your specific Linear team, it will appear here. Triage offers a opportunity to review, update, and prioritize issues before they are added to your team’s workflow. Consider using Triage responsibility to set a rotating schedule of ownership for monitoring incoming issues.
Configure[⁠](#configure)
------------------------
Go to your *Team Settings > Triage*. Once you toggle it on, Triage will appear under the team name in the sidebar.
Basics[⁠](#basics)
------------------
Navigate to Triage with `G` then `T`. If you are in another team’s views, use `O` then `T` to open the team you want to view first.
### Create issues[⁠](#create-issues)
New issues will default to Triage status if they are created through an integration (e.g. Slack, Sentry), created when inside of the Triage view, or if members outside of your specific team create the issue.
Setting default templates in Team Settings > Templates can override the triage status.
### Take actions[⁠](#take-actions)
Open the issue to review it and take one of the following issue actions: *accept* with `1`*, mark as duplicate* with `2`*, decline* with `3`*, or snooze* with `H`.
Accepting an issue will offer the option to leave a comment and then move the issue to your team’s defaultstatus.
To ask for more information from the user who created the issue, comment on the issue and keep it in Triage or snooze it until you’re ready to take an action.
**Marking as duplicate** will offer a choice of which existing issue to merge the duplicate into. Taking this action will also move the new issue’s attachments to the canonical issue, including [customer requests](https://linear.app/docs/customer-requests) and attachments. Once selected, the new issue is updated to a *Canceled* status type. The shortcut `MM` also triggers the mark as duplicate action.
**Declining** will update the issue to a *Canceled* status type and present the option of adding a comment with an explanation.
**Snoozing** will hide the issue from the triage queue to return at a time of your choosing, or when there’s new activity on that issue: whichever comes first. See snoozed Triage issues by toggling the preference in View Options. Snoozing hides the issue in Triage from other users by default as well.
Automation[⁠](#automation)
--------------------------
Triage Automations through Linear Agent, as well as Triage Intelligence, Triage Rules and Triage Responsibility are all available on our [Business](https://linear.app/pricing) and [Enterprise](https://linear.app/pricing) plans.
Triage supports a collection of automation that allow issues to be processed, enriched, and acted on automatically without manual overhead.
* [**Triage Rules**](https://linear.app/docs/triage#triage-rules) apply predefined actions when specific conditions are met
* [**Triage Intelligence**](https://linear.app/docs/triage#triage-intelligence) analyzes issues and is best used for routing to the right team and individual, while also setting properties based on context
* [**Triage Automations**](https://linear.app/docs/linear-agent#automations) extend this by letting you define more complex, open-ended behaviors for Linear Agent to act on issues
### Triage rules[⁠](#triage-rules)
Configure custom rules to take automated actions on issues when they enter Triage. Triggered on filterable properties, triage rules can update an issue’s team, status, assignee, label, project and priority.
Once configured, rules are executed in order from the top down. When moving issues to another team’s Triage via rule, the new team’s rules are applied to the issue as well. If rules conflict, this is surfaced in the interface.
Consider combining triage routing with [custom Asks fields](https://linear.app/docs/linear-asks#creating-additional-fields) to create a scalable system to intake issues from Slack. Users fill out what they know and automations send the issue to the right team or assignee.
To create a rule that triggers on when any condition in a set is true (like Customer name includes any of 3 customers,) hold `Shift` while selecting each customer name in the filter menu.
![two triage rules; if any of three customers set priority to high, and if labeled iOS move to team Mobile](https://webassets.linear.app/images/ornj730p/production/f41716bdc477cee4fadc5fabeff3bf47c09f27bc-1832x934.png?w=1440&q=95&auto=format&dpr=2)
### Triage Intelligence[⁠](#triage-intelligence)
Triage Intelligence allows LLMs to analyze every new issue in triage against your existing issues to suggest properties like assignee and label, and pro-actively surface likely related issues or duplicates based on the analysis of the issue’s content against historical behavior in your workspace.
Learn more about Triage Intelligence [here](https://linear.app/docs/triage-intelligence).
### Triage Automations[⁠](#triage-automations)
Triage Automations use Linear Agent to carry out flexible, instruction-based actions on issues in triage. They’re useful for solving complex workflows — like automated language translation, relevant document attachment, or comments made with additional information — that go beyond fixed rules or issue analysis.
Learn more in the [Linear Agent docs](https://linear.app/docs/linear-agent#automations).
![New Triage automation that adds documentation to relevant Linear issues when moving through Triage](https://webassets.linear.app/images/ornj730p/production/181a7422a7962ac90d91136c8353327bde52c3fd-2880x1623.heif?w=1440&q=95&auto=format&dpr=2)
### Triage responsibility[⁠](#triage-responsibility)
Enable triage responsibility to define who handles incoming issues. You can select specific members of your workspace to receive notifications of new issues or be automatically assigned to them. Configure triage responsibility in your team’s Triage settings.
![Triage view of a Linear workspace](https://webassets.linear.app/images/ornj730p/production/c40aa85cbcf9b1ae058bd94c2fb3dd7d2017270a-1784x515.png?w=1440&q=95&auto=format&dpr=2)
Once triage responsibility is set, optionally connect your PagerDuty, OpsGenie, Rootly, or Incident.io schedules to automate the rotation of first responders. If you use another provider, we have opened up that [API](https://studio.apollographql.com/public/Linear-API/variant/current/schema/reference/objects/Mutation?query=timeScheduleUpsertExternal#timeScheduleUpsertExternal) so you can build a custom schedule.
Members of your team will be able to easily see who is currently assigned to monitor triage when creating issues.
Integrations[⁠](#integrations)
------------------------------
### Asks[⁠](#asks)
Use Triage to seamlessly intake issues reported from non-Linear users through [Asks](https://linear.app/docs/linear-asks).
### Support integrations[⁠](#support-integrations)
Get more out of Triage by connecting it to our support integrations—Intercom, Front, and Zendesk—or Slack. Using these integrations, your support team can create new Linear issues or link customer reports to existing issues directly from their customer support tool.
FAQ[⁠](#faq)
------------
Can I require priority to be set before an issue leaves Triage?
Yes. Configure this behavior under Team Settings > Triage.
Why are issues in Triage not showing up in my views?
By default, we exclude triage issues from all views since triage is considered to be outside the normal workflow. To include them in a custom view, you need to explicitly include them by adding a status filter where “Triage” is included.
[Previous
Issue status](/docs/configuring-workflows)[Next
Create issues](/docs/creating-issues)
* [Overview](/docs/triage#overview)
* [Configure](/docs/triage#configure)
* [Basics](/docs/triage#basics)
* [Create issues](/docs/triage#create-issues)
* [Take actions](/docs/triage#take-actions)
* [Automation](/docs/triage#automation)
* [Triage rules](/docs/triage#triage-rules)
* [Triage Intelligence](/docs/triage#triage-intelligence)
* [Triage Automations](/docs/triage#triage-automations)
* [Triage responsibility](/docs/triage#triage-responsibility)
* [Integrations](/docs/triage#integrations)
* [Asks](/docs/triage#asks)
* [Support integrations](/docs/triage#support-integrations)
* [FAQ](/docs/triage#faq)