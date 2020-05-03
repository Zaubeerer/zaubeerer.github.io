Title: Use GitLab to manage your issues in an agile way
Date: 2020-05-03
Category: Tools
Tags: GitLab, projects, agile, KanBan, productivity, automation, GitHub
Slug: gitlab-projects
Author: Robin Beer
status: published
Illustration: gitlab-board.png 
Summary: In this article you will learn how to use boards in GitLab to organize your issues using agile methods.

When you start working in bigger projects, you may know the problem:
Many issues in different projects and groups can become quite confusing.

It would be nice to organize issues in boards, as I described in the [GitHub project boards article](https://www.robin-beer.de/github-projects.html#github-projects), right?

It's possible in GitLab, too! And GitLab has a more automatized approach, which gets you up and running quicker.

So let's dive in.

## Initialization of a GitLab group with several subgroups and projects

We need a complex GitLab structure consisting of a group with several subgroups and projects.
If you already have one, you may skip the first two sections and directly go to [creation of boards](#creation-of-boards).

First, create a new group on www.gitlab.com/dashboard/groups, analogously to the [demonstration group](https://gitlab.com/demonstration-group) that I created for this tutorial, by clicking on `New group`:

![New group illustration]({static}/Tools/images/gitlab-boards/2020-05-03-17-28-16.png)

Then, populate the group with subgroups and projects:

![group structure]({static}/Tools/images/gitlab-boards/2020-05-03-18-09-41.png)

Now, instead of manually filling the projects with issues, you might want to import them from previously exported GitLab projects.

## Create projects based on exported projects

To export a project open it and go to `Settings > General > Advanced > Export project`. A link will be generated and send to you via email such that you can download the project export file containing all milestones, files and issues of the project. If you are not able to export projects from my [demonstration group](https://gitlab.com/demonstration-group), you can download the export files that I uploaded to the project [Project Exports](https://gitlab.com/demonstration-group/project-exports).

To import the exported project, simply click on `New project` and then select `Import project > GitLab export`:

![Import GitLab export]({static}/Tools/images/gitlab-boards/2020-05-03-17-42-02.png)

Fill in a name and `Choose File` the previously downloaded project export. That's it! You have created a project based on an export, so all issues from the export should be included.

When creating issues manually, you might notice, that you can't create issues in groups, but only in projects. Therefore, the groups `Team 1` and `Team 2` need projects, too.

If you have a simplified, complex subgroup and project structure, move on to the next section.

## Creation of boards

No need to create anything, GitLab has you covered!

Open the project [fancy frontend](https://gitlab.com/demonstration-group/code/fancy-frontend) and in the left sidebar, go to `Issues > Boards` and voilà, the boards are already available:

![How to open the issue board]({static}/Tools/images/gitlab-boards/2020-05-03-18-15-46.png)

Alternatively, you can open the board by clicking on this [Fancy Frontend Board URL](https://gitlab.com/demonstration-group/code/fancy-frontend). This is possible, because each board has its own URL which you can save as a shortcut in your browser.

The board should look like the following:

![Issue board]({static}/Tools/images/gitlab-boards/2020-05-03-18-18-45.png)

The `columns` are referred to as `lists` by GitLab. The lists `Open` and `Closed` have been automatically generated and `To Do` and `Doing` are suggested as `default lists`.

However, I suggest to create different lists than the default lists so just click `Nevermind, I'll use my own`.

## Creation of columns (lists)

In GitLab, you can create lists based on labels. Therefore, you first have to create a label to then create a respective list on the GitLab boards. You can create these labels on project or group level.
I suggest creating the labels `TO DO` and `DOING` on the highest group level, such that it is available in all groups and projects. 

Therefore, open the highest group (i.e. demonstration group in my case) and go to `Issues > Labels`. Then, click on `New label` and create the following labels:

![Group label creation]({static}/Tools/images/gitlab-boards/2020-05-03-18-27-53.png)

Go back to the project board, you have previously visited and `Add list` the new labels:

![Add list]({static}/Tools/images/gitlab-boards/2020-05-03-18-29-19.png)

Now, you can drag and drop from the open issues (i.e. the backlog) to the `TODO` and `DOING` label:

![Updated issue board view]({static}/Tools/images/gitlab-boards/2020-05-03-18-31-04.png)

With this, you can already reproduce the respective functionality I described in the [GitHub project boards article](https://www.robin-beer.de/github-projects.html#github-projects).

However, there are some more useful functionalities in GitLab's issue boards.

## Board scope

The issues that have been created in the different projects are accessible via the issue boards of the groups. Therefore, just go to the highest group again and go to `Issues > Board`:

![Group issue board]({static}/Tools/images/gitlab-boards/2020-05-03-18-35-42.png)

Again, you have to create the lists based on your own labels. So click on `Nevermind, I'll use my own` and `Add list`:

![Group issue board - cleaned]({static}/Tools/images/gitlab-boards/2020-05-03-18-36-50.png)

As we used the highest group labels, the project issues are automatically moved in the respective lists. Awesome!

From this high-level view, you can drag and drop the issues to the different lists. Additionally, the location of the projects in which the issues are defined is indicated on the issue cards. And you can create issues simply by clicking on the `+` of the respective lists, selecting the project where to create the issue in and naming it.

## Further useful functionalities

GitLab provides further useful functionalities, such as [quick actions using the right sidebar](#quick-actions-using-the-right-sidebar), [filtering issues](#filter-issue-boards) and [creation of further labels](#create-additional-labels-%22high-priority%22-and-%22low-priority%22).

### Quick actions using the right sidebar

From the issue board, you can `open an issue by clicking on its title`. Additionally, you can `open the right sidebar by clicking on the issue card surface` (not on the title). That sidebar offers many quick actions such as assigning, milestone and more:

![quick action sidebar]({static}/Tools/images/gitlab-boards/2020-05-03-18-49-15.png)

### Filter issue boards

By clicking in the `Search or filter results...` form, you can easily filter for assignees, milestones etc. thus reducing the amount of shown issues based on your criteria:

![filtered issue board]({static}/Tools/images/gitlab-boards/2020-05-03-18-51-05.png)

As opposed to GitHub, you don't have to type in exactly what you search, as GitLab will automatically suggest you different options. Neat!

### Create additional labels "high priority" and "low priority" 

To visualize priority implicitly, the issues can be sorted according to their priority (high position = high priority) within their `lists`.

Additionally, further issue labels can be created to visualize priority explicitly. Therefore, create the `labels` named `high priority` and `low priority` as described in [this previous section](#creation-of-columns-lists) on the highest group level.

Using the quick actions on the sidebar, you can add further labels to the issues, such that they now show the priority labels:

![priority labels on issue board]({static}/Tools/images/gitlab-boards/2020-05-03-18-56-23.png)

## Summary & Conclusion

In this article, we have checked out how to use GitLabs `issue boards` to organize your issues into `lists` (columns).

Therefore, we have used the built-in group and project boards. Using the columns `Open`, `To Do`, `Doing`, `Waiting for Feedback` and `Closed`, we can now intuitively visualize the progress of the issues.

Additionally, we can visualize the priority of the issues implicitly using the position (highest = highest priority) as well as explicitly using labels `high priority` and `low priority`.

We have seen, that issue board creation is as easy as it can be, because GitLab just provides them out-of-the-box for different levels (project, group, highest group). Additionally, one does not need to create automation rules, because GitLab manages lists as a function of labels.

So, what are you waiting for? Get back control over all the open issues and manage them using `GitLab's issue boards`!

Whether you use the `project board` with [Scrum](https://www.scrum.org/resources/what-is-scrum) or [KanBan](https://www.atlassian.com/agile/kanban), it will simplify prioritization and visualization of progress.

This can also be a game-changer in communicating workload and available resources with your colleagues, your mentors or your boss.

---

You like the idea of issue organization into boards, but are using GitHub?

Check out [the GitHub project boards article](https://www.robin-beer.de/github-projects.html#github-projects)!

Cheers!

Robin