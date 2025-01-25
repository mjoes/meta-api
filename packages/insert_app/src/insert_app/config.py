FORM_HTML = """
<!doctype html>
<html>
    <head>
        <title>Input Form</title>
    </head>
    <body>
        <h1>Insert a new item into base data</h1>
        <form method="post">
            <label for="tag">Tag:</label>
            <input type="text" id="tag" name="tag" required><br><br>
            <label for="show_name">Show name:</label>
            <input type="text" id="show_name" name="show_name" required><br><br>
            <label for="show_nr">Show nr:</label>
            <input type="number" id="show_nr" name="show_nr" required><br><br>
            <label for="dj_name">DJ name:</label>
            <input type="text" id="dj_name" name="dj_name" required><br><br>
            <label for="picture">Picture:</label>
            <input type="text" id="picture" name="picture" required><br><br>
            <label for="description">Description:</label><br>
            <textarea id="description" name="description" rows="4" cols="50" placeholder="Enter description here"></textarea><br><br>
            <label for="tags_0">Tag 0:</label>
            <input type="text" id="tags_0" name="tags_0" required><br><br>
            <label for="tags_1">Tag 1:</label>
            <input type="text" id="tags_1" name="tags_1"><br><br>
            <label for="tags_2">Tag 2:</label>
            <input type="text" id="tags_2" name="tags_2"><br><br>
            <label for="tags_3">Tag 3:</label>
            <input type="text" id="tags_3" name="tags_3"><br><br>
            <label for="tags_4">Tag 4:</label>
            <input type="text" id="tags_4" name="tags_4"><br><br>
            <label for="live">Live:</label>
            <input type="checkbox" id="live" name="live" value="true"><br><br>
            <input type="submit" value="Submit">
        </form>
    </body>
</html>
"""
