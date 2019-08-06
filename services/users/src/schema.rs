table! {
    users (email) {
        email -> Varchar,
        subscribed -> Bool,
        termsandconditions -> Bool,
        firstname -> Nullable<Varchar>,
        lastname -> Nullable<Varchar>,
        address1 -> Nullable<Varchar>,
        address2 -> Nullable<Varchar>,
        city -> Nullable<Varchar>,
        state -> Nullable<Varchar>,
        zipcode -> Nullable<Varchar>,
        country -> Nullable<Varchar>,
        phone -> Nullable<Varchar>,
        birthmonth -> Nullable<Varchar>,
        birthday -> Nullable<Int2>,
        birthyear -> Nullable<Int2>,
        online -> Bool,
        lastlogin -> Timestamp,
        lastlogout -> Timestamp,
        created_at -> Timestamp,
    }
}
