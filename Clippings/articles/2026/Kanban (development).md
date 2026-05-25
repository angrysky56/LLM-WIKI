---
title: "Kanban (development)"
source: "https://en.wikipedia.org/wiki/Kanban_(development)"
author:
  - "[[Wikipedia]]"
published: 2010-09-24
created: 2026-05-25
description:
tags:
  - "clippings"
---
![](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Abstract_Kanban_Board.svg/250px-Abstract_Kanban_Board.svg.png)

A Kanban board

**Kanban** ([Japanese](https://en.wikipedia.org/wiki/Japanese_language "Japanese language"): 看板, meaning *[signboard](https://en.wikipedia.org/wiki/Signboard "Signboard")* or *[billboard](https://en.wikipedia.org/wiki/Billboard_\(advertising\) "Billboard (advertising)")*) is a [lean method](https://en.wikipedia.org/wiki/Lean_manufacturing "Lean manufacturing") to manage and improve work across human [systems](https://en.wikipedia.org/wiki/System "System"). This approach aims to manage work by balancing demands with available capacity, and by improving the handling of system-level [bottlenecks](https://en.wikipedia.org/wiki/Bottleneck_\(production\) "Bottleneck (production)").

Work items are visualized to give participants a view of progress and process, from start to finish—usually via a [kanban board](https://en.wikipedia.org/wiki/Kanban_board "Kanban board"). Work is [pulled](https://en.wikipedia.org/wiki/Push%E2%80%93pull_strategy#Complete_definition "Push–pull strategy") as capacity permits, rather than work being pushed into the process when requested.

In [knowledge work](https://en.wikipedia.org/wiki/Knowledge_worker "Knowledge worker") and in [software development](https://en.wikipedia.org/wiki/Software_development "Software development"), the aim is to provide a visual [process management](https://en.wikipedia.org/wiki/Business_process_management "Business process management") system which aids decision-making about what, when, and how much to produce. The underlying [kanban](https://en.wikipedia.org/wiki/Kanban "Kanban") method originated in [lean manufacturing](https://en.wikipedia.org/wiki/Lean_manufacturing "Lean manufacturing"),[^1] which was inspired by the [Toyota Production System](https://en.wikipedia.org/wiki/Toyota_Production_System "Toyota Production System").[^2] It has its origin in the late 1940s when the Toyota automotive company implemented a production system called just-in-time, which had the objective of producing according to customer demand and identifying possible material shortages within the production line. But it was a team at Corbis that realized how this method devised by Toyota could become a process applicable to any type of organizational process. Kanban is commonly used in software development in combination with methods and frameworks such as [Scrum](https://en.wikipedia.org/wiki/Scrum_\(software_development\) "Scrum (software development)").[^3]

## Kanban boards

The diagram here shows a software development workflow on a kanban board.[^4]

![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Sample_Kanban_Board.png/960px-Sample_Kanban_Board.png)

Kanban boards, designed for the context in which they are used, vary considerably and may show work item types ("features" and " [user stories](https://en.wikipedia.org/wiki/User_story "User story") " here), columns delineating workflow activities, explicit policies, and swimlanes (rows crossing several columns, used for grouping user stories by feature here). The aim is to make the general workflow and the progress of individual items clear to participants and stakeholders.

A Kanban Board represents the system's Definition of Workflow [^5] and requires the following minimum elements:

- A definition of the individual units of value that are moving through the workflow. These units of value are referred to as *work items* *(or items*).
- A definition for when work items are *started* and *finished* within the workflow. Your workflow may have more than one started or finished points depending on the work item.
- One or more defined states that the work items flow through from started to finished. Any work items between a started point and a finished point are considered *work in progress* (WIP).
- A definition of how WIP will be controlled from started to finished.
- Explicit policies about how work items can flow through each state from started to finished.
- A *service level expectation* (SLE), which is a forecast of how long it should take a work item to flow from started to finished.

## Kanban practices

The Practices of Kanban as described in the Kanban Guide [^6] are

- Defining and visualizing a workflow
- Actively managing items in a workflow
- Improving a workflow

Kanban is a strategy that aims to follow these in order to create systems that are efficient, effective, and predictable.

The Kanban Method is a specialized and detailed extrapolation of Kanban. As described in books on The Kanban Method for software development,[^7] [^3] the two primary practices of The Kanban Method are to visualize work and to limit work in progress (WIP). Four additional general practices of The Kanban Method listed in *Essential Kanban Condensed* are to make policies explicit, manage flow, implement feedback loops, and improve collaboratively.[^8]

The kanban board in the diagram above highlights the first three general practices of The Kanban Method.

- It visualizes the work of the development team (the features and user stories).
- It captures WIP limits for development steps: the circled values below the column headings that limit the number of work items under that step.
- It documents policies, also known as done rules,[^9] inside blue rectangles under some of the development steps.
- It also shows some kanban flow management for the "user story preparation", "user story development", and "feature acceptance" steps, which have "in progress" and "ready" sub-columns. Each step's WIP limit applies to both sub-columns, preventing work items from overwhelming the flow into or out of those steps.

## Managing workflow

Kanban manages workflow directly on the kanban board. The WIP limits for development steps provide development teams immediate feedback on common workflow issues.[^7] [^9]

For example, on the kanban board shown above, the "deployment" step has a WIP limit of five and there are currently five epics [^10] shown in that step. No more work items can move into deployment until one or more epics complete that step (moving to "delivered"). This prevents the "deployment" step from being overwhelmed. Team members working on "feature acceptance" (the previous step) might get stuck because they can't deploy new epics. They can see why immediately on the board and help with the current epic deployments.

Once the five epics in the "deployment" step are delivered, the two epics from the "ready" sub-column of "feature acceptance" (the previous step) can be moved to the "deployment" column. When those two epics are delivered, no other epics can be deployed (assuming no new epics are ready). Now, team members working on deployment are stuck. They can see why immediately and help with feature acceptance.

In a Kanban board setup, swimlanes are used to visually organize work into different stages of a process, ensuring clarity and focus. For efficient workflow management, it is crucial to maintain distinct swimlanes for key phases such as requirements, development, testing, and closed/completed tasks. Specifically, testing stories should always be placed within the designated "Testing" swimlane. This separation ensures that testing activities are easily trackable and not intermingled with other stories in development or other stages. By keeping testing tasks within their own swimlane, teams can quickly identify bottlenecks, prioritize issues, and maintain the integrity of the testing process without cross-contamination from development or requirement phases. This structure leads to clearer workflows and enhances team collaboration.

This workflow control works similarly for every step. Problems are visual and evident immediately, and re-planning can be done continuously. The work management is made possible by limiting work in progress in a way team members can see and track at all times.

## Evolution and documentation of method

David Anderson's 2010 book, *Kanban*,[^7] describes an evolution of the approach from a 2004 project at Microsoft [^11] using a [theory-of-constraints](https://en.wikipedia.org/wiki/Theory_of_constraints "Theory of constraints") approach and incorporating a [drum-buffer-rope](https://en.wikipedia.org/wiki/Theory_of_constraints#Operations "Theory of constraints") (comparable to the [kanban pull system](https://en.wikipedia.org/wiki/Kanban#Operation "Kanban")), to a 2006–2007 project at [Corbis](https://en.wikipedia.org/wiki/Branded_Entertainment_Network "Branded Entertainment Network") (a separate company, also founded by Bill Gates) in which the kanban method was identified. In 2009, Don Reinertsen published a book on second-generation lean product-development [^12] which describes the adoption of the kanban system and the use of data collection and an economic model for management decision-making. Another early contribution came from Corey Ladas, whose 2008 book *Scrumban* [^3] suggested that kanban could improve [scrum](https://en.wikipedia.org/wiki/Scrum_\(software_development\) "Scrum (software development)") for software development. Ladas saw [scrumban](https://en.wikipedia.org/wiki/Scrumban "Scrumban") as the transition from [scrum](https://en.wikipedia.org/wiki/Scrum_\(software_development\) "Scrum (software development)") to kanban. Jim Benson and Tonianne DeMaria Barry published *Personal Kanban*,[^13] applying kanban to individuals and small teams, in 2011. In *Kanban from the Inside* (2014),[^14] Mike Burrows explained kanban's principles, practices and underlying values and related them to earlier theories and models. In *Agile Project Management with Kanban* (2015),[^9] Eric Brechner provides an overview of kanban in practice at Microsoft and [Xbox](https://en.wikipedia.org/wiki/Xbox_Game_Studios "Xbox Game Studios"). *Kanban Change Leadership* (2015), by Klaus Leopold and Siegfried Kaltenecker,[^15] explained the method from the perspective of change management and provided guidance to change-initiatives. In 2016 Lean Kanban University Press published a condensed guide to the method, incorporating improvements and extensions from the early kanban projects.[^8]

In 2020 John Coleman and Daniel Vacanti published *The Kanban Guide* [^6] to describe the minimal conditions needed to operate a Kanban system. Colleen Johnson, Daniel Vacanti, and Prateek Singh published The Kanban Pocket Guide [^16] in 2022, which helps practitioners navigate the Kanban practices. Will Seele and Daniel Vacanti also published the Flow Metrics for Scrum Teams [^17] book in 2022 to bring the benefits of metrics commonly used in Kanban to Scrum teams.

[^1]: Womack, James P. (2007). *The Machine That Changed the World*. Simon & Schuster. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-1847370556](https://en.wikipedia.org/wiki/Special:BookSources/978-1847370556 "Special:BookSources/978-1847370556").

[^2]: Ohno, Taiichi (1988). *Toyota Production System: Beyond Large-Scale Production*. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0915299140](https://en.wikipedia.org/wiki/Special:BookSources/978-0915299140 "Special:BookSources/978-0915299140").

[^3]: Corey, Ladas (2008). *Scrumban and other essays on Kanban System for Lean Software development*. Seattle, Washington: Modus Cooperandi Press. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [9780578002149](https://en.wikipedia.org/wiki/Special:BookSources/9780578002149 "Special:BookSources/9780578002149"). [OCLC](https://en.wikipedia.org/wiki/OCLC_\(identifier\) "OCLC (identifier)") [654393465](https://search.worldcat.org/oclc/654393465).

[^4]: Boeg, Jasper (February 2012). ["Priming Kanban"](http://www.infoq.com/minibooks/priming-kanban-jesper-boeg). InfoQ. Retrieved 17 February 2014.

[^5]: Coleman, John; Vacanti, Daniel. ["Kanban Guide - Definition of Workflow"](https://kanbanguides.org/english/). *Kanban Guides*. Retrieved 17 August 2023.

[^6]: Coleman, John; Vacanti, Daniel. ["Kanban Guide"](https://kanbanguides.org/english/). *Kanban Guides*. Retrieved 17 August 2023.

[^7]: Anderson, David J. (April 2010). *Kanban: Successful Evolutionary Change for Your Technology Business*. Blue Hole Press. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-9845214-0-1](https://en.wikipedia.org/wiki/Special:BookSources/978-0-9845214-0-1 "Special:BookSources/978-0-9845214-0-1").

[^8]: Anderson, David J.; Carmichael, Andy (2016). *Essential Kanban Condensed*. Seattle, WA: Lean Kanban University Press. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-9845214-2-5](https://en.wikipedia.org/wiki/Special:BookSources/978-0-9845214-2-5 "Special:BookSources/978-0-9845214-2-5").

[^9]: Brechner, Eric (2015). *Agile Project Management with Kanban*. Microsoft Press. p. 160. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0735698956](https://en.wikipedia.org/wiki/Special:BookSources/978-0735698956 "Special:BookSources/978-0735698956").

[^10]: [""Mist""](https://web-mist.com/index.php/2025/03/22/work-using-kanban-wip/). *Mist*. Mist Technologies.

[^11]: Anderson, David J.; Dumitriu, Dragos (November 2005). [*From Worst to Best in 9 Months: Implementing a Drum-Buffer-Rope Solution at Microsoft's IT Department*](http://images.itrevolution.com/images/kanbans/From_Worst_to_Best_in_9_Months_Final_1_3-aw.pdf) (PDF). [TOC ICO](https://en.wikipedia.org/wiki/Theory_of_constraints#Certification_and_education "Theory of constraints") World Conference November 2005. USA: Microsoft Corporation. Retrieved 24 September 2020.

[^12]: Reinertsen, Donald (May 2009). *The Principles of Product Development Flow: Second Generation Lean Product Development*. Celeritas Publishing. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-1935401001](https://en.wikipedia.org/wiki/Special:BookSources/978-1935401001 "Special:BookSources/978-1935401001").

[^13]: Benson, Jim; DeMaria Barry, Tonianne (January 2011). *Personal Kanban: Mapping Work, Navigating Life*. Modus Cooperandi Press. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-1453802267](https://en.wikipedia.org/wiki/Special:BookSources/978-1453802267 "Special:BookSources/978-1453802267").

[^14]: Burrows, Mike (2014). *Kanban From The Inside*. Seattle, WA: Blue Hole Press. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-9853051-9-2](https://en.wikipedia.org/wiki/Special:BookSources/978-0-9853051-9-2 "Special:BookSources/978-0-9853051-9-2").

[^15]: Leopold, Klaus; Siegfried, Kaltenecker (2015). *Kanban Change Leadership*. Hoboken, NJ: John Wiley & Sons. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-1-119-01970-1](https://en.wikipedia.org/wiki/Special:BookSources/978-1-119-01970-1 "Special:BookSources/978-1-119-01970-1").

[^16]: Johnson, Colleen; Vacanti, Daniel; Singh, Prateek. ["The Kanban Pocket Guide"](https://prokanban.org/kpg/). *ProKanban.org*. Retrieved 17 August 2023.

[^17]: Seele, Wilbert; Vacanti, Daniel. ["Flow Metrics for Scrum Teams"](https://prokanban.org/scrum-flow-metrics/). *ProKanban.org*. Retrieved 17 August 2023.