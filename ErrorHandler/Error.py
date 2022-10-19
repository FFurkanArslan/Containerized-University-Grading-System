from flask import Flask, request, jsonify, Blueprint
from Connection.Connection import *
bp = Blueprint("errors", __name__)


@bp.app_errorhandler(400)
def handle_bad_request(e):
    # from-data gibi parametreleri girmeyince veriyor
    return 'custom bad request!', 400


@bp.app_errorhandler(405)
def handle_method_not_allowed(e):
    # method dışında gönderilen isteklerde çıkan hata
    return 'method not allowed', 405


@bp.app_errorhandler(KeyError)
def handle_KeyError(e):
    # KEY VALUE Kısmında KEY kısmını hatalı girdiğimizde çıkan hata
    return 'HTTP AUTHORIZATION', KeyError


@bp.app_errorhandler(404)
def handle_InvalidRoute(e):
    # olmayan bi urlye gitmek istediğimizde çıkıyor
    return 'Invalid URL', 404
