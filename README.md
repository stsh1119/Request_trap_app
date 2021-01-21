# Request_trap

## Requests Trap: A tool for capture and display HTTP requests

### Purpose:

This simple tool is useful during the development of apps that integrate with external services, such as http clients, webhooks, etc. The Requests Trap app provides these services with an endpoint to which they can send requests and notifications

For example, let's assume we are developing an ecommerce site named “myshop" with PayPal integration. During development, Myshop can use Req App to see PayPal requests details via a specific endpoint.

User can setup in the PayPal service the following callback URL: ``` http://requests-trap.com/myshop ```

Then the user could see the IPN(Instant Payment Notification) notifications sent by PayPal here: ``` http://requests-trap.com/myshop/requests ```

### How it works:

The app has three routes:

1. / (home page with some instructions)

2. /:request_id (this endpoint is used to capture requests)

3. /:request_id/requests (captured requests will be displayed here)

Any request [POST, PUT, GET, DELETE, ...] made to /:request_id will be saved in the db and displayed under /:request/requests.

In /:request_id/requests we should see the request_id in the header, and a list of the received requests, ordered by creation date DESC.

Each request item should display all the information contained in the request, well formatted:

* request date
* remote ip
* request-method
* scheme
* query-string
* query-params
* cookies
* headers

App is available at [heroku](https://stsh-request-trap.herokuapp.com)
