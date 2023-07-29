def menu_functions():
    print("""List of menu function
            1.phone book
            2.messages
            3.chat
            4.call register
            5.tones
            6.settings
            7.call divert
            8.games
            9.calculator
            10.reminder
            11.clock
            12.profiles
            13.Sim services**3
            14.turn off
           """)

    menu_function = input("Enter menu_number: ")
    if menu_function == "1":
        phone_book()
    elif menu_function == "2":
        messages()
    elif menu_function == "3":
        chat()
    elif menu_function == "4":
        call_register()
    elif menu_function == "5":
        tones()
    elif menu_function == "6":
        settings()
    elif menu_function == "7":
        call_divert()
    elif menu_function == "8":
        games()
    elif menu_function == "9":
        calculator()
    elif menu_function == "10":
        reminder()
    elif menu_function == '11':
        clock()
    elif menu_function == '12':
        profiles()
    elif menu_function == '13':
        sim_services()
    elif menu_function == '14':
        turn_off_phone()
    else:
        menu_functions()


def search():
    print("0.back")
    searches = input("enter searches: ")
    if searches == '0':
        phone_book()
    else:
        menu_functions()


def service_No():
    print("0.back")
    services = input("enter services: ")
    if services == '0':
        phone_book()
    else:
        menu_functions()


def add_name():
    print("0.back")
    add = input("enter add: ")
    if add == '0':
        phone_book()
    else:
        menu_functions()


def erase():
    print("0.back")
    erase_in = input("enter erase: ")
    if erase_in == '0':
        phone_book()

    else:
        menu_functions()


def edit():
    print("0.back")
    edit_in = input("enter edit: ")
    if edit_in == '0':
        phone_book()
    else:
        menu_functions()


def assign_tone():
    print("0.back")
    assigned = input("enter assigned: ")
    if assigned == '0':
        phone_book()
    else:
        menu_functions()


def send_b_card():
    print("0.back")
    send = input("enter send: ")
    if send == '0':
        phone_book()
    else:
        menu_functions()


def option():
    print("""
             Option
         1.Type of view
         2.Memory of status 
         0.Back

    """)
    option_menu = input("Enter option menu: ")
    if option_menu == '1':
        type_of_view()
    elif option_menu == '2':
        memory_of_status()
    elif option_menu == '0':
        phone_book()
    else:
        menu_functions()


def type_of_view():
    print("0.back")
    types = input("enter type: ")
    if types == "0":
        option()
    else:
        menu_functions()


def memory_of_status():
    print("0.back")
    status = input("enter status: ")
    if status == "0":
        option()
    else:
        menu_functions()


def speed_dials():
    print("0.back")
    speed = input("enter speed: ")
    if speed == '0':
        phone_book()
    else:
        menu_functions()


def voice_tags():
    print("0.back")
    voice = input("enter voice tags: ")
    if voice == "0":
        phone_book()
    else:
        menu_functions()


def phone_book():
    print("""phone book
               1.Search
               2.Service Nos.**1
               3.Add name
               4.Erase
               5.Edit
               6.Assign tone
               7.Send b'card
               8.option
               9.speed dials
               10.Voice tags
               0.back

             """)
    phone_books = input("Enter phonebook menu: ")
    if phone_books == '1':
        search()
    elif phone_books == '2':
        service_No()
    elif phone_books == '0':
        menu_functions()
    elif phone_books == '3':
        add_name()
    elif phone_books == '4':
        erase()
    elif phone_books == '5':
        edit()
    elif phone_books == '6':
        assign_tone()
    elif phone_books == '7':
        send_b_card()
    elif phone_books == '8':
        option()
    elif phone_books == '9':
        speed_dials()
    elif phone_books == '10':
        voice_tags()
    else:
        menu_functions()


def write_messages():
    print("0.back")
    write = input("Enter the write input: ")
    if write == '0':
        messages()


def inbox():
    print("0.back")
    inboxes = input("Enter the inboxes input: ")
    if inboxes == '0':
        messages()


def outbox():
    print("0.back")
    outboxes = input("Enter the outboxes input: ")
    if outboxes == '0':
        messages()


def picture_messages():
    print("0.back")
    pictures = input("Enter the pictures input: ")
    if pictures == '0':
        messages()


def templates():
    print("0.back")
    template = input("Enter the template input: ")
    if template == '0':
        messages()


def smileys():
    print("0.back")
    smiley = input("Enter the write input: ")
    if smiley == '0':
        messages()


def messages_centre_number():
    print("0.back")
    message_centre_number = input("Enter messages centre number: ")
    if message_centre_number == '0':
        set_1()
    else:
        menu_functions()


def message_sent_as():
    print("0.back")
    message_sent = input("Enter message sent as")
    if message_sent == '0':
        set_1()
    else:
        menu_functions()


def messages_validity():
    print("0.back")
    message_validity = input("enter message_validity")
    if message_validity == '0':
        set_1()
    else:
        menu_functions()


def set_1():
    print("""set 1**2
                  1.Messages centre number
                  2.Messages sent as
                  3.Messages validity
                  0.back
                   """)
    sets = input("Enter the set 1 menu: ")
    if sets == '1':
        messages_centre_number()
    elif sets == '2':
        message_sent_as()
    elif sets == '3':
        messages_validity()
    elif sets == '0':
        messages_settings()
    else:
        menu_functions()


def delivery_report():
    print("0.back")
    delivery_reports = input("Enter delivery report: ")
    if delivery_reports == '0':
        common_3()
    else:
        menu_functions()


def reply_via_same_centre():
    print("0.back")
    reply_via = input("Enter the reply to go back: ")
    if reply_via == '0':
        common_3()
    else:
        menu_functions()


def character_support():
    print("0.back")
    character = input("Enter the character support to go back: ")
    if character == '0':
        common_3()
    else:
        menu_functions()


def common_3():
    print(""" Common**3
                           1.Delivery reports
                           2.Reply via same centre
                           3.Character support
                           0.Back
                    """)
    common = input("Enter common menu: ")
    if common == '1':
        delivery_report()
    elif common == '2':
        reply_via_same_centre()
    elif common == '3':
        character_support()
    elif common == '0':
        messages_settings()
    else:
        menu_functions()


def messages_settings():
    print("""Messages settings
                1.set 1**2
                2.common**3
                0.back
                """)
    messages_setting = input("Enter the message settings menu")
    if messages_setting == '1':
        set_1()
    elif messages_setting == '2':
        common_3()
    elif messages_setting == '0':
        messages()
    else:
        menu_functions()


def info_service():
    print("0.back")
    info = input("Enter the info input: ")
    if info == '0':
        messages()


def voice_mailbox_number():
    print("0.back")
    voice = input("Enter the voice input: ")
    if voice == '0':
        messages()


def service_command_editor():
    print("0.back")
    service = input("Enter the service input: ")
    if service == '0':
        messages()


def messages():
    print("""Messages
               1.Write messages
               2.inbox
               3.Outbox
               4.Picture messages
               5.Templates
               6.Smileys
               7.Messages settings
               8.info service
               9.Voice mailbox number
               10.Service command editor
               0.back
               """)
    message = input("Enter message menu: ")
    if message == '1':
        write_messages()
    elif message == '2':
        inbox()
    elif message == '3':
        outbox()
    elif message == '4':
        picture_messages()
    elif message == '5':
        templates()
    elif message == '6':
        smileys()
    elif message == '7':
        messages_settings()
    elif message == '8':
        info_service()
    elif message == '9':
        voice_mailbox_number()
    elif message == '0':
        menu_functions()
    else:
        menu_functions()


def chat():
    print("0.back")
    chats = input("Enter the chat menu: ")
    if chats == '0':
        menu_functions()
    else:
        menu_functions()


def missed_call():
    print("0.back")
    missed_calls = input("Enter the missed calls menu")
    if missed_calls == '0':
        call_register()


def received_calls():
    print("0.back")
    received_call = input("Enter the received calls menu")
    if received_call == '0':
        call_register()
    else:
        menu_functions()


def dialled_numbers():
    print("0.back")
    dialled_number = input("Enter to dialled number")
    if dialled_number == '0':
        call_register()
    else:
        menu_functions()


def erase_recent_call():
    print("0.back")
    erase_recent = input("Enter erase recent call")
    if erase_recent == '0':
        call_register()
    else:
        menu_functions()


def last_call_duration():
    print("0.back")
    last_call = input("enter last call duration")
    if last_call == '0':
        show_call_duration()
    else:
        menu_functions()


def all_calls_duration():
    print("0.back")
    all_calls = input("enter all calls duration")
    if all_calls == '0':
        show_call_duration()
    else:
        menu_functions()


def received_calls_duration():
    print("0.back")
    received_call = input("enter all received calls")
    if received_call == '0':
        show_call_duration()
    else:
        menu_functions()


def dialled_call_duration():
    print("0.back")
    dialled_call = input("enter all received calls")
    if dialled_call == '0':
        show_call_duration()
    else:
        menu_functions()


def clear_timers():
    print("0.back")
    clear_timer = input("enter all received calls")
    if clear_timer == '0':
        show_call_duration()
    else:
        menu_functions()


def show_call_duration():
    print(""" Show call duration
                    1.Last call duration
                    2.ALL calls' duration
                    3.Received calls' duration
                    4.Dialled calls' duration
                    5.clear timers
                    0.back
                     """)
    show_call = input("Enter show call duration")
    if show_call == '1':
        last_call_duration()
    elif show_call == '2':
        all_calls_duration()
    elif show_call == '3':
        received_calls_duration()
    elif show_call == '4':
        dialled_call_duration()
    elif show_call == '5':
        clear_timers()
    elif show_call == '0':
        call_register()
    else:
        menu_functions()


def last_call_cost():
    print("0.back")
    last_call = input("enter all last call: ")
    if last_call == '0':
        show_costs()
    else:
        menu_functions()


def all_calls_cost():
    print("0.back")
    all_calls = input("enter all calls")
    if all_calls == '0':
        show_costs()
    else:
        menu_functions()


def clear_counters():
    print("0.back")
    clear_counter = input("enter all clear counters")
    if clear_counter == '0':
        show_costs()
    else:
        menu_functions()


def show_costs():
    print("""Show call cost
                  1.Last call cost
                  2.All calls' cost
                  3.Clear counters
                  0.back
                  """)
    show_cost = input("enter all show cost menu")
    if show_cost == '1':
        last_call_duration()
    elif show_cost == '2':
        all_calls_cost()
    elif show_cost == '3':
        clear_counters()
    elif show_cost == '0':
        call_register()
    else:
        menu_functions()


def call_cost_limit():
    print("0.back")
    call_cost = input("enter all call cost: ")
    if call_cost == '0':
        call_cost_settings()
    else:
        menu_functions()


def show_costs_in():
    print("0.back")
    show_in = input("enter all show: ")
    if show_in == '0':
        call_cost_settings()
    else:
        menu_functions()


def call_cost_settings():
    print("""Call cost settings
                   1.Call cost limit
                   2.Show costs in
                   0.back
                  """)
    call_cost = input("Enter call cost")
    if call_cost == '1':
        call_cost_settings()
    elif call_cost == '2':
        show_costs_in()
    elif call_cost == '3':
        call_register()
    else:
        menu_functions()


def prepaid():
    print("0.back")
    prepay = input("enter prepay: ")
    if prepay == '0':
        call_register()
    else:
        menu_functions()


def call_register():
    print(""" Call register
                1.Missed calls
                2.Received calls
                3.Dialled numbers
                4.Erase recent call lists
                5.Show call duration
                6.show costs
                7.Call cost settings
                8.prepaid
                0.back
                """)

    call_registers = input("Enter the call register menu")
    if call_registers == '1':
        missed_call()
    elif call_registers == '2':
        received_calls()
    elif call_registers == '3':
        dialled_numbers()
    elif call_registers == '4':
        erase_recent_call()
    elif call_registers == '5':
        show_call_duration()
    elif call_registers == '6':
        show_costs()
    elif call_registers == '7':
        call_cost_settings()
    elif call_registers == '8':
        prepaid()
    elif call_registers == '0':
        menu_functions()
    else:
        menu_functions()


def ringing_tone():
    print("0.back")
    ringing = input("enter ringing: ")
    if ringing == '0':
        tones()
    else:
        menu_functions()


def ringing_volume():
    print("0.back")
    ring = input("enter ring: ")
    if ring == '0':
        tones()
    else:
        menu_functions()


def incoming_call_alert():
    print("0.back")
    incoming = input("enter incoming: ")
    if incoming == '0':
        tones()
    else:
        menu_functions()


def composer():
    print("0.back")
    composers = input("enter composer: ")
    if composers == '0':
        tones()
    else:
        menu_functions()


def message_alert_time():
    print("0.back")
    message_alert = int(input("enter message alert: "))
    if message_alert == '0':
        tones()
    else:
        menu_functions()


def keypad_tones():
    print("0.back")
    keypad = input("enter keypad input: ")
    if keypad == '0':
        tones()
    else:
        menu_functions()


def warning_and_game_tones():
    print("0.back")
    warning_tone = input("enter warning input: ")
    if warning_tone == '0':
        tones()
    else:
        menu_functions()


def vibrating_alert():
    print("0.back")
    vibrating = input("enter vibrating: ")
    if vibrating == '0':
        tones()
    else:
        menu_functions()


def screen_saver():
    print("0.back")
    screen_savers = input("enter screen saver: ")
    if screen_savers == '0':
        tones()
    else:
        menu_functions()


def tones():
    print("""Tones
                1.Ringing tone
                2.Ringing volume
                3.Incoming  call alert
                4.Composer
                5.Message alert tone
                6.Keypad tones
                7.Warning and game tones
                8.Vibrating alert
                9.Screen saver
                0.back
                """)
    tone = input("Enter the tone menu: ")
    if tone == '1':
        ringing_tone()
    elif tone == '2':
        ringing_volume()
    elif tone == '3':
        incoming_call_alert()
    elif tone == '4':
        composer()
    elif tone == '5':
        message_alert_time()
    elif tone == '6':
        keypad_tones()
    elif tone == '7':
        warning_and_game_tones()
    elif tone == '8':
        vibrating_alert()
    elif tone == '9':
        screen_saver()
    elif tone == '0':
        menu_functions()
    else:
        menu_functions()


def automatic_redial():
    print("0.back")
    automatic = input("Enter the automatic: ")
    if automatic == '0':
        call_settings()
    else:
        menu_functions()


def speed_dialling():
    print("0.back")
    speeds = input("Enter the speed dialling: ")
    if speeds == '0':
        call_settings()
    else:
        menu_functions()


def call_waiting_option():
    print("0.back")
    call_waiting = input("Enter the call waiting: ")
    if call_waiting == "0":
        call_settings()
    else:
        menu_functions()


def own_number_sending():
    print("0.back")
    own_number = input("Enter the own number: ")
    if own_number == '0':
        call_settings()
    else:
        menu_functions()


def phone_line_in_use():
    print("0.back")
    phone_line = input("Enter the phone_line: ")
    if phone_line == '0':
        call_settings()
    else:
        menu_functions()


def automatic_answer():
    print("0.back")
    automatic = input("Enter the automatic: ")
    if automatic == '0':
        call_settings()
    else:
        menu_functions()


def call_settings():
    print("""Calling settings
                1.Automatic redial
                2.Speed dialling
                3.Call waiting option
                4.Own number sending
                5.Phone line in use
                6.Automatic answer**1
                0.back
                """)
    call = input("enter call: ")
    if call == '1':
        automatic_redial()
    elif call == '2':
        speed_dialling()
    elif call == '3':
        call_waiting_option()
    elif call == '4':
        own_number_sending()
    elif call == '5':
        phone_line_in_use()
    elif call == '6':
        automatic_answer()
    elif call == '0':
        settings()
    else:
        menu_functions()


def language():
    print("0.back")
    languages = input("Enter language: ")
    if languages == '0':
        phone_settings()
    else:
        menu_functions()


def cell_info_display():
    print("0.back")
    cell_info = input("Enter cell_info: ")
    if cell_info == '0':
        phone_settings()
    else:
        menu_functions()


def welcome_note():
    print("0.back")
    welcome = input("Enter welcome: ")
    if welcome == '0':
        phone_settings()
    else:
        menu_functions()


def network_selection():
    print("0.back")
    network = input("Enter network: ")
    if network == '0':
        phone_settings()
    else:
        menu_functions()


def light():
    print("0.back")
    lights = input("Enter light: ")
    if lights == 0:
        phone_settings()
    else:
        menu_functions()


def confirm_sim():
    print("0.back")
    confirm = input("Enter confirm: ")
    if confirm == '0':
        phone_settings()
    else:
        menu_functions()


def phone_settings():
    print("""Phone settings
                1.Language
                2.Cell info display
                3.Welcome note
                4.Network selection
                5.lights**2
                6.Confirm SIM service actions
               7.back
                """)
    phone = input("enter phone settings: ")
    if phone == "1":
        language()
    elif phone == "2":
        cell_info_display()
    elif phone == "3":
        welcome_note()
    elif phone == '0':
        settings()
    elif phone == "4":
        network_selection()
    elif phone == '5':
        light()
    elif phone == '6':
        confirm_sim()
    else:
        menu_functions()


def pin_code_request():
    print("0.back")
    pin = input("Enter the pin code: ")
    if pin == '0':
        security_settings()
    else:
        menu_functions()


def call_barring_service():
    print("0.back")
    call_barring = input("Enter the call barring: ")
    if call_barring == '0':
        security_settings()
    else:
        menu_functions()


def fixed_dialling():
    print("0.back")
    fixed = input("Enter the fixed dialling: ")
    if fixed == '0':
        security_settings()
    else:
        menu_functions()


def closed_user_group():
    print("0.back")
    closed = input("Enter the closed_user: ")
    if closed == '0':
        security_settings()
    else:
        menu_functions()


def phone_security():
    print("0.back")
    phone = input("Enter the phone security: ")
    if phone == '0':
        security_settings()
    else:
        menu_functions()


def change_access_codes():
    print("0.back")
    change = input("Enter the pin code")
    if change == '0':
        security_settings()
    else:
        menu_functions()


def security_settings():
    print("""Security settings
                  1.PIN code request
                  2.Call barring service
                  3.Fixed dialling
                  4.Closed user group
                  5.Phone security
                  6.Change access codes
            """)
    security = input("enter security: ")
    if security == '1':
        pin_code_request()
    elif security == '2':
        call_barring_service()
    elif security == '3':
        fixed_dialling()
    elif security == '4':
        closed_user_group()
    elif security == '5':
        phone_security()
    elif security == '6':
        change_access_codes()
    elif security == '0':
        settings()
    else:
        menu_functions()


def restore_factory():
    print("0.back")
    restore = input("enter restore: ")
    if restore == '0':
        settings()
    else:
        menu_functions()


def settings():
    print("""Settings
                1.Call settings
                2.Phone settings
                3.Security settings
                4.Restore factory
                0.back
                """)
    setting = input("Enter the setting menu: ")
    if setting == '1':
        call_settings()
    elif setting == '2':
        phone_settings()
    elif setting == '3':
        security_settings()
    elif setting == '4':
        restore_factory()
    elif setting == '5':
        menu_functions()
    else:
        menu_functions()


def call_divert():
    print("0.back")
    calls = input("Enter the call_divert: ")
    if calls == '0':
        menu_functions()


def games():
    print("0.back")
    game = input("Enter the games: ")
    if game == '0':
        menu_functions()


def calculator():
    print("0.back")
    calculators = input("Enter the calculator: ")
    if calculators == '0':
        menu_functions()


def reminder():
    print("0.back")
    reminders = input("Enter the remainder: ")
    if reminders == '0':
        menu_functions()


def alarm_clock():
    print("0,back")
    alarm_clocks = input("Enter the alarm clock: ")
    if alarm_clocks == '0':
        clock()
    else:
        menu_functions()


def clock_settings():
    print("0,back")
    clock_setting = input("Enter the clock setting: ")
    if clock_setting == '0':
        clock()
    else:
        menu_functions()


def date_settings():
    print("0,back")
    date_setting = input("Enter the date setting: ")
    if date_setting == '0':
        clock()
    else:
        menu_functions()


def stopwatch():
    print("0,back")
    stopwatch_in = input("Enter the stopwatch ")
    if stopwatch_in == '0':
        clock()
    else:
        menu_functions()


def countdown_timer():
    print("0,back")
    countdown = input("Enter the clock setting ")
    if countdown == '0':
        clock()
    else:
        menu_functions()


def auto_update():
    print("0,back")
    auto = input("Enter the auto update: ")
    if auto == '0':
        clock()
    else:
        menu_functions()


def clock():
    print("""Clock
                1.Alarm clock
                2.Clock settings
                3.Date settings
                4.Stopwatch
                5.Countdown timer
                6 Auto update of date and  time
                0.back
                  """)
    clocks = input("Enter the clock: ")
    if clocks == '1':
        alarm_clock()
    elif clocks == '2':
        clock_settings()
    elif clocks == '3':
        date_settings()
    elif clocks == '4':
        stopwatch()
    elif clocks == '5':
        countdown_timer()
    elif clocks == '6':
        auto_update()
    elif clocks == '0':
        menu_functions()
    else:
        menu_functions()


def profiles():
    print("0.back")
    profile = input("Enter the profile: ")
    if profile == '0':
        menu_functions()


def sim_services():
    print("0.back")
    sims = input("Enter the sim services")
    if sims == '0':
        menu_functions()


def turn_off_phone():
    print("""
        Nice dealing with you
        phone turning off....
        phone finally off
    """)


menu_functions()