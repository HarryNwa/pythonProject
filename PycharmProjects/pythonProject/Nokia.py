def menu_list():
    print(" 1. Phonebook\n "
          "2. Messages\n "
          "3. Call register\n "
          "4. Tones\n "
          "5. Settings\n "
          "6. Call divert\n "
          "7. Games\n "
          "8. Calculator\n "
          "9. Reminder"
          "0. Back")

    user_input_0 = input("Enter any number to navigate: ")
    if user_input_0 == "1":
        phonebook()
    if user_input_0 == "2":
        message()
    if user_input_0 == "3":
        call_register()


def search():
    print("Search contact")
    search = input("Enter 1 to return ")
    if search == "1":
        phonebook()


def service_nos():
    pass


def message():
    print("1. Write messages\n" +
          "2. Inbox\n" +
          "3. Outbox\n" +
          "4. Picture messages\n" +
          "5. Templates\n" +
          "6. Smileys\n" +
          "7. Message settings\n" +
          "    1. Set 1\n" +
          "        1. Message centre number\n" +
          "        2. Messages sent as\n" +
          "        3. Message validity\n" +
          "    2. Common 3\n" +
          "        1. Delivery reports\n" +
          "        2. Reply via same centre\n" +
          "        3. Character support\n" +
          "8. Info service\n" +
          "9. Voice mailbox number\n" +
          "10.Service command editor\n"
          "0. Back ")
    user_input_3 = input("Enter message box: ")
    if user_input_3 == "0":
        menu_list()


def add_name():
    print("Create new contact")
    print("New contact successfully created")
    phonebook()


def erase():
    print("Delete contact")


def edit():
    print("1. Select\v"
          "2. Edit now")


def phonebook():
    print("1. Search\n" +
          "2. Service Nos.\n" +
          "3. Add name\n" +
          "4. Erase\n" +
          "5. Edit\n" +
          "6. Assign tone\n" +
          "7. Send b’card\n" +
          "8. Options\n" +
          "   1. Type of view\n" +
          "   2. Memory status\n" +
          "9. Speed dials\n" +
          "10. Voice tags\n" +
          "0. Back")
    user_input_1 = input("Enter phonebook: ")
    if user_input_1 == "1":
        search()
    elif user_input_1 == "2":
        service_nos()
    elif user_input_1 == "3":
        add_name()
    elif user_input_1 == "4":
        erase()
    elif user_input_1 == "5":
        edit()
    elif user_input_1 == "0":
        menu_list()


def call_register():
    print("1. Outgoing call\n"
          "2. Incoming call\n"
          "3. Missed call\n"
          "0. Back")
    user_input_4 = input("Enter number: ")
    if user_input_4 == "0":
        menu_list()


menu_list()
user_input = input("Enter a number to navigate right or left: ")

if user_input == "1":
    phonebook()
elif user_input == "2":
    message()
elif user_input == "3":
    call_register()

#     public String messages(String messages) {
#         if (messages == "1")
#             messages = "1. Write messages\n" +
#                 "2. Inbox\n" +
#                 "3. Outbox\n" +
#                 "4. Picture messages\n" +
#                 "5. Templates\n" +
#                 "6. Smileys\n" +
#                 "7. Message settings\n" +
#                 "    1. Set 1\n" +
#                 "        1. Message centre number\n" +
#                 "        2. Messages sent as\n" +
#                 "        3. Message validity\n" +
#                 "    2. Common 3\n" +
#                 "        1. Delivery reports\n" +
#                 "        2. Reply via same centre\n" +
#                 "        3. Character support\n" +
#                 "8. Info service\n" +
#                 "9. Voice mailbox number\n" +
#                 "10.Service command editor";
#         if(messages == "0")
#             messages = "Menu";
#         return messages;
#     }
#
#     public String chatBox(String chatBox) {
#         if (chatBox == "1")
#             chatBox = " ";
#         if(chatBox == "0")
#             chatBox = "Menu";
#         return chatBox;
#     }
#
#     public String callRegister(String callRegister) {
#         if (callRegister == "1")
#             callRegister = "1. Missed calls\n" +
#                 "2. Received calls\n" +
#                 "3. Dialled numbers\n" +
#                 "4. Erase recent call lists\n" +
#                 "5. Show call duration\n" +
#                 "    1. Last call duration\n" +
#                 "    2. All calls’ duration\n" +
#                 "    3. Received calls’ duration\n" +
#                 "    4. Dialled calls’ duration\n" +
#                 "    5. Clear timers\n" +
#                 "6. Show call costs\n" +
#                 "    1. Last call cost\n" +
#                 "    2. All calls’ cost\n" +
#                 "    3. Clear counters\n" +
#                 "7. Call cost settings\n" +
#                 "    1. Call cost limit\n" +
#                 "    2. Show costs in\n" +
#                 "8. Prepaid credit";
#         if(callRegister == "0")
#             callRegister = "Menu";
#         return callRegister;
#     }
#
#     public String tones(String tones) {
#         if (tones == "1")
#             tones = "1. Ringing tone\n" +
#                 "2. Ringing volume\n" +
#                 "3. Incoming call alert\n" +
#                 "4. Composer\n" +
#                 "5. Message alert tone\n" +
#                 "6. Keypad tones\n" +
#                 "7. Warning and game tones\n" +
#                 "8. Vibrating alert\n" +
#                 "9. Screen saver";
#         if(tones == "0")
#             tones = "Menu";
#         return tones;
#     }
#
#     public String settings(String settings) {
#         if (settings == "1")
#             settings = "1. Call settings\n" +
#                 "    1. Automatic redial\n" +
#                 "    2. Speed dialling\n" +
#                 "    3. Call waiting options\n" +
#                 "    4. Own number sending\n" +
#                 "    5. Phone line in use\n" +
#                 "    6. Automatic answer 1\n" +
#                 "2. Phone settings\n" +
#                 "    1. Language\n" +
#                 "    2. Cell info display\n" +
#                 "    3. Welcome note\n" +
#                 "    4. Network selection\n" +
#                 "    5. Lights 2\n" +
#                 "    6. Confirm SIM service actions\n" +
#                 "3. Security settings\n" +
#                 "    1. PIN code request\n" +
#                 "    2. Call barring service\n" +
#                 "    3. Fixed dialling\n" +
#                 "    4. Closed user group\n" +
#                 "    5. Phone security\n" +
#                 "    6. Change access codes\n" +
#                 "4. Restore factory settings";
#         if(settings == "0")
#             settings = "Menu";
#         return settings;
#     }
#
#
#     public String callDivert(String callDivert) {
#         if (callDivert == "1")
#             callDivert = "Divert when busy\n" +
#                 "   1. Activate\n +" +
#                 "   2. Cancel";
#         if(callDivert == "0")
#             callDivert = "Menu";
#         return callDivert;
#     }
#
#     public String games(String games) {
#         if (games == "1")
#             games = "1. Sudoku\n +" +
#                 "2. Snake";
#         if(games == "0")
#             games = "Menu";
#         return games;
#     }
#
#     public int calculator(int number) {
#         int calculator = number + number;
#         return number;
#     }
#
#     public String reminder(String reminder) {
#         if (reminder == "1")
#             reminder = "set alarm reminder";
#         if(reminder == "0")
#             reminder = "Menu";
#         return reminder;
#     }
#
#     public String clock(String clock) {
#         if (clock == "1")
#             clock = "1. Alarm clock\n" +
#                 "2. Clock settings\n" +
#                 "3. Date setting\n" +
#                 "4. Stopwatch\n" +
#                 "5. Countdown timer\n" +
#                 "6. Auto update of date and time";
#         if(clock == "0")
#             clock = "Menu";
#         return clock;
#     }
#
#     public String profile(String profile) {
#         if (profile == "1")
#             profile = "1. General\n" +
#                 "2. Meeting\n" +
#                 "3. Silent\n"+
#                 "4. Vibrate\n"+
#                 "5. Outdoor";
#         if(profile == "0")
#             profile = "Menu";
#         return profile;
#     }
#
#     public String SIMApp(String SIMApp) {
#         if (SIMApp == "1")
#             SIMApp = "1. MTN Service\n" +
#                 "2. Virtual TopUp\n" +
#                 "3. MTN LinkUp\n" +
#                 "4. MTN MsgXpress";
#         if(SIMApp == "0")
#             SIMApp = "Menu";
#         return SIMApp;
#     }
# }
