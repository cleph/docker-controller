import json

from flask import Flask, render_template, redirect, url_for, Response
import docker

app = Flask(__name__)
client = docker.from_env()

@app.route('/')
def list_containers():
    containers = client.containers.list(all=True)
    return render_template('containers.html', containers=containers)

@app.route('/restart/<container_id>')
def restart_container(container_id):
    container = client.containers.get(container_id)
    container.restart()
    return redirect(url_for('list_containers'))

@app.route('/stop/<container_id>')
def stop_container(container_id):
    container = client.containers.get(container_id)
    container.stop()
    return redirect(url_for('list_containers'))

@app.route('/delete/<container_id>')
def delete_container(container_id):
    container = client.containers.get(container_id)
    container.remove(force=True)
    return redirect(url_for('list_containers'))


@app.route('/inspect/<container_id>')
def inspect_container(container_id):
    container = client.containers.get(container_id)
    inspection_data = container.attrs  # Fetches the detailed inspection information
    inspection_text = json.dumps(inspection_data, indent=4)  # Convert JSON data to pretty-printed text
    return Response(
        inspection_text,
        mimetype="text/plain",
        headers={"Content-Disposition": f"attachment;filename={container_id}_inspect.txt"}
    )


if __name__ == '__main__':
    app.run(debug=True)
