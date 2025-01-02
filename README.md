<h1 style="text-align:center; color:#4CAF50;">Movie Data Scraper and Exporter</h1>

<p style="text-align:center; color:#555;">
    This Python script extracts movie data from an HTML file (<code>bolly24.html</code>) using BeautifulSoup and exports it to an Excel file (<code>movie_data.xlsx</code>). The extracted data includes the movie's name, year of release, description, image URL, and duration.
</p>

<h2 style="color:#2196F3;">Features</h2>
<ul>
    <li><b>Data Extraction:</b> Scrapes movie details such as name, year, description, image URL, and duration.</li>
    <li><b>Data Validation:</b> Ensures all extracted data fields have consistent lengths to avoid misalignment.</li>
    <li><b>Excel Export:</b> Saves the processed data into an easy-to-read Excel file.</li>
</ul>

<h2 style="color:#2196F3;">Prerequisites</h2>
<p style="color:#555;">Ensure you have the following Python libraries installed:</p>
<ul>
    <li><b>pandas</b>: For creating and exporting the dataset to Excel.</li>
    <li><b>BeautifulSoup (bs4)</b>: For parsing HTML content.</li>
    <li><b>requests</b> (optional): For future extensions to fetch live data from the web.</li>
</ul>
<p>Install these libraries using pip:</p>
<pre><code>pip install pandas beautifulsoup4 requests openpyxl</code></pre>

<h2 style="color:#2196F3;">How It Works</h2>
<ol>
    <li><b>Read the HTML File:</b> The script loads <code>bolly24.html</code>, which is expected to contain the movie data.</li>
    <li><b>Parse with BeautifulSoup:</b> Extracts specific movie-related elements like names, years, descriptions, and image URLs.</li>
    <li><b>Ensure Consistent Data:</b> Matches the lengths of all extracted lists to ensure proper alignment of data.</li>
    <li><b>Export to Excel:</b> Creates a pandas DataFrame and saves it to <code>movie_data.xlsx</code>.</li>
</ol>

<h2 style="color:#2196F3;">Code Explanation</h2>

<h3 style="color:#4CAF50;">1. Reading the HTML File</h3>
<p>The script reads the content of the <code>bolly24.html</code> file:</p>
<pre><code>
file_path = 'bolly24.html'
with open(file_path, 'r') as file:
    html_content = file.read()
soup = BeautifulSoup(html_content, 'html.parser')
</code></pre>

<h3 style="color:#4CAF50;">2. Extracting Data</h3>
<p>Using BeautifulSoup, the script extracts:</p>
<ul>
    <li><b>Movie Names:</b> Found in <code>&lt;h3&gt;</code> tags with the class <code>ipc-title__text</code>.</li>
    <li><b>Years of Release:</b> Found in <code>&lt;span&gt;</code> tags with the class <code>sc-300a8231-7</code> containing numeric text.</li>
    <li><b>Descriptions:</b> Found in <code>&lt;div&gt;</code> tags with the class <code>ipc-html-content-inner-div</code>.</li>
    <li><b>Image URLs:</b> Found in <code>&lt;img&gt;</code> tags with the class <code>ipc-image</code>.</li>
    <li><b>Durations:</b> Found in <code>&lt;span&gt;</code> tags with the class <code>sc-300a8231-7</code> containing duration strings.</li>
</ul>

<h3 style="color:#4CAF50;">3. Data Alignment</h3>
<p>Ensures all lists have the same length:</p>
<pre><code>
min_length = min(len(movies), len(years), len(movies_description), len(movies_image), len(durations))
movies = movies[:min_length]
years = years[:min_length]
movies_description = movies_description[:min_length]
movies_image = movies_image[:min_length]
durations = durations[:min_length]
</code></pre>

<h3 style="color:#4CAF50;">4. Exporting Data</h3>
<p>The processed data is saved into an Excel file:</p>
<pre><code>
data = pd.DataFrame({
    'Movie Name': movies,
    'Year': years,
    'Image URL': movies_image,
    'Duration': durations  
})
data.to_excel('movie_data.xlsx', index=False)
</code></pre>

<h2 style="color:#2196F3;">Output</h2>

<h3 style="color:#4CAF50;">Example Data</h3>
<table style="border:1px solid #ddd; width:100%; text-align:center;">
    <tr style="background-color:#f2f2f2;">
        <th>Movie Name</th>
        <th>Year</th>
        <th>Image URL</th>
        <th>Duration</th>
    </tr>
    <tr>
        <td>Movie 1</td>
        <td>2021</td>
        <td><a href="https://example.com/image1">https://example.com/image1</a></td>
        <td>2h 10m</td>
    </tr>
    <tr>
        <td>Movie 2</td>
        <td>2022</td>
        <td><a href="https://example.com/image2">https://example.com/image2</a></td>
        <td>1h 45m</td>
    </tr>
</table>

<h3 style="color:#4CAF50;">Excel File</h3>
<p>The extracted data is saved to <code>movie_data.xlsx</code> in the same directory as the script.</p>

<h2 style="color:#2196F3;">How to Run</h2>
<ol>
    <li>Place the <code>bolly24.html</code> file in the same directory as the script.</li>
    <li>Run the script:
        <pre><code>python script_name.py</code></pre>
    </li>
    <li>Check the output file <code>movie_data.xlsx</code> in the directory.</li>
</ol>

<h2 style="color:#2196F3;">Notes</h2>
<ul>
    <li>Ensure the <code>bolly24.html</code> file matches the expected structure. Adjust the <code>class</code> names in the script if the HTML structure changes.</li>
    <li>Extend the script to fetch live movie data using the <code>requests</code> library if needed.</li>
</ul>

<p style="text-align:center; color:#555;">
    Enjoy your streamlined movie data extraction process! 🎥📊
</p>
