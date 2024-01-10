from marvin.beta.applications import Application
from marvin.tools.github import search_github_issues
from prefect import flow, task

@flow(log_prints=True)
def interaction_handler(user_query: str):
    with Application(
        name="Octocat",
        tools=[task(search_github_issues)],
        instructions=(
            "Scour GitHub for issues - if you don't find any"
            " results right away, try again with variations"
            " of the search terms. Ask the user if they want"
            " to want to focus on certain words or phrases."
            " Always give links to any results."
        )
    ) as app:
        app.say(user_query)
        print(
            "\n\n".join(
                m.content[0].text.value for m in app.default_thread.get_messages()
            )
        )

if __name__ == "__main__":
    import sys
    interaction_handler(
        sys.argv[1] if len(sys.argv) > 1 else "gh issues about k8s?"
    )