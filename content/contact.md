+++
draft = false
title = "Contact me"
slug = "contact"
description = "Get in touch with Fabio Oliveira"
+++

Want to get in touch? Drop a message below and it lands straight in my
inbox. I read everything, though I can't always promise a fast reply.

<form action="https://api.web3forms.com/submit" method="POST" class="contact-form">
  <!-- Web3Forms access key (public by design; only authorizes sending to my inbox) -->
  <input type="hidden" name="access_key" value="6c47e903-5bf5-4a43-a280-2a163f81e0c4">
  <input type="hidden" name="subject" value="New message from fbdo.github.io">
  <input type="hidden" name="from_name" value="fbdo.github.io contact form">

  <label for="cf-name">Name</label>
  <input id="cf-name" type="text" name="name" placeholder="Your name" required autocomplete="name">

  <label for="cf-email">Email</label>
  <input id="cf-email" type="email" name="email" placeholder="you@example.com" required autocomplete="email">

  <label for="cf-message">Message</label>
  <textarea id="cf-message" name="message" rows="6" placeholder="What's on your mind?" required></textarea>

  <!-- Honeypot: hidden from humans, bots fill it and get dropped -->
  <input type="checkbox" name="botcheck" class="hidden" style="display:none" tabindex="-1" autocomplete="off">

  <button type="submit">Send message</button>
</form>

## Other ways to reach me

- **[LinkedIn](https://www.linkedin.com/in/fabiobragaoliveira/)** — best for professional contact.
- **[GPG key](/gpg/fabio.braga-public.key)** — if you'd like to send me something encrypted or private.
