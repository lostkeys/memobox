from flask import Flask, render_template, request, jsonify, abort, Response
from helper.db import DBHelper, DBSelect
from helper.filter import FilterHelper
from helper.image import ImageHelper
from model.device import DeviceModel
from model.file import FileModel
import os

app = Flask(__name__)
app.debug = True

DBHelper('../../data/index.db')
ImageHelper('static/images', 'mint')
DeviceModel.install()
FileModel.install()
FilterHelper.install()

# Start page route
@app.route('/')
def index_action():
    return render_template('index.html')

@app.route('/files')
def files_action():

    data = []
    args = request.args
    pixel_ratio = 1
    models = FileModel.all().limit(240)

    for arg in args.keys():
        if arg == 'retina':
            val = args.get(arg)
            if val and val.lower() != 'false':
                pixel_ratio = 2
            continue
        vals = args.get(arg).split(',')
        if arg == 'device':
            models.add_filter(arg, {'in': vals})
        else:
            FilterHelper.apply_filter(arg, vals, models)

    ImageHelper().join_file_thumbnails(
        models,
        'm.%s' % FileModel._pk,
        260*pixel_ratio,
        260*pixel_ratio
    )
    ImageHelper().add_file_icons(models, 48*pixel_ratio, 128*pixel_ratio)
    for model in models:
        data.append(model.get_data())

    return jsonify({'files': data, 'sql': models.render()})

@app.route('/files/filters')
def file_filters_action():

    filters = FilterHelper.get_all_filters()

    device_opts = {}
    for device in DeviceModel.all():
        device_opts[device.id()] = device.product_name()
    if len(device_opts) > 1:
        filters.insert(0, {
            'label': 'Device',
            'multi': True,
            'param': 'device',
            'options': device_opts
        })

    return jsonify({'filters': filters})

@app.route('/files/details')
def file_details_action():

    model = FileModel().load(request.args.get('id'))
    return jsonify(model.get_data())

@app.route('/files/stream/<file_id>/<display_name>')
def file_stream_action(file_id=None, display_name=None):

    if not file_id:
        abort(404)

    model = FileModel().load(file_id)
    if not model.id():
        abort(404)

    filename = '%s/%s' % (model.abspath(), model.name())
    mimetype = '%s/%s' % (model.type(), model.subtype())

    if not os.path.isfile(filename):
        abort(404)

    return Response(
                file(filename),
                direct_passthrough=True,
                content_type=mimetype)

