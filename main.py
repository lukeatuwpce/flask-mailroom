#!/usr/bin/env python3
""" https://github.com/UWPCEWebPython/flask-mailroom """

import os

from flask import Flask, render_template, request, redirect, url_for

from model import Donor, Donation

app = Flask(__name__) # pylint: disable=invalid-name


@app.route('/', methods=['GET'])
def home():
    """ Redirect to donations page """
    return redirect(url_for('donations'))


@app.route('/donations', methods=['GET', 'POST'])
def donations():
    """ Prompt for donations and display current donations """
    if request.method == 'POST':
        donor_name = request.form['donor_name']
        donation_amount = request.form['donation_amount']
        print(f"donor_name {donor_name} donation_amount {donation_amount}")
        try:
            donor = Donor.get(Donor.name == donor_name)
        except Donor.DoesNotExist:
            donor = Donor(name=donor_name)
            donor.save()

        donation = Donation(donor=donor, value=donation_amount)
        donation.save()

        # README says to redirect to home page, but that just redirects here.
        # So, just fall through to what would be the GET processing.

    dons = Donation.select()
    return render_template('donations.jinja2', donations=dons)


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=PORT)
