# The Ethics of Communicating Data with Visualization
It is tempting to think of data and data visualization as a neutral. An emphasis on a minimalist aesthetic — particularly through the use clean, precise geometric lines — seems to make visualizations objective, transparent forms of communication that masks visualization's persuasive power. Given the growing ubiquity of visualization as a medium for recording, analyzing, and communicating data, we have a responsibility to examine how our design choices can influence the way a visualization is read, and what insights a reader walks away with.

In this assignment, we will grapple with these ethical concerns by visualizing a single dataset from two different perspectives:

  - P1: "honest/ethical/truthful" and
  - P2: "dishonest/unethical/deceiving"
For this assignment, we will consider a visualization from Perspective 1 to be one where:

The visualization is clear and easy to interpret for the intended audience (often parts of the general population);
  - Any data transformations (e.g., filters, additional computations, etc.) are clearly and transparently communicated; and
  - The sources of the data, including potential bias, is communicated.

A visualization from Perspective 2, on the other hand, exhibits one or several of the following characteristics:
  - The visual representation is intentionally inappropriate, overly complex and/or too cluttered for the audience;
  - Labels, axes, and legends are misleading;
  - Titles are skewed to intentionally influence the viewer’s perception;
  - The data has been transformed, filtered, or processed in an intentionally misleading way; or
  - The source and provenance of the data is not clear to the viewer.

We might never imagine ourselves to be (nor aspire to be) to fulfill all categories in the "ethical/honest/truthful" (P1) category so we are going to temporarily ignore that we can't be perfect in order to better appreciate the extent of the rhetorical force of visualization, and build our critical reading skills.

## Part One: Design
You will be working with a single dataset, one of three you can find below. These datasets are intentionally chosen to cover politically charged topics for the simple reason that these are typically the type of data where ethical visualization is important. Note that you do not have to visualize the entire dataset (i.e., you may choose a subset of the data to visualize).

The three datasets are the following:

  - The DEA Pain Pills Database. The Washington Post has published a significant portion of a database maintained by the Drug Enforcement Administration (DEA) that tracks every opioid from their manufacturer, through to distributors, and into pharmacies in towns and cities across the United States. This is an enormous database, and you can choose to work with it at any level of detail (e.g., state-wide, individual counties, or national summaries). You need to create a free account at the Washington Post to access this dataset.
  
  - Greenhouse Gas Emissions 1990–2018. The Organization for Economic Co-operation and Development (OECD) has compiled data for the emissions of all participating countries broken out by the pollutant (e.g., carbon monoxide, methane, etc.) and by different sources (e.g., energy, agriculture, etc.). The linked interface can be a little difficult to use, but you can access various slices of the data by either choosing alternate themes in the left-hand side menu, or by customizing the pollutants and variables in the dropdown menus in the main view.
  
  - Gender Equality Indicators 1960–2017. The World Bank tracks a number of different measures including fertility rate, literacy, employment and ownership of businesses, and wages to study the extent of gender equality around the world. The linked dataset curates a smaller subset of the overall set of gender indicators which you are welcome to use as well.

## Deliverables
You will be visualizing your dataset from two perspectives: P1 and P2. As a result, you will be generating two static visualizations – one for each perspective. We construe "visualization" broadly (e.g., a single visualization may comprise several small multiple views). You have to use Altair on Streamlit to generate your visualization.

You should carefully consider not only visual encoding decisions but also how you might transform your data (e.g., groupings, aggregations, and log transforms), and what annotations and labels might help best convey the message from a particular perspective. Document all of these decisions and describe your rationale in a short write-up (no more than 4 paragraphs per visualization). Make sure that your Visualization includes a descriptive title, potentially subtitle and labels. The writeup for each visualization needs to be submitted in a separate file and each visualization needs to be created with a different python file. Upload the data file to a cloud storage of your choice and link to it from your code. Make sure the data remains available until you have received your grade for the class.

## Grading Criteria
This part of the assignment will be scored using the following rubric. Note, rubric cells may not map exactly to specific point scores.

Component	      Perspective	                         Excellent	                              Satisfactory                                      Poor

Marks & Encodings	  P1	All design choices are effective. The visualization can be read and understood effortlessly.	Design choices are largely effective, but minor errors hinder comprehension.	Ineffective mark or encoding choices are distracting or potentially misleading.

Marks & Encodings	  P2	Subtle ineffective choices for marks or encodings require close and careful reading to identify.	Ineffective mark or encoding choices are not immediately obvious but...	Ineffective marks or encodings were chosen but could be immediately identified.

Data Transformation	P1	More advanced transformation were used to extend the dataset in interesting or useful ways.	Simple transforms (e.g., sorting, filtering) were primarily used.	The raw dataset was used directly, with little to no additional transformation.

Data Transformation	P2	More advanced transformation were used inappropriately or to intentionally mislead.	Simple transforms (e.g., sorting, filtering) were primarily used.	The raw dataset was used directly, with little to no additional transformation.

Titles & Labels	P1	Titles and labels helpfully describe and contextualize the visualization.	Most necessary titles and labels are present, but they could provide more context.	Many titles or labels are missing, or do not provide human-understandable information.

Titles & Labels	P2	Titles and labels subtly skew reading the visualization.	Titles and labels leave out important information, but an astute reader	Titles and labels are largely present, visible, and facilitate reading the visualization.

Write-up	Both	Your write ups are well-crafted and provides reasoned justification for all design choices.	Most design decisions are described, but rationale could be explained at a greater level of detail.	Missing or incomplete. Several design choices are left unexplained.

Critical Reading	 	You correctly identified more than 3/4 of the visualizations you evaluated. Your write-ups thoroughly described how you did so by connecting to lecture concepts.	You correctly identified more than half of the visualizations you evaluated. Your write-ups do a good job of describing why, but could explain your rationale to a greater level of detail.	You correctly identified only half of the visualizations you evaluated. Your write-ups were missing or incomplete.

Creativity & Originality	 	You exceeded the parameters of the assignment, with original insights or particularly creative visualizations or transformations.	You met all the parameters of the assignment.	You met most of the parameters of the assignment.

## Part 2
Design, however, is only half the story. To ensure we do not succumb to their allure of authority, we must hone our critical reading skills and to determine whether a visualization has been designed in a clear and transparent way (i.e., from Perspective 1) or whether it seeks to mislead the reader (i.e., created from Perspective 2).

We will assign you 5 visualizations from other students. For each visualization, your task is to:

determine whether it is an example of a Perspective 1 or Perspective 2 visualization
provide a short (4-5 sentence) description of why
