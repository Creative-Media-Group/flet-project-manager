from flet import *


def main(page: Page):
    # SETUP
    page.title = "Todo App"
    page.window.width = 1800
    page.window.height = 1200
    page.theme_mode = ThemeMode.SYSTEM
    page.padding = 10
    page.adaptive = True
    LOGO_URL = "assets/icon.png"

    def sidebar():
        return Container(
            Column(
                [
                    TextButton(
                        "Tasks",
                        icon=icons.FACT_CHECK_OUTLINED,
                        on_click=lambda x: page.go("/home"),
                    ),
                    TextButton(
                        "Projects",
                        icon=icons.ACCOUNT_TREE_OUTLINED,
                        on_click=lambda x: page.go("/projects"),
                    ),
                    TextButton(
                        "Routine",
                        icon=icons.OFFLINE_BOLT_OUTLINED,
                    ),
                    TextButton(
                        "Notes",
                        icon=icons.STICKY_NOTE_2_OUTLINED,
                    ),
                    TextButton(
                        "Automations",
                        icon=icons.AUTO_AWESOME_OUTLINED,
                        on_click=lambda x: page.go("/automations"),
                    ),
                    TextButton(
                        "Reports",
                        icon=icons.PIE_CHART_ROUNDED,
                        on_click=lambda x: page.go("/reports"),
                    ),
                ],
                spacing=20,
            ),
            padding=16,
            border_radius=10,
        )

    # END SETUP
    task_list = {
        "name": "Linkedin",
        "timeline": "Sun 12/12 - Mon 1/13",
        "items": [
            {"completed": False, "label": "Dribble"},
            {"completed": False, "label": "Moodboard"},
            {"completed": False, "label": "App Exploration"},
            {"completed": False, "label": "Strategy Planning"},
        ],
    }

    design_task_list = {
        "name": "Landing",
        "timeline": "Sun 12/12 - Mon 1/13",
        "items": [
            {"completed": False, "label": "Wireframes"},
            {"completed": False, "label": "Mockups"},
            {"completed": False, "label": "User Experience"},
            {"completed": False, "label": "DB Design"},
        ],
    }

    design_task_list2 = {
        "name": "Dashboard",
        "timeline": "Sun 12/22 - Mon 1/24",
        "items": [
            {"completed": False, "label": "Wireframes"},
            {"completed": False, "label": "Mockups"},
            {"completed": False, "label": "User Experience"},
            {"completed": False, "label": "DB Design"},
        ],
    }

    dev_task_list = {
        "name": "Basic User",
        "timeline": "Sun 12/12 - Mon 1/13",
        "items": [
            {"completed": False, "label": "Frontend"},
            {"completed": False, "label": "API"},
            {"completed": False, "label": "DB Design"},
            {"completed": False, "label": "Backend"},
        ],
    }

    dev_task_list2 = {
        "name": "Admins",
        "timeline": "Sun 12/12 - Mon 1/13",
        "items": [
            {"completed": False, "label": "Frontend"},
            {"completed": False, "label": "API"},
            {"completed": False, "label": "DB Design"},
            {"completed": False, "label": "Backend"},
        ],
    }

    marketing_task_list = {
        "name": "Index",
        "timeline": "Sun 12/12 - Mon 1/13",
        "items": [
            {"completed": False, "label": "Website"},
            {"completed": False, "label": "Social Media"},
            {"completed": False, "label": "Analytics"},
            {"completed": False, "label": "Branding"},
        ],
    }

    sales_task_list = {
        "name": "Index",
        "timeline": "Sun 12/12 - Mon 1/13",
        "items": [
            {"completed": False, "label": "Cold Calling"},
            {"completed": False, "label": "Yearly Campaigns"},
            {"completed": False, "label": "Monthly Campaigns"},
            {"completed": False, "label": "Weekly Compaigns"},
        ],
    }

    def dates(tl):
        return Row(
            [
                Container(
                    Text(tl["timeline"]),
                    padding=8,
                    border_radius=10,
                ),
            ]
        )

    def NewTaskList(tl=[]):
        task_list_component = Container(
            Column(
                [
                    Row(
                        [
                            Text(tl["name"], weight=FontWeight.W_500, size=16),
                        ],
                        alignment=MainAxisAlignment.START,
                    ),
                    Column(
                        [
                            Row(
                                [
                                    Checkbox(),
                                    Text(tl["items"][ndx]["label"]),
                                ]
                            )
                            for ndx, task in enumerate(tl["items"])
                        ]
                        + [dates(tl)]
                    ),
                ]
            ),
            padding=10,
            border_radius=10,
            width=200,
        )
        return task_list_component

    navbar = Container(
        Row(
            [
                Row(
                    [
                        Image(
                            width=30,
                            height=30,
                            src=LOGO_URL,
                        ),
                        Text(page.title, ),
                    ]
                ),
                Row(
                    [
                        TextField(hint_text="Search"),
                        ElevatedButton(
                            "Search",
                        ),
                        Text("About", ),
                        Text("Contact", ),
                        IconButton(
                            icon=icons.SETTINGS_ROUNDED,
                        ),
                    ]
                ),
            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=10,
        border_radius=8,
    )
    main_area = Container(
        Column(
            [
                navbar,
                Container(
                    Row(
                        [
                            Row(
                                [
                                    IconButton(icons.ARROW_BACK_ROUNDED),
                                    Text("Health Application for PHD Health"),
                                ]
                            ),
                            ElevatedButton("Add Phase"),
                        ],
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    padding=10,
                    border_radius=10,
                ),
                ResponsiveRow(
                    [
                        Container(
                            Column(
                                [
                                    Container(
                                        Text("Research", width=160),
                                        padding=20,
                                        border_radius=6,
                                    ),
                                    NewTaskList(task_list),
                                    NewTaskList(task_list),
                                ]
                            ),
                            col={"sm": 12, "lg": 2},
                        ),
                        Container(
                            Column(
                                [
                                    Container(
                                        Text("Design", width=160),
                                        padding=20,
                                        border_radius=6,
                                    ),
                                    NewTaskList(design_task_list),
                                    NewTaskList(design_task_list2),
                                ]
                            ),
                            col={"sm": 12, "lg": 2},
                        ),
                        Container(
                            Column(
                                [
                                    Container(
                                        Text("Development", width=160),
                                        padding=20,
                                        border_radius=6,
                                    ),
                                    NewTaskList(dev_task_list),
                                    NewTaskList(dev_task_list2),
                                    NewTaskList(dev_task_list),
                                ]
                            ),
                            col={"sm": 12, "lg": 2},
                        ),
                        Container(
                            Column(
                                [
                                    Container(
                                        Text("Marketing", width=160),
                                        padding=20,
                                        border_radius=6,
                                    ),
                                    NewTaskList(marketing_task_list),
                                    NewTaskList(marketing_task_list),
                                ]
                            ),
                            col={"sm": 12, "lg": 2},
                        ),
                        Container(
                            Column(
                                [
                                    Container(
                                        Text("Sales", width=160),
                                        padding=20,
                                        border_radius=6,
                                    ),
                                    NewTaskList(sales_task_list),
                                ]
                            ),
                            col={"sm": 12, "lg": 2},
                        ),
                    ],
                    alignment=MainAxisAlignment.START,
                    vertical_alignment=CrossAxisAlignment.START,
                    spacing=20,
                ),
            ]
        ),
        expand=True,
    )

    # ROUTING
    bar = NavigationBar(
        destinations=[
            NavigationBarDestination(icon=icons.EXPLORE, label="Home"),
            NavigationBarDestination(icon=icons.EXPLORE, label="Automations"),
            NavigationBarDestination(icon=icons.PIE_CHART_ROUNDED, label="Reports"),
            NavigationBarDestination(
                icon=icons.BOOKMARK_BORDER,
                selected_icon=icons.BOOKMARK,
                label="Store",
            ),
            NavigationBarDestination(
                icon=icons.ACCOUNT_TREE_OUTLINED, label="Projects"
            ),
        ],
        on_change=lambda x: page.go(
            f"/{x.control.destinations[x.control.selected_index].label.lower()}"
        ),
    )

    def render(path, controls=[Text("Hi")]):
        if page.route == f"{path}":
            page.views.append(View(f"{path}", controls))

    def route_change(route):
        page.views.clear()

        render(
            "/home",
            [
                AppBar(title=Text("Tasks")),
                Row(
                    [sidebar(), main_area], vertical_alignment=CrossAxisAlignment.START
                ),
                bar,
            ],
        )

        render(
            "/store",
            [
                AppBar(
                    title=Text("Store"),
                ),
                sidebar(),
                ElevatedButton("Go Home", on_click=lambda _: page.go("/home")),
                bar,
            ],
        )

        render(
            "/projects",
            [
                AppBar(
                    title=Text("Projects"),
                ),
                navbar,
                sidebar(),
                ElevatedButton("Go Home", on_click=lambda _: page.go("/home")),
                bar,
            ],
        )

        render(
            "/automations",
            [
                AppBar(
                    title=Text("Automations"),
                ),
                sidebar(),
                GridView([Text("Automations Page")]),
                ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),
                bar,
            ],
        )

        render(
            "/reports",
            [
                AppBar(
                    title=Text("Reports"),
                ),
                sidebar(),
                ElevatedButton("Go Home", on_click=lambda _: page.go("/reports")),
                bar,
            ],
        )

        page.update()

    page.on_route_change = route_change
    page.go(page.route)
    page.go("/home")
    # END ROUTING

    # GUI

    # END GUI

    # page.add(
    #     Row([sidebar(), main_area], vertical_alignment=CrossAxisAlignment.START)
    # )


app(target=main)
