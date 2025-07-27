# Wikipedia Research Assistant (with MCP)

## Overview
MCPs allow applications to provide context for LLMs in a standardized way.
In this project, we use the [Python MCP SDK](https://github.com/modelcontextprotocol/python-sdk) to power
a simple Wikipedia research assistant. The MCP communicates with a server that communicates with
the Wikipedia API to retrieve information.

One can ask questions like "Tell me about Alan Turing" or "Summarize the topic of photosynthesis"
and expect structured results.

## Client
The client establishes an MCP session, loads the appropriate tools, and
loads a LangGraph with built-in routing for tools and chat, (connected to Open AI through an API key
that should be populated in a .env file).

The standard behavior of the agent is to invoke the LLM, unless the /prompt or /resource features are used.

### Prompts
The server exposes two fleshed out prompts with formatting instructions: highlight_sections_prompt and find_fun_fact_prompt.
The client can invoke these with: `/prompt highlight_sections_prompt <topic>` or `/prompt find_fun_fact_prompt <topic>`.
Ensure there are no spaces within `<topic>`.

### Resources
A few example topics are provided through `/resource suggested_titles`.

## Server
 The server exposes three tools to (1) fetch information from the Wikipedia page, (2) list the sections of a page,
 and (3) get the contents of a specific section.

These tools may be triggered through a natural language prompt (e.g. "List the sections in the carbon cycle article.")
or indirectly through the prompts.

## Example Usage

Run the server and client files. From the client, example usage:
```
You: What does the section on Terminology in the article on Samurai say?

AI: The section on "Terminology" in the article on Samurai explains that the proper Japanese term for a warrior is "bushi," which means "warrior family," and was used to refer to elite warriors who fought on horseback. The word "samurai" was originally colloquial, initially referring to domestic servants, and later to landless foot soldiers serving vassals. Over time, the meaning of "samurai" evolved, and during the Tokugawa period, it generally referred to higher-ranking retainers, although the usage could vary by class and region.

You: What are the sections of the butter chicken article?

AI: The sections of the butter chicken article are "History," "Preparation," "See also," "References," and "Bibliography."

You: What are the sections of Concertgebouw article?

AI: The article on "Concertgebouw" appears to cover multiple topics, including the Concertgebouw in Amsterdam, the Royal Concertgebouw Orchestra, the Concertgebouw in Bruges, and Concertgebouw de Vereeniging. Would you like information on a specific one of these?

You: Amsterdam

AI: The sections of the article on the Concertgebouw in Amsterdam are "History," "Building," "Organ," "Names of composers in the Main Hall," "See also," "References," and "External links."

You: Teach me about the History.

AI: The history of the Concertgebouw in Amsterdam begins with its architect Adolf Leonard van Gendt, who was inspired by the Gewandhaus in Leipzig. Construction started in 1883 on a site outside the city, and the hall was completed in late 1886. It officially opened on April 11, 1888, with a grand concert featuring works by Wagner, Handel, Bach, and Beethoven. The resident orchestra, the Royal Concertgebouw Orchestra, gave its first concert there later that year. Today, the venue hosts around 900 concerts annually, attracting over 700,000 visitors, making it one of the most-visited concert halls in the world.

You: /resources
Processing request of type ListResourcesRequest

Available Resources:
[1] suggested_titles

Use: /resource <name> to view its content.

You: /resource suggested_titles
Processing request of type ListResourcesRequest
Processing request of type ReadResourceRequest

=== Resource Text ===
[
  "golden_state_warriors",
  "python_programming_language",
  "san_francisco_symphony"
]

You: /prompt highlight_sections_prompt python_programming_language

=== Prompt Result ===
- History: Provides background on the development and evolution of Python, helping to understand its origins and growth.
- Syntax and Semantics: Explains the language's structure and rules, essential for learning how to write Python code.
- Applications: Showcases the various fields and projects where Python is used, illustrating its versatility and importance.
- Libraries and Frameworks: Highlights the tools available in Python that extend its capabilities, crucial for practical programming.
- Community and Resources: Offers information on support, tutorials, and community involvement, aiding learners in their Python journey.

You: What is the name of Harry Potter's aunt?
AI: Harry Potter's aunt is named Petunia Dursley.

You: /prompt highlight_sections_prompt harry_potter

=== Prompt Result ===
- Plot: Provides an overview of the main story and key events in the Harry Potter series, essential for understanding the narrative.
- Characters: Introduces the main and supporting characters, helping readers connect with the story and its personalities.
- Themes: Explores the central ideas and messages conveyed through the series, offering deeper insights into its significance.
- Setting: Describes the magical world and locations, enriching the reader's understanding of the universe.
- Publication and Reception: Details the series' publication history and how it was received by audiences and critics, highlighting its cultural impact.

You: Does Harry Potter hold any records?
AI: Yes, the Harry Potter series holds several records. For example, it is one of the best-selling book series in history, with over 500 million copies sold worldwide. The books have been translated into numerous languages and have set records for sales and popularity. Additionally, the Harry Potter films are among the highest-grossing movie franchises of all time.
```
