# draftstemplate.mmbundle
Creating drafts from a template by replacing variables with values.

This is a [bundle](https://manual.mailmate-app.com/preferences.html#bundles_preferences) for [MailMate](http://mailmate-app.com). It allows the creation of a set of emails from a template by assigning variables of the form `${var}` to values. The template is written as an email and stored as a draft. The bundle creates instances of emails and saves them as drafts as well.

Here is an example. Assume that you want to sent an email of the form

```
Hi ${firstname},

It's nice to write to you again. I hope you are well.

Best,
Michael
```

to *Adam* at *foo.com* and *Eve* at *bar.org*. Store the above template as a draft and create a tab-separated value file named `variables.txt` with contents
 
```
firstname	to
Adam	adam@foo.com
Eve	eve@bar.org
```

at `~/Library/Application Support/MailMate/Bundles/draftstemplate.mmbundle`

In MailMate, select *Command* | *Drafts Template* | *Create Drafts from Template*. The resulting emails will be stored in the `Drafts` folder.

The documentation of the bundle mechanism is available [here](https://github.com/mailmate/mailmate_manual/wiki/Bundles).
