from datetime import datetime

import flask
from flask import jsonify, request

from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs', methods=['GET'])
def get_jobs():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()

    return jsonify(
        {
            "jobs": [
                job.to_dict(only=('id', 'team_leader_id', 'job', 'work_size',
                                  'collaborators', 'start_date', 'end_date', 'is_finished'))
                for job in jobs
            ]
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def add_jobs():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json
                 for key in ['team_leader_id', 'job', 'work_size', 'collaborators', 'is_finished']):
        return jsonify({'error': 'Bad request'})
    session = db_session.create_session()
    if 'id' in request.json:
        jobs = session.query(Jobs).filter(Jobs.id == request.json['id']).first()
        if jobs:
            return jsonify({'error': 'Id already exists'})
    job = Jobs()
    if 'id' in request.json:
        job.id = request.json['id']
    job.team_leader_id = request.json['team_leader_id']
    job.job = request.json['job']
    job.work_size = request.json['work_size']
    job.collaborators = request.json['collaborators']
    job.is_finished = request.json['is_finished']
    print(job)
    session.add(job)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:job_id>')
def get_one_job(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).filter(Jobs.id == job_id).first()

    if not job:
        return jsonify({'error': 'Not Found'})
    return jsonify(
        job.to_dict(only=('id', 'team_leader_id', 'job', 'work_size',
                          'collaborators', 'start_date', 'end_date', 'is_finished'))
    )
