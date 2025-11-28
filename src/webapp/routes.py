"""Reittimäärittelyt web-sovellukselle."""

from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Varasto, Tuote

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Näyttää kaikki varastot etusivulla."""
    varastot = Varasto.query.all()
    return render_template('index.html', varastot=varastot)


@main_bp.route('/varasto/uusi', methods=['POST'])
def luo_varasto():
    """Luo uuden varaston."""
    nimi = request.form.get('nimi', '').strip()
    if nimi:
        varasto = Varasto(nimi=nimi)
        db.session.add(varasto)
        db.session.commit()
    return redirect(url_for('main.index'))


@main_bp.route('/varasto/<int:varasto_id>')
def nayta_varasto(varasto_id):
    """Näyttää varaston ja sen tuotteet."""
    varasto = Varasto.query.get_or_404(varasto_id)
    return render_template('varasto.html', varasto=varasto)


@main_bp.route('/varasto/<int:varasto_id>/muokkaa', methods=['POST'])
def muokkaa_varastoa(varasto_id):
    """Muokkaa varaston nimeä."""
    varasto = Varasto.query.get_or_404(varasto_id)
    nimi = request.form.get('nimi', '').strip()
    if nimi:
        varasto.nimi = nimi
        db.session.commit()
    return redirect(url_for('main.index'))


@main_bp.route('/varasto/<int:varasto_id>/poista', methods=['POST'])
def poista_varasto(varasto_id):
    """Poistaa varaston ja sen tuotteet."""
    varasto = Varasto.query.get_or_404(varasto_id)
    db.session.delete(varasto)
    db.session.commit()
    return redirect(url_for('main.index'))


@main_bp.route('/varasto/<int:varasto_id>/tuote/uusi', methods=['POST'])
def lisaa_tuote(varasto_id):
    """Lisää uuden tuotteen varastoon."""
    varasto = Varasto.query.get_or_404(varasto_id)
    nimi = request.form.get('nimi', '').strip()
    maara = request.form.get('maara', '0')
    try:
        maara = int(maara)
    except ValueError:
        maara = 0
    if nimi:
        tuote = Tuote(nimi=nimi, maara=maara, varasto_id=varasto.id)
        db.session.add(tuote)
        db.session.commit()
    return redirect(url_for('main.nayta_varasto', varasto_id=varasto_id))


@main_bp.route('/tuote/<int:tuote_id>/poista', methods=['POST'])
def poista_tuote(tuote_id):
    """Poistaa tuotteen varastosta."""
    tuote = Tuote.query.get_or_404(tuote_id)
    varasto_id = tuote.varasto_id
    db.session.delete(tuote)
    db.session.commit()
    return redirect(url_for('main.nayta_varasto', varasto_id=varasto_id))


@main_bp.route('/tuote/<int:tuote_id>/muokkaa', methods=['POST'])
def muokkaa_tuotteen_maaraa(tuote_id):
    """Muokkaa tuotteen lukumäärää."""
    tuote = Tuote.query.get_or_404(tuote_id)
    maara = request.form.get('maara', '0')
    try:
        maara = int(maara)
    except ValueError:
        maara = tuote.maara
    tuote.maara = maara
    db.session.commit()
    return redirect(url_for('main.nayta_varasto', varasto_id=tuote.varasto_id))
