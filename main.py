from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML template for the form
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

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        item={}
        item["tag"] = request.form.get("tag")
        item["show_name"] = request.form.get("show_name")
        item["show_nr"] = request.form.get("show_nr")
        item["dj_name"] = request.form.get("dj_name")
        item["picture"] = request.form.get("picture")
        item["description"] = request.form.get("description")
        item["tags_0"] = request.form.get("tags_0")
        item["tags_1"] = request.form.get("tags_1")
        item["tags_2"] = request.form.get("tags_2")
        item["tags_3"] = request.form.get("tags_3")
        item["tags_4"] = request.form.get("tags_4", None)
        item["live"] = request.form.get("live") == "true"
        print(item)
        return f"Success"
    return render_template_string(FORM_HTML)

if __name__ == "__main__":
    app.run(debug=True)

