This is an attempt to integrate with the [Law Help Interactive][LHI]
endpoint that will allow us to submit XML data containing a user's
HP Action information and obtain a PDF of the form.

## Quick start

You will need Python 3 and virtualenv.

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

## Additional resources

* Take a look at [get_answers_and_documents.py][] for more details,
  I've tried to document it as best I can.

* Visit the [lhi-files][] directory for sample documents that
  LHI gave us.

* See the [LHI integration document][] for even more details.

[LHI]: https://lawhelpinteractive.org/
[get_answers_and_documents.py]: ./get_answers_and_documents.py
[lhi-files]: ./lhi-files/
[LHI integration document]: https://docs.google.com/document/d/1S3On8lTwkUJVtqoI4yaSq4cLuZIfQQVbeVzgQoJN6kI/edit#
