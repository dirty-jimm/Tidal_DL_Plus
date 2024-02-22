    f.write("typ=" + typ + "\n")
    f.write("tok=" + tok + "\n")
    f.write("ref=" + ref + "\n")
    f.write("exp=" + exp.strftime("%Y-%m-%d %H:%M:%S.%f"))
    f.close()
    print("New credentials saved to: " + cred_file)


def login(): #displays Tidal login prompt to allow credentials to be generated  FUTURE: Make this email when called automatically, use CLI flag to indicate when user available to authorise link
    session.login_oauth_simple()
    token_type = session.token_type
    access_token = session.access_token
    refresh_token = session.refresh_token
    expiry_time = session.expiry_time
    write_creds(token_type, access_token, refresh_token, expiry_time)
    print("New token expires:" + expiry_time.strftime("%Y-%m-%d %H:%M:%S.%f"))
    return session.check_login()


def connect(session):
    try:  # Try reading credentials
        creds = read_creds()
    except:  # If credentials cant be read
        print("API credentials could not be read")
        login()  # Login (and save credentials)
        return session.check_login()

    try:  # Try connecting using stored credentials
        if session.load_oauth_session(
            creds[0], creds[1], creds[2], creds[3]
        ):  # If we have successfully connected
            print("Session Connected")
    except:  # Else if connection failed
        print("Connection Failed, try getting new API credentials")
        if login():  # Login (and save credentials)
            print("Successfully logged in")
        else:  # Exit if login fails
            print("Log in failed, exiting")
            exit(0)
    return session.check_login()  # check we are logged in


def check_albums(session):
    favorite_albums = session.user.favorites.albums() #get list of favourited abums
    print("Favorited Albums:")
    for album in favorite_albums:
        print(f"{album.id} - {album.name} by {album.artist.name}")
        returned_output = subprocess.check_output( #call Tidal-dl for each album, pass it the album ID
            f"/home/X_USER_X/.local/bin/tidal-dl -l {album.id}", shell=True
        )
        print(returned_output.decode("utf-8"))
        session.user.favorites.remove_album(album.id) #remove album from favourites


if connect(session):
    check_albums(session)
else:
    print("Connection has failed somewhere")

