document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // Submit handler
  document.querySelector('#compose-form').addEventListener('submit', send_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // Fetch emails
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
      // Print emails
      console.log(emails);

      // Loop through emails
      emails.forEach(email => {
          // Create a div for each email
          const newEmail = document.createElement('div');
          newEmail.classList.add('list-group-item','list-group-item-action');

          newEmail.innerHTML = `
            <div class="row">
              <div class="col-3">${email.sender}</div>
              <div class="col-6">${email.subject}</div>
              <div class="col-3">${email.timestamp}</div>
            </div>
          `;

           // change background color for read emails
          if (email.read) {
            newEmail.classList.add('list-group-item-light');
          }

          newEmail.addEventListener('click', () => load_email(email.id, mailbox));
          document.querySelector('#emails-view').append(newEmail);
      });
  });
}

function send_email(event) {
  event.preventDefault();

  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
        recipients: document.querySelector('#compose-recipients').value,
        subject: document.querySelector('#compose-subject').value,
        body: document.querySelector('#compose-body').value
    })
  })
  .then(response => response.json())
  .then(result => {
      // Print result
      console.log(result);
      load_mailbox('sent');
  });
}

function toggle_archive(email_id, archived) {
  fetch(`/emails/${email_id}`, {
    method: 'PUT',
    body: JSON.stringify({
        archived: !archived
    })
  })
  .then(() => load_mailbox('inbox'));
}

function reply_email(email) {
  compose_email();

  // Pre-fill composition fields
  document.querySelector('#compose-recipients').value = email.sender;
  document.querySelector('#compose-subject').value = email.subject.startsWith('Re: ') ? email.subject : `Re: ${email.subject}`;
  document.querySelector('#compose-body').value = `\nOn ${email.timestamp} <${email.sender}> wrote:\n${email.body}`;
}


function load_email(email_id, mailbox) {
  fetch(`/emails/${email_id}`)
  .then(response => response.json())
  .then(email => {
      // Print email
      console.log(email);

      // Show the email and hide other views
      document.querySelector('#emails-view').style.display = 'block';
      document.querySelector('#compose-view').style.display = 'none';

      // Create a div for the email
      const emailView = document.createElement('div');
      emailView.innerHTML = `
        <div class="row pb-2">
          <div class="col-2"><strong>From:</strong></div>
          <div class="col-10">${email.sender}</div>
        </div>
        <div class="row pb-2">
          <div class="col-2"><strong>To:</strong></div>
          <div class="col-10">${email.recipients}</div>
        </div>
        <div class="row pb-2">
          <div class="col-2"><strong>Subject:</strong></div>
          <div class="col-10">${email.subject}</div>
        </div>
        <div class="row pb-2">
          <div class="col-2"><strong>Timestamp:</strong></div>
          <div class="col-10">${email.timestamp}</div>
        </div>
        <div class="row pb-2">
          <div class="col-2"><strong>Body:</strong></div>
          <div class="col-10">${email.body.replace(/\n/g, '<br>')}</div>
        </div>
      `;
      document.querySelector('#emails-view').innerHTML = '';
      document.querySelector('#emails-view').append(emailView);

      // Archive button
      const archiveButton = document.createElement('button');
      archiveButton.classList.add('btn', 'btn-sm', 'btn-outline-primary','me-1');
      archiveButton.innerHTML = email.archived ? 'Unarchive' : 'Archive';
      archiveButton.addEventListener('click', () => toggle_archive(email_id, email.archived));
      document.querySelector('#emails-view').append(archiveButton);

      // Reply button
      const replyButton = document.createElement('button');
      replyButton.classList.add('btn', 'btn-sm', 'btn-outline-primary');
      replyButton.innerHTML = 'Reply';
      replyButton.addEventListener('click', () => reply_email(email));
      document.querySelector('#emails-view').append(replyButton);


      // Mark email as unread
      if (!email.read) {
        fetch(`/emails/${email_id}`, {
          method: 'PUT',
          body: JSON.stringify({
              read: true
          })
        });
      }
  }
  );
}
