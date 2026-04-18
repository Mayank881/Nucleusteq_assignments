package com.mayank.session2.component;

import org.springframework.stereotype.Component;

// this class handles notification logic
// @Component annotation tells Spring that this class is a component and can be injected into other classes
// we use @component for reusable logic.
@Component
public class NotificationComponent {

    // send notification

    public String sendNotification() {
        return " Notification  sent";
    }
}