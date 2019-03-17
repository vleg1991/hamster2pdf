# - coding: utf-8 -

# Copyright (C) 2008-2010, 2014 Toms Bauģis <toms.baugis at gmail.com>

# This file is part of Project Hamster.

# Project Hamster is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Project Hamster is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Project Hamster.  If not, see <http://www.gnu.org/licenses/>.


# some widgets that repeat all over the place
# cells, columns, trees and other

import logging
logger = logging.getLogger(__name__)   # noqa: E402

import datetime as dt
import locale


def format_duration(minutes, human = True):
    """formats duration in a human readable format.
    accepts either minutes or timedelta"""

    if isinstance(minutes, dt.timedelta):
        minutes = duration_minutes(minutes)

    if not minutes:
        if human:
            return ""
        else:
            return "00:00"

    if minutes < 0:
        # format_duration did not work for negative values anyway
        # return a warning
        return "NEGATIVE"

    hours = minutes / 60
    minutes = minutes % 60
    formatted_duration = ""

    if human:
        if minutes % 60 == 0:
            # duration in round hours
            formatted_duration += ("%dh") % (hours)
        elif hours == 0:
            # duration less than hour
            formatted_duration += ("%dmin") % (minutes % 60.0)
        else:
            # x hours, y minutes
            formatted_duration += ("%dh %dmin") % (hours, minutes % 60)
    else:
        formatted_duration += "%02d:%02d" % (hours, minutes)


    return formatted_duration


def duration_minutes(duration):
    """returns minutes from duration, otherwise we keep bashing in same math"""
    if isinstance(duration, list):
        res = dt.timedelta()
        for entry in duration:
            res += entry

        return duration_minutes(res)
    elif isinstance(duration, dt.timedelta):
        return duration.total_seconds() / 60
    else:
        return duration


def zero_hour(date):
    return dt.datetime.combine(date.date(), dt.time(0,0))

# it seems that python or something has bug of sorts, that breaks stuff for
# japanese locale, so we have this locale from and to ut8 magic in some places
# see bug 562298
def locale_from_utf8(utf8_str):
    try:
        retval = str (utf8_str, "utf-8").encode(locale.getpreferredencoding())
    except:
        retval = utf8_str
    return retval


def locale_to_utf8(locale_str):
    try:
        retval = str (locale_str, locale.getpreferredencoding()).encode("utf-8")
    except:
        retval = locale_str
    return retval


def dateDict(date, prefix = ""):
    """converts date into dictionary, having prefix for all the keys"""
    res = {}

    res[prefix+"a"] = date.strftime("%a")
    res[prefix+"A"] = date.strftime("%A")
    res[prefix+"b"] = date.strftime("%b")
    res[prefix+"B"] = date.strftime("%B")
    res[prefix+"c"] = date.strftime("%c")
    res[prefix+"d"] = date.strftime("%d")
    res[prefix+"H"] = date.strftime("%H")
    res[prefix+"I"] = date.strftime("%I")
    res[prefix+"j"] = date.strftime("%j")
    res[prefix+"m"] = date.strftime("%m")
    res[prefix+"M"] = date.strftime("%M")
    res[prefix+"p"] = date.strftime("%p")
    res[prefix+"S"] = date.strftime("%S")
    res[prefix+"U"] = date.strftime("%U")
    res[prefix+"w"] = date.strftime("%w")
    res[prefix+"W"] = date.strftime("%W")
    res[prefix+"x"] = date.strftime("%x")
    res[prefix+"X"] = date.strftime("%X")
    res[prefix+"y"] = date.strftime("%y")
    res[prefix+"Y"] = date.strftime("%Y")
    res[prefix+"Z"] = date.strftime("%Z")

    for i, value in res.items():
        res[i] = locale_to_utf8(value)

    return res
