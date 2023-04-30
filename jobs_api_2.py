import flask
from flask import jsonify

from data.jobs import Jobs
from data import db_session

blueprint = flask.Blueprint('jobs_api', __name__, template_folder='templates')


# получение одной работы
@blueprint.route('/api/jobs')
def getting_jobs():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return flask.jsonify({'jobs': [item.to_dict(
        only=('id', 'team_leader', 'job', 'work_size', 'collaborators',
              'start_date', 'end_date', 'is_finished'))
        for item in jobs]})


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_one_job(job_id):
    session = db_session.create_session()
    jobs = session.query(Jobs).get(job_id)
    if not jobs:
        return jsonify({'error': 'Not found'})
    return jsonify({'jobs': jobs.to_dict(
        only=('id', 'team_leader', 'job', 'work_size', 'collaborators',
              'start_date', 'end_date', 'is_finished'))})
