This is an attempt to integrate with the [Law Help Interactive (LHI)][LHI]
SOAP endpoint that will allow us to submit XML data containing a user's
HP Action information and obtain a PDF of the form.

Thankfully, the [zeep][] library makes it easy for us to integrate
with LHI's SOAP service from Python.

## Quick start

You will need [Python 3][].

First copy `.env.sample` to `.env` and edit it as needed.

Then create your virtualenv and enter it:

```
python3 -m venv venv
source venv/bin/activate   # Or venv\Scripts\activate on Windows
```

Then install dependencies:

```
pip install -r requirements.txt
```

Then run the tool:

```
python3 get_answers_and_documents.py
```

### Running the postback server

You can run the postback server with:

```
flask run
```

You will probably want to use a service like [ngrok][] to
create a tunnel that will allow the LHI service to
access it. Then set the `LHI_POSTBACK_URL` in your
`.env` file to point at your tunnel URL.

## Additional resources

* Take a look at [get_answers_and_documents.py][] for more details,
  I've tried to document it as best I can.

* Visit the [lhi-files][] directory for sample documents that
  LHI gave us.

* See the [LHI integration document][] for even more details.

[Python 3]: https://www.python.org/
[LHI]: https://lawhelpinteractive.org/
[get_answers_and_documents.py]: ./get_answers_and_documents.py
[lhi-files]: ./lhi-files/
[LHI integration document]: https://docs.google.com/document/d/1S3On8lTwkUJVtqoI4yaSq4cLuZIfQQVbeVzgQoJN6kI/edit#
[zeep]: https://python-zeep.readthedocs.io/en/master/
[ngrok]: https://ngrok.com/
