select * from user;

ALTER TABLE user ADD online BOOLEAN;


CREATE TABLE message (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(250),
    body TEXT,
    sender_id INTEGER,
    FOREIGN KEY (sender_id) REFERENCES user(id)
);


INSERT INTO message (title, body, sender_id) VALUES
('Tjoho', 'Detta är kul!', 2);

SELECT * FROM message;

SELECT * FROM message_recv;

CREATE TABLE message_recv (
    user_id INTEGER,
    message_id INTEGER,
    PRIMARY KEY (user_id, message_id),
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (message_id) REFERENCES message(id)
);

INSERT INTO message_recv (user_id, message_id) VALUES
(3, 2);


SELECT msg.title, sender.name, recv.name FROM user sender
JOIN message msg on sender.id = msg.sender_id
JOIN main.message_recv mr on msg.id = mr.message_id
JOIN user recv on mr.user_id = recv.id;


