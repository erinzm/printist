from flask import Blueprint, request, session, g, redirect, url_for, abort, render_template, flash

interface = Blueprint('interface', __name__)

@interface.route('/')
def slash():
  return render_template('slash.html')