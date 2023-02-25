import flask
from flask import jsonify, make_response

from data import db_session
from data.jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'news':
                [item.to_dict(only=('id', 'content', 'user.name'))
                 for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:job_id>')
def get_job(jid):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(jid)
    if not job:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'job': job.to_dict(only=(
                'id', 'team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished',
                'team_leader.id', 'team_leader.email', 'team_leader.name', 'team_leader.surname'))
        }
    )
