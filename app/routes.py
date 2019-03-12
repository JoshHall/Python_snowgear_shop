from app import app
from flask import render_template, url_for, redirect


@app.route('/')
@app.route('/index')
def index():
    products = {
        1001: {
            'title': 'Soap',
            'price': 3.98,
            'desc': 'Very clean soapy soap, descriptive text'
        },
        1002: {
            'title': 'Grapes',
            'price': 4.56,
            'desc': 'Bundle of grapey grapes, yummy'
        },
        1003: {
            'title': 'Pickles',
            'price': 5.67,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1004: {
            'title': 'Juice',
            'price': 2.68,
            'desc': 'Yummy Yumy OJ Babyyyyy'
        },
        1005: {
            'title': 'Title 5',
            'price': 5.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1006: {
            'title': 'Title 6',
            'price': 6.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1007: {
            'title': 'Title 7',
            'price': 7.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1008: {
            'title': 'Title 8',
            'price': 8.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1009: {
            'title': 'Title 9',
            'price': 9.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1010: {
            'title': 'Title 10',
            'price': 10.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1011: {
            'title': 'Title 11',
            'price': 11.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1012: {
            'title': 'Title 12',
            'price': 12.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1013: {
            'title': 'Title 13',
            'price': 13.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1014: {
            'title': 'Title 14',
            'price': 14.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1015: {
            'title': 'Title 15',
            'price': 15.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1016: {
            'title': 'Title 16',
            'price': 16.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1017: {
            'title': 'Title 17',
            'price': 17.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1018: {
            'title': 'Title 18',
            'price': 18.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1019: {
            'title': 'Title 19',
            'price': 19.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1020: {
            'title': 'Title 20',
            'price': 20.00,
            'desc': 'A pickle a day keeps the goblins away'
        }
    }
    return render_template('index.html', title='Home', products=products)

@app.route('/shop')
def shop():
    products = {
        1001: {
            'title': 'Soap',
            'price': 3.98,
            'desc': 'Very clean soapy soap, descriptive text'
        },
        1002: {
            'title': 'Grapes',
            'price': 4.56,
            'desc': 'Bundle of grapey grapes, yummy'
        },
        1003: {
            'title': 'Pickles',
            'price': 5.67,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1004: {
            'title': 'Juice',
            'price': 2.68,
            'desc': 'Yummy Yumy OJ Babyyyyy'
        },
        1005: {
            'title': 'Title 5',
            'price': 5.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1006: {
            'title': 'Title 6',
            'price': 6.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1007: {
            'title': 'Title 7',
            'price': 7.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1008: {
            'title': 'Title 8',
            'price': 8.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1009: {
            'title': 'Title 9',
            'price': 9.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1010: {
            'title': 'Title 10',
            'price': 10.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1011: {
            'title': 'Title 11',
            'price': 11.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1012: {
            'title': 'Title 12',
            'price': 12.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1013: {
            'title': 'Title 13',
            'price': 13.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1014: {
            'title': 'Title 14',
            'price': 14.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1015: {
            'title': 'Title 15',
            'price': 15.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1016: {
            'title': 'Title 16',
            'price': 16.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1017: {
            'title': 'Title 17',
            'price': 17.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1018: {
            'title': 'Title 18',
            'price': 18.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1019: {
            'title': 'Title 19',
            'price': 19.00,
            'desc': 'A pickle a day keeps the goblins away'
        },
        1020: {
            'title': 'Title 20',
            'price': 20.00,
            'desc': 'A pickle a day keeps the goblins away'
        }
    }
    return render_template('shop.html', title='Shop', products=products)
